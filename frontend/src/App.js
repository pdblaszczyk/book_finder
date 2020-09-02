import React from "react";

import Books from "./components/books/Books";

function App() {
  return (
    <div className="wrapper">
      <div className="container">
        <h1>Book Finder</h1>
        <Books />
      </div>
    </div>
  );
}

export default App;
