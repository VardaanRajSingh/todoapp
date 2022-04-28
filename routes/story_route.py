from math import dist
from fastapi import APIRouter
from dbconfig.database import collection_name
from model.story_model import Story
from schemas.story_schemas import story_serializer,stories_serializer
from bson import ObjectId



story_api_router=APIRouter()

#getAll
@story_api_router.get("/")
async def get_stories():
    stories=stories_serializer(collection_name.find())
    return stories

#getOne
@story_api_router.get("/{id}")
async def get_story(id:str):
    story=story_serializer(collection_name.find_one({"_id": ObjectId(id)}))
    return story

#add
@story_api_router.post("/")
async def add_story(story: Story):
    resp=collection_name.insert_one(dict(story))
    return story_serializer(collection_name.find_one({"_id": resp.inserted_id}))
    


#update
@story_api_router.put("/{id}")
async def update_story(id:str,story:Story):
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(story)})
    #return 200
    return story_serializer(collection_name.find_one({"_id":ObjectId(id)}))

# delete
@story_api_router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}

