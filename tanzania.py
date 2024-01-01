import pandas as pd
import numpy as np
import streamlit as st
import joblib

# Load the model using joblib
loaded_model = joblib.load('b_classifier.joblib')

# Mapping dictionaries for categorical variables with descriptions
categorical_mappings = {
    'travel_with': {
        'Who did you travel with?': {
            'Friends / Relatives': 0,
            'Alone': 1,
            'Spouse': 2,
            'Children': 3,
            'Other': 4
        }
    },
    'purpose': {
        'Purpose of the trip': {
            'Leisure and Holidays': 0,
            'Visiting Friends and Relatives': 1,
            'Business': 2,
            'Meetings and Conference': 3,
            'Volunteering': 4,
            'Scientific and Academic': 5,
            'Other': 6
        }
    },
    'main_activity': {
        'Main Activity during the trip': {
            'Wildlife tourism': 0,
            'Cultural tourism': 1,
            'Mountain climbing': 2,
            'Beach tourism': 3,
            'Conference tourism': 4,
            'Hunting tourism': 5,
            'Bird watching': 6,
            'Business': 7,
            'Other': 8
        }
    },
    'info_source': {
        'Information Source': {
            'Friends, relatives': 0,
            'Others': 1,
            'Travel, agent, tour operator': 2,
            'Radio, TV, Web': 3,
            'Tanzania Mission Abroad': 4,
            'Inflight magazines': 5,
            'Newspaper, magazines, brochures': 6,
            'Other': 7
        }
    },
    'tour_arrangement': {
        'Tour Arrangement': {
            'Independent': 0,
            'Other': 1
        }
    },
    'package_transport_int': {
        'International Transport in Package': {
            'No': 0,
            'Yes': 1
        }
    },
    'package_accomodation': {
        'Accommodation in Package': {
            'No': 0,
            'Yes': 1
        }
    },
    'package_food': {
        'Food Included in Package': {
            'No': 0,
            'Yes': 1
        }
    },
    'package_transport_tz': {
        'Transport in Tanzania Included in Package': {
            'No': 0,
            'Yes': 1
        }
    },
    'package_sightseeing': {
        'Sightseeing in Package': {
            'No': 0,
            'Yes': 1
        }
    },
    'package_guided_tour': {
        'Guided Tour in Package': {
            'No': 0,
            'Yes': 1
        }
    },
    'package_insurance': {
        'Insurance Included in Package': {
            'No': 0,
            'Yes': 1
        }
    },
    'payment_mode': {
        'Payment Mode': {
            'Cash': 0,
            'Credit Card': 1,
            'Other': 2,
            'Online Purchase': 3
        }
    },
    'first_trip_tz': {
        'First Trip to Tanzania': {
            'No': 0,
            'Yes': 1
        }
    },
    'most_impressing': {
        'Most Impressing Aspect': {
            'Friendly People': 0,
            'Wonderful Country, Landscape, Nature': 1,
            'Excellent Experience': 2,
            'No comments': 3,
            'Wildlife': 4,
            'No most impression': 5,
            'Good service': 6,
            'Other': 7
        }
    },
    'Continent': {
        'Continent': {
            'Europe': 0,
            'Asia': 1,
            'Africa': 2,
            'North America': 3,
            'South America': 4,
            'Other': 5
        }
    }
}

# Streamlit Input Form
st.title('Tanzania Tourism Price Prediction')
st.sidebar.header("Enter Your Travel Details")

# Create input fields with descriptions for each feature
input_data = {}

for feature, mappings in categorical_mappings.items():
    description = list(mappings.keys())[0]
    options = list(mappings.values())[0]
    input_data[feature] = st.sidebar.selectbox(description, list(options.keys()))

# Numeric inputs
input_data['total_people'] = st.sidebar.number_input("Total People (e.g., number of travelers)", min_value=1)
input_data['total_night_spent'] = st.sidebar.number_input("Total Nights Spent", min_value=0)
input_data['mgf2'] = st.sidebar.number_input("Payment_Mode_and_Purpose_Combined (mgf2)", min_value=0)
input_data['mgf3'] = st.sidebar.number_input("Country_and_Tour_Arrangement_Combined (mgf3)", min_value=0)
input_data['mgf4'] = st.sidebar.number_input("Total_People_times_Age_Group (mgf4)", min_value=0)
input_data['mf1'] = st.sidebar.number_input("Total_Nights_Spent_times_Total_People (mf1)", min_value=0)

# Prediction button
if st.sidebar.button("Predict"):
    # Map categorical inputs to numerical values
    for feature, mappings in categorical_mappings.items():
        input_data[feature] = list(mappings.values())[0][input_data[feature]]

    # Create a DataFrame from the input data
    input_df = pd.DataFrame([input_data])

    # Use your loaded model to make predictions
    prediction = loaded_model.predict(input_df)

# Main Page Content
st.write("Welcome to the Tanzania Tourism Price Prediction App!")
st.write("Enter your travel details on the sidebar to get a cost prediction.")

# Display prediction result with a border and centered
if 'prediction' in locals():
    st.header("Predicted Total Cost")
    st.markdown(
        f"<div style='border: 2px solid #0366d6; padding: 10px; border-radius: 5px; text-align: center;'>"
        f"<h3>${prediction[0]:.2f}</h3>"
        f"</div>",
        unsafe_allow_html=True
    )

# Footer
st.sidebar.text("By: Saoban Lateefat")
st.sidebar.text("Credits: Data provided by Zindi Africa")
