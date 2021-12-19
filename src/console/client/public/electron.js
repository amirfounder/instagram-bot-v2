const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    useContentSize: true
  })
  // win.removeMenu()
  win.loadURL('http://localhost:3000')
}

app.whenReady().then(() => {
  createWindow()
})
