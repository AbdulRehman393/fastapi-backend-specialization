from fastapi import FastAPI

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
# and that's how we define our API endpoints using FastAPI.



