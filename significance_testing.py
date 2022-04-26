from scipy import stats

def significance_test(arr, points_dict):

''''Built to test a series of points and check signifiance relative to 
different regions/data points; basic design is from scipy function, but 
need it to be slightly more flexible for multiple region needs.

Define statistical significance as anything in 97.5th percentile and 
above or 2.5th percentile and below.

arr contains either POS, NEG, or NEU frequencies.
points_dict contains keys of regions and values of frequencies.'''

    significant = []
    for key in points_dict:
        percentile = stats.percentileofscore(arr, points_dict[key])
        if percentile <= 2.5 or percentile >= 97.5:
            significant.append(key)

    return significant