#!/usr/bin/node
/* returns the reversed version of a list */
exports.esrever = function (list) {
  const newList = [];
  for (let i = list.length - 1; i > -1; i--) {
    newList.push(list[i]);
  }
  return newList;
};
