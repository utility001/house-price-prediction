import streamlit as st
import joblib
import numpy as np
import pandas as pd

from wrangle import wrangle_year
from encode_user_inputs import encode_user_inputs

# Load the trained model
with open('model/elastic_pipeline.pkl', 'rb') as file:
    model = joblib.load(file)
# model = pickle.load(open('model/elastic_pipeline.pkl', 'rb'))

def predict_price(features):
    features = encode_user_inputs(features)
    features = pd.DataFrame(features, index=[0])
    features = wrangle_year(features)
    # st.write(features)
    price = model.predict(features)
    return price[0]


navigation = st.sidebar.radio('Select an Option', ('Usage', 'Live Demo'))

if navigation == "Usage":
    st.title("House Price Prediction App")
    st.write(
        """
### Welcome to the Live Demonstration of the **Real Estate Price Prediction App!** 
        
This tool is designed to assist **real estate professionals** in making informed decisions by **predicting property prices based on various key features**. Whether you're a seasoned realtor or just starting out in the industry, this app provides valuable insights to help you navigate the complex world of real estate.

Using **advanced machine learning techniques**, this app analyzes a wide range of property attributes such as location, size, condition, and amenities **to generate accurate price predictions**. From the type of property and its architectural style to details about the neighborhood and surrounding area, our app takes into account every factor that can influence property values.

**All you need to do** is to simply input the relevant information about the property you're interested in, and let our app do the rest! Whether you're evaluating a potential investment opportunity, determining the optimal listing price, or advising clients on their real estate decisions, our app is your trusted partner in the world of real estate.


##### Click on **"Live Demo"** on the left panel to get started
        """
    )
    
