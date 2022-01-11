import React from 'react';
import styles from './Card.module.scss';

export const Card = (props) => {
  const { children } = props;
  return (
    <div className={styles.main}>
      {children}
    </div>
  )
}