import React, { useState } from 'react';
import { Button, Input } from '../..';
import { startInstagramAgent } from './InstagramAgentViewService';

export const InstagramAgentView = () => {

  const [rootHashtagValue, setRootHashtagValue] = useState('');

  const handleRootHashtagValueChange = (e) => {
    setRootHashtagValue(e.target.value)
  }

  const handleStartAgentClick = () => { startInstagramAgent(rootHashtagValue) }

  return (
    <div>
      <Input
        label='Enter a root hashtag to start the instagram agent...'
        value={rootHashtagValue}
        onChange={handleRootHashtagValueChange}
        id='rootHashtagValue'
      />
      <Button
        label='Start Agent'
        onClick={handleStartAgentClick}
      />
    </div>
  )
}