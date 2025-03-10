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

## Exam Notes

- App Service Plan (SKU:B1 = Basic), resource group, runtime selection
- App name must be unique. The `deploy.sh` script generates a unique app name using a UUID and updates the `README.md` file with the new Live URL.
- `az webapp up` shortcut for combining plan creation, app creation, and deployment.

## Deployment Script

The `deploy.sh` script automates the deployment process:

1. Generates a unique web app name using a UUID.
2. Creates the resource group.
3. Deploys the web app with the generated name.
4. Updates the `README.md` file with the new web app URL.

## Live URL

[https://az204-helloworld.azurewebsites.net](https://az204-helloworld.azurewebsites.net)
