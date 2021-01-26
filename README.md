# Machine-Learning-Sec.2
Dataset Description
In the “dataset/” you will find two csv and a txt files:

• baby-weights-dataset.csv

It has 101400 rows (samples) with 37 columns (variables). Each sample represents a case of a new-born. Very last column is "BWEIGHT", that tells the true weight of the new-born (in lbs unit). Actually, this needs to be considered as the target variable here.

• data-description.txt

Here, you will find the names of the 37 variables used in the dataset above. And, the source of the dataset did not offer me description of every single of them. But, after studying about them, I could elaborate only few of them. Please pardon my laziness. Okay, this file contains few descriptions for the variables. All the rest are mostly talking about the Mother's medical history and all. No big deal, I guess, for you to work with these variables without knowing their meaning.

• judge-without-label.csv

This is an interesting file. It contains new samples: additional 2001 rows with 36 columns
(without the BWEIGHT target column). Once again, this should be part of the training, as there are no ground truth target labels, right? Once the training is complete with the dataset provided above, you may want to apply your prediction algorithm to predict BWEIGHT values of these 2001 samples. We (me and the TA) will evaluate that as well.

Q_01.py（分析数据大体趋势，数据EDA）

Compute mean, stdev, min, max, 25% percentile, median and 75% percentile of BWEIGHT target variable in the full_dataset, and return the computed values as a numpy array containing these 7 numbers (respectively).


Q_02.py（将分类型的数据进行one-hot encoding）

Takes full_dataset (Pandas dataframe) as input, and returns a revised full_dataset Dataframe after replacing all the non-numeric variables (i.e., categorical variables) with numeric encoding. Please consider using the "One-hot encoding" scheme i.e., introducing dummy variables. A brief description of the scheme can be found in the READMEs/DUMMY-variables.note.txt file


Q_03.py（检查missing value）

Given the full_dataset (Pandas Dataframe), check if there are missing values, and if yes, count how many, and impute the missing values with corresponding mean values. Finally, return the counting result as a Pandas dataframe with 2 columns {variable_name,num_of_missing_values). Please make sure the result lists all the variables (including the target) in the given dataset. 

Q_04.py （算相关性进行排列）

Given a full_dataset (Pandas dataframe) where all the categorical variables are already replaced with numeric values, return a list of top 20 highly correlated variables (with respect to the target variable) as a Pandas dataframe with 2 columns {variable,corr_score}. The corr_score between a variable x and the target variable y needs to be computed using the Pearson Correlation Coefficient.

Q_05.py （sort排序）

Given a full_dataset (as Pandas dataframe) having all the 37 columns and certain number of rows and columns_to_keep (as Pandas Dataframe) having 2 columns {variable_name,corr_score_with_target} similar to the one you computed in Q_04. Please return a reduced full_dataset keeping only the columns listed in the columns_to_keep dataframe..

Q_06.py

Separate the full_dataset into two parts: X and y, where X denotes the input matrix containing only the input variables, and y denotes the target vector containing only the target values for exactly the same number of samples in the given full_dataset (pandas Dataframe). Finally, return X and y as a tuple.

Q_07.py（将dataset和target分成训练集，测试集）

Given the X representing the input matrix from the full_dataset, y being the target vector (the rightmost column of the full_dataset), randomly split the (X,y) pair dataset into 75% for training and 25% for test using the library function from the library sklearn.model_selection. Please pass to the train_test_split function an additional argument random_state=45931 .
Return the 4 splits: X_train, X_test, y_train, y_test as a tuple

Q_08.py（min-max归一化）

Given the 4 splits denoting the training and test dataset, Apply min-max scaling on the training dataset (X_train). Then scale the test dataset based on the metrics you obtain when you scale the training dataset. PLEASE DO NOT SCALE y_train and y_test. Finally, return as a tuple the scaled X_train, X_test and the intact y_train and y_test.

Q_09.py（标准化）

Given the 4 splits denoting the training and test dataset, Apply standardization (i.e., normalization) scaling on the training dataset (X_train). Then scale the test dataset based on the metrics you obtain when you scale the training dataset. PLEASE DO NOT SCALE y_train and y_test. Finally, return as a tuple the scaled X_train, X_test and the intact y_train and y_test.

Q_10.py（用close-form进行线性回归，也就是不用第三方库，自己根据线性回归原理设计算法）

