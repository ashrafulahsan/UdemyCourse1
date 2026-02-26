from fastapi import APIRouter, File, UploadFile
import shutil

router = APIRouter(
    prefix="/file",
    tags=["file"]
)

@router.post("/upload")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split('\n')
    return {'lines': lines}

@router.post("/upload-large")
def get_large_file(upload_file: UploadFile = File(...)):
    path = f"files/{upload_file.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {
        "filename": path,
        "content_type": upload_file.content_type
    }

