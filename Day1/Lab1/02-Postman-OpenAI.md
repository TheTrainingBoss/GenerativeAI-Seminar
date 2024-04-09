### Download the free version of Postman from the official website and install 
it on your machine. Once installed, you can start using Postman to make API

### Use a POST request to send a prompt to the OpenAI API

1. Open Postman and create a new request.
2. Set the request method to `POST`.
3. Enter the API endpoint in the URL field. The API endpoint for the OpenAI API is `https://api.openai.com/v1/chat/completions`.
4. The OpenAI API requires an API key for authentication. Add the API key to the request headers. You can find your API key in your OpenAI account settings.
5. Add the required parameters to the request body.
```json
{
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": "Where do Visual Studio Live Conferences take place?"}],
"temperature" : 1.0,
"max_tokens": 1000
}
```