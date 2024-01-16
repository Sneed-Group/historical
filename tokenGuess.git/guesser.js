function guessToken(id) {
    let length = 27
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return btoa(id) + "." + btoa(Math.floor(Date.now() / 1000) + 1293840000) + "." + result;
}

async function main() {
let id = await prompt("Please enter a person's numeric discord ID")
while (true) {
console.log(guessToken(id))
await new Promise(r => setTimeout(r, 200));
}
}

main()
