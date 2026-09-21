from typing import Any

from fastapi import FastAPI

# A path parameter is a variable part of the URL, written inside { }.
# Example: /shipment/{id} → /shipment/1001

# FastAPI gets the value from the URL and passes it to the function.
# Type hints such as id: int tell FastAPI what type of value is expected,
# and FastAPI validates the incoming value automatically.


app = FastAPI()


@app.get("/shipment/{id}")
def get_shipment(id: int) -> dict[str, Any]:         # The return type hint -> dict[str, Any] tells FastAPI that the function    
        return{                                      # returns a dictionary with string keys and values of any type.              
                "id": id,
                "weight": 1.2,
                "content": "wooden table",
                "status": "in transit"
        }


