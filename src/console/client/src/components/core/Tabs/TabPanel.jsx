import React from 'react';
import { useTabsContext } from '../../context/TabsProvider';
import styles from './Tabs.module.scss'

export const TabPanel = (props) => {
  const { currentTabId } = useTabsContext()
  const {
    children,
    component,
    id
  } = props;

  const show = currentTabId === id;

  return (
    <div
      id={id}
      hidden={!show}
      className={styles.tabPanel}
    >
      {component ? component() : children}
    </div>
  )
}