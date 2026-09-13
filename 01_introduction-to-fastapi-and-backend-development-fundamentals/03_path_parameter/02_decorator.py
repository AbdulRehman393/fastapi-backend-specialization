# Decorator = A function that extends the behavior of another function
#             without modifying the base function
#             Pass the base function as an argument as an argument to the decorator


def custom_fence(fence: str = "+"):
    def add_fence(func):
        def wrapper(text: str):
            print(fence * len(text))
            func(text)
            print(fence * len(text))
        return wrapper
    return add_fence


# Using custom decorator
@custom_fence("-")
def log(text: str):
    print(text)

log("ballon")


