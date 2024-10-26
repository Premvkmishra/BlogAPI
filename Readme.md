# School Blog API

A simple and efficient **School Blog API** built using **FastAPI** and **MongoDB**. This API allows users to perform CRUD operations on blog posts. The project uses **Motor** (an asynchronous MongoDB driver) for database operations and **Pydantic** for data validation.

## Features

- **Create** new blog posts
- **Read** individual blog posts by ID
- **Update** existing blog posts
- **Delete** blog posts by ID
- Data validation using **Pydantic**
- MongoDB connection using **Motor** for async database operations

## Tech Stack

- **FastAPI** - For building the API endpoints
- **MongoDB** - Database for storing blog post data
- **Motor** - Async MongoDB driver
- **Pydantic** - For data validation
- **Uvicorn** - ASGI server to run the FastAPI app

## Prerequisites

- Python 3.8+
- MongoDB server running locally or remotely

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/SchoolBlogAPI.git
   cd SchoolBlogAPI
