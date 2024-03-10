import React from 'react';

const TableComponent = ({ data }) => {
  
  if (!data || data.length === 0) {
    return <div>No data available</div>; // Display a message if data is null, undefined, or empty
  }

  const headers = Object.keys(data);
  const rows = [Object.values(data)];


  return (
    <table>
      <thead>
        <tr>
          {headers.map(header => <th key={header}>{header}</th>)}
        </tr>
      </thead>
      <tbody>
        {rows.map((row, index) => (
          <tr key={index}>
            {row.map((cell, index) => <td key={index}>{cell}</td>)}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TableComponent;