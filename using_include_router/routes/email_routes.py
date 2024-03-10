from fastapi import APIRouter
from models.email_model import *
from typing import List
from constants import *

from routes_utility.email_utility import (
    get_all_email_details_data ,
    get_email_details_data,
    insert_email_details_data
)

email = APIRouter(prefix="/email", tags= ['Email'])

@email.get("/all_email_details", response_model= List[email_details_model])
async def get_all_email_details():
    return await get_all_email_details_data()

@email.post("/email_details", response_model= List[email_details_model])
async def get_email_details(user_data:email_details_model):
    return await get_email_details_data(user_data)

@email.post("/insert_email", response_model= email_details_model)
async def insert_email_details(user_data: email_details_model):
    return await insert_email_details_data(user_data)