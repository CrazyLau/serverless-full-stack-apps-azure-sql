import React from 'react';

const TableComponent = ({ data }) => {
  if (!data || data.length === 0) {
    return <div>No data available</div>; // Display a message if data is null, undefined, or empty
  }

  const headers = Object.keys(data[0] || {}); // Use the keys of the first object to determine headers

  return (
    <table>
      <thead>
        <tr>
          {headers.map(header => <th key={header}>{header}</th>)}
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index}>
            {headers.map((header, index) => <td key={index}>{row[header]}</td>)}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default TableComponent;
