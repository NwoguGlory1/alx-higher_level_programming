#!/usr/bin/node

const argv = process.argv[2];
const x = parseInt(argv);

function factorial(n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(x));
