const monerojs = require("monero-javascript");
const myArgs = process.argv.slice(2);
let to = myArgs[0];
let amount = myArgs[1] * 100000000000 || 100000000000;
async function zzz(ms) {
    await new Promise(r => setTimeout(r, ms));
}
async function main() {
    while (true) {
        //create new wallet with a random seed
        let wallet = await monerojs.createWalletFull();
        //send funds to the destination address or 
        try {
            let tx = await wallet.createTx({
                accountIndex: 0,  // source account to send funds from
                address: to,
                amount: amount, // send 1 XMR (denominated in atomic units)
                relay: true // relay the transaction to the network
            });
            console.log("Transaction created: " + tx.getTxId());
        } catch {
            console.log("Moving on to next wallet...");
        }
        zzz(100)
    }
}
main();
