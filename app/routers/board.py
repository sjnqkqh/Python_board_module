# from typing import List
# from sqlalchemy.orm import Session
# from fastapi import APIRouter, UploadFile, Form, Depends
#
# import os
# from ..db import database
# from .. import model
#
# model
#
# upload_directory = "./resource/"
# router = APIRouter
#
#
# @router.post("/api/board", tags=["board"])
# async def create_post(files: List[UploadFile], user_id: int = Form(''), title: str = Form(''), content: str = Form(''),
#     db: Session = Depends(database.get_db())):
#     """
#     게시글 작성
#     :param files: 업로드 할 파일 목록
#     :param user_id: FIXME 회원 ID
#     :param title: 게시글 제목
#     :param content: 게시글 내용
#     :return: 게시글 ID
#     """
#     user = crud
#
#     print(user_id, title, content)
#
#     for item in files:
#         contents = await item.read()
#         with open(os.path.join(upload_directory, item.filename), "wb") as fp:
#             fp.write(contents)
#
#     return {
#         "file_size": len(files)
#     }
