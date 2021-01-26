def Q_02(self, full_dataset):
    #Task 2: Takes full_dataset (Pandas dataframe) as input,
    # and returns a revised full_dataset Dataframe after replacing all the non-numeric variables (i.e.,
    # categorical variables) with numeric encoding. Please consider using the "One-hot encoding" scheme
    # i.e., introducing dummy variables. A brief description of the scheme can be found in the READMEs/DUMMY-variables.note.txt
    # file
    import pandas as pd

    ## YOUR CODE HERE ##
    HISPMOM_dummy = pd.get_dummies(full_dataset, columns=['HISPMOM', 'HISPDAD'])
    return HISPMOM_dummy