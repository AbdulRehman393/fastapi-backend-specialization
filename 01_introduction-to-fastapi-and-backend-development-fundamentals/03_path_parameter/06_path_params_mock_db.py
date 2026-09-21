from typing import Any

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


shipments = {
    12701: {
            "weight": 0.5,
            "content": "glassware",
            "status": "placed"
        },
        12702: {
            "weight": 1.8,
            "content": "books",
            "status": "in transit"
        },
        12703: {
            "weight": 3.4,
            "content": "laptop",
            "status": "delivered"
        },
        12704: {
            "weight": 2.1,
            "content": "coffee maker",
            "status": "placed"
        },
        12705: {
            "weight": 7.6,
            "content": "office chair",
            "status": "in transit"
        },
        12706: {
            "weight": 0.9,
            "content": "headphones",
            "status": "delivered"
        },
        12707: {
            "weight": 5.2,
            "content": "kitchen mixer",
            "status": "placed"
        },

    
}


@app.get("/shipment/latest")
def get_latest_shipment() -> dict[str, Any]:
        id = max(shipments.keys())   
        return shipments[id]

    

@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:

    if id not in shipments:
         return {"Detail": "Given Id doesnot exist"}

    return shipments[id]



@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )