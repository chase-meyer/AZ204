# ComputeSolutions/01-Create-WebApp/deploy.sh
#!/bin/bash

# Generate a GUID using Python
WEBAPP_NAME="az204-helloworld-$(python -c 'import uuid; print(uuid.uuid4())')"

# Create resource group
az group create --name AZ204RG --location westus

# Deploy web app with the generated GUID as the name
az webapp up --name $WEBAPP_NAME --resource-group AZ204RG --location westus --sku B1 --runtime "PYTHON|3.11"

# Update the README.md file with the new web app URL
README_FILE="/workspaces/AZ204/ComputeSolutions/AppServiceWebApps/01-Create-WebApp/HelloWorldApp/README.md"
LIVE_URL="https://${WEBAPP_NAME}.azurewebsites.net"

if [ -f "$README_FILE" ]; then
    sed -i "s|https://az204-helloworld.azurewebsites.net|${LIVE_URL}|g" "$README_FILE"
    echo "Updated README.md with Live URL: $LIVE_URL"
else
    echo "README.md file not found."
fi

echo "Web app deployed with name: $WEBAPP_NAME"