from pydantic import BaseModel, Field
from typing import Optional

class BlogPostModel(BaseModel):
    title: str = Field(...)
    content: str = Field(...)
    author: str = Field(...)
    published: Optional[bool] = Field(default=True)

class BlogPostResponseModel(BlogPostModel):
    id: str = Field(..., alias="_id")
