#!/usr/bin/node

const argv = process.argv;
let index = 2;
if (argv[index] === undefined) {
	console.log('No argument');
}else {	
	console.log(argv[2]);
		}
