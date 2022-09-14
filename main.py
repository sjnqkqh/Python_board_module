import os

from fastapi import FastAPI, UploadFile, Form
from typing import List

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send")
async def create_file(files: List[UploadFile], user_id: int = Form(''), title: str = Form(''), content: str = Form('')):
    upload_directory = "./resource/"
    print(user_id, title, content)

    for item in files:
        contents = await item.read()
        with open(os.path.join(upload_directory, item.filename), "wb") as fp:
            fp.write(contents)

    return {
        "file_size": len(files)
    }
