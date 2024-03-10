import React from 'react';
import RecipeTitle from './RecipeTitle'
import TableComponent from './TableComponent'
import './index.css'

function callApi() {
    fetch('https://proud-bush-0cec8fb03.5.azurestaticapps.net/api/bus-data') // api for the get request
    .then(response => response.json())
    .then((data) => {return 'hej';})
    // return data
    // return [{"Id": 1, "Item": "Apples", "Amount": 2}]
  }

function myFunction() {
document.getElementById("demo").innerHTML = callApi();
}

function App() {
    return (
        <div className="article">
                <h2>Hello World!</h2> 
                <TableComponent data={callApi()} />

                <button onClick={myFunction}>Fetch data</button>
                <p id="demo"></p>

                <button onClick={myFunction}>Run Databricks job</button>
 
        </div>
    )
}

export default App;