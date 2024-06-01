"""
This module is used to encode user inputs for the house price prediction model.
"""

def encode_user_inputs(inputs: dict):
    """
    encodes user inputs to the required format for input into the model

    Parameters:
    inputs (dict): Dictionary containing user inputs.

    Returns:
    dict: Dictionary containing the encoded codes
    """
    
    # This dictionary maps the input into its corresponding code
    conversion_dict = {
        'MSSubClass': {
            "1-STORY 1946 & NEWER ALL STYLES": 20,
            "1-STORY 1945 & OLDER": 30,
            "1-STORY W/FINISHED ATTIC ALL AGES": 40,
            "1-1/2 STORY - UNFINISHED ALL AGES": 45,
            "1-1/2 STORY FINISHED ALL AGES": 50,
            "2-STORY 1946 & NEWER": 60,
            "2-STORY 1945 & OLDER": 70,
            "2-1/2 STORY ALL AGES": 75,
            "SPLIT OR MULTI-LEVEL": 80,
            "SPLIT FOYER": 85,
            "DUPLEX - ALL STYLES AND AGES": 90,
            "1-STORY PUD (Planned Unit Development) - 1946 & NEWER": 120,
            "1-1/2 STORY PUD - ALL AGES": 150,
            "2-STORY PUD - 1946 & NEWER": 160,
            "PUD - MULTILEVEL - INCL SPLIT LEV/FOYER": 180,
            "2 FAMILY CONVERSION - ALL STYLES AND AGES": 190
        },
        'MSZoning': {
            "Agriculture": 'A',
            "Commercial": 'C',
            "Floating Village Residential": 'FV',
            "Industrial": 'I',
            "Residential High Density": 'RH',
            "Residential Low Density": 'RL',
            "Residential Low Density Park": 'RP',
            "Residential Medium Density": 'RM'
        },
        'Street': {
            "Paved": 'Pave',
            "Gravel": 'Grvl'
        },
        'Alley': {
            "Paved": 'Pave',
            "Gravel": 'Grvl',
            "No alley access": 'NA'
        },
        'LotShape': {
            "Regular": 'Reg',
            "Slightly irregular": 'IR1',
            "Moderately Irregular": 'IR2',
            "Irregular": 'IR3'
        },
        'LandContour': {
            "Level": 'Lvl',
            "Banked - Quick and significant rise from street grade to building": 'Bnk',
            "Hillside - Significant slope from side to side": 'HLS',
            "Depression": 'Low'
        },
        'Utilities': {
            "All public Utilities (E,G,W,& S)": 'AllPub',
            "Electricity, Gas, and Water (Septic Tank)": 'NoSewr',
            "Electricity and Gas Only": 'NoSeWa',
            "Electricity only": 'ELO'
        },
        'LotConfig': {
            "Inside lot": 'Inside',
            "Corner lot": 'Corner',
            "Cul-de-sac": 'CulDSac',
            "Frontage on 2 sides of property": 'FR2',
            "Frontage on 3 sides of property": 'FR3'
        },
        'LandSlope': {
            "Gentle slope": 'Gtl',
            "Moderate Slope": 'Mod',
            "Severe Slope": 'Sev'
        },
        'Neighborhood': {
            "Bloomington Heights": 'Blmngtn',
            "Bluestem": 'Blueste',
            "Briardale": 'BrDale',
            "Brookside": 'BrkSide',
            "Clear Creek": 'ClearCr',
            "College Creek": 'CollgCr',
            "Crawford": 'Crawfor',
            "Edwards": 'Edwards',
            "Gilbert": 'Gilbert',
            "Iowa DOT and Rail Road": 'IDOTRR',
            "Meadow Village": 'MeadowV',
            "Mitchell": 'Mitchel',
            "North Ames": 'Names',
            "Northridge": 'NoRidge',
            "Northpark Villa": 'NPkVill',
            "Northridge Heights": 'NridgHt',
            "Northwest Ames": 'NWAmes',
            "Old Town": 'OldTown',
            "South & West of Iowa State University": 'SWISU',
            "Sawyer": 'Sawyer',
            "Sawyer West": 'SawyerW',
            "Somerset": 'Somerst',
            "Stone Brook": 'StoneBr',
            "Timberland": 'Timber',
            "Veenker": 'Veenker'
        },
        'Condition1': {
            "Adjacent to arterial street": 'Artery',
            "Adjacent to feeder street": 'Feedr',
            "Normal": 'Norm',
            "Within 200' of North-South Railroad": 'RRNn',
            "Adjacent to North-South Railroad": 'RRAn',
            "Near positive off-site feature--park, greenbelt, etc.": 'PosN',
            "Adjacent to positive off-site feature": 'PosA',
            "Within 200' of East-West Railroad": 'RRNe',
            "Adjacent to East-West Railroad": 'RRAe'
        },
        'Condition2': {
            "Adjacent to arterial street": 'Artery',
            "Adjacent to feeder street": 'Feedr',
            "Normal": 'Norm',
            "Within 200' of North-South Railroad": 'RRNn',
            "Adjacent to North-South Railroad": 'RRAn',
            "Near positive off-site feature--park, greenbelt, etc.": 'PosN',
            "Adjacent to positive off-site feature": 'PosA',
            "Within 200' of East-West Railroad": 'RRNe',
            "Adjacent to East-West Railroad": 'RRAe'
        },
        'BldgType': {
            "Single-family Detached": '1Fam',
            "Two-family Conversion; originally built as one-family dwelling": '2FmCon',
            "Duplex": 'Duplx',
            "Townhouse End Unit": 'TwnhsE',
            "Townhouse Inside Unit": 'TwnhsI'
        },
        'HouseStyle': {
            "One story": '1Story',
            "One and one-half story: 2nd level finished": '1.5Fin',
            "One and one-half story: 2nd level unfinished": '1.5Unf',
            "Two story": '2Story',
            "Two and one-half story: 2nd level finished": '2.5Fin',
            "Two and one-half story: 2nd level unfinished": '2.5Unf',
            "Split Foyer": 'SFoyer',
            "Split Level": 'SLvl'
        },
        'RoofStyle': {
            "Flat": 'Flat',
            "Gable": 'Gable',
            "Gambrel (Barn)": 'Gambrel',
            "Hip": 'Hip',
            "Mansard": 'Mansard',
            "Shed": 'Shed'
        },
        'RoofMatl': {
            "Clay or Tile": 'ClyTile',
            "Standard (Composite)": 'CompShg',
            "Roll": 'Roll',
            "Gravel & Tar": 'Gravl',
            "Membrane": 'Membran',
            "Metal": 'Metal',
            "Wood Shingles": 'WdShngl',
            "Wood Shakes": 'WdShake'
        },
        'Exterior1st': {
            "Asbestos Shingles": 'AsbShng',
            "Asphalt Shingles": 'AsphShn',
            "Brick Common": 'BrkComm',
            "Brick Face": 'BrkFace',
            "Cinder Block": 'CBlock',
            "Cement Board": 'CemntBd',
            "Hard Board": 'HdBoard',
            "Imitation Stucco": 'ImStucc',
            "Metal Siding": 'MetalSd',
            "Other": 'Other',
            "Plywood": 'Plywood',
            "PreCast": 'PreCast',
            "Stone": 'Stone',
            "Stucco": 'Stucco',
            "Vinyl Siding": 'VinylSd',
            "Wood Siding": 'Wd Sdng',
            "Wood Shingles": 'WdShing'
        },
        'Exterior2nd': {
            "Asbestos Shingles": 'AsbShng',
            "Asphalt Shingles": 'AsphShn',
            "Brick Common": 'BrkComm',
            "Brick Face": 'BrkFace',
            "Cinder Block": 'CBlock',
            "Cement Board": 'CemntBd',
            "Hard Board": 'HdBoard',
            "Imitation Stucco": 'ImStucc',
            "Metal Siding": 'MetalSd',
            "Other": 'Other',
            "Plywood": 'Plywood',
            "PreCast": 'PreCast',
            "Stone": 'Stone',
            "Stucco": 'Stucco',
            "Vinyl Siding": 'VinylSd',
            "Wood Siding": 'Wd Sdng',
            "Wood Shingles": 'WdShing'
        },
        'MasVnrType': {
            "Brick Common": 'BrkCmn',
            "Brick Face": 'BrkFace',
            "Cinder Block": 'CBlock',
            "None": 'None',
            "Stone": 'Stone'
        },
        'ExterQual': {
            "Excellent": 'Ex',
            "Good": 'Gd',
            "Average/Typical": 'TA',
            "Fair": 'Fa'
        },
        'ExterCond': {
            "Excellent": 'Ex',
            "Good": 'Gd',
            "Average/Typical": 'TA',
            "Fair": 'Fa',
            "Poor": 'Po'
        },
        'Foundation': {
            "Brick & Tile": 'BrkTil',
            "Cinder Block": 'CBlock',
            "Poured Contrete": 'PConc',
            "Slab": 'Slab',
            "Stone": 'Stone',
            "Wood": 'Wood'
        },
        'BsmtQual': {
            "Excellent (100+ inches)": 'Ex',
            "Good (90-99 inches)": 'Gd',
            "Typical (80-89 inches)": 'TA',
            "Fair (70-79 inches)": 'Fa',
            "Poor (<70 inches & Over": 'Po',
            "No Basement": 'NA'
        },
        'BsmtCond': {
            "Excellent": "Ex",
            "Good": 'Gd',
            "Typical - slight dampness allowed": 'TA',
            "Fair - dampness or some cracking or settling": 'Fa',
            "Poor - Severe cracking or settling": 'Po',
            "No Basement": 'NA'
        },
        'BsmtExposure': {
            "Good Exposure": 'Gd',
            "Average Exposure (split levels or foyers typically)": 'Av',
            "Mimimum Exposure": 'Mn',
            "No Exposure": 'No',
            "No Basement": 'NA'
        },
        'BsmtFinType1': {
            "Good Living Quarters": 'GLQ',
            "Average Living Quarters": 'ALQ',
            "Below Average Living Quarters": 'BLQ',
            "Rec Room": 'Rec',
            "Low Quality": 'LwQ',
            "Unfinshed": 'Unf',
            "No Basement": 'NA'
        },
        'BsmtFinType2': {
            "Good Living Quarters": 'GLQ',
            "Average Living Quarters": 'ALQ',
            "Below Average Living Quarters": 'BLQ',
            "Rec Room": 'Rec',
            "Low Quality": 'LwQ',
            "Unfinshed": 'Unf',
            "No Basement": 'NA'
        },
        'Heating': {
            "Floor Furnace": 'Floor',
            "Gas forced warm air furnace": 'GasA',
            "Gas hot water or steam heat": 'GasW',
            "Gravity furnace": 'Grav',
            "Hot water or steam heat other than gas": 'OthW',
            "Wall furnace": 'Wall'
        },
        'HeatingQC': {
            "Excellent": 'Ex',
            "Good": 'Gd',
            "Average/Typical": 'TA',
            "Fair": 'Fa',
            "Poor": 'Po'
        },
        'CentralAir': {
            "Yes": 'Y',
            "No": 'N'
        },
        'Electrical': {
            "Fuse Box over 60 AMP and all Romex wiring (Average)": 'FuseA',
            "Fuse Box 60 AMP and all Romex wiring (Average/Typical)": 'FuseF',
            "Fuse Box 60 AMP and some Romex wiring": 'FuseP',
            "Mixed": 'Mix',
            "Standard Circuit Breakers & Romex": 'SBrkr'
        },
        'KitchenQual': {
            "Excellent": 'Ex',
            "Good": 'Gd',
            "Average/Typical": 'TA',
            "Fair": 'Fa',
            "Poor": 'Po'
        },
        'Functional': {
            "Major Deductions 2": 'Maj2',
            "Major Deductions 1": 'Maj1',
            "Minor Deductions 2": 'Min2',
            "Minor Deductions 1": 'Min1',
            "Moderate Deductions": 'Mod',
            "Typical Functionality": 'Typ',
            "Salvage only": 'Sal',
            "Severely Damaged": 'Sev'
        },
        'FireplaceQu': {
            "Excellent - Exceptional Masonry Fireplace": 'Ex',
            "Good - Masonry Fireplace in main level": 'Gd',
            "Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement": 'TA',
            "Fair - Prefabricated Fireplace in basement": 'Fa',
            "Poor - Ben Franklin Stove": 'Po',
            "No Fireplace": 'NA'
        },
        'GarageType': {
            "More than one type of garage": '2Types',
            "Attached to home": 'Attchd',
            "Basement Garage": 'Basment',
            "Built-In (Garage part of house - typically has room above garage)": 'BuiltIn',
            "Car Port": 'CarPort',
            "Detached from home": 'Detchd',
            "No Garage": 'NA'
        },
        'GarageFinish': {
            "Finished": 'Fin',
            "Rough Finished": 'RFn',
            "Unfinished": 'Unf',
            "No Garage": 'NA'
        },
        'GarageQual': {
            "Excellent": 'Ex',
            "Good": 'Gd',
            "Average/Typical": 'TA',
            "Fair": 'Fa',
            "Poor": 'Po',
            "No Garage": 'NA'
        },
        'GarageCond': {
            "Excellent": 'Ex',
            "Good": 'Gd',
            "Average/Typical": 'TA',
            "Fair": 'Fa',
            "Poor": 'Po',
            "No Garage": 'NA'
        },
        'PavedDrive': {
            "Paved": 'Y',
            "Partial Pavement": 'P',
            "Dirt/Gravel": 'N'
        },
        'PoolQC': {
            "Excellent": 'Ex',
            "Good": 'Gd',
            "Average/Typical": 'TA',
            "Fair": 'Fa',
            "No Pool": 'NA'
        },
        'Fence': {
            "Good Privacy": 'GdPrv',
            "Minimum Privacy": 'MnPrv',
            "Good Wood": 'GdWo',
            "Minimum Wood/Wire": 'MnWw',
            "No Fence": 'NA'
        },
        'MiscFeature': {
            "Elevator": 'Elev',
            "2nd Garage (if not described in garage section)": 'Gar2',
            "Other": 'Othr',
            "Shed (over 100 SF)": 'Shed',
            "Tenis Court": 'TenC',
            "None": 'NA'
        },
        'SaleType': {
            "Warranty Deed - Conventional": 'WD',
            "Warranty Deed - Cash": 'CWD',
            "Warranty Deed - VA Loan": 'VWD',
            "New Construction": 'New',
            "Court Officer Deed/Estate": 'COD',
            "Contract 15% Down payment regular terms": 'Con',
            "Contract Low Down payment and low interest": 'ConLw',
            "Contract Low Interest": 'ConLI',
            "Contract Low Down": 'ConLD',
            "Other": 'Oth'
        },
        'SaleCondition': {
            "Normal Sale": 'Normal',
            "Abnormal Sale - trade, foreclosure, short sale": 'Abnorml',
            "Adjoining Land Purchase": 'AdjLand',
            "Allocation - two linked properties with separate deeds, typically condo with a garage unit": 'Alloca',
            "Family Sale": 'Family',
            "Home was renovated": 'Partial'
        }
    }

    # Iterate through the input dictionary and convert the values based on the conversion_dict
    for feature in inputs:
        if feature in conversion_dict:
            inputs[feature] = conversion_dict[feature][inputs[feature]]
    
    return inputs
