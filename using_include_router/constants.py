LOCAL_HOST= "127.0.0.1"
PORT= 8090
BASE_PATH= "/api/{ENV}"

GET_EMAIL_DETAILS_QUERY= "select * from public.email;"
INSERT_EMAIL_DETAILS_QUERY= """
INSERT INTO public.email
(id, dept, email_id, subject, body)
VALUES({ID}, '{DEPT}', '{EMAIL_ID}', '{SUBJECT}', '{BODY}');
"""
GET_EMAIL_QUERY= """
select * from public.email where dept = '{DEPT}' and email_id = '{EMAIL_ID}';
"""


GET_SALES_DETAILS_QUERY= "select * from public.sales;"
GET_REGION_SALES_QUERY= "select * from public.sales {WHERE_CLAUSE};"