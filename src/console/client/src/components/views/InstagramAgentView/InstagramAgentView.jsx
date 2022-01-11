import React from 'react';
import styles from './InstagramAgentView.module.scss'
import { startInstagramAgent } from './InstagramAgentViewService';
import { ScrapeHashtagsCard, ScrapeUsersCard } from './cards';

export const InstagramAgentView = () => {
  return (
    <div className={styles.main}>
      <div>
        <div className={styles.tasks}>
          <ScrapeHashtagsCard />
          <ScrapeUsersCard />
        </div>
      </div>
      <div>
        <div className={styles.queuedTasksContainer}>
          
        </div>
      </div>
    </div>
  )
}