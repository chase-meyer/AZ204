# ComputeSolutions/01-Create-WebApp/README.md
# Create an Azure App Service Web App

A basic Flask app deployed to Azure App Service.

## Steps
1. Created `app.py` with a simple "Hello, AZ-204!" endpoint.
2. Installed dependencies: `pip install -r requirements.txt`.
3. Tested locally: `python app.py` (port 8080).
4. Deployed with: `./deploy.sh`.

## Azure CLI Commands
- Resource group: `az group create --name AZ204RG --location westus`
- Web app: `az webapp up --name az204-helloworld --resource-group AZ204RG --location westus --sku B1 --runtime "PYTHON|3.11"`

## Live URL
[https://az204-helloworld.azurewebsites.net](https://az204-helloworld.azurewebsites.net)