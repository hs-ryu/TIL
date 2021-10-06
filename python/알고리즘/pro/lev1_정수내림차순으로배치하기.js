
// 내림차순 정렬 -> sort(function(a,b) {return b-a})
// 배열을 문자열로 만들기 -> 배열.join('')

function solution(n) {
  var answer = 0;
  var string_n = String(n)

  var arr = []
  for (var i = 0; i < string_n.length; i++) {
      arr.push(string_n[i])
  }
  console.log(arr)
  arr.sort(function(a,b) {
      return b-a
  })
  var new_n = arr.join('')
  answer = Number(new_n)
  return answer;
}