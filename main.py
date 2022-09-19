import os
import uuid
from typing import List

from fastapi import FastAPI, UploadFile, Form, Depends
from sqlalchemy.orm import Session

from app import model
from app.db.database import SessionLocal

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello, World"}


@app.post("/send")
async def create_file(files: List[UploadFile], user_id: int = Form(default=0, alias="userId"), title: str = Form(''), content: str = Form(''),
    db: Session = Depends(get_db)
):
    """
    게시글 작성
    :param files: 업로드 할 파일 목록
    :param user_id: FIXME 회원 ID
    :param title: 게시글 제목
    :param content: 게시글 내용
    :return: 게시글 ID
    """
    upload_directory = "./resource/"
    post = model.Post(USER_ID=user_id, TITLE=title, CONTENT=content)
    db.add(post)

    for item in files:
        contents = await item.read()
        with open(os.path.join(upload_directory, (str(uuid.uuid4()) + '.' + item.filename.split('.')[-1])), "wb") as fp:
            fp.write(contents)

    db.commit()

    return {
        "postId": post.POST_ID
    }
