import React from "react";
import PropTypes from "prop-types";

const BookTable = ({ books }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Tytuł</th>
          <th>Autor</th>
          <th>Średnia</th>
        </tr>
      </thead>
      <tbody>
        {books.map(({ title, author, avg_rate }, index) => (
          <tr key={index}>
            <td>{title}</td>
            <td>{author}</td>
            <td>{avg_rate || "brak ocen"}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

BookTable.propTypes = {
  books: PropTypes.array.isRequired,
};

export default BookTable;
