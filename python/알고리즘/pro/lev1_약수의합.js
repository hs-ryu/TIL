// function solution(n) {
//     var answer = 0;
//     for (var i=1; i < n+1; i++) {
//         if (n % i === 0) {
//             answer += i
//         }
//     }
    
    
//     return answer;
// }

function solution(n) {
  var answer = 0;
  if (n != 1) {
      for (var i=1; i < Number(n/2+1); i++) {
          if (n % i === 0) {
              answer += i
          }
      }
      answer += n
  }
  else {
      answer = 1
  }
      
  return answer;
}