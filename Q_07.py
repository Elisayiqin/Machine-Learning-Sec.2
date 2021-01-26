def Q_07(self, X, y):
    # Task 7: Given the X representing the input matrix from the full_dataset,
    #   y being the target vector (the rightmost column of the full_dataset),
    #   randomly split the (X,y) pair dataset into 75% for training and 25% for test using
    #   the library function from the library sklearn.model_selection. Please pass to the train_test_split function
    #   an additional argument random_state=45931
    #   Return the 4 splits: X_train, X_test, y_train, y_test as a tuple

    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split


    X_train = pd.DataFrame()
    X_test = pd.DataFrame()
    y_train = pd.DataFrame()
    y_test = pd.DataFrame()


    ####YOUR CODE HERE###


    return (X_train, X_test, y_train, y_test)