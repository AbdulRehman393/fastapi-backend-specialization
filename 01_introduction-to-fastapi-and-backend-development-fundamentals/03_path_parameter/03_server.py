from collections.abc import Callable
from typing import Any

routes: dict[str, Callable[[Any], None]] = {}

def route(path: str):
    def register_route(func):
        routes[path] = func
        return func
    return register_route



@route("/shipment")
def get_shipment():
    return "Shipment<1001, in transit"


request : str = ""

while request != "quit":
    request = input(">  ")

    if request in routes:
        response = routes[request]()
        print(response, end="\n\n")
    else:
        print("Not found")