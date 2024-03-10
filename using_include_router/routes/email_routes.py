from fastapi import APIRouter
from models.email_model import *
from typing import List
from constants import *

from routes_utility.email_utility import (
    get_all_email_details_data ,
)

email = APIRouter(prefix="/email")

@email.get("/all_email_details", response_model= List[email_details_model])
async def get_all_email_details():
    return await get_all_email_details_data()