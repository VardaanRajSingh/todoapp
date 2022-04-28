import uvicorn
from fastapi import FastAPI
from routes.story_route import story_api_router

app = FastAPI()

app.include_router(story_api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)

#$ uvicorn example:app --reload --port 5000
