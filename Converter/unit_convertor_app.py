import streamlit as st

def convert_unit(value, unit_from, unit_to):
    conversion = {
        "meter_kilometer": 0.001,  # 1 meter = 0.001 kilometers
        "kilometer_meter": 1000,   # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001,    # 1 gram = 0.001 kilograms
        "kilogram_gram": 1000      # 1 kilogram = 1000 grams
    }

    key = f"{unit_from.strip()}_{unit_to.strip()}"

    if unit_from == unit_to:
        return f"🔄 No conversion needed! {value} {unit_from} = {value} {unit_to} ✅"

    if key in conversion:
        converted_value = value * conversion[key]
        return f"🎯 {value} {unit_from} = {converted_value} {unit_to} ✅"

    return "❌ Conversion not supported! Please select valid units. ⚠️"

# 🌟 Streamlit App
st.title("🔢 Unit Converter 🛠️")

input_value = st.number_input("📏 Enter the value:", min_value=0.0, format="%.2f")  

from_selector = st.selectbox("🔄 Convert From:", ["meter", "kilometer", "gram", "kilogram"])
to_selector = st.selectbox("🔁 Convert To:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("🚀 Convert Now!"):
    result = convert_unit(input_value, from_selector, to_selector)
    st.success(result)  # ✅ Green success message

# 🔽 Muzna Amir ka credit (small text) 🔽
st.markdown('<p style="font-size:12px; text-align:center;">🚀 Built with ❤️ by Muzna Amir</p>', unsafe_allow_html=True)
