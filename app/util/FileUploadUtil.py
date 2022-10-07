import os.path
import uuid
from typing import List

from fastapi import UploadFile

UPLOAD_DIRECTORY = "./resource/"


async def upload_file_list(file_list: List[UploadFile]):
    file_name_list = []
    for item in file_list:
        contents = await item.read()
        if contents != bytes():  # 업로드한 파일이 비어있지 않은 경우에만 업로드
            file_path = os.path.join(UPLOAD_DIRECTORY, (str(uuid.uuid4()) + '.' + item.filename.split('.')[-1]))
            with open(file_path, "wb") as fp:
                fp.write(contents)
                file_name_list.append(file_path)

    return file_name_list


