from constants import *
from common_utility.database import run_sql

async def get_all_email_details_data():
    DATA= await run_sql(operation_type= '', query= GET_EMAIL_DETAILS_QUERY)
    return DATA