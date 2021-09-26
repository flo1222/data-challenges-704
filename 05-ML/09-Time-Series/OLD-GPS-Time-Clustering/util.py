import os
import json
import pandas as pd
import numpy as np
import datetime
from matplotlib import style
import matplotlib.pyplot as plt
from haversine import haversine


BASE_PATH_DATA = "./data/"
BASE_PATH_DATA_DF = "./data/df/"
EARTH_RADIUS = 6371



def standardize(df=None, field=None):
    mean_field = df[field].mean()
    std_field = df[field].std()
    serie = (df[field] - mean_field) / std_field
    return serie

def get_haversine(a, b):
    return haversine((a['latitude'], a['longitude']), (b['latitude'], b['longitude']))

# FUNCTION 1
def load_and_transform_json(file_path):
    raw_data = [] # initiate raw data storage
    # Loop to read line by line and append to raw_data
    with open(os.path.join(BASE_PATH_DATA,file_path), 'r') as file:
        for line in file: 
            raw_data.append(json.loads(line))
    df_data = pd.DataFrame(raw_data) # to dataframe
    return df_data

# FUNCTION 2
def add_datetime(df, source_col, end_col, extract_datetime=True, save_path=None):
    """Adds datetime, to extract day, month etc after
    It extracts info from source_col to end_col"""
    
    df[end_col] = df[source_col].apply(lambda x: pd.to_datetime(x, unit='s'))
    
    
    if extract_datetime:
        for i in ['year', 'month', 'day', 'hour', 'minute', 'second']:
            df[i] = df[end_col].apply(lambda x: getattr(x, i))
        df['week_day'] = df[end_col].apply(lambda x: x.weekday())
    if save_path:
        df.to_csv(os.path.join(BASE_PATH_DATA_DF,save_path+'.csv'))
    return df

# FUNCTION 3
def load_transform_files():
    """
    Loads json file made of jsons, and import as pandas df.
    Inputs:
    -----------------
    from_save: bool, import straight enhanced df_points, and others, or not
    Output:
    -----------------
    df_points, df_pois, df_checkins: 3 pandas dataframe
    """
    df_points = load_and_transform_json(file_path='points.json')

    df_points = add_datetime(
        df=df_points, source_col='timestamp', end_col='datetime',
        extract_datetime=True, save_path='df_points')

    df_pois = load_and_transform_json(file_path='pois.json')
    df_pois.to_csv(os.path.join(BASE_PATH_DATA_DF,'df_pois.csv'))
    df_checkins = load_and_transform_json(file_path='checkins.json')

    df_checkins = add_datetime(
        df=df_checkins, source_col='startTimestamp', end_col='start_datetime',
        extract_datetime=False)
    df_checkins = add_datetime(
        df=df_checkins, source_col='endTimestamp', end_col='end_datetime',
        extract_datetime=False, save_path='df_checkins')
    return df_points, df_pois, df_checkins


# FUNCTION 4
def load_df(file_path=None):
    """Loads file_path as pandas df
    Inputs:
    -----------------
    file_path: str, path of file, corresponding to csv file to
    read
    Output:
    -----------------
    df_data: pandas df
    """
    df_data = pd.read_csv(os.path.join(BASE_PATH_DATA_DF,file_path+'.csv'), index_col=0)
    return df_data


BASE_PATH_DATA = "./data/"

BASE_PATH_DATA_DF = "./data/df/"

EARTH_RADIUS = 6371

from sklearn.cluster import DBSCAN

def get_description_cluster(sub_df=None):
    """
    Aggregates values to describe a cluster of gps data into a dict
    Inputs:
    --------------------
    sub_df: a pandas dataframe

    Outputs:
    --------------------
    dict_description: dictionnary of description of cluster
    """
    dict_description = {}
    dict_description['different_hour'] = sub_df['hour'].unique()
    dict_description['min_hour'] = sub_df['hour'].min()
    dict_description['max_hour'] = sub_df['hour'].max()
    dict_description['different_week_day'] = sub_df['week_day'].unique()
    dict_description['min_week_day'] = sub_df['week_day'].min()
    dict_description['max_week_day'] = sub_df['week_day'].max()
    dict_description['horizontal_precision_descr'] = sub_df[
        'horizontal_precision'].describe()
    dict_description['number_points'] = len(sub_df)
    dict_description['time_elapsed'] = {'values': sub_df[
        'time_elapsed'].unique(), 'mean': sub_df['time_elapsed'].unique()}
    return dict_description

    ##Optional function, useful to gather useful information to extract from the clustering, such as the radius of the 
