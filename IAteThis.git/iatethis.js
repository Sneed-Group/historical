var d = new Date();
var cals = document.getElementsByClassName("MuiTypography-root MuiCardHeader-title MuiTypography-h4 MuiTypography-colorInherit MuiTypography-gutterBottom MuiTypography-displayBlock").item(0).innerText;
var title = document.getElementsByClassName("MuiTypography-root MuiTypography-h4").item(0).innerText.replace("How many calories in\n", "")
var month = d.getMonth() + 1;
var details = "You ate " + title + " with " + cals + " on " + month + "-" + d.getDate() + "-" + d.getFullYear() + " at " + d.getHours() + ":" + d.getMinutes(); + ".\n"
console.log(details); 
var blob = new Blob([details],
                { type: "text/plain;charset=utf-8" });
var blobUrl = URL.createObjectURL(blob);
var link = document.createElement("a")
link.href = blobUrl;
link.download = "What I ate on " + Date.now() + ".txt";
link.innerHTML = "Click here to download your calorie file."
document.body.appendChild(link);