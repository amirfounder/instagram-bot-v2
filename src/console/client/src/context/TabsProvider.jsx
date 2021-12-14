import React, { createContext, useContext, useState } from 'react';

const TabsContext = createContext();

export const TabsProvider = (props) => {
  const { children } = props;

  const [currentTabId, setCurrentTabId] = useState(1);

  const value = {
    currentTabId, setCurrentTabId
  }

  return (
    <TabsContext.Provider value={value}>
      {children}
    </TabsContext.Provider>
  )
}

export const useTabsContext = () => {
  const context = useContext(TabsContext)
  if (context === undefined) {
    throw new Error("Cannot call useTabsContext outside of TabsProvider")
  }
  return context;
}