// function solution(seoul) {
//     var answer = '';
//     var x = 0
//     for (var i = 0; i < seoul.length; i++) {
//         if (seoul[i] === "Kim") {
//             x = i
//         }
//     }
    
//     answer = "김서방은 " + x + "에 있다"
    
//     return answer;
// }

// 배열.indexOf(찾고싶은 값)으로 위치를 쉽게 뽑아낼 수 있다.

function solution(seoul) {
  var answer = '';
  answer = "김서방은 " + seoul.indexOf('Kim') + "에 있다"
  
  return answer;
}