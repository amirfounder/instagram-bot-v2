import React, { createContext, useContext, useReducer, useState } from 'react';

const AppContext = createContext();

export const TabsProvider = (props) => {
  const { children } = props;

  const initialState = {}
  const reducer = () => {
    
  }

  const [state, dispatch] = useReducer(reducer, initialState)

  const value = {
    state, dispatch
  }

  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  )
}

export const useAppContext = () => {
  const context = useContext(AppContext)
  if (context === undefined) {
    throw new Error("Cannot call useAppContext outside of TabsProvider")
  }
  return context;
}