elif navigation == "Live Demo":
    st.title("Predict House Prices")

    st.write(
        """
        Input the characteristics of **your property** in the form below to get started.
        """
    )

    with st.form("prediction_form"):
        MSSubClass = st.selectbox("Building Class", [
            "1-STORY 1946 & NEWER ALL STYLES",
            "1-STORY 1945 & OLDER",
            "1-STORY W/FINISHED ATTIC ALL AGES",
            "1-1/2 STORY - UNFINISHED ALL AGES",
            "1-1/2 STORY FINISHED ALL AGES",
            "2-STORY 1946 & NEWER",
            "2-STORY 1945 & OLDER",
            "2-1/2 STORY ALL AGES",
            "SPLIT OR MULTI-LEVEL",
            "SPLIT FOYER",
            "DUPLEX - ALL STYLES AND AGES",
            "1-STORY PUD (Planned Unit Development) - 1946 & NEWER",
            "1-1/2 STORY PUD - ALL AGES",
            "2-STORY PUD - 1946 & NEWER",
            "PUD - MULTILEVEL - INCL SPLIT LEV/FOYER",
            "2 FAMILY CONVERSION - ALL STYLES AND AGES"
        ])

        MSZoning = st.selectbox("General Zoning Classification", [
            "Agriculture",
            "Commercial",
            "Floating Village Residential",
            "Industrial",
            "Residential High Density",
            "Residential Low Density",
            "Residential Low Density Park",
            "Residential Medium Density"
        ])

        LotFrontage = st.number_input("Linear feet of street connected to property", 21, 320, 200, 1)
        LotArea = st.number_input("Lot Area in square feet", 1300, 215000, 20000, 1)

        LotShape = st.selectbox("General shape of property", [
            "Regular",
            "Slightly irregular",
            "Moderately Irregular",
            "Irregular"
        ])

        LotConfig = st.selectbox("Lot configuration", [
            "Inside lot",
            "Corner lot",
            "Cul-de-sac",
            "Frontage on 2 sides of property",
            "Frontage on 3 sides of property"
        ])

        Neighborhood = st.selectbox("Physical locations within Ames city limits", [
            "Bloomington Heights",
            "Bluestem",
            "Briardale",
            "Brookside",
            "Clear Creek",
            "College Creek",
            "Crawford",
            "Edwards",
            "Gilbert",
            "Iowa DOT and Rail Road",
            "Meadow Village",
            "Mitchell",
            "North Ames",
            "Northridge",
            "Northpark Villa",
            "Northridge Heights",
            "Northwest Ames",
            "Old Town",
            "South & West of Iowa State University",
            "Sawyer",
            "Sawyer West",
            "Somerset",
            "Stone Brook",
            "Timberland",
            "Veenker"
        ])

        Condition1 = st.selectbox("Proximity to various conditions", [
            "Adjacent to arterial street",
            "Adjacent to feeder street",
            "Normal",
            "Within 200' of North-South Railroad",
            "Adjacent to North-South Railroad",
            "Near positive off-site feature--park, greenbelt, etc.",
            "Adjacent to positive off-site feature",
            "Within 200' of East-West Railroad",
            "Adjacent to East-West Railroad"
        ])

        BldgType = st.selectbox("Type of dwelling", [
            "Single-family Detached",
            "Two-family Conversion; originally built as one-family dwelling",
            "Duplex",
            "Townhouse End Unit",
            "Townhouse Inside Unit"
        ])

        HouseStyle = st.selectbox("Style of dwelling", [
            "One story",
            "One and one-half story: 2nd level finished",
            "One and one-half story: 2nd level unfinished",
            "Two story",
            "Two and one-half story: 2nd level finished",
            "Two and one-half story: 2nd level unfinished",
            "Split Foyer",
            "Split Level"
        ])

        OverallQual = st.slider("Overall quality", 1, 10, 5, 1)
        OverallCond = st.slider("Overall condition", 1, 10, 5, 1)
        YrSold = st.slider("Year Sold", 1984, 2010, 2005, 1)
        YearBuilt = st.slider("Original Construction year", 1984, 2010, 2005, 1)
        YearRemodAdd = st.slider(
            "Remodel date (same as construction date if no remodeling or additions)",
            1984, 2010, 2005, 1000
        )
        GarageYrBlt = st.slider(
            "The garage was built in which year?", 1984, 2010, 2005, 1)

        RoofStyle = st.selectbox("Type of roof", [
            "Flat",
            "Gable",
            "Gambrel (Barn)",
            "Hip",
            "Mansard",
            "Shed"
        ])

        Exterior1st = st.selectbox("Exterior covering on house", [
            "Asbestos Shingles",
            "Asphalt Shingles",
            "Brick Common",
            "Brick Face",
            "Cinder Block",
            "Cement Board",
            "Hard Board",
            "Imitation Stucco",
            "Metal Siding",
            "Other",
            "Plywood",
            "PreCast",
            "Stone",
            "Stucco",
            "Vinyl Siding",
            "Wood Siding",
            "Wood Shingles"
        ])

        Exterior2nd = st.selectbox("Exterior covering on house (if more than one material)", [
            "Asbestos Shingles",
            "Asphalt Shingles",
            "Brick Common",
            "Brick Face",
            "Cinder Block",
            "Cement Board",
            "Hard Board",
            "Imitation Stucco",
            "Metal Siding",
            "Other",
            "Plywood",
            "PreCast",
            "Stone",
            "Stucco",
            "Vinyl Siding",
            "Wood Siding",
            "Wood Shingles"
        ])

        MasVnrType = st.selectbox("Masonry veneer type", [
            "Brick Common",
            "Brick Face",
            "Cinder Block",
            "None",
            "Stone"
        ])

        MasVnrArea = st.number_input("Masonry veneer area in square feet", min_value=0)

        ExterQual = st.selectbox("Exterior quality", [
            "Excellent",
            "Good",
            "Average/Typical",
            "Fair",
            "Poor"
        ])

        ExterCond = st.selectbox("Exterior condition", [
            "Excellent",
            "Good",
            "Average/Typical",
            "Fair",
            "Poor"
        ])

        Foundation = st.selectbox("Foundation", [
            "Brick & Tile",
            "Cinder Block",
            "Poured Concrete",
            "Slab",
            "Stone",
            "Wood"
        ])

        BsmtQual = st.selectbox("Basement height", [
            "Excellent (100+ inches)",
            "Good (90-99 inches)",
            "Typical (80-89 inches)",
            "Fair (70-79 inches)",
            "Poor (<70 inches)",
            "No Basement"
        ])

        BsmtCond = st.selectbox("Basement condition", [
            "Excellent",
            "Good",
            "Typical - slight dampness allowed",
            "Fair - dampness or some cracking or settling",
            "Poor - Severe cracking, settling, or wetness",
            "No Basement"
        ])

        BsmtExposure = st.selectbox("Basement exposure", [
            "Good Exposure",
            "Average Exposure",
            "Minimum Exposure",
            "No Exposure",
            "No Basement"
        ])

        BsmtFinType1 = st.selectbox("Rating of basement finished area", [
            "Good Living Quarters",
            "Average Living Quarters",
            "Below Average Living Quarters",
            "Rec Room",
            "Low Quality",
            "Unfinshed",
            "No Basement"
        ])

        BsmtFinSF1 = st.number_input("Type 1 finished square feet", 0, 5600, 700, 1)

        BsmtFinType2 = st.selectbox("Rating of basement finished area (if multiple types)", [
            "Good Living Quarters",
            "Average Living Quarters",
            "Below Average Living Quarters",
            "Rec Room",
            "Low Quality",
            "Unfinshed",
            "No Basement"
        ])

        BsmtFinSF2 = st.number_input("Type 2 finished square feet", 0, 5600, 700, 1)
        BsmtUnfSF = st.number_input("Unfinished square feet of basement area", 0, 5600, 700, 1)
        TotalBsmtSF = st.number_input("Total square feet of basement area", 0, 7000, 400, 1)
        HeatingQC = st.selectbox("Heating quality and condition", [
            "Excellent",
            "Good",
            "Average/Typical",
            "Fair",
            "Poor"
        ])

        FirstFlrSF = st.number_input("First floor square feet", 200, 5000, 500, 1)
        SecondFlrSF = st.number_input("Second floor square feet", 200, 5000, 500, 1)
        GrLivArea = st.number_input("Above grade (ground) living area square feet", 300, 6000, 1000, 1)
        BsmtFullBath = st.number_input("Number of full bathrooms in the Basement", 0, 4, 1, 1)
        FullBath = st.number_input("Number of Full bathrooms above the basement", 0, 5, 3, 1)
        HalfBath = st.number_input("Half bathrooms above the basement", 0, 5, 3, 1)
        BedroomAbvGr = st.number_input("Number of Bedrooms above ground", 1, 12, 3, 1)
        KitchenQual = st.selectbox("Kitchen quality", [
            "Excellent",
            "Good",
            "Average/Typical",
            "Fair",
            "Poor"
        ])

        TotRmsAbvGrd = st.number_input("Total rooms above grade (does not include bathrooms)", 1, 20, 5, 1)
        Fireplaces = st.number_input("Number of fireplaces", 0, 5, 1, 1)
        FireplaceQu = st.selectbox("Fireplace quality", [
            "Excellent - Exceptional Masonry Fireplace",
            "Good - Masonry Fireplace in main level",
            "Average - Prefabricated Fireplace in main living area or Masonry Fireplace in basement",
            "Fair - Prefabricated Fireplace in basement",
            "Poor - Ben Franklin Stove",
            "No Fireplace"
        ])

        GarageType = st.selectbox("Garage location", [
            "More than one type of garage",
            "Attached to home",
            "Basement Garage",
            "Built-In (Garage part of house - typically has room above garage)",
            "Car Port",
            "Detached from home",
            "No Garage"
        ])

        GarageFinish = st.selectbox("Interior finish of the garage", [
            "Finished",
            "Rough Finished",
            "Unfinished",
            "No Garage"
        ])

        GarageCars = st.number_input("Size of garage in car capacity", 0, 6, 2, 1)
        GarageArea = st.number_input("Size of garage in square feet", 0, 1500, 0, 1)
        WoodDeckSF = st.number_input("Wood deck area in square feet", 0, 900, 0, 1)
        OpenPorchSF = st.number_input("Open porch area in square feet", 0, 600, 0, 1)
        EnclosedPorch = st.number_input("Enclosed porch area in square feet", 0, 500, 0, 1)
        ScreenPorch = st.number_input("Screen porch area in square feet", 0, 500, 0, 1)
        Fence = st.selectbox("Fence quality", [
            "Good Privacy",
            "Minimum Privacy",
            "Good Wood",
            "Minimum Wood/Wire",
            "No Fence"
        ])

        MoSold = st.number_input("Month Sold (MM)", min_value=1, max_value=12)
        SaleType = st.selectbox("Type of sale", [
            "Warranty Deed - Conventional",
            "Warranty Deed - Cash",
            "Warranty Deed - VA Loan",
            "New Construction",
            "Court Officer Deed/Estate",
            "Contract 15% Down payment regular terms",
            "Contract Low Down payment and low interest",
            "Contract Low Interest",
            "Contract Low Down",
            "Other"
        ])

        SaleCondition = st.selectbox("Sale condition", [
            "Normal Sale",
            "Abnormal Sale - trade, foreclosure, short sale",
            "Adjoining Land Purchase",
            "Allocation - two linked properties with separate deeds, typically condo with a garage unit",
            "Family Sale",
            "Home was renovated"
        ])

        submitted = st.form_submit_button("Predict property price")


    if submitted:
        features = {
            "MSSubClass": MSSubClass,
            "MSZoning": MSZoning,
            "LotFrontage": LotFrontage,
            "LotArea": LotArea,
            "LotShape": LotShape,
            "LotConfig": LotConfig,
            "Neighborhood": Neighborhood,
            "Condition1": Condition1,
            "BldgType": BldgType,
            "HouseStyle": HouseStyle,
            "OverallQual": OverallQual,
            "OverallCond": OverallCond,
            "YrSold": YrSold,
            "YearBuilt": YearBuilt,
            "YearRemodAdd": YearRemodAdd,
            "GarageYrBlt": GarageYrBlt,
            "RoofStyle": RoofStyle,
            "Exterior1st": Exterior1st,
            "Exterior2nd": Exterior2nd,
            "MasVnrType": MasVnrType,
            "MasVnrArea": MasVnrArea,
            "ExterQual": ExterQual,
            "ExterCond": ExterCond,
            "Foundation": Foundation,
            "BsmtQual": BsmtQual,
            "BsmtCond": BsmtCond,
            "BsmtExposure": BsmtExposure,
            "BsmtFinType1": BsmtFinType1,
            "BsmtFinSF1": BsmtFinSF1,
            "BsmtFinType2": BsmtFinType2,
            "BsmtFinSF2": BsmtFinSF2,
            "BsmtUnfSF": BsmtUnfSF,
            "TotalBsmtSF": TotalBsmtSF,
            "HeatingQC": HeatingQC,
            "1stFlrSF": FirstFlrSF,
            "2ndFlrSF": SecondFlrSF,
            "GrLivArea": GrLivArea,
            "BsmtFullBath": BsmtFullBath,
            "FullBath": FullBath,
            "HalfBath": HalfBath,
            "BedroomAbvGr": BedroomAbvGr,
            "KitchenQual": KitchenQual,
            "TotRmsAbvGrd": TotRmsAbvGrd,
            "Fireplaces": Fireplaces,
            "FireplaceQu": FireplaceQu,
            "GarageType": GarageType,
            "GarageFinish": GarageFinish,
            "GarageCars": GarageCars,
            "GarageArea": GarageArea,
            "WoodDeckSF": WoodDeckSF,
            "OpenPorchSF": OpenPorchSF,
            "EnclosedPorch": EnclosedPorch,
            "ScreenPorch": ScreenPorch,
            "Fence": Fence,
            "MoSold": MoSold,
            "SaleType": SaleType,
            "SaleCondition": SaleCondition
        }

        predicted_price = predict_price(features)      
        st.write(f"The predicted price of the house is **${predicted_price:,.2f}**")
