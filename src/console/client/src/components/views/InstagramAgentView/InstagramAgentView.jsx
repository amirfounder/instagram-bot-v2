import React, { useState } from 'react';
import styles from './InstagramAgentView.module.scss'
import { Button, Heading, TextInput } from '../..';
import {
  startInstagramAgent,
  handleSeedHashtagChangeService
} from './InstagramAgentViewService';
import { Inputs } from '../../core/inputs/Inputs/Inputs';

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
            <Inputs>
              <TextInput
                label='Seed:'
                value={seedHashtag}
                // value={state.researchHashtags.seed}
                placeholder='#nutrition'
                onChange={handleSeedHashtagChange}
                id='research_hashtags_seed'
              />
              <TextInput
                label='Account:'
                // value={state.researchHashtags.account}
                placeholder='@researchaccount1'
                id='research_hashtags_account'
              />
            </Inputs>
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