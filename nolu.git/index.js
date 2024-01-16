const request = require("request");
const cheerio = require('cheerio');
const process = require('process');
//require puppeteer
const puppeteer = require('puppeteer');
let resultsFinal = [];
const searchPluto = async (searchTerm) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://pluto.tv/en/on-demand');
    await new Promise(r => setTimeout(r, 2000));
    const result = await page.evaluate(searchTerm => {
        let results = [];
        let elements = document.querySelectorAll('a');
        elements.forEach(element => {
            if (element.innerText.toLowerCase().includes(searchTerm.toLowerCase())) { results.push({
                title: element.innerText,
                url: element.href,
            }); }
        });
        return results;
    }, searchTerm);
    await browser.close();
    return result;
}

const searchYT = async (searchTerm) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setDefaultNavigationTimeout(0);
    let st = searchTerm.replace(/ /g, "+");
    await page.goto(`https://www.youtube.com/results?search_query=${st}+full`);
    await new Promise(r => setTimeout(r, 2000));
    const result = await page.evaluate(searchTerm => {
        let results = [];
        let elements = document.querySelectorAll('a');
       elements.forEach(element => {
           if (element.innerText.toLowerCase().includes(searchTerm.substring(0,3))) { results.push({
               title: element.title,
               url: element.href,
           }); }
       });
        return results;
    }, searchTerm);
    await browser.close();
    return result;
}

const searchTubi = async (searchTerm) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(`https://tubi.tv/search/${searchTerm}`);
    await new Promise(r => setTimeout(r, 2000));
    const result = await page.evaluate(searchTerm => {
        let results = [];
        let elements = document.querySelectorAll('a');
       elements.forEach(element => {
           if (element.innerText.toLowerCase().includes(searchTerm.substring(0,3))) { results.push({
               title: element.title,
               url: element.href,
           }); }
       });
        return results;
    }, searchTerm);
    await browser.close();
    return result;
}
//full+movie+free

const searchYTOfficial  = async (searchTerm) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    let st = searchTerm.replace(/ /g, "+");
    await page.setDefaultNavigationTimeout(0);
    await page.goto(`https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx`);
    await new Promise(r => setTimeout(r, 2000));
    const result = await page.evaluate(searchTerm => {
        let results = [];
        let elements = document.querySelectorAll('a');
       elements.forEach(element => {
           if (element.innerText.toLowerCase().includes(searchTerm)) { results.push({
               title: element.innerText,
               url: element.href,
           }); }
       });
        return results;
    }, searchTerm);
    await browser.close();
    return result;
}

const searchArchiveTV = async (searchTerm) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(`https://archive.org/details/tvarchive?query=${searchTerm}`);
    await new Promise(r => setTimeout(r, 2000));
    const result = await page.evaluate(() => {
        let results = [];
        let elements = document.querySelectorAll('a');
        elements.forEach(element => {
            if (element.innerText.toLowerCase().includes(document.querySelectorAll("[type='search']")[0].value.toLowerCase())) { results.push({
                title: element.innerText,
                url: element.href,
            }); }
        });
        return results;
    });
    await browser.close();
    return result;
}



const searchArchiveNews = async (searchTerm) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(`https://archive.org/details/tvnews?query=${searchTerm}`);
    await new Promise(r => setTimeout(r, 2000));
    const result = await page.evaluate(() => {
        let results = [];
        let elements = document.querySelectorAll('a');
        elements.forEach(element => {
            if (element.innerText.toLowerCase().includes(document.querySelectorAll("[type='search']")[0].value.toLowerCase())) { results.push({
                title: element.innerText,
                url: element.href,
            }); }
        });
        return results;
    });
    await browser.close();
    return result;
}

const searchArchiveMovies = async (searchTerm) => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(`https://archive.org/details/moviesandfilms?query=${searchTerm}`);
    await new Promise(r => setTimeout(r, 2000));
    const result = await page.evaluate(() => {
        let results = [];
        let elements = document.querySelectorAll('a');
        elements.forEach(element => {
            if (element.innerText.toLowerCase().includes(document.querySelectorAll("[type='search']")[0].value.toLowerCase())) { results.push({
                title: element.innerText,
                url: element.href,
            }); }
        });
        return results;
    });
    await browser.close();
    return result;
}
function getMovieSearchResults(searchTerm) {
    
    searchPluto(searchTerm).then(resultsPluto => {
        resultsFinal = resultsFinal.concat(resultsPluto);
        searchArchiveMovies(searchTerm).then(resultArchiveMovies => {
            resultsFinal = resultsFinal.concat(resultArchiveMovies);
            searchArchiveNews(searchTerm).then(resultArchiveNews => {
                resultsFinal = resultsFinal.concat(resultArchiveNews);
                searchTubi(searchTerm).then(resultTubi => {
                    resultsFinal = resultsFinal.concat(resultTubi);
                    searchYTOfficial(searchTerm).then(resultYTOfficial => {
                        resultsFinal = resultsFinal.concat(resultYTOfficial);
                        searchYT(searchTerm).then(resultYT => {
                            resultsFinal = resultsFinal.concat(resultYT);
                            searchArchiveTV(searchTerm).then(resultArchiveTV => {
                                resultsFinal = resultsFinal.concat(resultArchiveTV);
                                console.log("Results:")
                                for (let i = 0; i < resultsFinal.length; i++) {
                                    console.log(`* ${resultsFinal[i].title}`);
                                    console.log(`   - ${resultsFinal[i].url}`);
                                }
                            });
                        });
                    });
                });
            });
        });
    });
}

//let the user input a search term
let searchTerm = String(process.argv[2]);
if (searchTerm == "undefined" || searchTerm == "" || searchTerm == " ") {
    console.log("Please enter a search term");
} else {
    console.log("OK, searching for: " + searchTerm);
    getMovieSearchResults(searchTerm);
}
