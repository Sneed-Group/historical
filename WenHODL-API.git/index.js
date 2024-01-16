//WenHODL
//Copyright Samuel Lord. Licensed under the MIT License.
const GUN = require('gun/gun');
const EC = require("elliptic").ec;
let ec = new EC('secp256k1');
//require bitcore
const bitcore = require('bitcore-lib');
//require crypto lib
const crypto = require('crypto');
let gun = GUN(['http://localhost:8765/gun', 'https://gun-manhattan.herokuapp.com/gun']);
let apiport = 42069;
let gunIdWenHODL;
let breakSaveLoop = false;

//DEFINE IF TESTNET OR MAINNET HERE
let isTestnet = true; //set to true for testnet (aka testing), false for mainnet (aka nontesting)

if (isTestnet) {
    gunIdWenHODL = "wenhodl-testing-v2";
} else {
    gunIdWenHODL = "wenhodl-nontesting-v2";
}

let p2pbc = gun.get(gunIdWenHODL).get('blockchain'); //add -nontest to wenhodl for release
let p2pnftc = gun.get(gunIdWenHODL).get('nftchain'); //add -nontest to wenhodl for release
let version = '1.3'; //change the version of wenhodl to the latest version every time you update the code
let codename = 'Introducing New WenHODL! More anonymity, same great spaghetti code! :D'; //change this to the version's codename every time you update the version
let difficulty = 2;
let numberOfUsers = 0;

function sha256(data) {
    //convert string to sha256
    let hash = crypto.createHash('sha256');
    hash.update(data);
    //turn hash into a string
    let hashString = hash.digest('hex');
    return hashString;
}

//deprecated, please use the one in lowercase instead! (this just redirects to the one in lowercase)
function SHA256(data) {
    sha256(data);
}

//create a function to shuffle strings randomly
function shuffle(string) {
    let array = string.split("");
    let currentIndex = array.length, temporaryValue, randomIndex;
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    return array.reverse().join("");
}

function appendArray(oldArray, addArray) {
    return oldArray.concat(addArray);
}

class NFTchain {
    constructor() {
        this.chain = [];
    }
}

class Blockchain {
    constructor() {
        this.chain = [];
        this.pendingTransactions = [];
        this.miningReward = .0000001;
    }
    createNewBlock(nonce, previousBlockHash) {
        const newBlock = {
            index: this.chain.length + 1,
            timestamp: Date.now(),
            transactions: this.pendingTransactions,
            nonce: nonce,
            hash: '',
            previousBlockHash: previousBlockHash
        };
        this.pendingTransactions = [];
        newBlock.hash = this.calculateHash(newBlock);
        this.chain.push(newBlock);
        return newBlock;
    }
    getWallet(address) {
        let deets = gun.get(gunIdWenHODL).get(this.publicKey);
        let wallet = {
            balance: deets[1],
            transactions: deets[2]
        };
        this.chain.forEach(block => {
            block.transactions.forEach(transaction => {
                if (transaction.toAddress === address) {
                    wallet.transactions.push(transaction);
                }
            });
        });
        return wallet;
    }
    getLastBlock() {
        try {
            return this.chain[this.chain.length - 1];
        } catch {
            let firstBlock = this.createNewBlock()
            this.hashBlock(firstBlock)
            return firstBlock;
        }
    }
    createNewTransaction(amount, sender, recipient) {
        const newTransaction = {
            amount: amount,
            sender: sha256(shuffle(sender).toString(16)),
            recipient: recipient
        };
        this.pendingTransactions.push(newTransaction);
        //get sender's wallet
        let senderWallet = this.getWallet(sender);
        //get recipient's wallet
        let recipientWallet = this.getWallet(recipient);
        //subtract amount from sender's wallet
        //check if sender has enough money
        if (senderWallet.balance - amount >= 0) {
            if (this.calculateHash(this.getLastBlock()) !== this.getLastBlock().hash) {
                return false;
            } else if (this.chainIsValid(this.chain) == false) {
                return false;
            } else {
                senderWallet.balance -= amount;
                recipientWallet.balance += amount;
                this.chain.push(this.createNewBlock(this.proofOfWork(this.getLastBlock().hash, this.pendingTransactions), this.getLastBlock().hash));
                this.pendingTransactions = [];
                return this.getLastBlock().index + 1;
            }
        } else {
            this.pendingTransactions = [];
            return false;
        }
    }
    calculateHash(block) {
        return SHA256(JSON.stringify(block));
    }
    hashBlock(previousBlockHash, currentBlockData, nonce) {
        const dataAsString = previousBlockHash + nonce.toString() + JSON.stringify(currentBlockData);
        const hash = SHA256(dataAsString);
        return hash;
    }
    proofOfWork(previousBlockHash, currentBlockData) {
        let hash;
        let nonce = 0;
        if (hash != undefined) {
            while (typeof(hash.substring(0, difficulty) !== Array(difficulty + 1).join("0"))) {
                nonce++;
                hash = this.hashBlock(previousBlockHash, currentBlockData, nonce);
            }
        }
        difficulty++;
        this.miningReward += .0000001;
        return nonce;
    }
    chainIsValid(blockchain) {
        for (let i = 1; i < blockchain.length; i++) {
            const currentBlock = blockchain[i];
            const prevBlock = blockchain[i - 1];
            const blockHash = this.calculateHash(currentBlock);
            if (currentBlock.previousBlockHash !== prevBlock.hash) {
                return false;
            }
            if (currentBlock.hash !== blockHash) {
                return false;
            }
        }
        return true;
    }
}
let bc = new Blockchain();
//create transaction class
class Transaction {
    constructor(amount, sender, recipient) {
        bc.createNewTransaction(amount, sender, recipient);
    }
}

