#!/usr/bin/node

const argv = process.argv[2];
const x = parseInt(argv);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
