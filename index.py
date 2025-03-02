import streamlit as st

# Custom CSS for better styling
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .main-title {
            color: #4A90E2;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .result-box {
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            color: #333;
        }
        .convert-btn {
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 18px;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meter": 1, "kilometer": 0.001, "centimeter": 100, "millimeter": 1000,
        "mile": 0.000621371, "yard": 1.09361, "foot": 3.28084, "inch": 39.3701
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        celsius = value - 273.15
    else:
        celsius = value
    if to_unit == "Fahrenheit":
        return (celsius * 9/5) + 32
    elif to_unit == "Kelvin":
        return celsius + 273.15
    return celsius

def main():
    st.markdown("<h1 class='main-title'>📏🌡️ Unit Converter</h1>", unsafe_allow_html=True)
    st.sidebar.header("Configuration")
    conversion_type = st.sidebar.radio("Choose Conversion Type:", ["Length", "Temperature"])

    if conversion_type == "Length":
        st.subheader("🔄 Length Conversion")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter value:", min_value=0.0, step=0.1)
            from_unit = st.selectbox("From unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
        with col2:
            to_unit = st.selectbox("To unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])

        if st.button("Convert Length", key="length_btn"):
            result = length_converter(value, from_unit, to_unit)
            st.markdown(f"<div class='result-box'>✅ {value:.2f} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)

    elif conversion_type == "Temperature":
        st.subheader("🌡️ Temperature Conversion")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("Enter temperature:", step=0.1)
            from_unit = st.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
        with col2:
            to_unit = st.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"])

        if st.button("Convert Temperature", key="temp_btn"):
            result = temperature_converter(value, from_unit, to_unit)
            st.markdown(f"<div class='result-box'>✅ {value:.2f}°{from_unit[0]} = {result:.2f}°{to_unit[0]}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
