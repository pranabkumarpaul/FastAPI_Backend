from pydantic import BaseModel, Field
from typing import Union

class sales_details_model(BaseModel):
    region : str
    sales : int

    class config:
        orm_mode = True