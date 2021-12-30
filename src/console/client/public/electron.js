const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    useContentSize: true
  })
  win.loadURL('http://localhost:3000')
}

app.on('ready', () => {
  createWindow()
})

app.on('render-process-gone', () => {
  app.quit()
})

app.on('child-process-gone', () => {
  app.quit()
})