//define ec
//create a wallet class
class Wallet {
    constructor() {
        this.balance = 0;
        this.keyPair = ec.genKeyPair();
        this.publicKey = this.keyPair.getPublic().encode('hex');
        this.address = sha256(this.keyPair.getPublic().toString(16));
        this.privateKey = this.keyPair.getPrivate().toString(16);
    }
    sign(dataHash) {
        return this.keyPair.sign(dataHash);
    }
    setBalance(balance) {
        this.balance = balance;
    }
}
//create a block class
class Block {
    constructor(timestamp, transactions, nonce, previousBlockHash, hash) {
        this.timestamp = timestamp;
        this.transactions = transactions;
        this.nonce = nonce;
        this.previousBlockHash = previousBlockHash;
        this.hash = hash;
    }
}
//create miner class
class Miner {
    constructor(blockchain, transactionPool) {
        this.blockchain = bc || bc.chain;
        this.transactionPool = bc.pendingTransactions;
    }
    mine(address) {
        const lastBlock = this.blockchain.getLastBlock();
        const previousBlockHash = lastBlock;
        const currentBlockData = {
            transactions: this.transactionPool.transactions
        };
        const nonce = this.blockchain.proofOfWork(previousBlockHash, currentBlockData);
        const blockHash = this.blockchain.hashBlock(previousBlockHash, currentBlockData, nonce);
        const newBlock = this.blockchain.createNewBlock(nonce, previousBlockHash);
        new Block(Date.now(), this.transactionPool.transactions, nonce, previousBlockHash, blockHash);
        this.transactionPool = [];
        new Transaction(this.miningReward, '00', address);
        return newBlock;
    }
}


async function donationMiner() {
let donations = await new Wallet()
donations.privateKey = await sha256("N0d3mix*%)(*ah0lic69$!@")
donations.publicKey = await "nodemixaholicDonations"
console.log(`**MINING DONATION STARTED** ${donations.address}`)
while (true) {
    miner.mine(donations.address)
    console.log(`**MINING DONATION SUCCESS** ${donations.address}`)
    await new Promise(r => setTimeout(r, 1000));
}
}

function saveWallet(privateKey, address, wallet) {
    if (wallet.privateKey === privateKey) {
        gun.get(gunIdWenHODL).get(wallet.publicKey).put([address, wallet.balance])
        gun.get(gunIdWenHODL).get(wallet.publicKey).get(address).put(true);
        return savedWallet;
    }
}

function loadWallet(publicKey) {
    //load user's wallet data
    let walletDeets = gun.get(gunIdWenHODL).get(publicKey)
    let wallet = new Wallet();
    wallet.address = walletDeets[0];
    wallet.balance = walletDeets[1];
    return wallet;
}

function loadWalletPrivate(publicKey, privateKey) {
    if (privateKey) {
        let walletDeets = gun.get(gunIdWenHODL).get(publicKey)
        if (walletDeets.get(privateKey) == true) {
            let wallet = new Wallet();
            wallet.address = walletDeets[0];
            wallet.balance = walletDeets[1];
            wallet.privateKey = privateKey;
            return wallet;
        } else { 
            return false;
        }
    } else {
        return false;
    }
}


