function solution(arr1, arr2) {
  // var answer = [[]];
  var row = arr1.length;
  var col = arr1[0].length;
  var answer = new Array(row);
  for (var i = 0; i < row; i++) {
      answer[i] = new Array(col);
  }
  for (var i=0; i < arr1.length; i++) {
      for (var j=0; j < arr1[i].length; j++) {
          answer[i][j] = arr1[i][j] + arr2[i][j]
      }
  }
  
  return answer;
}