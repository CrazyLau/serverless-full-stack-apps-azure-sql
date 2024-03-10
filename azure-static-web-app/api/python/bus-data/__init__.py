import os
import json
import pyodbc
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    AZURE_CONN_STRING = os.environ.get("AzureSQLConnectionString")

    try: 
        with pyodbc.connect(AZURE_CONN_STRING) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.GroceryList FOR JSON AUTO, INCLUDE_NULL_VALUES, WITHOUT_ARRAY_WRAPPER")
            rows = cursor.fetchall()

            # Initialize an empty list to store JSON objects for each row
            # result = []
            result = rows
            # Iterate through each row and append its JSON representation to the result list
            # for row in rows:
            #     result.append(json.loads(row[0]))
            
    except pyodbc.Error as e:
        error_string = f"Database error: {str(e)}"
        return func.HttpResponse(error_string, status_code=500)
        
    except Exception as e:
        error_string = f"Error: {str(e)}"
        return func.HttpResponse(error_string, status_code=500)
        
    return func.HttpResponse(result, status_code=200)  # json.dumps(result)
