from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import streamlit.components.v1 as components
import sqlite3
import dbSearch
import math

def main():
    cs_body()

    return None

def get_database_connection():
    return sqlite3.connect('transcripts_fts.db')

def close_database_connection(conn):
    conn.close()

def filter_videos(videos):
    filtered = []
    ids = []
    for video in videos:
        try:
            ids.index(video['video_id'])
            continue
        except ValueError:
            ids.append(video['video_id'])
            filtered.append(video)
    return filtered

def cs_body():
    st.set_page_config(page_title="Search")

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    
    st.header("Let's find your content")
    
    title = st.text_input(' ', '', placeholder='Search using a keyword or phrase')

    found_entries = []

    if(title != ''):
        with st.spinner('Searching...'):
            conn = get_database_connection()
            found_entries = dbSearch.search_phrase_in_db(title, conn)
            close_database_connection(conn)
        
        if(len(found_entries) > 0):
            filtered = filter_videos(found_entries)
            for i, video in enumerate(filtered):
                col1, col2 = st.columns([3, 2])

                with col1:
                    components.html(f"""
                            
                            <iframe width="100%" height="210" src="https://www.youtube.com/embed/{video['video_id']}?start={math.floor(video['start'])}" title="YouTube video player" 
                            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                            
                            """,
                            height=210)

                with col2:
                    st.subheader('\"' + video['text'] + '\"')

                
                st.divider()
                if (i > 10):
                    st.subheader("Didn't find what you're looking for?")
                    st.write("Adjust your search query to align with phrases she might have used. To prevent page overload, search results are capped.")
                    break
            
        else:
            st.warning("Nothing Found")
    else:
        st.warning("If SSSniperWolf has used your content and you're struggling to locate it, simply input relevant keywords. This platform searches through transcripts of all her YouTube videos to help you pinpoint the exact video where your content appears. By utilizing this search function, you agree to the site's disclaimer.")
 
if __name__ == '__main__':
    main()