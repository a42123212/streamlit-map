import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("YcHsu's Geo Disaster Demos")

st.markdown(
    """
    This multipage app demonstrates various interactive demos about geo disaster, which come from YcHsu's academic research. The website is an open-source project and you are very welcome to visit the [GitHub repository](https://github.com/a42123212/streamlit-map).
    """
)

st.header("Instructions")

markdown = """
The framwork about this website is based on [Open Geospatial Solutions](https://github.com/opengeos), which inspired me a lot. Below is the instructions about how to build a website like this.
1. For the [GitHub repository](https://github.com/opengeos/streamlit-map-template) or [use it as a template](https://github.com/opengeos/streamlit-map-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
