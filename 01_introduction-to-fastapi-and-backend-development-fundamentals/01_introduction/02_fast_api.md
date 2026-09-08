# FastAPI
FastAPI is a modern, high-performance Python web framework used to build **APIs (Application Programming Interfaces)** quickly and efficiently. It is especially popular for developing backend services, machine learning APIs, and microservices.

The name FastAPI has two meanings:

1. Fast to run – It is one of the fastest Python web frameworks because it is built on Starlette for web functionality and Pydantic for data validation. Its performance is comparable to frameworks written in languages like Node.js and Go.
2. Fast to develop – It reduces the amount of code you need to write by using Python type hints. This leads to faster development, fewer bugs, and automatic documentation.

Exampple:

To build simple API endpoints with FastAPI, we can start with a basic python function

```text
def read_shipment(id: int):
  pass
```

We can make it endpoint using a decorator, telling it which request method and path to handle. Then you can return data from that function and FastAPI sends it back as the
response to the client

example:
```text
from fastapi import FastAPI

app = FASTAPI()

@app.get("/shipment"):
def read_shipment(id: int):
  return{
        "id" : id.
        "status" : "delivered"
        }
```

Once the endpoints are defined, we can run the API server using FastAPI and it's ready to accept requests and send responses.



