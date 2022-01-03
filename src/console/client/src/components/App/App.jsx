import React from 'react';
import { Tab, TabPanel, Tabs } from '..';
import { HomeView, DataView } from '../views';
import { InstagramAgentView } from '../views/InstagramAgentView/InstagramAgentView';
import { ProcessesView } from '../views/ProcessesView/ProcessesView';
import styles from './App.module.scss';

export const App = () => {
  return(
    <div className={styles.app}>
      <Tabs>
        <Tab id='1'>Home</Tab>
        <Tab id='2'>Data</Tab>
        <Tab id='3'>Processes</Tab>
        <Tab id='4'>Intagram Agent</Tab>
      </Tabs>
      <TabPanel id='1' component={HomeView} />
      <TabPanel id='2' component={DataView} />
      <TabPanel id='3' component={ProcessesView} />
      <TabPanel id='4' component={InstagramAgentView} />
    </div>
  )
}