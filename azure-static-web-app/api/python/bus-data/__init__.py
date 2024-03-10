import os
import json
import pyodbc
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    AZURE_CONN_STRING = os.environ.get("AzureSQLConnectionString")

    try: 
        with pyodbc.connect(AZURE_CONN_STRING) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dbo.GroceryList FOR JSON AUTO, INCLUDE_NULL_VALUES--, WITHOUT_ARRAY_WRAPPER")
            row = cursor.fetchone()

            if row:
                json_data = str(row[0])
            else:
                json_data = "[]"  # Return empty JSON array if no data is fetched

    except pyodbc.Error as e:
        error_string = f"Database error: {str(e)}"
        return func.HttpResponse(error_string, status_code=500)
        
    except Exception as e:
        error_string = f"Error: {str(e)}"
        return func.HttpResponse(error_string, status_code=500)
        
    return func.HttpResponse(json_data, status_code=200, mimetype="application/json")  
