const { app, BrowserWindow } = require('electron');
const path = require('path')

const createWindow = () => {
  window = new BrowserWindow({
    width: 1040,
    height: 720,
  })
  window.loadFile('index.html')
}

app.whenReady().then(() => { createWindow() })