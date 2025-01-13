Deploy LangGraph graphs on Digital ocean, using module 1 of the ["Intro to LangGraph"](https://academy.langchain.com/courses/intro-to-langgraph) course as an example.

Main documentation article that I used:
- https://langchain-ai.github.io/langgraph/how-tos/deploy-self-hosted/#using-docker-compose


# Run docker image on Digital Ocean

1. Crate cheapest droplet with 1 GB RAM and 1 vCPU
1. SSH into it
1. Set up your Python virtual environment:
   ```bash
   apt update && apt upgrade -y # or your package manager, brew on MacOS
   apt install python3-pip python3.12-venv -y # change python3.12 to your version
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
1. Install Docker and Docker Compose:
   ```
   apt install docker.io docker-compose -y
   ```
1. Clone repository:
   ```
   git clone https://github.com/langchain-ai/langchain-academy.git
   cd langchain-academy/module-1-self-hosted/studio
   ```
1. You should now be in the studio folder: configure the `.env` file there
1. Build Docker image `langgraph build -t module-1` which will create `.langgraph_api` folder
1. Run locally with `docker-compose up` or in detached mode with `docker-compose up -d`.  Detached mode is recommended if you want the server to keep running after you exit the SSH session.
1. Test that the API works locally with `curl --request GET --url 0.0.0.0:8123/ok`
1. Exit from SSH and test that the API works remotely with `curl --request GET --url <IP ADDRESS OF DROPLET>:8123/ok`
1. The final test is to list the agents in the deployed graph:
   ```bash
   python scripts/show_deployed_graphs.py http://<IP ADDRESS OF DROPLET>:8123
   ```

# Run local graph on LangChain Studio UI

1. Configure .env file
1. Run `langgraph dev` to start the local server with your graphs API
1. Browser should automatically open to smith.langchain.com connected to your local server

# Run docker image locally

1. Configure .env file
1. Build Docker image `langgraph build -t module-1` which will create `.langgraph_api` folder
1. Run locally with `docker compose up` and test with `curl --request GET --url 0.0.0.0:8123/ok`
