# FastAPI is a python class that provides all the functionality for the API i.e is a
# class that inherits directly from Starlette
# thus you can use all the Starlette  functionality with FastAPI too
from fastapi import FastAPI
# creating a fastapi instance
# the variable (app) will be an instance of the class FastAPI
# thus the "model" created i.e the app is the one
# referred in the uvicorn in the command line.....uvicorn main:app --reload
app = FastAPI()
# have use GET method to read data i.e @app.get("/")
# tells the FastAPI that the function below it is in-charge of handling requests
# that go to the path (/) using a get operation.
# @something is called the (decorator) in python
@app.get("/")
# hence the above line of code tells the FastAPI that the
# right function below it corresponds to the path / with an operation get.
# thus called the path operation decorator
async def root():
    # its the python fucntion that is called by FastAPI whenever
    # it receives a request to the URL ('/') using a get operation
    # but in the case its a async function
    # you can also define it normally...i.e def root()
    return "Hello felix"
# return the content
# you can return the a dict,list,Pydamic models,singular values i.e str,int etc.