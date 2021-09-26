"""stats"""

def my_mean(samples):
    """function to get mean"""
    num = len(samples)
    mumu = (1/num) * sum(samples)
    return mumu

def my_standard_deviation(samples):
    """function to get stdeva"""
    num = len(samples)
    mumu = my_mean(samples)
    diff_list = [(sample - mumu)**2 for sample in samples]
    sigma = (1/(num - 1) * sum(diff_list))**0.5
    return sigma

def my_median(samples):
    """Function to get median"""
    samples.sort()
    if len(samples)%2 != 0:
        ind = int((len(samples) - 1)/2)
        return samples[ind]
    ind = int(len(samples)/2)
    return (samples[ind] + samples[ind-1])/2

def my_quartiles(samples):
    """Expected to return a list of float or int => [Q1, Q2, Q3]"""
    samples.sort()
    if len(samples)%2 == 0:
        ind = int(len(samples)/2)
        return [my_median(samples[:ind]), my_median(samples), my_median(samples[ind:])]
    ind = int((len(samples)-1)/2)
    return [my_median(samples[:ind+1]), my_median(samples), my_median(samples[(ind):])]

def my_mode(samples):
    """Function to get mode"""
    mode = []
    samples = sorted(samples,key=samples.count,reverse=True)
    mode.append(samples[0])
    occ = samples.count(samples[0])
    for i in range(occ, len(samples)):
        if samples.count(samples[i]) == occ:
            mode.append(samples[i])
    mode = list(dict.fromkeys(mode))
    if len(mode) > 1:
        return None
    return mode[0]