#cluster, the distance to the centroid and to the "mean-point", the stop point proportion of a cluster (a user can pass by the POI)
#

def get_stop_move_and_clusters_user(df_user=None, dict_clust=None,
                                    quantile_diameter_cluster=None):
    """
    From a dataframe of gps locations and clustering results, gives back a dicitonnary
    summarizing clustering and stop points detection for the user.
    Inputs:
    --------------------
    df_user: pandas dataframe of gps locaiton for user.
    dict_clust: output of clustering of points.
    quantile_diameter_cluster: float beteen 0 and 1.
    Outputs:
    --------------------
    dict
    """
    dict_description_clusters = {}
    #We perform the computation on every cluster of our user.
    dfgb = df_user.groupby('label')
    for label, sub_df in dfgb:
        dict_description_clusters[label] = {}
        sub_df['distance_to_centroid'] = np.nan
        centroid = [np.nan, np.nan]
        cluster_mean = {'latitude': sub_df['latitude'].mean(), 'longitude': sub_df[
            'longitude'].mean()}
        lambda_dist_cluster_mean = lambda x: get_haversine(
            a=x, b=cluster_mean)

        sub_df['distance_to_cluster_mid'] = sub_df.apply(
            lambda_dist_cluster_mean, axis=1)
        df_user.loc[sub_df.index, 'distance_to_cluster_mid'] = sub_df[
            'distance_to_cluster_mid']
        df_user.loc[sub_df.index, 'distance_to_centroid'] = sub_df[
            'distance_to_centroid']
        
        # Take quantile instead of max to avoid outliers again
        # We only keep "quantile percent" of the data.
        cluster_radius = sub_df['distance_to_cluster_mid'].quantile(
            quantile_diameter_cluster) / 2
        dist_to_mean_mean = sub_df['distance_to_cluster_mid'].mean()
        dist_to_mean_std = sub_df['distance_to_cluster_mid'].std()
        dict_feat_cluster = get_description_cluster(sub_df=sub_df)
        # Clusters can have both moving and still data
        stop_prop = (df_user['stop_move'] == 0).sum() / len(df_user) * 100
        
        dict_description_clusters[label] = dict(
            stop_prop=stop_prop, dict_feat_cluster=dict_feat_cluster,
            cluster_radius=cluster_radius, cluster_mean=cluster_mean,
            cluster_centroid=centroid,
            dist_to_mean_mean=dist_to_mean_mean,
            dist_to_mean_std=dist_to_mean_std)
    return dict_description_clusters

##We wrap up the previous process into one method:


def get_labels_points(df_points, user_id,
                      fields=['latitude', 'longitude', 'times_cen'],
                      params_clustering=None):
    """This methods labels df_points (label column), as different groups
    of points
    Inputs:
    --------------------
    df_points: pandas Dataframe of geolocalisation of users.
    user_id: str, id of user to label.
    fields: the features to take into consideration.
    Outputs:
    --------------------
    dict_res: dictionnary of results
    """
    mask_user = df_points['user_uuid'] == user_id
    print("In clustering, len mask_user: {}".format(mask_user.sum()))
    df_user = df_points[mask_user]
    data_to_label = df_user[fields]
    # print(data_to_label.head())
    data_to_label = df_user[['latitude', 'longitude']]
    dict_clust = get_clustering_res_dbscan(
        data=data_to_label, eps=0.2/EARTH_RADIUS, min_samples=5)
    df_points.loc[mask_user, 'label'] = dict_clust['cluster']

    return dict(user_id=user_id, df_points=df_points, dict_clust=dict_clust)



def stop_places_labelling(df_points,
                          user_id,
                          quantile_diameter_cluster,
                          min_time_clust):
    """
    from the dataframe of GPS locations, performs all clustering and
    stop points detection.
    Inputs:
    --------------------
    df_points: pandas dataframe of gps locations.
    user_id: str
    quantile_diameter_cluster: float between 0 and 1, to denoise.
    Outputs:‰
    --------------------
    """
    
    ##CLUSTERING
    dict_labels_clustering = get_labels_points(
        df_points=df_points,user_id=user_id)
    
    df_points = dict_labels_clustering['df_points']
    dict_clustering = dict_labels_clustering['dict_clust']
    
    #STOP POINTS
    df_points = label_stop_or_not(df_points=df_points, user_id=user_id,
                                  min_time_clust=min_time_clust)
    
    df_user = df_points[df_points['user_uuid'] == user_id]
    
    ##INFORMATIONS
    dict_description_clusters = get_stop_move_and_clusters_user(
        df_user=df_user, dict_clust=dict_clustering,
        quantile_diameter_cluster=quantile_diameter_cluster)
    
    return df_points, dict_description_clusters

