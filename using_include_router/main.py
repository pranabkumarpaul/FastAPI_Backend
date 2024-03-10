##################################
# Using Include Router ###########

from fastapi import FastAPI, Depends, HTTPException, APIRouter
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from constants import *
from routes import (
    email_routes , 
    dashboard_routes
)

app = FastAPI(docs_url= BASE_PATH.format(ENV= 'dev') + "/docs",
              openapi_url= BASE_PATH.format(ENV= 'dev') + "/openapi.json"
              )
# app = FastAPI()

# origins = ["http://localhost", "http://localhost:8090", ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["POST", "GET"],
#     allow_headers=["*"],
#     max_age=3600,
# )

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)

app.include_router(email_routes.email, prefix= BASE_PATH.format(ENV= 'dev'))
app.include_router(dashboard_routes.dashboard, prefix= BASE_PATH.format(ENV= 'dev'))

if __name__ == "__main__":
    uvicorn.run("main:app", host= LOCAL_HOST, port= PORT, reload= True)

# # http://127.0.0.1:8090/api/dev/docs