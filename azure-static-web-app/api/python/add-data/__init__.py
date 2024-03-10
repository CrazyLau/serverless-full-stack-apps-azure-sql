import datetime
import logging
import os
import requests
import json
import pyodbc
from datetime import datetime as dt
import azure.functions as func



def main(req: func.HttpRequest) -> func.HttpResponse:
    AZURE_CONN_STRING = str(os.environ["AzureSQLConnectionString"])

    result = {}
    

    try: 
        conn = pyodbc.connect(AZURE_CONN_STRING)
        
        with conn.cursor() as cursor:

            cursor.execute(f"select top(1) * from dbo.GroceryList for json auto, include_null_values, without_array_wrapper")
            result = cursor.fetchone()[0]
            
            if result:
                result = json.loads(result)                           
            else:
                result = {}     

            logging.info(result)   
            
    except Exception as e:
        error_string = str(e)
        return func.HttpResponse(error_string)
        
    finally:
        cursor.close()

    return func.HttpResponse(json.dumps(result))
    


