import weaviate
import os
from dotenv import load_dotenv

load_dotenv()

weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)

client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=auth_config
)

client.schema.delete_all()

podcast_schema = {
    "classes": [
        {
            "class": "Podcast",
            "description": "Weaviate podcast",
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "generative-openai": {
                    "model": "gpt-3.5-turbo"
                }
            },
            "properties": [
                {
                    "name": "Content",
                    "dataType": ["text"],
                    "description": "Content from the podcasts.",
                }
            ]
        }
    ]
}

topic_schema = {
    "classes": [
        {
            "class": "Topic",
            "description": "Topics extracted from the podcast",
            "vectorizer": "text2vec-openai",
            "moduleConfig": {
                "generative-openai": {
                    "model": "gpt-3.5-turbo"
                }
            },
            "properties": [
                {
                    "name": "Content",
                    "dataType": ["text"],
                    "description": "Content in the topics.",
                }
            ]
        }
    ]
}

client.schema.create(podcast_schema)
client.schema.create(topic_schema)



