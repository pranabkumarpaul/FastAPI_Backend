from fastapi import APIRouter
from models.dashboard_model import *
from typing import List
from constants import *
from routes_utility.dashboard_utility import (
    get_all_sales_details_data
)

dashboard = APIRouter(prefix="/dashboard")

@dashboard.get("/all_sales_details", response_model= List[sales_details_model])
async def get_all_sales_details():
    return await get_all_sales_details_data()