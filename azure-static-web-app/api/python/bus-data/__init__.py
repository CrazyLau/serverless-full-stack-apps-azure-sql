import os
import json
import pyodbc
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    AZURE_CONN_STRING = os.environ.get("AzureSQLConnectionString")
    results = []

    try: 
        with pyodbc.connect(AZURE_CONN_STRING) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.GroceryList -- FOR JSON AUTO, INCLUDE_NULL_VALUES")
            rows = cursor.fetchall()
            for row in rows:
                results.append(json.loads(row[0]))
            
    except pyodbc.Error as e:
        error_string = f"Database error: {str(e)}"
        return func.HttpResponse(error_string, status_code=500)
        
    except Exception as e:
        error_string = f"Error: {str(e)}"
        return func.HttpResponse(error_string, status_code=500)
        
    return func.HttpResponse(json.dumps(results), status_code=200)
