// MAURY FREDERIC 10/08/2018


var casper = require('casper').create({
	// define timeout, catch url if timeout and log it on file.
    stepTimeout: 4000,
	waitTimeout: 5000,
	onStepTimeout: function() {
		var timeOOut = ';' + "tTIMEOUT"
		fs.write(path, timeOOut, 'a')
		casper.exit(1);
	},
	onWaitTimeout: function() {
		var timeOOut = ';' + "wTIMEOUT"
		fs.write(path, timeOOut, 'a')
		casper.exit(1);
	},

});
var fs = require('fs'); // i call filesystem module, to handle files.
var path = 'capture.csv'; // output "string"
var output = 'capture.png'; // output "screenshoot"



/////////////////////////// method to call this script with argument//////////////////
/// .\phantomjs .\casperjs.js .\thisscript.js args4, args5 etc..///

var system = require('system');
var args = system.args;
var url = args[4];

if (args.length === 1) {
  console.log('Try to pass some arguments when invoking this script!');
} else {
	  args.forEach(function(arg, i) {
    console.log(i + ': ' + arg);
  });
}

//////////////////////// i catch casper error and write it on .csv for log.////////////////
casper.on('error', function(msg, backtrace) {
    var erreur = ' message: ' + JSON.stringify(msg, null, 4);
    fs.write(path, erreur, 'a');
    casper.exit(1);
})


/////////////////////////////the main function./////////////////////////////////////
//connect on website define by url.txt.
//select an HTML code
//write url and the selected code on file.

//start url
casper.start(url, function(status) {
	console.log('Connexion to url');
});

//Login form
casper.waitForSelector(".form-horizontal", function() {
	console.log('login form found')

	this.fillSelectors('.form-horizontal', {
		'input[name = username ]' : 'censuré',
		'input[name = password ]' : 'censuré'
	});

	this.click('.do-signin ')
});

//Wait Loggin
casper.waitWhileSelector('.form-horizontal', function(){
	this.echo('logged');
	//var content = this.getHTML('title'); // I capture HTML Code
	var content = this.getHTML('div .codec-info > div'); // I capture HTML Code
	content = url + ';' + content  ;
	fs.write (path, "\n" + content.replace(/(?:\r\n|\r|\n)/g, ''), 'a');
	//casper.capture('screenshots/touch_logged.png');
});

//Go to Peripherals
casper.thenOpen(url + '/web/peripherals', function() {
	console.log('goto status');
});

//Wait Peripherals
casper.waitForSelector('.dl-horizontal', function(){
	this.echo('loaded');
	//casper.capture('screenshots/touch_loading.png');
});

//field Capture
casper.then(function() {

	//casper.capture('screenshots/touch_status.png');



	content = ";" + this.getHTML('dd:last-of-type');

	//fs.write (path, content , 'a');
	// if another selector uncomment, and comment the preceding code
	//casper.capture(output);  // i take a screenshoot , use for debug script.
	fs.write (path, content.replace(/(?:\r\n|\r|\n)/g, ''), 'a');
});

//EOF
casper.then(function() {
	casper.exit
});

casper.run();
