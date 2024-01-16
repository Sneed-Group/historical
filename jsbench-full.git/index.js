// JS BENCH FULL 1.0
// By Samuel Lord
// LICENSED UNDER MIT LICENSE
async function jsBench(func) {
  let preform = performance.now()
  await func()
  preform = performance.now()
  return `Score: ${preform/1000} seconds`
}

async function cool() {
	let jscool = true
	while (jscool) {
		let guess = await Math.random() * 1000
		console.log(`Guessing: ${guess}`)
		if (guess < 666 && guess > 409.90635000098587) {
			console.log(`${guess} was the correct number!`)
			jscool = false
		} else {
		console.log('Wrong guess! Retrying...')
		}
		await new Promise(r => setTimeout(r, 3));
	}
}

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

// Create a Fibonacci sequence calculation function for a given length
async function fib(n) {
  if (n < 2) {
    return n;
  }
  return await fib(n - 1) + await fib(n - 2);
}


async function bench() {
  for (let i = 0; i < 6; i++) {
    for (let i = 0; i < 255; i++) {
      await cool()
    } 

    for (let i = 0; i < 100; i++) {
      let f = await fib(1000)
      console.log(f)
    } 
  
    for (let i = 0; i < 400; i++) {
      await createAndFind()
    } 
    for (let i = 0; i < 200; i++) {
      await createAndFindHashes()
    } 
  
    for (let i = 0; i < 300; i++) {
      await createAndMedian()
    } 
  }
}



async function main() {
  let benchmark = await jsBench(bench);
  console.log(benchmark)
}
main()
