from fastapi import APIRouter, Query
from models.dashboard_model import *
from typing import List
from constants import *
from routes_utility.dashboard_utility import (
    get_all_sales_details_data ,
    get_region_sales_data
)

dashboard = APIRouter(prefix="/dashboard", tags= ['Dashboard'])

@dashboard.get("/all_sales_details", response_model= List[sales_details_model])
async def get_all_sales_details():
    return await get_all_sales_details_data()

@dashboard.post("/region_sales", response_model= List[sales_details_model])
async def get_region_sales(region:List[str] = Query(['All'])):
    return await get_region_sales_data(region)