Given the (X_train, y_train) pairs denoting input matrix and output vector respectively, Fit a linear regression model using the closed-form solution you learned in class to obtain the coefficients, beta's, as a numpy array of m+1 values. Then using the computed beta values, predict the test samples provided in the "X_test_scaled" argument, and let's call your prediction "y_pred". Compute Root Mean Squared Error (RMSE) of your prediction. Finally, return the beta vector, y_pred, RMSE as a tuple. PLEASE DO NOT USE ANY LIBRARY FUNCTION THAT DOES THE LINEAR REGRESSION.

Q_11.py（用batch梯度下降法进行拟合和预测）

Given the (X_train, y_train) pairs denoting input matrix and output vector respectively, Fit a linear regression model using the batch gradient descent algorithm to obtain the coefficients, beta's, as a numpy array of m+1 values. Please use the learning_rate and nIteration (number of iterations) parameters in your implementation of the gradient descent algorithm. Please measure the cpu_time needed during the training step. cpu_time is not equal to the wall_time. So, use time.perf_counter() for an accurate measurement. Documentation on this function can be found here: https://docs.python.org/3/library/time.html Then using the computed beta values, predict the test samples provided in the "X_test_scaled" argument, and let's call your prediction "y_pred". Compute Root Mean Squared Error (RMSE) of your prediction. Finally, return the beta vector, y_pred, RMSE, cpu_time as a tuple. PLEASE DO NOT USE ANY LIBRARY FUNCTION THAT DOES THE LINEAR REGRESSION

Q_12.py（随机梯度下降法）

Given the (X_train, y_train) pairs denoting input matrix and output vector respectively, Fit a linear regression model using the stochastic gradient descent algorithm you learned in class to obtain the coefficients, beta's, as a numpy array of m+1 values (Please recall class lecture). Please use the learning_rate and nIteration (number of iterations) parameters in your implementation of the gradient descent algorithm. Please measure the cpu_time needed during the training step. cpu_time is not equal to the wall_time. So, use time.perf_counter() for an accurate measurement. Documentation on this function can be found here: https://docs.python.org/3/library/time.html Then using the computed beta values, predict the test samples provided in the "X_test_scaled" argument, and let's call your prediction "y_pred". Compute Root Mean Squared Error (RMSE) of your prediction. Finally, return the beta vector, y_pred, RMSE, cpu_time as a tuple.
PLEASE DO NOT USE ANY LIBRARY FUNCTION THAT DOES THE LINEAR REGRESSION

Q_13.py（迷你batch梯度下降法）

Given the (X_train, y_train) pairs denoting input matrix and output vector respectively, Fit a linear regression model using the mini-batch gradient descent algorithm you learned in class to obtain the coefficients, beta's, as a numpy array of m+1 values. Please use the batch_size, learning_rate and nIteration (number of iterations) parameters in your implementation of the gradient descent algorithm. Please measure the cpu_time needed during the training step. PLEASE DO NOT USE ANY LIBRARY FUNCTION THAT DOES THE LINEAR REGRESSION.

Q_14.py（以上三种算法的预测RMSE的比较）

Given the 3 sets of tuples from the 3 experiments with batch gradient descent, stochastic gradient descent and mini-batch gradient descent, return a string from the set {"batch-GD", "stochastic-GD", "minibatch-GD"} that demonstrated the best predictive performance in terms of RMSE.

Q_15.py （以上三种算法的训练时间比较）

Given the 3 sets of tuples from the 3 experiments with batch gradient descent, stochastic gradient descent and mini-batch gradient descent, return a string from the set {"batch-GD", "stochastic-GD", "minibatch-GD"} that demonstrated the least training time.


Q_16.py（改变学习率分析对不同线性回归模型的影响）

Given the (X_train, y_train) pairs denoting input matrix and output vector respectively, call your implementation of Q_15(): stochastic gradient descent based linear regression for each of these learning rates: {0.0001, 0.001, 0.05, 0.01, 0.1, 1.0} Please use the nIteration (number of iterations) parameters in your implementation of the gradient descent algorithm. For each of the linear regression model, using the computed beta values, predict the test samples provided in the "X_test_scaled" argument, and let's call your prediction "y_pred". Compute Root Mean Squared Error (RMSE) of your prediction. Finally, return the learning rate that shows the best test performance, and also return as part of a tuple besides the learning rate, the beta's representing the best performing linear regression model, and a pandas dataframe named summary with 2 columns: {learning_rate, test_RMSE} containing RMSE's of the 6 linear regression models.

Q_17.py （用最好的模型预测）

Utilizing the best trained linear regression model (so far), predict the target for each of the samples in the judge_dataset. Return only a vector, y_pred, as a numpy array the predicted target values.
