import React, { useState } from 'react';
import {
  Button,
  Heading,
  InputsContainer,
  TextInput,
  Card
} from '../../../..';
import {
  handleBotAccountInputChangeService,
  handleSeedHashtagInputChangeService,
  handleQueueTaskService
} from './ScrapeHashtagsCardService';

export const ScrapeHashtagsCard = () => {
  
  const [seedHashtag, setSeedHashtag] = useState('')
  const [botAccount, setBotAccount] = useState('')
  const handleSeedHashtagInputChange = (e) => { handleSeedHashtagInputChangeService(e.target.value, setSeedHashtag) }
  const handleBotAccountInputChange = (e) => { handleBotAccountInputChangeService(e.target.value, setBotAccount) }
  const handleQueueTaskClick = () => { handleQueueTaskService(seedHashtag, botAccount) }

  return (
    <Card>
      <Heading level='3'>Scrape Hashtag Data</Heading>
      <InputsContainer>
        <TextInput
          label='Seed:'
          value={seedHashtag}
          placeholder='#nutrition_niche'
          onChange={handleSeedHashtagInputChange}
          id='scrapeHashtags_seedHashtagValue'
        />
        <TextInput
          label='Bot:'
          value={botAccount}
          placeholder='@nutrition_bot'
          onChange={handleBotAccountInputChange}
          id='scrapeHashtags_botAccountValue'
        />
      </InputsContainer>
      <Button
        label='Queue Task'
        onClick={handleQueueTaskClick}
      />
    </Card>
  )
}