import streamlit as st
import os

pages_list = [
    st.Page(os.path.join("frontend", "simplest_chat.py"), title="ChatCITT v1", icon=":material/checklist:"),
    st.Page(os.path.join("frontend", "configurable_chat.py"), title="ChatCITT v2", icon=":material/robot_2:"),
]

# Add the pages to the navigation
pg = st.navigation(pages_list)
pg.run()

# Add logos
LOGO_URL_LARGE = os.path.join("assets", "images", "logo_arkana_large.png")
LOGO_URL_SMALL = os.path.join("assets", "images", "logo_arkana_small.png")
if os.path.exists(LOGO_URL_LARGE) and os.path.exists(LOGO_URL_SMALL):
    st.logo(
        image=LOGO_URL_LARGE,
        link="https://citt.duoc.com/",
        icon_image=LOGO_URL_SMALL,
    )
