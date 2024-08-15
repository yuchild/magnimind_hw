#!/usr/bin/env python3
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def iris_func():
    """
    Assignment 1 & Submit
    A. Loading Dataset from ScikitLearn
    Step 1: Load iris dataset from ScikitLearn using load_iris(). Assign the dataset to X and the target values to y.
    
    Step 2: Print the dataset keys using iris_dataset.keys()
    Step 3: Print the names of the categories in the target file
    Step 4: Print the feature names in the Iris dataset
    Step 5: Print the type of the Iris dataset.
    Step 6: Print the shape of the Iris dataset.
    Step 7: Print the first five rows of the Iris dataset.
    Step 8: Print the type of the target variable of Iris dataset.
    Step 9: Print the shape of the target variable of Iris dataset.
    Step 10: Print the entire target variable values of the Iris dataset.
    Step 11: Import NumPy with import numpy as np and use the numpy.unique() function to print the unique values of the target variable of Iris dataset
    Step 12: Split dataset into train and test datasets using from sklearn.model_selection import train_test_split
    Step 13: Print the shape of train/test datasets and the train/test target variables.
    Step 14: Build your K-neighbors classifier for nearest neighbor of 1 using from sklearn.neighbors import KNeighborsClassifier, fit the model to your train dataset and make a prediction for the data point of [5, 1.9, 1, 0.2]. Print your prediction class value as an integer and also the corresponding string label.
    """
    # Step 1:
    iris = load_iris()
    
    X = iris.data
    y = iris.target
    
    # Step 2:
    keys = iris.keys()
    
    # Step 3:
    target_names = iris.target_names 

    # Step 4:
    feature_names = iris.feature_names
    
    # Step 5:
    df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
    
    data_types = df.dtypes
    
    # Step 6:
    data_shape = df.shape
    
    # Step 7:
    first_five = df.head(5)
    
    # Step 8:
    target_data_type = y.dtype
    
    # Step 9:
    target_shape = y.shape
    
    # Step 11:
    target_unique = np.unique(y)
    
    # Step 12:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Step 14:
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    
    new_data_point = [5, 1.9, 1, 0.2]
    prediction = knn.predict([new_data_point])
    prediction_class_value = prediction[0]
    
    prediction_class_label = iris.target_names[prediction_class_value]
    
    return print(f'Iris dataset keys: {keys}\nIris target names: {target_names}\nIris feature names: {feature_names}\nIris data types: {data_types}\nIris data shape: {data_shape}\nIris first 5 rows: {first_five}\nTarget data type: {target_data_type}\nTarget shape: {target_shape}\nTarget values: {y}\nUnique target variable names: {target_unique}\nX Train Shape: {X_train.shape}\nX Test Shape: {X_test.shape}\nX Train Shape: {y_train.shape}\nX Train Shape: {y_test.shape}\nPredicted class value (integer): {prediction_class_value}\nPredicted class label (string): {prediction_class_label}')


def auto_func():
    """
    Loading a Dataset and exploring it
    Step 1: Import the modules needed to explore the data
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    Step 2: Import auto_mpg.csv dataset using pandas'read_csv function. Print the first three samples from your dataset, print the index range of the observations, and print the column names of your dataset

    Step 3: Assign mpg column as output and name it as y and the rest of the data as the features and assign it to X. Print the shape of X.

    Step 4: Bonus: Check the dataset if there are any missing values in any of the columns using isnull().any() functions.

    Step 5: Check the data types of each feature. Which columns are continuous and which are categorical?

    Step 6: Look at the unique elements of horsepower

    Step 7: Let's describe data since everything looks in order. See the statistical details of the dataset using describe and info methods.
    
    Step 8: Let's specifically look at the description of the mpg feature

    Step 9: Visualize the distribution of the features of the data using hist method, use bins=20.

    Step 10: BONUS: Visualize the relationships between these data points.

    Create a function to scale your dataset by using the formula b = x-minmax-minb = (x - min) / (max - min)

    Using this function, scale displacement, horsepower, acceleration, weight, and mpg.

    Create a boxplot of mpg for different origin values before and after scaling.

    Please add the URL of the assignments you uploaded to Github to the Online Text section.
    """

    # Step 2: load data
    auto_df_raw = pd.read_csv('./data/auto_mpg.csv')
    auto_df = auto_df_raw.copy()
    
    # Step 3: set X and y
    y = auto_df['mpg'].copy()
    X = auto_df.drop('mpg', axis=1).copy()
    
    # Step 4: check for nulls in columns
    null_check = auto_df.isnull().any()
    
    # Step 5: check for data types of columns for continuous or categorical
    data_types = auto_df.dtypes
    continuous_columns = auto_df.select_dtypes(include=['int64', 'float64']).columns
    categorical_columns = auto_df.select_dtypes(include=['object', 'category']).columns
    
    # Step 6: unique elements of horsepower
    unique_horsepower = np.unique(auto_df['horsepower'])
    
    # Step 9: visualize continuous data
    # Calculate the number of rows and columns for the grid
    num_features = len(continuous_columns)
    num_cols = 2  # Number of columns in the grid
    num_rows = (num_features + num_cols - 1) // num_cols  # Calculate number of rows needed

    # Set up the matplotlib figure
    plt.figure(figsize=(11, num_rows * 4))  # Adjust height to fit all rows

    # Plot histograms for each feature
    for i, feature in enumerate(auto_df[continuous_columns]):
        plt.subplot(num_rows, num_cols, i + 1)  # Position of subplot
        plt.hist(auto_df[feature], bins=20, edgecolor='black')
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()
    
    # Step 10: scale columns
    
    def scale(x, maximum, minimum):
        return (x - minimum) / (maximum - minimum)
    
    scaled_raw = auto_df[['displacement', 'horsepower', 'acceleration','weight', 'mpg']].copy()
    
    scaled_df = scaled_raw.apply(lambda row: scale(row, row.max(), row.min()))
    
    # Plot
    plt.figure(figsize=(8, 6))

    # Plot box plots for each type
    plt.subplot(1,2,1)
    plt.boxplot(auto_df['mpg'])
    plt.title(f'Original')

    plt.subplot(1,2,2)
    plt.boxplot(scaled_df['mpg'])
    plt.title(f'Scaled')

    plt.tight_layout()
    plt.show()
    
    return print(f"Sample data (3): {auto_df.sample(3)}\nIndex range: {auto_df.index}\nColumn names: {auto_df.columns}\nShape of X: {X.shape}\nMissing values in columns: {null_check}\nColumn data types: {data_types}\nContinuous columns: {continuous_columns}\nCategorical columns: {categorical_columns}\nUnique horsepower: {unique_horsepower}\nDescribe: {auto_df.describe().T}\nInfo: {auto_df.info()}\nDescribe mpg: {auto_df.describe()['mpg']}")

if __name__ == "__main__":
    iris_func()
    auto_func()
    
    
    
    