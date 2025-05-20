import streamlit as st

# Dictionaries for conversion factors
conversion_factors = {
    "Length": {
        "meter": 1.0,
        "kilometer": 1000.0,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    },
    "Weight": {
        "kilogram": 1.0,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495
    },
    "Temperature": {
        "celsius": "celsius",
        "fahrenheit": "fahrenheit",
        "kelvin": "kelvin"
    }
}

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32

# Streamlit UI
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🔄 Google Style Unit Converter")

category = st.selectbox("Select a category", list(conversion_factors.keys()))

units = list(conversion_factors[category].keys())

from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

value = st.number_input(f"Enter value in {from_unit}", format="%.4f")

if st.button("Convert"):
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        factor_from = conversion_factors[category][from_unit]
        factor_to = conversion_factors[category][to_unit]
        result = value * (factor_from / factor_to)

    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
