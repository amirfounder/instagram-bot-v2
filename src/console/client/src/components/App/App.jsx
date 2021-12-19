import React from 'react';
import { Tab, TabPanel, Tabs } from '..';
import { DataManager } from '../views/DataManager/DataManager';
import { InstagramAgentManager } from '../views/InstagramAgentManager/InstagramAgentManager';
import { ProcessManager } from '../views/ProcessManager/ProcessManager';
import styles from './App.module.scss';

export const App = () => {
  return(
    <div className={styles.app}>
      <Tabs>
        <Tab id='1'>Data</Tab>
        <Tab id='2'>Processes</Tab>
        <Tab id='3'>Intagram Agent</Tab>
      </Tabs>
      <TabPanel id='1' component={DataManager} />
      <TabPanel id='2' component={ProcessManager} />
      <TabPanel id='3' component={InstagramAgentManager} />
    </div>
  )
}