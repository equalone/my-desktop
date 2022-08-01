function largestOfFour(arr) {
  let m = [];
  let n = 0;
  for (let i = 0; i < arr.lenght; i++) {
    for (let j = 0; j < arr[i].lenght; j++) {
      if (n < arr[i][j]) {
        n = arr[i][j];
        console.log(n);
      }
      m.push(n);
    }
  }
  return m;
}
largestOfFour([
  [4, 5, 1, 3],
  [13, 27, 18, 26],
  [32, 35, 37, 39],
  [1000, 1001, 857, 1],
]);
