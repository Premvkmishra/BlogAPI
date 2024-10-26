from fastapi import FastAPI
from .routes import router as blog_router

app = FastAPI(
    title="School Blog API",
    description="A simple school blog API with FastAPI and MongoDB",
    version="1.0.0",
)

app.include_router(blog_router, prefix="/blog", tags=["Blog"])

@app.get("/")
async def root():
    return {"message": "Welcome to the School Blog API"}
