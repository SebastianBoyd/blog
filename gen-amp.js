var ampl = require('ampl');
const fs = require('fs-extra')

var markdownString = fs.readFileSync( __dirname + '/welcome.md', "utf8"); // or read from a .md file
console.log(markdownString)
var cssStyle = 'h1 { color: green; }'; // or load your style.css file
ampl.parse(markdownString, {style: cssStyle}, function(ampHtml) {
  fs.writeFileSync('welcome.html', ampHtml)
});