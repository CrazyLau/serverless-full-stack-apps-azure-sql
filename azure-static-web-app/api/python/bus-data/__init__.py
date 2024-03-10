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
            cursor.execute("SELECT * FROM dbo.GroceryList FOR JSON AUTO, INCLUDE_NULL_VALUES")
            rows = cursor.fetchall()
            for row in rows:
                try:
                    row_data = json.loads(row[0])
                    results.append(row_data)
                    logging.info(f"Row data: {row_data}")
                except json.JSONDecodeError as e:
                    logging.error(f"Error decoding JSON: {e}")
            
    except pyodbc.Error as e:
        error_string = f"Database error: {str(e)}"
        return func.HttpResponse(error_string, status_code=500)
        
    except Exception as e:
        error_string = f"Error: {str(e)}"
        return func.HttpResponse(error_string, status_code=500)
        
    return func.HttpResponse(json.dumps(results), status_code=200)
