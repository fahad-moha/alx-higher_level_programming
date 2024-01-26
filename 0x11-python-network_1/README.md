To fetch internet resources in Python, you can use the `urllib` or `requests` package. While `urllib` is a built-in module, `requests` is a third-party package known for its simplicity and ease of use. Here's how you can accomplish various tasks using both packages:

## Fetching Internet Resources with `urllib`:
To fetch internet resources using `urllib`, you can utilize the `urllib.request` module. Here's an example of fetching the content of a web page:

```python
import urllib.request

url = 'https://example.com'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)
```

- The `urlopen()` function opens the specified URL and returns a response object.
- The `read()` method retrieves the content of the response as bytes.
- The `decode()` method converts the bytes into a string using the specified encoding (e.g., UTF-8).

## Decoding `urllib` Response Body:
In the previous example, the `decode()` method is used to convert the response body from bytes to a string. The specified encoding should match the encoding used by the server to send the response. Common encodings include 'utf-8', 'latin-1', and 'iso-8859-1'.

## Fetching Internet Resources with `requests`:
To fetch internet resources using the `requests` package, you need to install it first by running `pip install requests`. Here's an example of fetching the content of a web page using `requests`:

```python
import requests

url = 'https://example.com'
response = requests.get(url)
content = response.text
print(content)
```

- The `get()` function sends an HTTP GET request to the specified URL and returns a response object.
- The `text` attribute of the response object contains the response body as a string.

## Making an HTTP GET Request:
To make an HTTP GET request using `requests`, you can use the `get()` function as shown in the previous example. Simply provide the URL you want to fetch.

## Making HTTP POST/PUT/DELETE Requests:
To make HTTP POST, PUT, DELETE, or other types of requests with `requests`, you can use the corresponding functions: `post()`, `put()`, `delete()`, etc. Here's an example of making a POST request with JSON data:

```python
import requests
import json

url = 'https://example.com/api'
data = {'name': 'John', 'age': 30}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.status_code)
print(response.json())
```

- The `post()` function sends an HTTP POST request with the specified data and headers.
- The `json.dumps()` function converts the Python dictionary to a JSON string.
- The `headers` dictionary sets the content type to JSON.

## Fetching JSON Resources:
To fetch JSON resources, you can use either `urllib` or `requests`. Here's an example using `requests`:

```python
import requests

url = 'https://example.com/api/data'
response = requests.get(url)
json_data = response.json()
print(json_data)
```

- The `response.json()` method parses the response body as JSON and returns a Python dictionary or list representing the JSON data.

## Manipulating Data from an External Service:
Manipulating data from an external service depends on the specific service and the data format it provides. If the service offers an API, you can use `requests` or `urllib` to fetch data and manipulate it using Python's built-in data manipulation capabilities. This may involve parsing JSON, XML, or other formats, performing calculations, filtering, transforming, or storing the data as needed.

