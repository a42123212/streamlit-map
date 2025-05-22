import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
This is the landslide evaluation results at Ailiao catchment in 2015.
It's base on a method developed by YcHsu, using machine learing to accomplish.
<http://dx.doi.org/10.6342/NTU202400078>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://upload.wikimedia.org/wikipedia/commons/3/35/Landslide_near_the_city.svg"
st.sidebar.image(logo)

st.title("Landslide evaluation Demo")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(minimap_control=True)
        #m.add_remote_tile("https://github.com/a42123212/shareable/releases/download/test/cut_2015_ailiao.tif",cmap="Reds_r", layer_name="landslides", nodata=0, zoom_to_layer=True)
        m.add_basemap(basemap='SATELLITE')
        m.set_center(120.7254,22.7474, zoom=11)
        m.split_map(left_layer="https://github.com/a42123212/shareable/releases/download/test3/att_his2__src_ailiao_2.tif",
            right_layer="https://github.com/a42123212/shareable/releases/download/test3/cut_2015_ailiao.tif",
            )
        legend_dict = {
            "Predicted Landslide": "e31a1c",
            "Landslides in reality": "000000"

        }

        m.add_legend(title="Landslide Evaluation", legend_dict=legend_dict, position="bottomleft", draggable=False, style={"bottom": "45px", "border-radius": "25px"})
m.to_streamlit(height=900)
