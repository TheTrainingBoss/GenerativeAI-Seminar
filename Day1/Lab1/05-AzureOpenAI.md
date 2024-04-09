## Creating an Azure OpenAI Resource
Head over to the Azure Portal and create a new resource. Search for "OpenAI" and select the "OpenAI" resource. Click on "Create" to start creating a new resource.

Fill in the required fields, such as the resource name, subscription, resource group, and location. Click on "Review + Create" to review the details and then click on "Create" to create the resource.

Once the resource is created, you can access the API key and endpoint to start using the OpenAI API.

## Using the Azure OpenAI Resource

To use the Azure OpenAI resource, you will need to authenticate using the API key and endpoint provided in the Azure Portal. You can use the API key and endpoint to make requests to the OpenAI API and get responses from the model.

## Try it from Postman

You can try using the Azure OpenAI resource from Postman by creating a new request and setting the endpoint and API key in the request headers. You can then send a request to the OpenAI API and get a response from the model.

The method is a **POST**
The endpoint is https://**name of the AZ OpenAI resource**.openai.azure.com/openai/deployments/**Name of the Model given during creation**/completions/?api-key=xxxxxxx&api-version=2024-02-01

You can get the full parameters from the Azure OpenAI resource documentation.
https://learn.microsoft.com/en-us/azure/ai-services/openai/reference 

The body of the request can be as simple as something like
```json
{
  "prompt": "Where do Visual Studio Live Conferences take place?",
  "max_tokens": 100
}
```
