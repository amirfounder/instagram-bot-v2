import React from 'react';
import ReactDOM from 'react-dom';
import './index.scss';
import { App } from './components'
import { TabsProvider } from './components/context/TabsProvider';


ReactDOM.render(
  <React.StrictMode>
    <TabsProvider>
      <App />
    </TabsProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
