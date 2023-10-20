import streamlit as st

st.set_page_config(page_title="Disclaimer")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.title("Site Disclaimer")
st.write(""" 
        This platform facilitates the search for user content within SSSniperWolf's YouTube videos. 
         We are not affiliated with, endorsed by, or connected to SSSniperWolf or any associated parties. 
         Misuse of this platform or using it with malicious intent is not supported or condoned by its creator.
        
        \n\nIf you have any questions or inquiries, feel free to reach out via email at iamtechnerd@gmail.com.
""")