# Podcast Flow 🌀

Podcast flow enables you to build content off of your existing content using RAG. 

## Get Started
You will first need to install Weaviate using either:
1. [Weaviate Embedded](https://weaviate.io/developers/weaviate/installation/embedded)
2. [Weaviate Cloud Service](https://console.weaviate.cloud)
3. [Docker Comppse](https://weaviate.io/developers/weaviate/installation/docker-compose)
4. [Kubernetes](https://weaviate.io/developers/weaviate/installation/kubernetes)

### Schema 
Create your schema by running `python3 create-schema.py`.

### Upload Data
First we're retrieving the transcript from the YouTube video. We will then take the transcript and upload it to the `Podcast` class. Do this by running: `python3 upload.py`.

### Extract Topics 
From the transcript, we can ask the LLM to extract 5 key ideas that were discussed in the podcast. We will then take those 5 concepts and store it in our `Topics` class. 
Run `python3 topics.py`

### Generate New Content 
Now we can take the 5 topics and prompt the LLM to create 5 new content ideas based on the topics. It will list out the title and then give a brief description about it. Run this with:
`python3 new-content.py`