def get_clustering_res_dbscan(data=None, eps=0.05/EARTH_RADIUS, min_samples = 5, ):
    dbs = DBSCAN(eps=eps, min_samples=min_samples,
                 algorithm='ball_tree', metric='haversine')
    clusters = dbs.fit_predict(np.radians(data))
    dict_res = {}
    dict_res['centroids'] = [0, 0]
    dict_res['n_cluster'] = len(np.unique(clusters))
    dict_res['model_clust'] = dbs
    clusters[np.where(clusters == -1)] = -100  # Non clustered data
    clusters = [int(i) for i in clusters]
    dict_res['cluster'] = clusters
    return dict_res

def get_clustering_res_dbscan(data=None, eps=0.05/EARTH_RADIUS, min_samples = 5, ):
    
    ##########
    
    # Initiate DBSCAN 
    dbs = DBSCAN(eps=eps, min_samples=min_samples,
                 algorithm='ball_tree', metric='haversine')
    
    clusters = dbs.fit_predict(np.radians(data))
    
    ##########
    
    
    dict_res = {}
    dict_res['centroids'] = [0, 0]
    dict_res['n_cluster'] = len(np.unique(clusters))
    dict_res['model_clust'] = dbs
    clusters[np.where(clusters == -1)] = -100  # Non clustered data
    clusters = [int(i) for i in clusters]
    dict_res['cluster'] = clusters
    return dict_res


def get_labels_points(df_points, user_id,
                      fields=['latitude', 'longitude', 'times_cen'],
                      params_clustering=None):

    mask_user = df_points['user_uuid'] == user_id
    df_user = df_points[mask_user]
    data_to_label = df_user[fields]
    # print(data_to_label.head())
    data_to_label = df_user[['latitude', 'longitude']]
    dict_clust = get_clustering_res_dbscan(
        data=data_to_label, eps=0.2/EARTH_RADIUS, min_samples=5)
    df_points.loc[mask_user, 'label'] = dict_clust['cluster']

    return dict(user_id=user_id, df_points=df_points, dict_clust=dict_clust)

def label_stop_or_not(df_points=None, user_id=None, min_time_clust=None):
    """Given a clustering, will look the time elapsed
    between entering and exiting cluster.
    if too small : moving.
    else: will request check-in,
    assumes it has  a label
    stop_move = 1 if moves, 0 if stop"""
    """
    Heuristich function, that labels GPS points moving (1) or stop (0), looking
    sequentially at time difference between points.
    We have to do this because a user may do several "visits" in one cluster.
    Inputs:
    --------------------
    df_points: pandas dataframe, gps coordinates for users.
    user_id: user to perform algo on, str. exp: 'u-1'
    min_time_clust: float, minimum time in second to spend in a cluster to be
    labeled stopped.
    Outputs:
    --------------------
    """

    if user_id not in df_points['user_uuid'].unique():
        raise ValueError("Should select appropriate user_id")
    mask_user = df_points['user_uuid'] == user_id
    df_user = df_points[mask_user]
    # prev_row = dfu.ix[0]
    current_label = df_user['label'].values[0]
    time_elapsed = 0
    indx_start = df_user.index[0]
    df_user['stop_move'] = 0
    # Take in consideration previous cluster
    for indx, row in df_user.iterrows():
        if row['label'] != current_label:  # we left a cluster
            # print('changin of clster')
            # print("changin cluster (time elapsed: {})".format(time_elapsed))
            if time_elapsed < min_time_clust:
                # print("not enough time in it !=> moving")
                # Not enough time in cluster
                df_user.loc[indx_start: indx - 1, 'stop_move'] = 1
                df_user.loc[indx_start: indx - 1, 'time_elapsed'] = time_elapsed
            else:
                # print("enough time in it: stop")
                # Enough time in cluster
                df_user.loc[indx_start: indx - 1, 'stop_move'] = 0
                df_user.loc[indx_start: indx - 1, 'time_elapsed'] = time_elapsed
            time_elapsed = 0
            indx_start = indx
            current_label = row['label']
        else:  # We stay in same cluster
            time_elapsed += row['time_diff']
    # End: label last clust:
    if time_elapsed < min_time_clust:
        df_user.loc[indx_start: indx - 1, 'stop_move'] = 1
        df_user.loc[indx_start: indx - 1, 'time_elapsed'] = time_elapsed
    else:
        df_user.loc[indx_start: indx - 1, 'stop_move'] = 0
        df_user.loc[indx_start: indx - 1, 'time_elapsed'] = time_elapsed
    df_points.loc[mask_user, 'stop_move'] = df_user['stop_move']
    df_points.loc[mask_user, 'time_elapsed'] = df_user['time_elapsed']
    return df_points

