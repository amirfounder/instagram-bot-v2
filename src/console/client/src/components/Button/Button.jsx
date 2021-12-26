import React from "react";

export const Button = (props) => {
  const {
    children,
    onClick,
    label,
    ...other
  } = props;

  return (
    <button
      onClick={onClick}
      {...other}
    >
      {children || label}
    </button>
  )
}