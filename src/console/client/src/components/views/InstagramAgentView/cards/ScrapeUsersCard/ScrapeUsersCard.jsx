import React, { useState } from 'react';
import {
  Button,
  Heading,
  InputsContainer,
  TextInput,
  Card
} from '../../../..';
import {
  handleUsernameChangeService,
} from './ScrapeUsersCardService';

export const ScrapeUsersCard = () => {
  
  const [seedAccount, setSeedAccount] = useState('')
  const [botAccount, setBotAccount] = useState('')
  const handleSeedAccountInputChange = (e) => { handleUsernameChangeService(e.target.value, setSeedAccount) }
  const handleBotAccountInputChange = (e) => { handleUsernameChangeService(e.target.value, setBotAccount) }
  const handleQueueTaskClick = () => {}

  return (
    <Card>
      <Heading level='3'>Scrape Users Data</Heading>
      <InputsContainer>
        <TextInput
          label='Seed:'
          value={seedAccount}
          placeholder='#nutritional_influencer_page'
          onChange={handleSeedAccountInputChange}
          id='scrapeUsers_seedAccountValue'
        />
        <TextInput
          label='Bot:'
          value={botAccount}
          placeholder='@nutrition_niche_bot'
          onChange={handleBotAccountInputChange}
          id='scrapeUsers_botAccountValue'
        />
      </InputsContainer>
      <Button
        label='Queue Task'
        onClick={handleQueueTaskClick}
      />
    </Card>
  )
}