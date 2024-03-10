CREATE_EMAIL_TBL= """
create table public.email( id int, dept varchar(5), 
email_id varchar(20), subject varchar(10), body varchar (30) ) ;
"""

INSERT_DATA_TO_EMAIL_TBL= """
insert into public.email values
(1, 'IT', '61169test@gmail.com', 'sub - IT', 'This is IT dept.'),
(2, 'BPO', '61169test@gmail.com', 'sub - BPO', 'This is BPO dept.'),
(3, 'HR', '61169test@gmail.com', 'sub - HR', 'This is HR dept.');
"""

CREATE_SALES_TBL= "create table sales(region varchar(15), sales int);"

INSERT_DATA_TO_SALES_TBL= """
insert into sales values ('east', 200), ('west', 12578), ('north', 6512700), ('south', 3111);
"""

from common_utility.database import run_sql
import asyncio

if __name__ == '__main__':
    asyncio.run(run_sql(operation_type= 'Execute', query= CREATE_EMAIL_TBL))
    asyncio.run(run_sql(operation_type= 'Execute', query= INSERT_DATA_TO_EMAIL_TBL))

    asyncio.run(run_sql(operation_type= 'Execute', query= CREATE_SALES_TBL))
    asyncio.run(run_sql(operation_type= 'Execute', query= INSERT_DATA_TO_SALES_TBL))


