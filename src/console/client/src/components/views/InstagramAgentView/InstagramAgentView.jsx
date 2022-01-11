import React from 'react';
import styles from './InstagramAgentView.module.scss'
import { ScrapeHashtagsCard, ScrapeUsersCard } from './cards';
import { QueuedTasksTableContent, QueuedTasksTableHeader } from './QueuedTasksTable';

export const InstagramAgentView = () => {
  return (
    <div className={styles.main}>
      <div>
        <div className={styles.cards}>
          <ScrapeHashtagsCard />
          <ScrapeUsersCard />
        </div>
      </div>
      <div>
        <div className={styles.queuedTasks}>
          <QueuedTasksTableHeader />
          <QueuedTasksTableContent />
        </div>
      </div>
    </div>
  )
}