from fastapi import FastAPI
# the value of the path parameter item_id will be passed to the function as an argument item_id
items = {
    "books":1,
    "students":4,
    "laptops":3,
    "food_chunks":2
}

app = FastAPI()

@app.get("/items/{item_id}")
# note that the value the function received and returned is 3,as a python  int,not a string "3"
# so with the of declaration,FastAPI gives you automatic request "parsing"
async def root(item_id: str):
    return {"item_id":item_id}