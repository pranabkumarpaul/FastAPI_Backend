import json
import pathlib
import asyncpg
import asyncio

Config_File_Path= str(pathlib.Path(__file__).parent.parent) + "\config.json"

with open(Config_File_Path, 'r') as conf:
    data= json.loads(conf.read())
    conf.close()

database_connection_details= data['database_connection']  
database_credential= {'user' : database_connection_details['user'], 
                     'password' : database_connection_details['password'],
                     'database' : database_connection_details['database'], 
                     'port' : database_connection_details['port'],
                     'host' : database_connection_details['host']
                       }

async def run_sql( query , operation_type= ''):
    '''
    operation_type = Execute or Fetch (it is default)
    '''
     
    conn = await asyncpg.connect(**database_credential)

    try:
        if operation_type == 'Execute':
            res = await conn.execute(query)
            print(res)
            # return res
        else:
            res = await conn.fetch(query)
            data= [dict(i) for i in res]
            # print(data)
            return data

        print("Done")
    except Exception as e:
        print("### Issue")
        print(e)
    finally:
        await conn.close()
        print("Connection close")
    
    