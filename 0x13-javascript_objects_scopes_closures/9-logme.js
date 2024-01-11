#!/usr/bin/node

exports.logMe = function (item) {
  const arry = ['Hello', 'Best', 'School'];

  for (let i = 0; i <= arry.length; i++) {
    console.log(`${i}: ${arry[i]}`);
  }
};
