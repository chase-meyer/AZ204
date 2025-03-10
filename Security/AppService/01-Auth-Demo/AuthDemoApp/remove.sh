#!/bin/bash

# Name of the resource group to delete
RESOURCE_GROUP="AZ204RG"

# Delete the resource group and all associated resources
az group delete --name $RESOURCE_GROUP --yes --no-wait

echo "Resource group $RESOURCE_GROUP and all associated resources are being deleted."