##Very optional: given the shape of the opening hours of a place, create new dummy features to indicate whether a place is 
#open at a given day / hour.
##Here are Some feature engineering, we create opening hours features, adding the number of checkins per user on given pois and so on.

import ast


def get_date_ts_from_str(date_str=None):
    """From a string of date, gives back date ts"""
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

def get_dict_open_hours(poi=None):
    """
    Subfunction. In order to get dummy variables, first
    processes a dictionnary of opening times.
    """
    opening_hours = ast.literal_eval(poi['opening_hours'])
    dict_open_hours = {}
    days_to_try = [int(i) for i in opening_hours.keys()]
    days_close = [i for i in range(7) if i not in days_to_try]
    #print("days close: {}".format(days_close))
    for ind_day in days_to_try:
        dict_open_hours[ind_day] = {}
        for ind_hour in range(24):
            # try:
            is_open = 0
            if len(opening_hours[str(ind_day)]) > 0:
                for open_spots in opening_hours[str(ind_day)]:
                    if int(open_spots['_1']) <= ind_hour <= int(open_spots['_2']):
                        is_open = 1
            dict_open_hours[ind_day][ind_hour] = is_open
    for ind_day in days_close:
        dict_open_hours[ind_day] = {}
        for ind_hour in range(24):
            dict_open_hours[ind_day][ind_hour] = 0
        # except:
            # print("error")
            # pass
    #assert sum(days_to_try.extend(day_close)) == 19
    return dict_open_hours

def process_opening_hours_one_poi(poi=None):
    """
    Subfunction to get dummy variables on a single POI.
    """
    dict_open_hours = get_dict_open_hours(poi=poi)
    for ind_day in range(7):
        for ind_hour in range(24):
            # All close
            poi['open_at_hour_{}_day_{}'.format(ind_hour, ind_day)] = dict_open_hours[
                ind_day][ind_hour]
    return poi


def process_opening_hours(df_pois=None):
    """
    Feature engineering of the opening hours to create dummy
    variables.
    Inputs:
    --------------------
    df_pois: dataframe of POIS raw, contening opening_hours in columns

    Outputs:
    --------------------
    df_pois_enhanced: containing new dummy variables.
    """

    for ind_day in range(7):
        for ind_hour in range(24):
            df_pois['open_at_hour_{}_day_{}'.format(
                ind_hour, ind_day)] = 0  # all close
    df_pois = df_pois.apply(process_opening_hours_one_poi, axis=1)
    return df_pois


##TOOL function.
def get_pois_open_at_checkin(poi=None, checkin_hours=None, checkin_days=None):
    """
    Given a poi and checkin hours and days, returns if POI is open at given time (boolean)

    """
    is_open_at_checkin_l = [0, ]
    for ind_day in checkin_days:
        for ind_hour in checkin_hours:
            is_open_at_checkin_l.append(
                poi['open_at_hour_{}_day_{}'.format(ind_hour, ind_day)])
    is_open_at_checkin = max(is_open_at_checkin_l)
    return is_open_at_checkin



def get_matrix_checkins(df_checkins, user_list):
    """
    Inputs:
    --------------------
    df_checkins: history of checkins
    user_list: users to consider (list of str)
    Outputs:
    --------------------
    matrix: pd.dataframe with (user_id, poi_id) and number of checkins seen.
    """
    gb = df_checkins.groupby(['name', 'user_uuid'],
                             as_index=False).agg({'id': 'count'})
    matrix = pd.pivot_table(
        data=gb, columns='name', index='user_uuid')['id']
    for user_id in user_list:
        if user_id not in matrix.T.columns:
            matrix.ix[user_id, :] = 0
    matrix = matrix.fillna(0)
    return matrix

def enhance_pois(df_pois, df_checkins, user_list):
    """We expand the df pois indicating the number of previous checkins 
    realized there per user, and similar informations"""
    
    matrix_checkins = get_matrix_checkins(df_checkins, user_list)
    
    missing = list(set(df_pois['name'].unique()).difference(
    set(matrix_checkins.columns)))
    for name in missing:
        matrix_checkins[name] = 0
    
    #Global checkins features
    for user_id in user_list:
        df_pois['nb_checkins_by_user_{}'.format(user_id)] = df_pois.apply(
            lambda x: matrix_checkins[x['name']][user_id], axis=1)
    df_pois['nb_checkins_total'] = df_pois.apply(
        lambda x: matrix_checkins[x['name']].sum(), axis=1)
  
    return df_pois

