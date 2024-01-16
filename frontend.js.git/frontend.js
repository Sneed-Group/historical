//Created by Samuel Lord (NodeMixaholic/Sparksammy)
//Licensed under MIT with <3

//Just like readTextFile("path/to/file.txt"); except based off of the WWW and needs a full URL. Also: requires JQuery
var litext;
var itext = "";
function returner(valueToReturn) {
  return valueToReturn;
}

function readInternetText(url) {
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    src = request.responseText;
    itext += src;
    setTimeout("return itext", 13);
  }

  request.open("GET", url, true);

  request.send();
}


var urlParams = new URLSearchParams(window.location.search); // Added, just in case someone wants to do something to the urlparams


//Example: readTextFile("path/to/file.txt");
function readTextFile(file) {
    file = file.toString();
    var file2read = new File([""], file);
    var reader = new FileReader();
    var lastReadOutput = reader.readAsText(file2read, "UTF-8");
    return lastReadOutput;
  }
var varifyOutput = "";
function varify(value) {
  varifyOutput = value;
}

//Example: readDataFile("path/to/file.txt");
function readDataFile(file) {
    file = file.toString();
    var file2read = new File([""], file);
    var reader = new FileReader();
    var lastReadOutput = reader.readAsDataURL(file2read);
    return lastReadOutput;
}

function writeToBody(html) {
    document.append(html.toString())
}

function overwriteBody(html) {
    document.body.innerHTML = html.toString()
}

function randomPOS(elementID) {
  var top=Math.floor(Math.random() * Math.floor(90));             
  var left=Math.floor(Math.random() * Math.floor(90));                    
  document.getElementById(elementID.toString).style.top=top+"%";                   
  document.getElementById(elementID.toString).style.left=left+"%"
}

function pos(elementID,x,y) {
  var top=y;             
  var left=x;                    
  document.getElementById(elementID.toString).style.top=top+"%";                   
  document.getElementById(elementID.toString).style.left=left+"%"
}

// Selects a random value in a array
// Example: randomSelectArray(Array); (Change the array!)
function randomSelectArray(avar){ 
  var isarray = Array.isArray(avar)
  if (isarray == true) {
    var rnfa = Math.floor(Math.random()*avar.length);
    var rrfa = avar[rnfa]
    return rrfa;
  } else if (isarray == false){
    console.log(`Error, ${avar} is not a Array...`);
  }
}


function sleep(ms) {
  setTimeout(function () {}, ms)
}

async function asyncSleep(ms) {
  await new Promise(r => setTimeout(r, ms));
}

// Remade by Sparksammy
// Example: isFunction(el)
function isFunction(item) {
  if (typeof item === 'function') {
    return true;
  } else {
    return false;
  }
}

function applyCSS(elemID, prop, value) {
    let e = document.getElementById(elemID)
    e.style[prop] = value
}

function createParagraph(elementID) {
    let e = document.createElement("p")
    e.setAttribute("id", elementID)
    document.body.appendChild(e)
}

function createHeader(num, elementID) {
    let e = document.createElement(`h${num}`)
    e.setAttribute("id", elementID)
    document.body.appendChild(e)
}

function createElement(tagName, elementID) {
    let e = document.createElement(tagName)
    e.setAttribute("id", elementID)
    document.body.appendChild(e)
}

function alignSelf(elemID, alignDirection) {
    let e = document.getElementById(elemID)
    e.style.alignSelf = alignDirection
}

function alignContent(elemID, alignDirection) {
    let e = document.getElementById(elemID)
    e.style.alignContent = alignDirection
}

function alignAll(elemID, alignDirection) {
    alignSelf(elemID, alignDirection)
    alignContent(elemID, alignDirection)
}

function writeTimeAndDate(elemID, hourFormat) {
    let e = document.getElementById(elemID)
    let d = new Date()
    let locale = "en-GB"
    if (hourFormat == 24) {
        locale = locale //leave it the same.
    } else {
        locale = "en-US"
    } 
    let tdStr = d.toLocaleString(locale)
    e.innerText = tdStr 
}

function writeText(elemID, str) {
    let e = document.getElementById(elemID)
    e.innerText = String(str) 
}

function writeHTML(elemID, str) {
    let e = document.getElementById(elemID)
    e.innerHTML = String(str) 
}

function clearPage() {
    document.body.innerHTML = ""
}

function createList(listID, jsArray) {
    let listParent = document.createElement("ul")
    listParent.setAttribute("id", listID)
    document.body.appendChild(listParent)
    jsArray.forEach(item => {
        listParent.innerHTML = listParent.innerHTML + `<li>${item}</li>`
    })
}

function addToList(listID, jsArray) {
    let listParent = document.getElementById(listID)
    jsArray.forEach(item => {
        listParent.innerHTML = listParent.innerHTML + `<li>${item}</li>`
    })
}


// Gets the value of a attribute
// Example: getAttribute(document.getElementById("link"), "href");
function getAttribute(el, att) {
  var result = el.getAttribute(att);
  return result;
}

// Show/Hide Elements
// Example: hideShow(el)
function hideShow(el) {
  if (el.style.display == 'none') {
    el.style.display = '';
  } else{
    el.style.display = 'none';
  }
}

// Example: fadeOut(el, 1000)
function fadeOut(el, ms) {
  elem = getElementById(el)
  ms = parseInt(ms);
  for (i = 0; i < (ms + 1); i++) {
    elem.style.opacity = elem.style.opacity - (i / 100);
    sleep(1)
  }
}

// Example: fadeIn(el, 1000);
function fadeIn(el, ms) {
  elem = getElementById(el)
  elem.style.opacity = 0;
  ms = parseInt(ms);
  for (i = 0; i < (ms + 1); i++) {
    elem.style.opacity = elem.style.opacity + (i / 100);
    sleep(1)
  }
}
function spin(el, ms){
  elem = getElementById(el)
  for (i = 0; i < (ms / 360); i++) {
    elem.style.transform = 'rotate(' + i + 'deg)';
  }
}


//Eval alternative
//Example: exec("alert('Hello, world!')")
function exec(jsCode) {
  js = jsCode.toString()
  setTimeout( js, 1);
}

function requir3(jsFile) {
  var req = readInternetText();
  exec(readInternetText);
}

// Example: getFileSize(path/to/file)
function getFileSize(file) {
  file = file.toString();
  var file = new File([""], file);
  return file.getFileSize;
}

function lastModified(file) {
  file = file.toString();
  var file = new File([""], file);
  return file.lastModified;
}

// Example: playAudio("https://interactive-examples.mdn.mozilla.net/media/examples/t-rex-roar.mp3", 0.4)
function playAudio(audio, speed) {
  var ma = new Audio(audio);
  ma.playbackRate = speed;
  ma.play()
}

// Example: redir(url);
function redir(url) {
  window.location.href = url.toString();
}


