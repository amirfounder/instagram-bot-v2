import React from 'react';
import styles from './QueuedTasksTable.module.scss'

export const QueuedTasksTableContent = (props) => {
  const { tasks } = props;

  return (
    <div className={styles.content}>
      {Array.isArray(tasks) ? tasks.map((task) => (
        <tr>
          <td>{task?.id}</td>
          <td>{task?.name}</td>
          <td>{task?.args}</td>
          <td>{task?.status}</td>
        </tr>
      )) : (
        <p>No tasks to show...</p>
      )}
    </div>
  )
}