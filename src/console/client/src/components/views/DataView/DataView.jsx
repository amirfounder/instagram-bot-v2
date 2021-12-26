import React from 'react';
import socket from '../../../utils/sockets';


export const DataView = () => {
  return (
    <div>
      Data Manager
      <button onClick={() => socket.send('hello')}>
        Ping server
      </button>
    </div>
  )
}