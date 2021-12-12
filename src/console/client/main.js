const { app, BrowserWindow } = require('electron');
const path = require('path')

const CreateWindow = () => {
  window = new BrowserWindow({
    width: 800,
    height: 600,
    webPreference: {
      preload: path.join(__dirname, 'preload.js')
    }
  })
  window.loadFile('index.html')
}