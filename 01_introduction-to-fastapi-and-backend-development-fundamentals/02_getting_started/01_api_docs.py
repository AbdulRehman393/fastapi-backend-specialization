from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

@app.get("/shipment")
def get_shipment():
    return{
        "content": "wooden table",
        "status": "in transit"
            }

# Above we have defined a function that simply returns the shipment data and then we used FastAPI
# to mark this as a route handler on get method for this url i.e., /shipment, We start our server
# with this command fastapi dev <file_name> on development mode at local host, then we used any 
# browser to make a request inside of our server and it used our function to return this data back
# FastAPI automatically converts this dictionary into JSON when sending it as an HTTP response.
# and that's how we define our API endpoints using FastAPI.

# A route handler is a function that runs when a request comes to a particular API route.
# @app.get("/shipment") → defines the route or path
# get_shipment() → route handler function
# return {...} → response sent back to the client


# ------- API Documentation  ---------
# FastAPI takes the endpoints which we have defined and the OpenAPI specification for them.
# OpenAPI is the industry-standard specification for designing and documenting APIs (formerly known as Swagger).
# FastAPI generates OpenAPI specifications and Swagger UI is used to generate this documentation.
# We can use it as an API client as well; we can make requests there and check the response.
# If we write /redoc instead of /docs in the URL, it generates documentation that is lightweight.
# We can also generate custom documentation using the OpenAPI specifications. Here we are
# generating Scalar docs.

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )

# Above we have defined custom documentation using the OpenAPI specification.


