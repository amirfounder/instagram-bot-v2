import React, { useState } from 'react';
import styles from './InstagramAgentView.module.scss'
import { Button, Heading, TextInput } from '../..';
import {
  startInstagramAgent,
  handleSeedHashtagChangeService
} from './InstagramAgentViewService';

export const InstagramAgentView = () => {

  const [seedHashtag, setSeedHashtag] = useState('');
  const handleSeedHashtagChange = (e) => { handleSeedHashtagChangeService(e.target.value, setSeedHashtag) }
  const handleSeedUsernameChange = (e) => { handleSeedHashtagChangeService(e.target.value, setSeedHashtag) }

  const handleStartAgentClick = () => { startInstagramAgent(seedHashtag) }

  return (
    <div className={styles.main}>
      <div>
        <Heading>New Task</Heading>
        <div className={styles.tasksContainer}>
          <div className={styles.taskBox}>
            <Heading level='3'>Find Hashtags</Heading>
            <TextInput
              label='Seed:'
              value={seedHashtag}
              placeholder='#nutrition'
              onChange={handleSeedHashtagChange}
              id='seedHashtag'
            />
            <TextInput
              label='Account:'
              value={seedHashtag}
              placeholder='#nutrition'
              onChange={handleSeedHashtagChange}
              id='seedHashtag'
            />
            <Button
              label='Queue Task'
              onClick={handleStartAgentClick}
            />
          </div>
          <div className={styles.taskBox}>
            <Heading level='3'>Find Users</Heading>
            <TextInput
              label='Seed:'
              placeholder='@bodybuilding'
            />
            <Button
              label='Queue Task'
              onClick={handleStartAgentClick}
            />
          </div>
        </div>
      </div>
      <div>
        <Heading>Pending Tasks</Heading>
        <div className={styles.queuedTasksContainer}>

        </div>
      </div>
    </div>
  )
}