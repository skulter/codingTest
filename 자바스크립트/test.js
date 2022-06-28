function solution(A) {
  // only positive values, sorted
  A = A.filter((x) => x >= 1).sort((a, b) => a - b);

  let x = 1;

  for (let i = 0; i < A.length; i++) {
    // if we find a smaller number no need to continue, cause the array is sorted
    if (x < A[i]) {
      return x;
    }
    x = A[i] + 1;
  }

  return x;
}
function solution2(A) {
  // only positive values, sorted
  return A.sort()
    .filter((x) => x >= 1)
    .reduce((acc, cur) => {
      if (acc < cur) {
        return acc;
      }
      return cur + 1;
    }, 1);
}

// console.log(solution([1, 3, 6, 4, 1, 2]))
console.log(solution2([1, 3, 6, 4, 1, 2]));

function jinosort(x) {
  return x.sort((x, y) => x - y);
}

console.log(jinosort([1, 2, 3, 4, 5, 6, 7, 8, 0, 9, 10, 11, 12, 13, 14, 15]));
console.log([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]);

const test = [1,2,3,4,5]
const test2 = test
[test[0], test[1]] = [test[1],test[0]]
console.log(test,test2 )