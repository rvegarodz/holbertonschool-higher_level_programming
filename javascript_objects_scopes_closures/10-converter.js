#!/usr/bin/node
exports.converter = function (base) {
  if (base === 2) {
    return function (num) {
      return num.toString(2);
    };
  }
  if (base === 10) {
    return function (num) {
      return num.toString(10);
    };
  }
  if (base === 16) {
    return function (num) {
      return num.toString(16);
    };
  }
};
