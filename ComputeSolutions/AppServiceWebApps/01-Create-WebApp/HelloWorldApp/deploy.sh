# ComputeSolutions/01-Create-WebApp/deploy.sh
#!/bin/bash
az group create --name AZ204RG --location westus
az webapp up --name az204-helloworld --resource-group AZ204RG --location westus --sku B1 --runtime "PYTHON|3.11"