from imp import reload
from fastapi import FastAPI, APIRouter
from routes.users import api_router
import uvicorn
app=FastAPI()
app.include_router(api_router)

uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

