import streamlit as st
import json

st.set_page_config(page_title="Agridex - Crop Identifier", layout="centered")

st.title("🌾 Agridex - Smart Crop Info Finder")
st.write("Upload a crop image (or select one) to identify and get details.")

# Simulate prediction (for now)
uploaded_file = st.file_uploader("Upload a crop image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Crop Image", use_column_width=True)
    # Fake prediction
    predicted_crop = "Wheat"  # static for demo
    st.success(f"✅ Identified: **{predicted_crop}**")
    
    # Load data
    with open("data/crop_info.json", "r") as f:
        crop_info = json.load(f)
    if predicted_crop in crop_info:
        st.subheader("Crop Information:")
        st.markdown(f"- **Soil:** {crop_info[predicted_crop]['soil']}")
        st.markdown(f"- **Climate:** {crop_info[predicted_crop]['climate']}")
        st.markdown(f"- **Water Needs:** {crop_info[predicted_crop]['water']}")
    else:
        st.warning("No data found for this crop.")