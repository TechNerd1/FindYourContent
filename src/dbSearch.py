import sqlite3
from youtube_transcript_api import YouTubeTranscriptApi
import scrapetube

# videos = scrapetube.get_channel("UCpB959t8iPrxQWj7G6n0ctQ")
# url = https://www.youtube.com/watch?v={id}t={start}s
def print_video(vid_id):
    print (vid_id)

def search_phrase_in_db(phrase, conn):
    c = conn.cursor()
    c.execute("SELECT video_id, text, start, duration FROM transcript_fts ORDER BY video_id")
    rows = c.fetchall()

    video_id = None
    concatenated_text = ''
    found_entries = []
    
    for row in rows:
        if row[0] != video_id:
            video_id = row[0]
            concatenated_text = ''
        
        concatenated_text = ' '.join([concatenated_text, row[1]]).strip()
        
        if phrase.lower() in concatenated_text.lower():
            entry = {
                'video_id': row[0],
                'text': row[1],
                'start': row[2],
                'duration': row[3]
            }
            found_entries.append(entry)
            
            concatenated_text = concatenated_text.replace(phrase.lower(), '', 1)

    return found_entries

conn = sqlite3.connect('transcripts.db')

conn.close()