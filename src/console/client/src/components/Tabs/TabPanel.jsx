import React from 'react';
import { useTabsContext } from '../../context/TabsProvider';

export const TabPanel = (props) => {
  const { currentTabId } = useTabsContext()
  const { children, id } = props;

  const show = currentTabId == id;

  return (
    <div
      id={id}
      hidden={!show}
    >
      {children}
    </div>
  )
}