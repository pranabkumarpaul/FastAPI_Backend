from constants import *
from common_utility.database import run_sql

async def get_all_sales_details_data():
    DATA= await run_sql(operation_type= '', query= GET_SALES_DETAILS_QUERY)
    return DATA


async def get_region_sales_data(region):
    if region[0] == 'All':
        WHERE_CLAUSE= ''
    else:
        Regions= ', '.join(["'" + Each_Region + "'" for Each_Region in region])
        WHERE_CLAUSE= f"where region in ({Regions})"

    DATA= await run_sql(operation_type= '', 
                        query= GET_REGION_SALES_QUERY.format(WHERE_CLAUSE= WHERE_CLAUSE
                                                                                 )
                                                                )
    return DATA