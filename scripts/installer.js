const electronInstaller = require('electron-winstaller');

try {
  electronInstaller.createWindowsInstaller({
    appDirectory: './tmp/build/File Organizer-win32-x64/',
    outputDirectory: './tmp/installer',
    authors: 'Oliwier Gesla',
    exe: 'fileorganizer.exe',
    loadingGif: './assets/img/installing.gif',
    noMsi: true,
    setupExe: 'FileOrganizerSetup.exe',
    setupIcon: './assets/icons/win/icon.ico',
    iconUrl: 'https://raw.githubusercontent.com/OliwierGesla/FileOrganizer/master/assets/icons/win/icon.ico',
  });
  console.log('It worked!');
} catch (e) {
  console.log(`No dice: ${e.message}`);
}
