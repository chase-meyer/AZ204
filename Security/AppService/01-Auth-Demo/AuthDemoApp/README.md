# Security/01-Auth-Demo/README.md

# Azure App Service Authentication & Authorization Demo

A Flask app showcasing App Service's built-in auth features.

## Steps

1. Deployed with: `./deploy.sh`
2. Configured auth in Azure Portal:
   - Microsoft: New app registration.
   - Google: Client ID/Secret from Google Cloud Console.
   - Required authentication enabled.

## Azure CLI Commands

- Resource group: `az group create --name AZ204RG --location westus`
- Web app: `az webapp up --name $WEBAPP_NAME --resource-group AZ204RG --location westus --sku B1 --runtime "PYTHON|3.11"`

## Azure Portal Acctins

1. Go to your app in Azure Portal
2. Navigate to Authentication in the left menu
3. Click Add identity provider
   - Add Microsoft
      - Create new app registration
      - Tenant type: workforce
   - Add Google
      - Get Client ID and Secret from Google Cloud Console (create a project, enable OAuth, set redirect URI)
      - Enter Client ID and Secret, then click Add.

## Features
- Multiple identity providers (Microsoft Entra ID, Google).
- User claims via headers (`X-MS-CLIENT-PRINCIPAL-*`).
- Protected route (`/secure`) requiring authentication.
- Simulated token use (`/api-call`).

## Exam Notes
- Easy Auth handles sign-ins without code.
- Headers provide claims (e.g., `X-MS-CLIENT-PRINCIPAL-ID`).
- Use tokens for downstream calls (e.g., Microsoft Graph).

## Live URL
[https://az204-helloworld.azurewebsites.net](https://az204-helloworld.azurewebsites.net)