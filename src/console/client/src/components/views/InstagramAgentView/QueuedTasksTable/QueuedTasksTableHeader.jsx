import React from 'react';
import styles from './QueuedTasksTable.module.scss'

export const QueuedTasksTableHeader = () => {
  return (
    <th className={styles.header}>
      <td>ID</td>
      <td>Name</td>
      <td>Args</td>
      <td>Status</td>
    </th>
  )
}