<img src="https://github.com/NodeMixaholic/WenHODL-API/blob/main/wenhodl-logo.png?raw=true" width="50%"></img>
## The Main Peer/Client API/Backend
***(a memecoin that has effort put into it!)***

### NOTE

You must transfer all rights to Samuel Lord (NodeMixaholic)

### About

An automated, digital currency made in: NodeJS, elliptic, GUN.JS, NodeJS crypto lib, and Express.js.

### Important notices!

In order to contribute, you must follow the [NodeMixaholic C.O.C.](https://github.com/NodeMixaholic/NodeMixaholic-COC)

Also, to learn more on how WHODL was first imagined, visit [the write-up](https://github.com/NodeMixaholic/WenHODL-Writeup/) and go to the earliest commit. (Note: the write-up won't be updated much since I am focusing on the project itself more)

### How to install dependencies (Do this before running!)
cd to the directory where the files are stored, then run:

npm i

### How to run
* cd into the directory
* install dependencies
* npm start

### Where is the server?
There is none! Like Bitcoin, no one user owns the network. This backend uses GUN.JS and Express.JS to make a peer of your own to interact with other users! Go to /api/ to view your details! Save your private key, you will need it for loading your wallet from the GUN.JS network using the /api/load-wallet endpoint!

### Is there an official frontend I could use?
Not yet. I am working on making sure the backend is a bit more polished. However, devs out there can feel free to create their own frontends that use the client API! For example, the user would start up their backend API, then the user would open up the front end. The front end would check for an existing API endpoint /api/, and if it detects the API the user would get his details, an option to load old details from the network via private key, and the ability to make a transaction (and so on if the dev feels like it.)

### Recent development reset
Due to a high dpendency count, as well as some bad code and dependencies starting to rot, I decided to reset development and bring a much more stable version of the API.

### What is a NFTchain?

NFTchain is very similar to the Blockchain, except it's a ledger of bought and new NFTs strictly, and all purchaced nfts come with a "NFT certificate of ownership" which goes on the NFTchain as a form of proof of ownership.
