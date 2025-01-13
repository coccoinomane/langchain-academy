# Run locally running graph on LangChain Studio

1. Run `langgraph dev` to start the local server with your graphs API
2. Browser should automatically open to smith.langchain.com connected to your local server

# Run docker image locally

1. Configure .env file
2. Build Docker image `langgraph build -t module-1` which will create `.langgraph_api` folder
3. Run locally with `docker compose up` and test with `curl --request GET --url 0.0.0.0:8123/ok`

Docs here > https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/#using-docker-compose

# Run docker image on Digital Ocean

1. Crate droplet with 1 GB RAM and 1 CPU
2. SSH into it
3. TBD