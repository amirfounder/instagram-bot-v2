import React from 'react';
import styles from './Card.module.scss';

export const Card = (props) => {
  const {
    children,
    padding,
    margin
  } = props;

  return (
    <div
      className={styles.main}
      style={{
        padding,
        margin
      }}
    >
      {children}
    </div>
  )
}