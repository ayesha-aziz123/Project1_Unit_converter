import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversions = {
        'Meter': 1,
        'Kilometer': 0.001,
        'Centimeter': 100,
        'Millimeter': 1000,
        'Inch': 39.3701,
        'Foot': 3.28084,
        'Yard': 1.09361,
        'Mile': 0.000621371
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'Kilogram': 1,
        'Gram': 1000,
        'Milligram': 1e6,
        'Pound': 2.20462,
        'Ounce': 35.274
    }
    return value * conversions[to_unit] / conversions[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    return value

st.set_page_config(page_title="Ultimate Unit Converter", page_icon="🔄", layout="wide")

st.sidebar.title("🔧 Unit Converter")
st.sidebar.markdown("**Fast & Accurate Unit Conversion in Seconds!**")

unit_type = st.sidebar.radio("Select Conversion Type", ["Length", "Weight", "Temperature"])

if unit_type == "Length":
    units = ['Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Inch', 'Foot', 'Yard', 'Mile']
elif unit_type == "Weight":
    units = ['Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce']
elif unit_type == "Temperature":
    units = ['Celsius', 'Fahrenheit', 'Kelvin']

# Stylish Header
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2; font-size: 42px; font-weight: bold;'>
        🔄 Ultimate Unit Converter
    </h1>
    <h3 style='text-align: center; color: #555; font-size: 20px;'>
        Convert Length, Weight & Temperature Instantly 🚀
    </h3>
    <hr style='border: 2px solid #4A90E2;'>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    value = st.number_input("Enter Value", value=1.0, step=0.1, format="%.2f")
    from_unit = st.selectbox("From", units)
with col3:
    to_unit = st.selectbox("To", units)
    converted_value = ""
    if st.button("Convert Now 🚀"):
        if unit_type == "Length":
            converted_value = convert_length(value, from_unit, to_unit)
        elif unit_type == "Weight":
            converted_value = convert_weight(value, from_unit, to_unit)
        elif unit_type == "Temperature":
            converted_value = convert_temperature(value, from_unit, to_unit)

        st.success(f"🎯 Converted Value: {converted_value:.2f} {to_unit}")

st.markdown("""
    <style>
        .stButton>button {
            background-color: #4A90E2;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            font-weight: bold;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #357ABD;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>🌍 Made with ❤️ by Ayesha</p>", unsafe_allow_html=True)
