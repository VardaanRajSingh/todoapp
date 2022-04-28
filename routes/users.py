from fastapi import APIRouter
from mongomock import ObjectId
from model.users import App_Schema
from config.db import conn
from collections import defaultdict
from bson import ObjectId
#user=APIRouter()
from schemas.user import userEntity, usersEntity
#app = FastAPI(title="To-DO Application", openapi_url="/openapi.json")
api_router = APIRouter()
tasks=[]

@api_router.post("/add", status_code=201)
#@api_router.post("/create/", status_code=201,include_in_schema=False)
def create_app(data: App_Schema):
    #for key in tasks:
        #if 'task ->'+data.task in tasks[key]:
    #if 'task ->'+data.task in tasks[data.priority]:
    #tasks[data.priority].append('task ->'+data.task)
    if data.task in tasks:
        return {"msg":'Task already exists'}
    conn.local.user.insert_one(dict(data))
    return {"msg":'Task successfully added to-do list!'}


@api_router.delete("/delete_task/{task_id}", status_code=200)
def delete_app(task_id : str):
    if not conn.local.user.find_one({"_id":ObjectId(task_id)}):
        return {'msg':'Task does not exist!'}
    #if task_id not in tasks:
    #    return {'msg':'There are no tasks with the given prority!'}
    #if 'task ->'+task_name not in tasks[task_id]:
    #    return {'msg':'Task does not exist!'}
    conn.local.user.find_one_and_delete({"_id":ObjectId(task_id)})
    #tasks[task_id].remove('task ->'+task_name)
    return {'msg':'Task successfully deleted!'}

@api_router.get("/get-all", status_code=200)
def get_all():
    #sorted_tasks=sorted(tasks.items(), key=lambda x: x[1][0])
    #all_tasks=defaultdict(list)
    #for taskId in tasks:
    # all_tasks['available_tasks'].append({taskId:['priority ->', tasks[taskId][0],'task ->',tasks[taskId][1]]})
    return usersEntity(conn.local.user.find())
    

@api_router.patch("/update/{id}", status_code=200)
def modify( id, data :App_Schema):
    if not conn.local.user.find_one({"_id":ObjectId(id)}):
        return {'msg':'Task does not exist!'}
    '''
    if task_name:
        tasks[data.priority].remove('task ->'+task_name)
    for k in tasks:
        if 'task ->'+data.task in tasks[k]:
            tasks[k].remove('task ->'+data.task)
            if data.priority in tasks:
                tasks[data.priority].append('task ->'+data.task)
                break
    if not data.priority in tasks or task_name:
    '''
    conn.local.user.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(data)})
    #tasks[data.priority].append('task ->'+data.task)
    return {'msg':'Task updated successfully'}