//comine array function
function combineArray(arr) {
    var r = [];
    for (var i = 0, l = arr.length; i < l; i++) {
        var v = arr[i];
        if (v) {
            r = r.concat(v);
        }
    }
    return r;
}

let nftc = new NFTchain();
let transactionPool = bc.pendingTransactions;
let miner = new Miner(bc, transactionPool);
//create a new blockchain
async function bcLoop() {
    while (true) {
        await new Promise(r => setTimeout(r, 2000));
        bc.oninput = () => { p2pbc.put(bc) };
        nftc.oninput = () => { p2pnftc.put(nftc) };
        p2pnftc.on((newnftc) => { try { if (true) { nftc.chain = combineArray(nftc.chain,newnftc.chain) } } catch (e) {console.log(e);} });
        p2pbc.on((newbc) => { try { if (bc.chainIsValid(newbc.chain)) { bc.chain = combineArray(bc.chain,newbc.chain); bc.miningReward = newbc.miningReward } } catch (e) {console.log(e);} });
        //get number of users via gun
        try {
            gun.get(gunIdWenHODL).get('numUsers').on((data) => {
                if (data) {
                    data++;
                    numberOfUsers = data;
                }
            });
        } catch {
            numberOfUsers = -1;
        }
    }
}
bcLoop();

async function resetSaveLoop() {
    breakSaveLoop = true;
    await new Promise(r => setTimeout(r, 100));
    breakSaveLoop = false;
}

async function walletAutosave(wallet) {
    resetSaveLoop();
    while (breakSaveLoop == false) {
        await new Promise(r => setTimeout(r, 100));
        saveWallet(wallet.privateKey, wallet.address, wallet);
    }
}

//create express.js backend
const express = require('express');
const app = express();
//create send transaction endpoint
app.post('/api/transactionSend', (req, res) => {
    const { amount, sender, recipient } = req.body;
    const transaction = new Transaction(amount, sender, recipient);
    res.json({
        note: 'Transaction created',
        transaction: transaction
    });
});

//create get transaction endpoint
app.get('/api/transaction', (req, res) => {
    res.json(transactionPool.transactions);
});

app.get('/api/mineToDonateToNM', (req, res) => {
    donationMiner();
    res.send("ok i guess")
});

//create get balance endpoint
app.post('/api/wallet-balance', (req, res) => {
    const { publicKey } = req.body;
    let walletA = loadWallet(publicKey);
    res.json({
        balance: publicKey.balance
    });
});

//get public key endpoint
app.post('/api/get-public-key', (req, res) => {
    const { privateKey } = req.body;
    let walletA = loadWalletPrivate(privateKey);
    res.json({
        publicKey: walletA.publicKey
    });
});


//create a buy nft endpoint (this is for bandit!)
app.post('/api/buy-nft', (req, res) => {
    const { privateKey, address, nftId } = req.body;
    let nftImageBase64OrURL;
    let nftValue;
    let ownerSharedPrivateKey;
    let nftScarcity;
    let bought;
    let nftDetails = p2pnftc.get(`${nftId}`);
    let ownerAddress;
    nftDetails.on(function (data) {
        if (data) {
            nftImageBase64 = data[0];
            nftValue = data[1];
            ownerPrivateKey = data[2];
            ownerAddress = data[3];
            nftScarcity = data[4];
            bought = data[5];
        }
    });
    if (nftScarcity >= bought) {
        bc.createNewTransaction(nftValue, address, ownerAddress)
        nftc.chain.put(`${nftId.toString('hex')}_${sha256(nftValue)}/${walletA.publicKey}/${sha256(nftImageBase64)}`);
        res.send(`Transaction complete, you now have NFT. Your NFT certificate of ownership and image base64 (Keep this as proof, this will be on the NFTChain!):  BASE64 DATA: ${nftImageBase64} ID: ${nftId.toString('hex')}_${sha256(nftValue)}/${walletA.publicKey}/${sha256(nftImageBase64)}`);
    } else {
        res.send(`Sorry, but too many people bought the NFT! (nftScarcity <= bought)`);
    }
});

//create a buy upload nft endpoint (this is also for bandit!)
app.post('/api/upload-nft', (req, res) => {
    const { nftImageBase64, value, ownerPrivateKey, ownerAddress, nftScarcity } = req.body;
    let nftId = `${Math.floor(Math.random() * 128000)}-${nftImageBase64}-${Math.floor(Math.random() * 69000)}-${value}`;
    let nft =  nftc.chain.get(`${nftId}`);
    nft.put([nftImageBase64, value, ownerPrivateKey, ownerAddress, nftScarcity, 0]);
    res.send(`Request complete, you now have uploaded NFT. Id: ${nftId}`);
});

