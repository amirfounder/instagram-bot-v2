import React from 'react';
import styles from './Inputs.module.scss'

export const Inputs = (props) => {
  const { children } = props;
  return (
    <div className={styles.main}>
      {children}
    </div>
  )
}