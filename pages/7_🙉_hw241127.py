import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Split Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=(22.6273, 120.3014), zoom=24, height="600px") 
        m.split_map(
        left_layer="https://github.com/CcCid1213/1121/raw/refs/heads/main/ima.tif", 
        right_layer="https://github.com/CcCid1213/1121/raw/refs/heads/main/veg.tif"
        )

m.to_streamlit(height=700)
