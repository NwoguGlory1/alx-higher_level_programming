#!/usr/bin/node

const argv1 = process.argv[2];
const argv2 = process.argv[3];
const x = parseInt(argv1);
const y = parseInt(argv2);

function add(a, b) {
  return a + b;
}
const sum = add(x, y);
console.log(sum);
