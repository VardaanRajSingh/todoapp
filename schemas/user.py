def userEntity(item):
    return {
        "id":str(item["_id"]),
        "task": item["task"],
        "priority":item["priority"]

    }

def usersEntity(entity):
    return [userEntity(item) for item in entity]