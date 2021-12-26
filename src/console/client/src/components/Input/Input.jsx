import React from 'react';


export const Input = (props) => {
  const {
    value,
    onChange,
    label,
    id
  } = props;

  return (
    <>
      <label htmlFor={id}>
        {label}
        <input
          id={id}
          type='text'
          value={value}
          onChange={onChange}
        />
      </label>
    </>
  )
}