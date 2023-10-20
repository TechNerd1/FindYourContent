import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="About")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
link = '[Disclaimer](/Disclaimer)'
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.title('About this site')
st.write("""
         This platform is designed to assist content creators in identifying and locating instances where their videos might have been used or incorporated within SSSniperWolf's YouTube channel, specifically to aid in the process of requesting removals or addressing copyright concerns.
         
        """)
st.markdown(link, unsafe_allow_html=True)