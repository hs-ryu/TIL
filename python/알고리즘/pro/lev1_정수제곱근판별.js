// 정수판별 : Number.isInteger(숫자)
// Math.sqrt(n) -> 제곱근이면 정수, 아니면 실수로 반환

function solution(n) {
  var answer = 0;
  if (Number.isInteger(Math.sqrt(n))) {
      var x = Math.sqrt(n) + 1
      answer = x * x
  }
  else {
      answer = -1
  }
  
  return answer;
}