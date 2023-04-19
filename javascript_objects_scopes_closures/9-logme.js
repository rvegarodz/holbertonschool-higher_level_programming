#!/usr/bin/node
let count = 0;

exports.logMe = function (item) {
  const tempCount = count;
  count += 1;
  console.log(tempCount + ' : ' + item);
};
