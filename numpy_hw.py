#!/usr/bin/env python3

import numpy as np

def house_features():
    """
    1- Create three lists representing house features, each list containing ten values. The first one for the house's size in square meters, the second one for rooms and last for price. Then, create an array combining these lists.
    
    2- Transpose the array you have created, so that every line can represent features of one house.
    """
    house_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    house_size = [123, 156, 112, 234, 134, 145, 178, 167, 189, 115]
    rooms = [4, 4, 3, 6, 4, 5, 5, 4, 5, 3]
    price = [600000, 750000, 550000, 900000, 450000, 500000, 750000, 600000, 750000, 470000]
    
    house_features = np.array([house_id, house_size, rooms, price])
    
    return print(f'{house_features.T}')

    
def earthquake_3_4():
    """
    3- Display the shape of the array and explain what it means.
    For the following assignment, you are going to use Earthquakes dataset.

    4- Load the Earthquakes dataset. Export the dataset to an array as you covered in the previous lesson.
    """
    
    earthquakes_csv_file_path = './data/earthquakes1970-2014.csv'
    earthquakes_array_csv_file_path = './data/earthquakes1970-2014_array.csv'
    data = np.genfromtxt(earthquakes_csv_file_path, delimiter=',', dtype=None, names=True, skip_header=1, encoding='utf-8')
    
    # Extract the fields and stack them into a 2D array
    data_2d = np.column_stack([data[field] for field in data.dtype.names])
    
    # Convert to string format
    data_str = np.array([list(row) for row in data_2d.astype(str)])
    
    np.savetxt(earthquakes_array_csv_file_path, data_str, delimiter=',', fmt='%s')
    
    return print(f'Dimensions: {data_2d.ndim}\nShape: {data_2d.shape}\nThe array is 1d with 5404 rows of earthquake measurements\nArray saved to {earthquakes_array_csv_file_path}')
    
    
def earthquake_5_6_7_8():
    """
    5- Slice first 20 rows and column numbers 3, 5, 6, 7, 12. Then, assign the array you sliced to a variable.
    
    6- Display the row numbers where last values are equal to 4.5 or higher.

    7- Assign 1 to first row.

    8- Save the final state of the array to disk. You are going to use this in the next assignment.
    """
    
    earthquakes_csv_file_path = './data/earthquakes1970-2014.csv'
    data = np.genfromtxt(earthquakes_csv_file_path, delimiter=',', dtype=None, names=True, skip_header=1, encoding='utf-8')
    
    # reshape data
    # Extract the fields and stack them into a 2D array
    data_2d = np.column_stack([data[field] for field in data.dtype.names])

    # 5 Slice first 20 rows and column numbers 3, 5, 6, 7, 12, but 6 is string, so 7 and 8
    data_2d = data_2d[:20, [2, 4, 6, 8, 11]].copy()
    
    # 6
    row_nums = np.where(data_2d[:, -1].astype(float) >= 4.5)[0]
    
    # 7
    data_2d[0, :] = 1
    
    # 8
    np.save('./results/earthquake_results1_8.npy', data_2d)
    
    return print(f'Rows with last value >= 4.5: {row_nums}')


def earthquake_9_10_11_12():
    """
    9- Load the array you saved in the previous lesson from the disk.

    10- Display the mean and the standard deviation for each column.

    11- Subtract 1, 25, 25, 10, 4 from columns in order. (Remember it can be dobe in one line of code.)

    12- Multiply each element by 2. (Remember it can be done in one line of code.)
    """
    
    # 9 
    data = np.load('./results/earthquake_results1_8.npy')
    
    # Select numeric columns
    numeric_data = data.astype(float)
    
    # 10
    col_mu = np.mean(numeric_data, axis=0)
    col_std = np.std(numeric_data, axis=0) 
    
    # 11      
    numeric_data -= np.array([1, 25, 25, 10, 4])   
    
    # 12
    numeric_data *= 2    
    
    # save results of 9 through 12
    np.save('./results/earthquake_results9_12.npy', numeric_data)
    
    return print(f'Column Means: {col_mu}/nColumn Standard Deviations: {col_std}')
    
    
if __name__ == "__main__":
    house_features()
    earthquake_3_4()
    earthquake_5_6_7_8()
    earthquake_9_10_11_12()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    