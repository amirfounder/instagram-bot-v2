import React from 'react';
import styles from './InstagramAgentView.module.scss'
import { ScrapeHashtagsCard, ScrapeUsersCard } from './cards';
import { QueuedTasksTableContent, QueuedTasksTableHeader } from './QueuedTasksTable';
import { Card } from '../..';
import { QueuedTasksActions } from './QueuedTasksActions/QueuedTasksActions';

export const InstagramAgentView = () => {
  return (
    <div className={styles.main}>
      <div>
        <div className={styles.tasks}>
          <ScrapeHashtagsCard />
          <ScrapeUsersCard />
        </div>
      </div>
      <div className={styles.queuedTasks}>
        <QueuedTasksActions />
        <Card>
          <QueuedTasksTableHeader />
          <QueuedTasksTableContent />
        </Card>
      </div>
    </div>
  )
}