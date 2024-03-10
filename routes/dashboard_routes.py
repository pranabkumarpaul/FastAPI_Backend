from fastapi import FastAPI
from models.dashboard_model import *
from typing import List
from constants import *
from routes_utility.dashboard_utility import (
    get_all_sales_details_data
)

dashboard = FastAPI(docs_url= BASE_PATH.format(ENV= 'dev') + "/docs",
              openapi_url= BASE_PATH.format(ENV= 'dev') + "/openapi.json"
              )

@dashboard.get("/all_sales_details", response_model= List[sales_details_model])
async def get_all_sales_details():
    return await get_all_sales_details_data()