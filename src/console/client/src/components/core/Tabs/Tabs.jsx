import React from 'react'
import styles from './Tabs.module.scss'

export const Tabs = (props) => {
  const { children} = props;

  return (
    <div
      className={styles.tabs}
    >
      {children}
    </div>
  )
}
