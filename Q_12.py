def Q_12(self, X_train_scaled, X_test_scaled, y_train, y_test, learning_rate=0.001, nIteration=7000):
    # Task 12: Given the (X_train, y_train) pairs denoting input matrix and output vector respectively,
    # Fit a linear regression model using the stochastic gradient descent algorithm you learned in class to obtain
    # the coefficients, beta's, as a numpy array of m+1 values (Please recall class lecture).
    # Please use the learning_rate and nIteration (number of iterations) parameters in your implementation
    #  of the gradient descent algorithm.
    # Please measure the cpu_time needed during the training step. cpu_time is not equal to the wall_time. So,
    # use time.perf_counter() for an accurate measurement. Documentation on this function can be found here:
    # https://docs.python.org/3/library/time.html
    # Then using the computed beta values, predict the test samples provided in the "X_test_scaled"
    # argument, and let's call your prediction "y_pred".
    # Compute Root Mean Squared Error (RMSE) of your prediction.
    # Finally, return the beta vector, y_pred, RMSE, cpu_time as a tuple.
    # PLEASE DO NOT USE ANY LIBRARY FUNCTION THAT DOES THE LINEAR REGRESSION.
    import random
    random.seed(554433)
    beta = []
    y_pred = []
    RMSE = -1
    cpu_time = 0

    ## YOUR CODE HERE ###



    return (beta, y_pred, RMSE, cpu_time)