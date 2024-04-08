import pandas as pd

def missing_data(data, show_all=True):
    """
    Calculate the number and percentage of missing values for each column in a DataFrame.
    
    Parameters:
        data (DataFrame): The input DataFrame.
        show_all (bool): Whether to show all columns regardless of missing values. Default is True.
    
    Returns:
        DataFrame: A DataFrame containing the number and percentage of missing values for each column.
                   If show_all is True, all columns are included. If show_all is False, only columns
                   with missing values are included.
    """
    # Calculate total missing values for each column
    total = data.isnull().sum()
    # Calculate percentage of missing values for each column
    percent = (data.isnull().sum() / data.isnull().count() * 100)
    # Concatenate total and percent missing values into a DataFrame
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    
    # Get data types of each column
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['Types'] = types
    
    # Return either all columns or only columns with missing values based on show_all parameter
    if show_all:
        return tt
    else:
        return tt[tt['Total'] > 0]


def find_constant_columns(data):
    """
    Find columns in a DataFrame containing constant values.

    Parameters:
        data (DataFrame): The input DataFrame.

    Returns:
        list: A list containing the names of columns with constant values.
    """
    constant_columns = []
    for column in data.columns:
        # Get unique values in the column
        if data[column].nunique() == 1:
            constant_columns.append(column)
    return constant_columns



import pandas as pd

def unique_values(data, max_colwidth=50):
    """
    Get unique values for each column in a DataFrame.

    Parameters:
        data (DataFrame): The input DataFrame.
        max_colwidth (int): Maximum width for displaying column values. Default is 50.

    Returns:
        DataFrame: A DataFrame containing the total count, number of unique values,
                   and unique values for each column.
    """
    # Set maximum column width for display
    pd.options.display.max_colwidth = max_colwidth
    
    # Count total values in each column
    total = data.count()
    
    # Create a DataFrame with total values
    tt = pd.DataFrame(total, columns=['Total'])
    
    # Initialize lists for unique values and their counts
    uniques = []
    values = []
    
    # Iterate over each column
    for col in data.columns:
        # Get unique values and their count for the column
        unique_values = data[col].unique()
        unique_count = data[col].nunique()
        
        # Append unique values and their count to respective lists
        values.append([unique_values])
        uniques.append(unique_count)
    
    # Add columns for unique values and their counts to the DataFrame
    tt['Uniques'] = uniques
    tt['Values'] = values
    
    # Sort DataFrame by number of unique values
    tt = tt.sort_values(by='Uniques', ascending=True)
    
    return tt


# Mini describe
def mini_describe(data, column_name):
    """
    Get Mini description of numeric data
    """
    desc = pd.DataFrame(data.describe().loc[:, column_name]).T
    desc["Range"] = desc["max"] - desc['min']
    desc['IQR'] = desc['75%'] - desc["25%"]
    return desc


# Get highly imbalanced features
import pandas as pd

def get_highly_imbalanced_columns(df, threshold=0.9):
    """
    Get the names of categorical columns where any category constitutes more than a specified threshold.
    
    Parameters:
    - df: pandas DataFrame
        The input DataFrame containing categorical columns.
    - threshold: float (default=0.9)
        The threshold percentage (0 to 1) for identifying highly imbalanced categories.

    Returns:
    - list
        A list of column names (strings) representing highly imbalanced categorical columns.
    """
    highly_imbalanced_columns = []
    
    # Iterate over columns
    for col in df.columns:
        category_counts = df[col].value_counts(normalize=True)
        max_percentage = category_counts.max()
        if max_percentage > threshold:
            highly_imbalanced_columns.append(col)
    
    return highly_imbalanced_columns