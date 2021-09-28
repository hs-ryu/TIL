// 배열에 값 추가 : push
// 배열에서 특정 인덱스 제거 : splice(제거할 인덱스, 그 인덱스부터 제거할 개수)
// 혹은 filter() 사용.
// filter((ellement) => element !== '제거할 값')

function solution(arr) {
  var answer = [];
  var minV = arr[0];
  var minIndex = 0
  for (var i=0; i < arr.length; i++) {
      if (arr[i] < minV) {
          minV = arr[i]
          minIndex = i
      }
  }
  arr.splice(minIndex,1)
  if (arr.length === 0) {
      arr.push(-1)
  }
  answer = arr
  
  return answer;
}