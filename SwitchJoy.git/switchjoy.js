
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
  function sleepEvent() {
    print("Sleeping...")
  }
  setTimeout(sleepEvent, ms)
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

// Removes all Elements from the page! (Please be careful when using this function!)
// Example: clearHTML()
function clearHTML(){ 
  document.body.innerHTML = "";
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

// Recoded by Sparksammy. (Oklomsy's version doesn't really work but he tried...)
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

// Rewritten by Sparksammy (Oklomsy's version works but sparksammy's version was better)
// Example: redir(url);
function redir(url) {
  window.location.href = url.toString();
}
