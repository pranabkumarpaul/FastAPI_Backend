from constants import *
from common_utility.database import run_sql

async def get_all_email_details_data():
    DATA= await run_sql(operation_type= '', 
                        query= GET_EMAIL_DETAILS_QUERY
                        )
    return DATA


async def get_email_details_data(user_data):
    DATA= await run_sql(operation_type= '', 
                        query= GET_EMAIL_QUERY.format(DEPT= user_data.dept ,
                                                              EMAIL_ID= user_data.email_id
                                                              )
                                                    )
    return DATA

async def insert_email_details_data(user_data):
    await run_sql(operation_type= 'Execute', 
            query= INSERT_EMAIL_DETAILS_QUERY.format(ID= user_data.id,
                                                    DEPT= user_data.dept,
                                                    EMAIL_ID= user_data.email_id,
                                                    SUBJECT= user_data.subject,
                                                    BODY= user_data.body
                                                    )
                                                )
    return user_data