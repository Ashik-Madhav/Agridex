import streamlit as st
import json

st.set_page_config(page_title="Agridex - Crop Identifier", layout="centered")

st.title("🌾 Agridex - Smart Crop Info Finder")
st.write("Upload a crop image (or select one) to identify and get details.")

# Simulate prediction (for now)
uploaded_file = st.file_uploader("Upload a crop image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Crop Image", use_column_width=True)

    # Fake prediction for demo
    predicted_crop = "Wheat"  # you can replace this with actual prediction later
    st.success(f"✅ Identified: **{predicted_crop}**")

    # Load crop info JSON
    with open("data/crop_info.json", "r") as f:
        crop_info = json.load(f)

    # Normalize predicted crop name to match keys (capitalize first letter)
    predicted_crop_normalized = predicted_crop.capitalize()

    if predicted_crop_normalized in crop_info:
        crop = crop_info[predicted_crop_normalized]
        st.subheader("Crop Information:")
        st.markdown(f"- **Scientific Name:** {crop['scientific_name']}")
        st.markdown(f"- **Season:** {crop['season']}")
        st.markdown(f"- **Growth Duration:** {crop['growth_duration']}")
        st.markdown(f"- **Climate Temperature:** {crop['climate']['temperature']}")
        st.markdown(f"- **Climate Rainfall:** {crop['climate']['rainfall']}")
        st.markdown(f"- **Soil:** {crop['soil']}")
        st.markdown(f"- **Region:** {crop['region']}")
    else:
        st.warning(f"No data found for the crop: {predicted_crop}")
