from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Query, Path

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

class BlogModel(BaseModel):
    title: str
    content: str


@router.get("/")
def list_blogs(page: int = 1, page_size: int = 10):
    return {"page": page, "page_size": page_size}

@router.post("/add")
def create_blog(blog: BlogModel):
    return blog


@router.get("/{id}")
def get_blog(id: int):
    return {"blog_id": id}


@router.post("/new/{id}/comment")
def create_comment(
    blog: BlogModel,
    id: int = Path(..., title="Blog ID"),
    comment_id: int = Query(
        None,
        title="ID of the comment",
        description="Description of the comment",
        alias="commentId",
        deprecated=True
    )
):
    return {
        "blog": blog,
        "id": id,
        "comment_id": comment_id
    }

