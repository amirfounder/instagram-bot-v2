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
      <span
        className={styles.labelText}
      >
        {label}
      </span>
      <span>
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
        {error && <p className={styles.error}>{error}</p>}
      </span>
    </label>
  )
}