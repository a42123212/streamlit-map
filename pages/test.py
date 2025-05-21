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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        #m.add_raster("cut_2015_ailiao.tif",cmap="Reds_r", layer_name="landslides", nodata=0, zoom_to_layer=True)
        m.add_basemap(basemap='HYBRID')
        m.set_center(120.7254,22.7474, zoom=11)
        m.split_map(left_layer="https://github.com/a42123212/shareable/releases/download/test/cut_2015_ailiao.tif",
            right_layer="HYBRID",
              left_label="Landslide", 
              right_label="landscope")
m.to_streamlit(height=700,width=800)
