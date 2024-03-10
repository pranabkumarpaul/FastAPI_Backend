from constants import *
from common_utility.database import run_sql

async def get_all_sales_details_data():
    DATA= await run_sql(operation_type= '', query= GET_SALES_DETAILS_QUERY)
    return DATA