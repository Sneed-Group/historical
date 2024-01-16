const crypto = require('crypto');
const ed25519 = require('ed25519');
const { SHA3 } = require('sha3');

let addr = process.argv[2]

function createMoneroWallet(addressToMatch) {
  const privateKey = crypto.randomBytes(32);
  const publicKey = ed25519.MakeKeypair(privateKey).publicKey;
  const address = getMoneroAddress(publicKey);

  if (address === addressToMatch) {
    return `
      privateKey: ${privateKey.toString('hex')},
      publicKey: ${publicKey.toString('hex')},
      address: ${address}
    `;
    process.exit()
  } else {
    return `Not found yet, retrying... (currently on: ${privateKey.toString('hex')})`;
  }
}



function getMoneroAddress(publicKey) {
  const hexPublicKey = publicKey.toString('hex');
  const hash = new SHA3(256).update(hexPublicKey, 'hex').digest();
  const address = hash.subarray(0, 8).toString('hex');
  return address;
}

async function main(addr) {
  const delay = ms => new Promise(res => setTimeout(res, ms));
  while(true) {
    await console.log(`${createMoneroWallet(addr)}`);
    await delay(1);
  }
}

main(addr)
