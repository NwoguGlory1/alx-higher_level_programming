#!/usr/bin/node

exports.esrever = function (list) {
  const reversedlist = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reversedlist.push(list[i]);
    // pushed each i in list to reversedlist
  }
  return reversedlist;
};
