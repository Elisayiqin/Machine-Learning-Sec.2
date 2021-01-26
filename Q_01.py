def Q_01(self):
    #Task 1: Compute mean, stdev, min, max, 25% percentile, median and 75% percentile of BWEIGHT target variable
    # in the full_dataset, and return the computed values as a numpy array containing these 7 numbers (respectively).


    ## YOUR CODE HERE ##
    import numpy as np
    from numpy import array
    babydataset = self.full_dataset
    mean = babydataset[36].mean()
    stdev = babydataset[36].std()
    min = babydataset[36].min()
    max = babydataset[36].max
    percentile1 = np.percentile(babydataset[36], 25)
    median = babydataset[36].median()
    percentile2 = np.percentile(babydataset[36], 75)
    describe_dataset = array([mean,stdev,min,max,percentile1,median,percentile2])
    return describe_dataset