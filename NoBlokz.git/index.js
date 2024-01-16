const express = require('express')
var { Readability } = require('@mozilla/readability');
var { JSDOM } = require('jsdom');
const request = require('request');
const helmet = require("helmet");
const fs = require('fs');
const path = require('path');
const { waitForDebugger } = require('inspector');
const app = express()
function helmetPotato() {
    app.use(helmet.hidePoweredBy());
    app.use(helmet.ieNoOpen());
    app.use(helmet.xssFilter());
}
helmetPotato()
const port = 8080 //use this as the external port if you plan on publishing this.
const internalPort = 3000 //use this if you are inside your LAN
const subdomain = "www.sparksammy.com"
const siteName = `http://${subdomain}:${port}`
const proxying = `${siteName}/net?url=`
const proxyResource = `${siteName}/res?url=`
var headHTML = `<head>
<title>Wikipedia</title>
<style>
/* Media Queries: Tablet Landscape */
@media screen and (max-width: 1060px) {
    #primary { width:67%; }
    #secondary { width:30%; margin-left:3%;}  
}

/* Media Queries: Tabled Portrait */
@media screen and (max-width: 768px) {
    #primary { width:100%; }
    #secondary { width:100%; margin:0; border:none; }
}
html { font-size:1rem; }
p {font-size:1rem;}
b {font-size:1.2rem;}
a {font-size:1.23rem;} 
input {font-size:1.23rem;} 
h6 {font-size:1.23rem;}
h5 {font-size:1.35rem;}
h4 {font-size:1.5rem;}
h3 {font-size:1.6rem;}
h2 {font-size:1.8rem;}
h1 {font-size:2rem;}

body { font-family: Arial, Helvetica, sans-serif; }

</style>
</head>`

app.get('/', (req, res) => {
    res.send(`<html>
    ${headHTML}
    <body>
    <h1>Totally Wikipedia</h1><br>
    <form action="/net" style="algin: center;" method="get">
        <input type="text" width="100%" id="url" name="url" value="http://"><br>
        <input type="submit" value="pls work....">
    </form> 
    <hr>
    <p>Copyright Samuel Lord. Licensed under the MIT license.
    <br>Source available on the <a href="https://github.com/sparksammy/NoBlokz" target="_blank">GitHub Repo.</a></p>
    </body>
    </html>`)
})


