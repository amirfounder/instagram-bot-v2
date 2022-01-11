import React from 'react';
import styles from './InputsContainer.module.scss'

export const InputsContainer = (props) => {
  const { children } = props;
  return (
    <div className={styles.main}>
      {children}
    </div>
  )
}