import React, { useState } from "react";
import PropTypes from "prop-types";

import Input from "../Input";

const BookForm = ({ onSubmit }) => {
  const [search, setSearch] = useState("");

  return (
    <form
      className="form"
      onSubmit={(event) => {
        event.preventDefault();
        onSubmit(search);
        setSearch("");
      }}
    >
      <Input
        label="Tytuł szukanej książki"
        name="search"
        onChange={(event) => setSearch(event.target.value)}
        type="search"
        value={search}
      />
      <button type="submit" disabled={!search}>
        Wyszukaj
      </button>
    </form>
  );
};

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
};

export default BookForm;
