MIN_STOP_TIME = 60
MIN_STOP_PROP = 0.8
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

