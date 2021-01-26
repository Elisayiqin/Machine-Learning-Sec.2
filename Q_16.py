def Q_16(self, X_train_scaled, X_test_scaled, y_train, y_test, nIteration=7000):
    # Task 16: Given the (X_train, y_train) pairs denoting input matrix and output vector respectively,
    # call your implementation of Q_15(): stochastic gradient descent based linear regression for each of these
    # learning rates: {0.0001, 0.001, 0.05, 0.01, 0.1, 1.0}
    # Please use the nIteration (number of iterations) parameters in your implementation
    #  of the gradient descent algorithm.
    # For each of the linear regression model, using the computed beta values,
    # predict the test samples provided in the "X_test_scaled" argument, and let's call your prediction "y_pred".
    # Compute Root Mean Squared Error (RMSE) of your prediction.
    # Finally, return the learning rate that shows the best test performance, and
    # also return as part of a tuple besides the learning rate,  the beta's representing the best
    # performing linear regression model, and a pandas dataframe named summary with 2 columns:
    # {learning_rate, test_RMSE} containing RMSE's of the 6 linear regression models.
    # PLEASE DO NOT USE ANY LIBRARY FUNCTION THAT DOES THE LINEAR REGRESSION.
    import random
    import pandas as pd
    random.seed(554433)
    beta = []
    y_pred = []
    RMSE = -1
    learning_rate = -1
    summary = pd.DataFrame()

    ## YOUR CODE HERE ###



    return (learning_rate, beta, summary)