#!/usr/bin/node
exports.converter = function (base) {
  if (base === 10) {
    return function (num) {
      const result = num.toString(10);
      return result;
    };
  }
  if (base === 16) {
    return function (num) {
      const result = num.toString(16);
      return result;
    };
  }
};
