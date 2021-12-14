import React, { useState } from 'react';
import { Tab, TabPanel, Tabs } from '..';
import styles from './App.module.scss'

export const App = () => {
  return(
    <div className={styles.app}>
      <Tabs>
        <Tab id='1'>Database Analytics</Tab>
        <Tab id='2'>Process Manager</Tab>
      </Tabs>
      <TabPanel id='1'>Database analytics here</TabPanel>
      <TabPanel id='2'>Processes here</TabPanel>
    </div>
  )
}