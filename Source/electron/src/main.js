const { updateElectronApp } = require('update-electron-app');
const { app, BrowserWindow, shell } = require('electron');
const path = require('path');

const Store = require('./store.js');
const log = require('electron-log')
log.initialize()
// First instantiate the class
const store = new Store({
  // We'll call our data file 'user-preferences'
  configName: 'user-preferences',
  defaults: {
    // 800x600 is the default size of our window
    windowBounds: { width: 800, height: 600 },
    fullscreen: false,
  }
});

// First we'll get our height and width. This will be the defaults if there wasn't anything saved
let { width, height } = store.get('windowBounds');


// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require('electron-squirrel-startup')) {
  app.quit();
}
const port = 41408

const { spawn, spawnSync } = require('node:child_process');
const startDjangoServer = () => {

  const fs = require("fs")
  let db_path = path.join(process.env.LOCALAPPDATA, app.getName(), "db.sqlite3")
  if (!fs.existsSync(db_path)) {
    let migrate = spawnSync(path.join(process.resourcesPath, 'manage.exe'), ['migrate'])
    log.info("migrate:stdout: " + migrate.stdout)
    log.info("migrate:stderr: " + migrate.stderr)
  }

  const djangoBackend = spawn(path.join(process.resourcesPath, 'manage.exe'), ['runserver', '0.0.0.0:' + port, '--noreload']);

  app.on('before-quit', function () {
    djangoBackend.kill();
  });

  return djangoBackend;
}

const createWindow = () => {

  const splashWindow = new BrowserWindow({
    show: false,
    width: 300,
    height: 300,
    center: true,
    frame: false,
    hasShadow: true,
  });

  splashWindow.loadFile(path.join(__dirname, 'splash.html'));
  splashWindow.once('ready-to-show', function () {
    splashWindow.show();
    updateElectronApp();
    startDjangoServer();
  });

  // Create the browser window.
  const mainWindow = new BrowserWindow({
    show: false,
    center: true,
    autoHideMenuBar: true,
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
    },
    fullscreen: store.get("fullscreen"),
  });

  // The BrowserWindow class extends the node.js core EventEmitter class, so we use that API
  // to listen to events on the BrowserWindow. The resize event is emitted when the window size changes.
  mainWindow.on('resize', () => {
    // The event doesn't pass us the window size, so we call the `getBounds` method which returns an object with
    // the height, width, and x and y coordinates.
    let { width, height } = mainWindow.getBounds();
    // Now that we have them, save them using the `set` method.
    store.set('windowBounds', { width, height });
    store.set('fullscreen', mainWindow.isFullScreen())
  });

  const http = require('node:http')

  const options = {
    host: '127.0.0.1',
    port: port,
    path: '/',
    method: 'GET'
  };

  function check() {
    http.get(options, function (response) {
      // console.log('statusCode:', response.statusCode);
      // console.log('headers:', response.headers);

      mainWindow.loadURL('http://127.0.0.1:' + port);
      mainWindow.once('ready-to-show', function () {
        splashWindow.close();
        mainWindow.show();
        shell.openExternal('https://ilkadam.com.tr')
      });
      // Open the DevTools.
      // mainWindow.webContents.openDevTools();

    }).on('error', function (error) {
      // console.log('check_error:', error);
      setTimeout(check, 1000);
    });
  };

  check();

  // and load the index.html of the app.
  //mainWindow.loadFile(path.join(__dirname, 'index.html'));

  // Open the DevTools.
  //mainWindow.webContents.openDevTools();
};

app.commandLine.appendSwitch('ignore-certificate-errors')

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', () => {
  createWindow();
});

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.
