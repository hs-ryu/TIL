// 소문자 변환 : 문자.toLowerCase()
// 대문자 변환 : 문자.toUpperCase()

function solution(s){
  var answer = true;
  
  var p_cnt = 0
  var y_cnt = 0
  for (var i = 0; i < s.length; i++) {
      if (s[i].toLowerCase() === 'p') {
          p_cnt += 1
      }
      else if (s[i].toLowerCase() === 'y') {
          y_cnt += 1
      }
  }
  if (p_cnt !== y_cnt) {
      answer = false
  }

  return answer;
}