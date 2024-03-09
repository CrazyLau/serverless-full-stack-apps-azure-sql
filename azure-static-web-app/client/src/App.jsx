import React from 'react';
import RecipeTitle from './RecipeTitle'
import './index.css'

function callApi() {
    fetch('https://proud-bush-0cec8fb03.5.azurestaticapps.net/api/bus-data') // api for the get request
    .then(response => response.json())
    .then(data => console.log(data));
  }
  

function App() {
    return (
        <button onClick={callApi}>Call API</button>
    )
}

export default App;