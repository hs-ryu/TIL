function solution(arr)
{
    var answer = [];

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for (let i=0; i < arr.length-1; i++) {
        if (arr[i] === arr[i+1]) {
            continue
        }
        answer.push(arr[i])
    }
    if (arr[arr.length-1] !== answer[answer.length-1]) {
        answer.push(arr[arr.length-1])
    }
    return answer;
}