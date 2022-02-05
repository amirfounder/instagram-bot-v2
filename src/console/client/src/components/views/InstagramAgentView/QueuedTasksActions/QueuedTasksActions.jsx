import React from 'react';
import { Button, Heading } from '../../..';
import styles from './QueuedTasksActions.module.scss'
import { startAgentService } from './QueuedTasksActionsService';

export const QueuedTasksActions = () => {
  return (
    <div className={styles.main}>
      <div>
        <Heading
          level='4'
          ignoreMargin
        >
          Let's do something fun!
        </Heading>
      </div>
      <div>
        <Button
          label='Start Agent'
          onClick={startAgentService}
        />
      </div>
    </div>
  )
}