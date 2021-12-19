import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { App } from './components'
import { TabsProvider } from './context/TabsProvider';

ReactDOM.render(
  <React.StrictMode>
    <TabsProvider>
      <App />
    </TabsProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
