import React, { useState, useEffect } from 'react';
import TableComponent from './TableComponent';
import './index.css';

const API_URL = 'https://proud-bush-0cec8fb03.5.azurestaticapps.net/api/bus-data';

function callApi() {
    return fetch(API_URL)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            return response.json();
        });
}

function updateApiData(updatedData) {
    const PUT_URL = 'https://dummyjson.com/products/1';
    return fetch(PUT_URL, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to update data');
        }
        return response.json();
    });
}

function App() {
    const [apiData, setApiData] = useState(null);
    const [newData, setNewData] = useState({});

    useEffect(() => {
        fetchData();
    }, []);

    async function fetchData() {
        try {
            const data = await callApi();
            setApiData(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    async function handleUpdate() {
        try {
            await updateApiData(newData);
            fetchData();
        } catch (error) {
            console.error('Error updating data:', error);
        }
    }

    function handleChange(event) {
        const { name, value } = event.target;
        setNewData(prevData => ({
            ...prevData,
            [name]: value,
        }));
    }

    return (
        <div className="article">
            <h2>Hello World!</h2>

            <button onClick={fetchData}>Refresh Table</button>
            {apiData && <TableComponent data={apiData} />}

            <div>
                <input
                    type="text"
                    name="name"
                    placeholder="Name"
                    value={newData.name || ''}
                    onChange={handleChange}
                />
                <input
                    type="number"
                    name="price"
                    placeholder="Price"
                    value={newData.price || ''}
                    onChange={handleChange}
                />
                <button onClick={handleUpdate}>Update Data</button>
            </div>
        </div>
    );
}

export default App;
