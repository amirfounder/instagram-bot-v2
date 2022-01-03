import React from 'react';
import { Heading } from '../..';
import styles from './HomeView.module.scss'

export const HomeView = () => {
  return (
    <div className={styles.main}>
      <div>
        <Heading level='3'>Processes overview</Heading>
        <div>
          
        </div>
      </div>
      <div>
        <Heading level='3'>Data overview</Heading>
      </div>
      <div>
        <Heading level='3'>Agents overview</Heading>

      </div>
    </div>
  )
}