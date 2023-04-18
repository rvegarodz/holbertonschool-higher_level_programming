#!/usr/bin/node
exports.esrever = function (list) {
  const tempList = [];
  let listLength = list.length - 1;
  while (listLength >= 0) {
    tempList.push(list[listLength]);
    listLength -= 1;
  }
  return tempList;
};
