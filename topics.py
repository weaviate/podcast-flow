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
Write 5 topics discussed in the podcast:
Topic: {content}

Do not make up new information that was not discussed in the podcast.
"""


generate_properties = ["content"]

topics = client.query\
           .get("Podcast", generate_properties)\
           .with_generate(single_prompt=generatePrompt)\
           .with_limit(5)\
           .with_additional(["id"])\
           .do()["data"]["Get"]["Podcast"]

for content in topics:
 new_property = {
     "content": content["_additional"]["generate"]["singleResult"]
 }
 id = get_valid_uuid(uuid4())
 client.data_object.create(
     new_property,
     class_name = "Topic",
     uuid=id
 )