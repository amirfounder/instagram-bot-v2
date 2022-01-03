import React from 'react';
import { useTabsContext } from '../../context/TabsProvider';
import styles from './Tabs.module.scss'

export const Tab = (props) => {
  const { currentTabId, setCurrentTabId } = useTabsContext()
  const { children, id } = props;

  const handleClick = () => { setCurrentTabId(id); }
  const show = currentTabId === id;

  return (
    <div
      id={id}
      className={`
        ${styles.tab}
        ${show ? styles.selected : ''}
      `}
      onClick={handleClick}
      hidden={!show}
    >
      {children}
    </div>
  )
}