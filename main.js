if(require('electron-squirrel-startup')) return;
const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require('path')
const url = require('url')
const settings = require('electron-settings');


// Set Default user settings
settings.set('directory', null)
settings.set('overwrite_existing_directories', 'false')
settings.set('capitalize_first_letter', 'false')
settings.set('create_subdirectories', 'true')

// Keep a global reference of the window object
let mainWindow

function createWindow () {

  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    center: true,
    show: false,
    minHeight: 600,
    minWidth: 800,
    maxHeight: 600,
    maxWidth: 800,
    resizable: false,
    frame: false,
    icon: path.join(__dirname, '/assets/icons/png/512x512.png'),
  })

  // Graceful window loading
  mainWindow.on('ready-to-show', () => {
    mainWindow.show();
    mainWindow.focus();
  })

  // Load the index.html of the app.
  mainWindow.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))

  // Emitted when the window is closed.
  mainWindow.on('closed', function () {
    // Dereference the window object
    mainWindow = null
  })
}

app.on('ready', createWindow)

// Quit when all windows are closed.
app.on('window-all-closed', function () {
    app.quit()
})

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow()
  }
})
