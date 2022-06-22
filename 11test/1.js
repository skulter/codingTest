const arr = [1, 2, [2, 3, [5, 6]]];

// to enable deep level flatten use recursion with reduce and concat
function flatDeep(arr, d) {
  return d > 0 ? arr.reduce((acc, val) => acc.concat(Array.isArray(val) ? flatDeep(val, d - 1) : val), [])
                : arr.slice();
};

flatDeep(arr);
// [1, 2, 3, 4, 5, 6]

console.log(arr.flat(Infinity).filter(x=>x == 2).length)
