const fs = require('fs')
const gm = require('gm').subClass({ imageMagick: '7+' });
const crypto = require("crypto");

var width;
let args = process.argv.slice(2);
gm(`${args[0]}`)
.blur(1.5,0.1)
.modulate(104.20,130,102.5)
.noProfile()
.size(function (err, size) {
  if (!err)
    width = size.width
})
.resize(width * 2)
.sharpen(1.25,1)
.write(`output-${crypto.randomBytes(16).toString("hex")}.png`, function (err) {
  if (err) console.log(`${err}`); 
})
