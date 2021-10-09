// 공백으로 자르기 -> string.split(" ")
// 대문자 처리 -> string.toLowerCase
// 문자열 슬라이싱 -> string.slice(시작, 끝)


function solution(s) {
  var answer = '';
  var arr = s.split(" ");
  
  for (var i=0; i < arr.length; i++) {
      for (var j=0; j < arr[i].length; j++) {
          if (j % 2) {
              answer += arr[i][j].toLowerCase()
          }
          else {
              answer += arr[i][j].toUpperCase()
          }
      }
      answer += ' '
  }
  
  
  return answer.slice(0, answer.length-1);
}