import React from "react";
import styles from './Button.module.scss'


export const Button = (props) => {
  const {
    children,
    onClick,
    label,
    ...other
  } = props;

  return (
    <button
      className={styles.main}
      onClick={onClick}
      {...other}
    >
      {children || label}
    </button>
  )
}