# jsBench
Tiny JavaScript benchmark tool

## Example to benchmark: Create array and median
```
function createAndMedian() {
    let array = [];
    for (var i = 0; i < 40000; i++) {
        array[i] = Math.floor(Math.random() * 100);
    }
    var len = array.length;
    var mid = Math.floor(len / 2);
    if (len % 2 === 0) {
        return (array[mid] + array[mid - 1]) / 2;
    } else {
        return array[mid];
    }
}
let cam = await jsBench(createAndMedian);
console.log(cam)
```

## Example to benchmark: Create an array and to find a random value via for loop

```
function createAndFind() {
    let array = [];
    for (var i = 0; i < 40000; i++) {
        array[i] = Math.floor(Math.random() * 100);
    }
    var len = array.length;
    //choose a number between 0 and the length of the array
    var random = Math.floor(Math.random() * len);
    //get the value of random
    var toFind = array[random];
    //for loop to find the value
    for (var i = 0; i < len; i++) {
        if (array[i] === toFind) {
            return i;
        }
    }
}

let caf = await jsBench(createAndFind);
console.log(caf)
```

## Example to benchmark: Create an array of 6900000 hashes, sanely find one. (NodeJS only)
```
let crypto = require('crypto');
function createAndFindHashes() {
//an array of 6900000 random hashes
let hashes = [];
for (let i = 0; i < 6900000; i++) {
    hashes.push(crypto.randomBytes(20).toString('hex'));
}

//get a random hash
let hash = hashes[Math.floor(Math.random() * hashes.length)];

//check if the hash is in the array
let found = hashes.includes(hash)

//if found, print the hash
if (found) {
    console.log(`${hash} was found!`);
}

}

let hashesBig = await jsBench(createAndFindHashes);
console.log(hashesBig)
```

## Same as above, except with 40k hashes and compatible with Vanilla JS

```
function createAndFindHashes() {
//an array of 40000 random hashes
let hashes = [];
for (let i = 0; i < 40000; i++) {
    hashes.push(Number(`${Math.random() * 690000}`).toString(16));
}

//get a random hash
let hash = hashes[Math.floor(Math.random() * hashes.length)];

//check if the hash is in the array
let found = hashes.includes(hash)

//if found, print the hash
if (found) {
    console.log(`${hash} was found!`);
}

}

let hashes = await jsBench(createAndFindHashes);
console.log(hashes)
```
