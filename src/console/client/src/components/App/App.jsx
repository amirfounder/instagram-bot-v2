import React from 'react';
import { Tab, TabPanel, Tabs } from '..';
import { DataView } from '../views/DataView/DataView';
import { InstagramAgentView } from '../views/InstagramAgentView/InstagramAgentView';
import { ProcessesView } from '../views/ProcessesView/ProcessesView';
import styles from './App.module.scss';

export const App = () => {
  return(
    <div className={styles.app}>
      <Tabs>
        <Tab id='1'>Data</Tab>
        <Tab id='2'>Processes</Tab>
        <Tab id='3'>Intagram Agent</Tab>
      </Tabs>
      <TabPanel id='1' component={DataView} />
      <TabPanel id='2' component={ProcessesView} />
      <TabPanel id='3' component={InstagramAgentView} />
    </div>
  )
}