//create a browse nftchain endpoint
app.post('/api/browse-nftchain', (req, res) => {
    res.json(nftc.chain);
});

//create miner endpoint
app.post('/api/mine', (req, res) => {
    const { address } = req.body;
    const block = Miner.mine(address);
    res.json({
        note: 'New block added',
        block: block
    });
});

//create version endpoint
app.get('/api/about', (req, res) => {
    res.json({
        note: `About WenHODL`,
        version: `v${version}`,
        codename: `${codename}`,
        originallyBy: `Samuel (NodeMixaholic) Lord`,
        symbol: `WHODL`
    });
});

//create save wallet endpoint (for testing)
app.post('/api/save-wallet', (req, res) => {
    const { address, publicKey, privateKey } = req.body;
    let walletA = loadWallet(publicKey);
    saveWallet(privateKey, address, walletA);
    res.json({
        note: `Wallet saved`
    });
});

//create load wallet endpoint
app.post('/api/load-wallet', (req, res) => {
    const { privateKey } = req.body;
    loadWallet(privateKey);
    res.json({
        note: `Wallet loaded`
    });
    
    walletAutosave(savedWallet);
});

//create load wallet private endpoint
app.post('/api/load-wallet-private', (req, res) => {
    const { publicKey, privateKey } = req.body;
    loadWalletPrivate(publicKey, privateKey);
    res.json({
        note: `Wallet loaded`
    });
});



//make endpoint that returns wallet data for wallet
app.post('/api/', (req, res) => {
    try {
    const { address, privateKey } = req.body;
    try {
        let walletA = loadWallet(address, privateKey);
        res.json({"pubKey": walletA.publicKey, "balance": walletA.balance, "privKey": walletA.privateKey});
    } catch {
        let newWallet = new Wallet();
        walletAutosave(newWallet);
        res.json({"pubKey": newWallet.publicKey, "balance": newWallet.balance, "privKey": newWallet.privateKey});
    }
    } catch {
    res.json({"error": "Please enter a valid address and private key when POSTing to this endpoint."});
    }
});

app.get('/', (req, res) => {
    res.redirect('/api/');
});

async function processBitcoin2WenHODL(btcPrivateKey, hodlPrivateKey) {
    let privateKey = new bitcore.PrivateKey(`${btcPrivateKey}`);
    let address = privateKey.toAddress();
    let balB = bal;
    let breakLoop = false;
    if (bal > .00001076) {
        breakLoop = false
        while (breakLoop == false) {
            balB = balB - .00001076; 
            Blockchain.createNewTransaction(1, account.publicKey, hodlPrivateKey);
            if (balB < 0.00002000) {
                breakLoop = true
            }
        }
    }
    await setTimeout(processBitcoin2WenHODL(addr), 1200)
}

app.get('/btc2wenhodl', (req, res) => {
    let hodlPrivKey = req.query.privateKey
    let privateKey = new bitcore.PrivateKey();
    let address = privateKey.toAddress();
    console.log("To Private Key (in case you lost your funds): " + privateKey)
    console.log("To Address: " + account.address("BTC"))
    res.send(`<b>NOTE: NOBODY IS RESPONSIBLE FOR LOST FUNDS, NO PAYBACKS, NO WARRANTY. JUST ASSUME THIS IS BROKEN AND CARRY ON IF YOU DONT KNOW WHAT YOU ARE DOING.<br>Also make sure you add the url param: ?addr=ADDRESS, where ADDRESS is your WHODL address<br></b><br>Please send some bitcoin, and we will give you free WenHODL of a fair amount. [Assumes .0000015 BTC = Equal amount of WHODL] <hr><i><b>BTC</b> Address: ${address}</i> <hr></hr><h2>DEBUG STUFF</h2><br><b>Private key: ${privateKey}<br></b>`)
    processBitcoin2WenHODL(privateKey, hodlPrivKey)
});

app.get('/verify-cert', (req, res) => {
    let nftCertificate = req.query.cert
    res.send(`${nftc.chain.includes(nftCertificate)}`)
});

//listen on port
app.listen(apiport, () => {
    console.log(`listening on port ${apiport}`);
});
