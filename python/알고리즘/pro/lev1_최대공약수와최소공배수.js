function solution(n, m) {
  var answer = [];
  var a = 0
  var b = 0
  for (var i = 1; i < n*m; i++) {
      if (n % i === 0 & m % i === 0) {
          a = i
      }
  }
  for (var j = 1; j < n*m + 1; j ++) {
      if (j % n === 0 & j % m === 0) {
          b = j
          break
      }
  }
  answer.push(a)
  answer.push(b)
  return answer;
}
