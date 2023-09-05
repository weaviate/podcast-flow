
import weaviate
from weaviate.util import get_valid_uuid
from uuid import uuid4
import os
from dotenv import load_dotenv

load_dotenv()

weaviate_url = os.getenv("WEAVIATE_URL")
weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)

client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=auth_config,
    additional_headers={'X-OpenAI-API-Key': openai_api_key}
)


generatePrompt = """
From the 5 topics listed, please suggest 5 ideas to build content on top of it: {content}

Do not make up new information that was not discussed in the podcast.
"""

result = client.query\
           .get("Topic")\
           .with_generate(single_prompt=generatePrompt)\
           .with_limit(5)\
           .do()["data"]["Get"]["Topic"]

print(result)
