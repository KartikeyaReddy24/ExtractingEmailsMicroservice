from fastapi import FastAPI
from mylib.sqs import *
from mylib.extracting_emails_function import *
import uvicorn
import os


app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "This is a Extracting Emails API Microservice."
    }


@app.get("/postgres")
async def postgres():
    """This is an extracting emails microservice"""

    return {"message": "This retrives data from PostgreSQL Database"}


@app.get("/cloudwatchlogs")
def cloudwatchlogs():
    """This is an create posts"""

    return {
        "message": "This retrives data from Cloud Watch Logs"

    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
