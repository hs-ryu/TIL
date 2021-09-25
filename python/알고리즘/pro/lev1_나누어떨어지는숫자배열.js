function solution(arr, divisor) {
  var answer = [];
  for (let i=0; i < arr.length; i++) {
      if (arr[i] % divisor === 0) {
          answer.push(arr[i])
      } 
  }
  if (answer.length === 0) {
      answer.push(-1)    
  }
  // sort 함수는 2개의 배열 element를 파라미터로 받음. 
  // a,b를 입력으로 받는다면, 리턴값이 0보다 크면 b가 a보다 앞으로 가도록 위치 변경
  // 리턴값이 0보다 작으면 a가 b보다 앞으로 가도록 위치 변경
  // 만약 리턴값이 0이면 위치 변경 없음.
  answer.sort(function(a, b){
      return a - b;
  })
  return answer;
}