app.get('/net', (req, res) => {
    const reqf = req;
    const resf = res;
    var baseurl = ""
    
    request(req.query.url, { json: false }, (err, res, body) => {
        if (err) { return console.log(err); }
        //console.log(body)
        try { 
            
            if (req.query.url.startsWith("http://")) {
                baseurl = req.query.url.replace("http://","")
            } else {
                baseurl = req.query.url.replace("https://","")
            }
            
            var arrOfURL = req.query.url.split("/")
            var urlNoDoc = req.query.url
            for (let i = 0; i < arrOfURL.length; i++) {
                if (String(arrOfURL[i]).includes("html")) {
                    arrOfURL.pop(i)
                    urlNoDoc = arrOfURL.join("/")
                    break;
                }
            }

            var olddom = new JSDOM(`${body}`, { url: req.query.url});
            var newbody = body
            var arrOfTags = []
            newbody = newbody.replace(/href="/g, `href="${proxying}${urlNoDoc}/`)
            newbody = newbody.replace(/href='/g, `href='${proxying}${urlNoDoc}/`)
            newbody = newbody.replace(/src="/g, `src="${proxyResource}${urlNoDoc}/`)
            newbody = newbody.replace(/src='/g, `src='${proxyResource}${urlNoDoc}/`)
            newbody = newbody.replace(`href="${urlNoDoc}/http://`, `href="http://`)
            newbody = newbody.replace(`href='${urlNoDoc}/http://`, `href='http://`)
            newbody = newbody.replace(`${urlNoDoc}/http://`, `http://`)
            newbody = newbody.replace(`${urlNoDoc}/https://`, `https://`)            
            newbody = newbody.split(`href="https://www.${baseurl}`).join(`href="${proxying}https://${baseurl}`)
            newbody = newbody.split(`href="http://www.${baseurl}`).join(`href="${proxying}http://${baseurl}`)
            newbody = newbody.split(`href="https://${baseurl}`).join(`href="${proxying}https://${baseurl}`)
            newbody = newbody.split(`href="http://${baseurl}`).join(`href="${proxying}http://${baseurl}`)
            var newdom = new JSDOM(`${newbody}`, { url: req.query.url});
            resf.send(`<html>
            ${headHTML}
            <body>
            <b>Totally Wikipedia</b>
            <form action="/net" align="center" width="100%" method="get">
                <input type="text" width="100%" id="url" name="url" value="http://"><input type="submit" value="pls work...">
            </form>
            <hr>
            
            ${newbody}
        
            </body>
            </html>`)
        } catch (error) {
            console.log(error);
            if (req.query.url.startsWith("http://")) {
                baseurl = req.query.url.replace("http://","")
            } else {
                baseurl = req.query.url.replace("https://","")
            }

            var arrOfURL = req.query.url.split("/")
            var urlNoDoc = req.query.url
            for (let i = 0; i < arrOfURL.length; i++) {
                if (String(arrOfURL[i]).includes("html")) {
                    arrOfURL.pop(i)
                    urlNoDoc = arrOfURL.join("/")
                    break;
                }
            }

            var olddom = new JSDOM(`${body}`, { url: req.query.url});
            var newbody = body
            var arrOfTags = []
            newbody = newbody.replace(/href="/g, `href="${proxyResource}${urlNoDoc}/`)
            newbody = newbody.replace(/href='/g, `href='${proxyResource}${urlNoDoc}/`)
            newbody = newbody.replace(/src="/g, `src="${proxyResource}${urlNoDoc}/`)
            newbody = newbody.replace(/src='/g, `src='${proxyResource}${urlNoDoc}/`)
            newbody = newbody.split(`href="https://www.${baseurl}`).join(`href="${proxying}https://${baseurl}`)
            newbody = newbody.split(`href="http://www.${baseurl}`).join(`href="${proxying}http://${baseurl}`)
            newbody = newbody.split(`href="https://${baseurl}`).join(`href="${proxying}https://${baseurl}`)
            newbody = newbody.split(`href="http://${baseurl}`).join(`href="${proxying}http://${baseurl}`)

            resf.send(`<html>
            ${headHTML}
            <body>
            <b>Totally Wikipedia</b>
            <form action="/net" align="center" width="100%" method="get">
                <input type="text" width="100%" id="url" name="url" value="http://"><input type="submit" value="pls work...">
            </form>
            <hr>
            
            ${newbody}
        
            </body>
            </html>`)
        }

    });
    
})

app.get('/res', (req, res) => {
    const reqf = req;
    const resf = res;
    var basename = path.basename(req.query.url)
    var extname = path.extname(basename)

    var filename = `${String(Math.floor(Math.random() * 420))}${extname}`
    var filepath = path.join(__dirname, "siteresources", filename)
    var sendpath = String(filepath)
    function exterm() {
        fs.unlink(`${filepath}`, function() {
            console.log("Deleted!")
        })
    }
    request(req.query.url, { json: false }, (err, res, body) => {
        if (err) { return console.log(err); }
        try { 
            fs.writeFile(`${filepath}`, body, function (err) {
                if (err) return console.log(err);
                console.log("Sending file...")
                resf.status(200).sendFile(sendpath, (err) => {
                    setTimeout(exterm,15000)
                    console.log("File send timeout reached! Deleting...")
                })
            });
            
        } catch (error) {
            console.log(error)
            resf.status(404).send(`<html>
            ${headHTML}
            <body>
            404...
            </body>
            </html>`)
        }

    });
    
})

app.listen(internalPort, () => {
    console.log(`NoBlokz listening at http://localhost:${internalPort}, external port is ${port}.`)
})
