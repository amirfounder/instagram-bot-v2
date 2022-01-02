import React, { useState } from 'react';
import styles from './InstagramAgentView.module.scss'
import { Button, Heading, TextInput } from '../..';
import { startInstagramAgent } from './InstagramAgentViewService';

export const InstagramAgentView = () => {

  const [seedHashtag, setSeedHashtag] = useState('');
  const handleSeedHashtagChange = (e) => {
    let newValue;
    newValue = e.target.value;
    
    if (newValue === '') {
      setSeedHashtag(newValue);
      return;
    }

    newValue = newValue.startsWith('#') ? newValue : '#' + newValue;
    newValue = newValue.toLowerCase();
    newValue = newValue.trim();

    setSeedHashtag(newValue)
  }
  const handleStartAgentClick = () => { startInstagramAgent(seedHashtag) }

  return (
    <div className={styles.main}>
      <div>
        <Heading>Launch New Task</Heading>
        <div className={styles.taskContainer}>
          <TextInput
            label='Enter seed hashtag:'
            value={seedHashtag}
            onChange={handleSeedHashtagChange}
            id='seedHashtag'
          />
        </div>
        <Button
          label='Queue Task'
          onClick={handleStartAgentClick}
        />
      </div>
      <div>
      </div>
    </div>
  )
}