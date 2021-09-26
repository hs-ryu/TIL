function solution(n)
{
    var answer = 0;
    var string = String(n)
    
    for (var i=0; i<string.length; i++) {
        answer += Number(string[i])
    }
    
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.


    return answer;
}