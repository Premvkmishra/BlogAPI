from fastapi import APIRouter, HTTPException
from bson import ObjectId
from .database import blog_collection
from .models import BlogPostModel, BlogPostResponseModel

router = APIRouter()

@router.post("/", response_model=BlogPostResponseModel)
async def create_blog_post(blog: BlogPostModel):
    blog = await blog_collection.insert_one(blog.dict())
    new_blog = await blog_collection.find_one({"_id": blog.inserted_id})
    return BlogPostResponseModel(**new_blog)

@router.get("/{id}", response_model=BlogPostResponseModel)
async def get_blog_post(id: str):
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog:
        return BlogPostResponseModel(**blog)
    raise HTTPException(status_code=404, detail="Blog not found")

@router.put("/{id}", response_model=BlogPostResponseModel)
async def update_blog_post(id: str, blog: BlogPostModel):
    await blog_collection.update_one({"_id": ObjectId(id)}, {"$set": blog.dict()})
    updated_blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if updated_blog:
        return BlogPostResponseModel(**updated_blog)
    raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/{id}", response_model=dict)
async def delete_blog_post(id: str):
    result = await blog_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Blog post deleted"}
    raise HTTPException(status_code=404, detail="Blog not found")
