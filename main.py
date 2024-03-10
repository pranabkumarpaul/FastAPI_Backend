from fastapi import FastAPI, Depends, HTTPException, APIRouter
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from constants import *
from routes import (
    email_routes , 
    dashboard_routes
)

app = FastAPI()

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

app.mount(path= "/email", app= email_routes.email)
app.mount(path= "/dashboard", app= dashboard_routes.dashboard)

# if __name__ == "__main__":
#     uvicorn.run("main:app", host= LOCAL_HOST, port= PORT, reload= True)

# # http://127.0.0.1:8090/email/api/dev/docs
# # http://127.0.0.1:8090/dashboard/api/dev/docs