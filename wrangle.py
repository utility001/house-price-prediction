import pandas as pd
from sklearn.model_selection import train_test_split

def ingest_and_split_train_val():
    """
    Reads 'train.csv' file located at 'datasets' into a DataFrame 
    then split into train and validation set. 
    
    Returns:
        DataFrame, DataFrame: The training and validation sets.
    """
    df = pd.read_csv('dataset/train.csv', index_col='Id')
    train, val = train_test_split(
        df, test_size=0.2, 
        stratify=df['Neighborhood'], 
        shuffle=True, random_state=42)
    return train, val


def wrangle(df):
    """
    Performs wrangling Operation
    
    Should only be used on 'train.csv' and 'test.csv' located in 'datasets' folder
    It is not guaranteed to work elsewhere, you may need to pull up the code and 
    modify it to your needs
    """
    # Numeric to categoricals
    cats = ["MSSubClass", "OverallCond", "OverallQual", "MoSold"]
    df[cats] = df[cats].astype(object)
    
    # Drop imbalanced columns
    df = df.drop(columns=[
         'Street', 'Utilities',
         'LandSlope', 'Condition2',
         'RoofMatl', 'Heating',
         'LowQualFinSF', 'KitchenAbvGr',
         'GarageQual', 'GarageCond',
         '3SsnPorch', 'PoolArea',
         'MiscVal'])

    # Add age columns
    df["Age"] = df["YrSold"] - df["YearBuilt"]
    df["RemodAddAge"] = df["YrSold"] - df["YearRemodAdd"]
    df["GrgAge"] = df["YrSold"] - df["GarageYrBlt"]

    # Drop year columns
    df = df.drop(columns=[
        'YearBuilt', 'YearRemodAdd', 
        'GarageYrBlt', 'YrSold'])

    # Skewed Half bath
    df = df.drop(columns=["BsmtHalfBath"])

    # Drop cols with > 90% missing values
    df = df.drop(columns=[
        'Alley', 'LandContour',
        'CentralAir', 'Electrical',
        'Functional', 'PavedDrive',
        'PoolQC', 'MiscFeature'])

    return df