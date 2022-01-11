import { createTask } from "../../../../../sockets/taskController";
import constants from "../../../../../utils/constants";

const {
  STATUSES: {
    QUEUED
  }
} = constants

export const handleSeedHashtagInputChangeService = (value, setValue) => {
  let newValue = value;
  
  if (newValue !== '') {
    newValue = newValue.startsWith('#') ? newValue : '#' + newValue;
    newValue = newValue.toLowerCase();
    newValue = newValue.trim();
  }

  setValue(newValue)
}

export const handleBotAccountInputChangeService = (value, setValue) => {
  let newValue = value;
  
  if (newValue !== '') {
    newValue = newValue.startsWith('@') ? newValue : '@' + newValue;
    newValue = newValue.toLowerCase();
    newValue = newValue.trim();
  }

  setValue(newValue)
}

export const handleQueueTaskService = (seedHashtag, botAccount) => {
  const taskObject = {
    name: 'Scrape Hashtags',
    seed: seedHashtag,
    bot: botAccount,
    status: QUEUED
  }

  createTask(taskObject)
}
