from pydantic import BaseModel, Field
from typing import Union

class email_details_model(BaseModel):
    id : int
    dept : str
    email_id : str
    subject : str
    body : str
    
    class config:
        orm_mode = True

class email_query_model(BaseModel):
    dept : str
    email_id : str

    class config:
        orm_mode = True

        