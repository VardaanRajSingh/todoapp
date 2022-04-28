def story_serializer(story) ->dict:
    return{
        "id": str(story["_id"]),
        "name": story["name"],
        "description": story["description"],
        "assignedTo": story["assignedTo"],
        "completed": story["completed"],
        "date": story["date"],
    }

def stories_serializer(stories) -> list :
    return [story_serializer(story) for story in stories]
