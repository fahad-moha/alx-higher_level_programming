# How to manipulate JSON data

JavaScript provides built-in support for manipulating JSON data. Here are some common operations:

1. **Parsing JSON**: To work with JSON data in JavaScript, you first need to parse it into a JavaScript object using the `JSON.parse()` function. For example:

```javascript
const jsonString = '{"name": "John", "age": 30}';
const obj = JSON.parse(jsonString);
console.log(obj.name); // Output: John
```

2. **Stringifying JSON**: If you have a JavaScript object and want to convert it to a JSON string, you can use the `JSON.stringify()` function. For example:

```javascript
const obj = { name: "John", age: 30 };
const jsonString = JSON.stringify(obj);
console.log(jsonString); // Output: {"name":"John","age":30}
```

3. **Accessing JSON data**: Once you have parsed JSON into a JavaScript object, you can access its properties using dot notation or square brackets. For example:

```javascript
const jsonString = '{"name": "John", "age": 30}';
const obj = JSON.parse(jsonString);
console.log(obj.name); // Output: John
console.log(obj["age"]); // Output: 30
```

4. **Modifying JSON data**: You can modify JSON data by assigning new values to its properties. For example:

```javascript
const jsonString = '{"name": "John", "age": 30}';
const obj = JSON.parse(jsonString);

obj.name = "Alice";
obj.age = 25;

const modifiedJsonString = JSON.stringify(obj);
console.log(modifiedJsonString); // Output: {"name":"Alice","age":25}
```

These are just a few examples of how you can manipulate JSON data in JavaScript. There are additional methods and techniques available depending on your specific requirements.

# How to use request and fetch API

To make HTTP requests in JavaScript, you can use the `fetch` API or external libraries like `axios` or `request`.

## Using the fetch API (modern approach):

The `fetch` API is built into modern web browsers and provides a simple and powerful way to make HTTP requests. Here's an example of using the fetch API to make a GET request:

```javascript
fetch("https://api.example.com/data")
  .then(response => response.json())
  .then(data => {
    // Process the response data
    console.log(data);
  })
  .catch(error => {
    // Handle any errors
    console.error(error);
  });
```

This example makes a GET request to the URL "https://api.example.com/data". The response is obtained using the `response.json()` method, which returns a Promise that resolves to the parsed JSON data.

## Using external libraries (e.g., axios):

External libraries like axios provide additional features and support for older browsers. To use axios, you need to include the library in your project:

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

Here's an example of making a GET request using axios:

```javascript
axios.get("https://api.example.com/data")
  .then(response => {
    // Process the response data
    console.log(response.data);

    // Alternatively, you can access the response status code
    console.log(response.status);
  })
  .catch(error => {
    // Handle any errors
    console.error(error);
  });
```

This example demonstrates a GET request using `axios.get()`. The response data is available in the `response.data` property.

# How to read and write a file using the fs module

In Node.js, you can read and write files using the built-in `fs` module. Here are examples of how to perform file operations:

## Reading a file:

```javascript
const fs = require("fs");

fs.readFile("path/to/file.txt", "utf8", (error, data) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log(data);
});
```

In this example, `fs.readFile()` is used to read the contents of a file. The file path is specified as the first argument, and the second argument is the encoding (e.g., "utf8") to interpret the file's contents as text. The callback function is invoked with an error object and the file data.

## Writing to a file:

```javascript
const fs = require("fs");

const content = "Hello, World!";

fs.writeFile("path/to/file.txt", content, "utf8", (error) => {
  if (error) {
    console.error(error);
    return;
  }

  console.log("File written successfully.");
});
```

In this example, `fs.writeFile()` is used to write data to a file. The file path is specified as the first argument, the content to write is provided as the second argument, and the encoding is specified as the third argument. The callback function is invoked with an error object if an error occurs during the write operation.

These examples demonstrate basic file read and write operations using the `fs` module in Node.js. Remember to handle errors appropriately and provide the correct file paths and encodings based on your specific use case.
