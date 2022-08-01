// 找出多个数组中的最大数字
function largestOfFour(arr) {
  const m = [];

  for (let i = 0; i < arr.length; i++) {
    let n = 0;
    for (let j = 0; j < arr[i].length; j++) {
      if (n < arr[i][j]) {
        n = arr[i][j];
      }
    }
    m.push(n);
  }
  return m;
}
console.log(
  largestOfFour([
    [4, 5, 1, 3],
    [13, 27, 18, 26],
    [32, 35, 37, 39],
    [1000, 1001, 857, 1],
  ])
);
