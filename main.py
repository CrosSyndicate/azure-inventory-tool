import json
from config import USE_MOCK, DEMO_SECRET

#----------------------------MOCK DATA----------------------------#
def build_inventory_mock():
    return {
        "subscription_id": "mock_subscription_id",
        "resource_groups": [
            {
                "name": "rg-demo",
                "location": "eastus",
                "resources": [
                    {
                        "name": "vm-01", "type": "Microsoft.Compute/virtualMachines"},
                        {"name": "storage01", "type": "Microsoft.Storage/storageAccounts"}
                    ]
                }
            ]
        }

#----------------------------AZURE MODE---------------------------#

def build_inventory_azure(subscription_id):
    from azure.identity import DefaultAzureCredential
    from azure.mgmt.resource import ResourceManagementClient

    credential = DefaultAzureCredential()
    client = ResourceManagementClient(credential, subscription_id)

    # Implementation for building inventory from Azure
    inventory = {
        "subscription_id": subscription_id,
        "resource_groups": []
    }
    
    for rg in client.resource_groups.list():
        rg_entry = {
            "name": rg.name,
            "location": rg.location,
            "resources": []
        }

        for res in client.resources.list_by_resource_group(rg.name):
            rg_entry["resources"].append({
                "name": res.name,
                "type": res.type
            })
        inventory["resource_groups"].append(rg_entry)

    return inventory

#----------------------------MAIN----------------------------#
def main():
    if USE_MOCK:
        print("Running in MOCK mode")
        inventory = build_inventory_mock()
    else:
        print("Running in Azure mode")
        inventory = build_inventory_azure("<subscription_id>")
    
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=2)

    print("Inventory has been written to inventory.json")

if __name__ == "__main__":
    main()