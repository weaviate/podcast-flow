import weaviate
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi


load_dotenv()

# Connect to Weaviate instance
weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)

client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=auth_config,
    additional_headers={'X-OpenAI-API-Key': openai_api_key}
)

# Grab transcript from the podcast
video_id = "HUtYOLX7HZ4"

video = YouTubeTranscriptApi.get_transcript(video_id)

transcript = ""

for entry in video:
    transcript += entry['text'] + ' '

# chunk the transcript to 4000 tokens
transcript_chunks = []
tokens = transcript.split()
chunk_size = 4000
for i in range(0, len(tokens), chunk_size):
    transcript_chunks.append(' '.join(tokens[i:i+chunk_size]))

# Upload the transcript to Weaviate
with client.batch as batch:
    for i, chunk in enumerate(transcript_chunks):
        property = {
            "content": chunk
        }
        client.batch.add_data_object(
            property,
            class_name="Podcast"
        )

print("Uploaded transcript")