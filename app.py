import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load("flight_price_pipeline.pkl")

st.set_page_config(
    page_title="Flight Price Predictor",
    page_icon="✈️",
    layout="wide"
)


st.title("✈️ Flight Price Prediction")
st.write("Enter the flight details below to predict the ticket price.")

st.divider()

st.subheader("🛫 Flight Details")


col1, col2, col3, col4 = st.columns(4)

with col1:
    airline = st.selectbox(
        "Airline",
        ["Air India", "IndiGo", "Vistara", "SpiceJet",
         "AirAsia", "GO FIRST", "Akasa Air", "Alliance Air"]
    )

with col2:
    source = st.selectbox(
        "From",
        ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad"]
    )

with col3:
    destination = st.selectbox(
        "To",
        ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata", "Hyderabad"]
    )

with col4:
    flight_class = st.selectbox(
        "Class",
        ["Economy", "Business"]
    )


col5, col6, col7, col8 = st.columns(4)

with col5:
    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=15
    )

with col6:
    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=6
    )

with col7:
    dep_hour = st.slider(
        "Departure Hour",
        min_value=0,
        max_value=23,
        value=10
    )

with col8:
    arr_hour = st.slider(
        "Arrival Hour",
        min_value=0,
        max_value=23,
        value=12
    )


col9, col10, col11, col12 = st.columns(4)

with col9:
    dep_period = st.selectbox(
        "Departure Period",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

with col10:
    arr_period = st.selectbox(
        "Arrival Period",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

with col11:
    duration = st.number_input(
        "Duration (minutes)",
        min_value=30,
        max_value=3000,
        value=120,
        step=10
    )

with col12:
    stops = st.number_input(
        "Number of Stops",
        min_value=0,
        max_value=5,
        value=0,
        step=1
    )


col13, col14 = st.columns(2)

with col13:
    arr_daytime = st.number_input(
        "Arrival Daytime",
        min_value=0,
        max_value=23,
        value=12
    )

with col14:
    dep_daytime = st.number_input(
        "Departure Daytime",
        min_value=0,
        max_value=23,
        value=10
    )

st.divider()


# Prediction button
if st.button("🔮 Predict Flight Price", use_container_width=True):

    # Create input dataframe
    input_data = pd.DataFrame({
        'airline': [airline],
        'from': [source],
        'to': [destination],
        'class_category': [flight_class],
        'day': [day],
        'month': [month],
        'dep_hour': [dep_hour],
        'arr_hour': [arr_hour],
        'dep_period': [dep_period],
        'arr_period': [arr_period],
        'duration_in_min': [duration],
        'stops': [stops],
        'arr_daytime': [arr_daytime],
        'dep_daytime': [dep_daytime]
    })

   
    prediction = pipeline.predict(input_data)[0]

   
    st.success(
        f"💰 Predicted Flight Price: ₹{prediction:,.2f}"
    )