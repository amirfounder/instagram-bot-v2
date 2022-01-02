import React from 'react';
import styles from './TextInput.module.scss'

export const TextInput = (props) => {
  const {
    label,
    id,
    onChange,
    value,
    error,
    onKeyDown,
    placeholder
  } = props;

  return (
    <label
      data-testid='text-label'
      className={styles.label}
      htmlFor={id}
    >
      <div
        className={styles.labelText}
      >
        {label}
      </div>
      <input
        data-testid='text-input'
        type="text"
        className={styles.input}
        id={id}
        value={value}
        onChange={onChange}
        onKeyDown={onKeyDown}
        placeholder={placeholder}
      />
      <p className={styles.error}>{error}</p>
    </label>
  )
}