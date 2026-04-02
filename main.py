import os
import uvicorn
from fastapi import FastAPI
from database import connect_to_mongo, close_mongo_connection
from routes import candidate

app = FastAPI(
    title="Candidate Management API",
    description="A simple API for managing candidates with MongoDB and FastAPI.",
    version="1.0.0"
)

# Application startup and shutdown events
@app.on_event("startup")
async def startup_event():
    """Execute startup events when the application starts."""
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    """Execute shutdown events when the application closes."""
    await close_mongo_connection()

# Include the candidate router
app.include_router(candidate.router)

@app.get("/", tags=["health"])
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok", "message": "Candidate Management API is running."}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    # Run the application using uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
