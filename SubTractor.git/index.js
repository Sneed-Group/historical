//Made by Sparksammy. Inspired by Oklomsy.
const express = require('express')
fs = require('fs');
const https = require('https');
const Discord = require('discord.js');
var request = require('request');
const app = express()
const port = 3000
var count = 0;
const client = new Discord.Client();

fs.readFile('count', 'utf8', function (err,data) {
    if (err) {
        return console.log(err);
    }
    count = Number(data)
});

app.get('/', (req, res) => {
    fs.readFile('count', 'utf8', function (err,data) {
        if (err) {
            return console.log(err);
        }
        count = Number(data)
    });  
    res.send(`<h1>SubTractor</h1><hr><p>Count: ${count}</p>`)
})

app.get('/add', function(req, res) {
    count++;
    fs.writeFile('count', count.toString(), function (err) {
        if (err) return console.log(err);
        console.log(`${count} written to count`)
    });
    res.send('OK')
});

app.get('/subtract', function(req, res) {
    count = count - 1;
    fs.writeFile('count', count.toString(), function (err) {
        if (err) return console.log(err);
        console.log(`${count} written to count`)
    });
    res.send('OK')
});

app.get('/squared', function(req, res) {
    count = count * count;
    fs.writeFile('count', count.toString(), function (err) {
        if (err) return console.log(err);
        console.log(`${count} written to count`)
    });
    res.send('OK')
});

app.get('/double', function(req, res) {
    count = count * 2;
    fs.writeFile('count', count.toString(), function (err) {
        if (err) return console.log(err);
        console.log(`${count} written to count`)
    });
    res.send('OK')
});

app.get('/half', function(req, res) {
    count = count / 2;
    fs.writeFile('count', count.toString(), function (err) {
        if (err) return console.log(err);
        console.log(`${count} written to count`)
    });
    res.send('OK')
});

app.get('/reset', function(req, res) {
    count = count * 0;
    fs.writeFile('count', count.toString(), function (err) {
        if (err) return console.log(err);
        console.log(`${count} written to count`)
    });
    res.send('OK')
});

client.once('ready', () => {
	console.log('Ready!');
});

client.on('message', message => {
    request.get(`http://localhost:${port}/${message.content}`,{json: false},function(err,res,body){
        if(err) {
            console.log(err.toString());
            message.channel.send(`Error doing operation. Maybe a 404?`)
        }
        if (res.statusCode === 200 ) {
            console.log(`Did operation ${message.content}`)
            message.channel.send(`Did operation OK. New value: ${count}.`)
        }
    });
});

app.listen(port, () => {
    console.log(`SubTractor app listening at http://localhost:${port}`);
    fs.readFile('token', 'utf8', function (err,data) {
        if (err) {
            return console.log(err);
        }
        client.login(data);
    });
})