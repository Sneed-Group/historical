# WenHODL-Writeup (old, back when it was called SparkyCoin)
## An automated, digital, unstable fiat-like currency made in NodeJS and Express.js with a so-simple-its-genius design

### Automated
* Automated growth, can "mint" more money automatically as circulation grows
  * Starting at 250000 total coins
  * Down to 19 digits behind the decimal point

## Digital, unstable, and fiat-like
* Mining in a different way.
  * Since this is fiat, we do not need "mining" in a typical sence.
  * So we instead have a faucet of sorts, but with a guessing game, where you guess the Y for `X * Y  = Z`. The Y is randomized, and these two numbers only last for ~42 seconds.
* Wallets are different, too!
  * Since we don't have banks, and we are fiat, you just send the money to someones wallet via their address, and then it's just there!
* Everything done via Express.js and NodeJS via an API.
* Unstable as in the value does fluctuate, fiat-like as in it's backed by the people.
* There's 2 Databases using Quick.db, they only hold: Current amount of coins in wallet, public, private keys, and currently "minted" coins.

## Centrally Decentralized.
* Decentralized meaning there are servers everywhere
* Centrally meaning that each server hosts their own database
 * With their own data.
* However you are able to send SPARKY Peer to Peer
 
### Most importantly, people don't have to ask for a fork. Fork Freely. Just follow the licenses provided.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
