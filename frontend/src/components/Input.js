import React from "react";
import PropTypes from "prop-types";

const Input = ({ label, name, onChange, type, value }) => (
  <>
    <label className="label" htmlFor={name}>
      {label}
    </label>
    <input name={name} type={type} onChange={onChange} value={value} />
  </>
);

Input.propTypes = {
  label: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  type: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
};

export default Input;
