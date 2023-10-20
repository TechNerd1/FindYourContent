import streamlit as st
import streamlit.components.v1 as components


donate = """
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" 
        data-name="bmc-button" data-slug="caleblafeve" data-color="#FFDD00" data-emoji="☕"  
        data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
        """

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
components.html(donate)
        

