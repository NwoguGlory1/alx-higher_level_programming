#!/usr/bin/node

const arg = process.argv;

function secondBig (array) {
  if (array.length <= 3) {
    return (0);
  }

  array = array.slice(2).map(n => parseInt(n));

  const max = Math.max(...array);

  const arr = array.filter(arr => arr < max);

  return (Math.max(...arr));
}

console.log(secondBig(arg));
