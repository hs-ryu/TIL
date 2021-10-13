// 효율성 0

function solution(n) {
  var answer = 0;
  
  for (var i = 1; i <= n; i++) {
      var im = true
      if (i === 1) {
          im = false
      }
      if (i >= 4) {
          for (var j = 2; j <= Math.sqrt(i); j++) {
              if (i % j === 0) {
                  im = false
              }
          }
      }
      
      
      if (im) {
          answer += 1
      }
  }

  return answer;
}