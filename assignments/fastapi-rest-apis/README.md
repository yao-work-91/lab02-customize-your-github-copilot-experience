# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a REST API using FastAPI and practice designing endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️	Create the API Foundation

#### Description
Set up a FastAPI application with a small in-memory dataset and implement core endpoints to create and read resources.

#### Requirements
Completed program should:

- Initialize a FastAPI app and run it locally
- Define at least one Pydantic model for request and response data
- Implement a `GET /items` endpoint that returns all items
- Implement a `POST /items` endpoint that creates a new item with validation
- Return JSON responses with appropriate HTTP status codes


### 🛠️	Add Resource Operations and Error Handling

#### Description
Extend the API with additional operations and error handling so clients can fetch individual resources and update or delete data safely.

#### Requirements
Completed program should:

- Implement `GET /items/{item_id}` to return a single item
- Implement `PUT /items/{item_id}` to update an existing item
- Implement `DELETE /items/{item_id}` to remove an item
- Return `404` when an item does not exist
- Include clear response messages for successful updates and deletes