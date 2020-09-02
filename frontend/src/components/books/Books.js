import React, { useState } from "react";

import BookForm from "./BookForm";
import BookTable from "./BookTable";

export default () => {
  const [books, setBooks] = useState([]);

  async function getBooks(title) {
    if (!title) return;
    const url = new URL("books/", process.env.REACT_APP_API_URL);
    url.searchParams.append("title", title);
    const response = await fetch(url);
    const { data } = await response.json();
    setBooks(data);
  }

  return (
    <>
      <BookForm onSubmit={getBooks} />
      {books.length ? (
        <BookTable books={books} />
      ) : (
        <small>Brak książek do wyświetlenia.</small>
      )}
    </>
  );
};
