let {PythonShell} = require('python-shell')
const settings = require('electron-settings')
var path = require("path")
const $ = require('jquery')
const {remote} = require('electron')

//Home Page

//Load Pages into index.html
$(function(){
  $("#settings").load("./assets/settings.html");
  $("#success").load("./assets/success.html");
  $("#error").load("./assets/error.html");
});

//Main Organizer Function
function organize() {

  //Options and arguments for script
  var options = {

    //Un-Comment the line below to package python in the app
    //This is so people without python installed can still run the software
    //pythonPath: path.join(__dirname, './fileorganizer/python-3.7.4/python.exe'),

    scriptPath : path.join(__dirname, './fileorganizer/'),
    args : [settings.get('directory'),
      settings.get('overwrite_existing_directories'),
      settings.get('capitalize_first_letter'),
      settings.get('create_subdirectories')
    ]
  }

  //Run Python Script
  PythonShell.run('fileorganizer.py', options, function (err, results) {
  if (err) {
    console.log(err)
    document.getElementById('home').removeAttribute('class', 'is-open')
    document.getElementById('error').setAttribute('class', 'is-open')
  }
  else {
    document.getElementById('home').removeAttribute('class', 'is-open')
    document.getElementById('success').setAttribute('class', 'is-open')
  }
  });
}



// Directory Picker
function pick_directory() {
  document.getElementById('picker-button').click()
}

// Update the Directory input box
function update_directory() {
  dir = document.getElementById("picker-button").files[0].path
  document.getElementById("directory").value = dir;
  save_directory()
}

function save_directory() {
  settings.set('directory', document.getElementById("directory").value)
}

// Buttons
function back_to_home() {
  document.getElementById('home').setAttribute('class', 'is-open')
  document.getElementById('error').removeAttribute('class', 'is-open')
  document.getElementById('success').removeAttribute('class', 'is-open')
  document.getElementById('settings').removeAttribute('class', 'is-open')
}
function options() {
  document.getElementById('settings').setAttribute('class', 'is-open')
  document.getElementById('home').removeAttribute('class', 'is-open')
}

var win = remote.getCurrentWindow();
