import Foundation

func solution(_ n:Int) -> Int {
    var answer = 0
    let binaryN = String(n, radix:2)
    // 여기서, oneCount를 반복문 돌려서 하는거 보다, 이게 더 효율이 좋다. 
    // 반복문 돌려서 체크하니까 효율성 하나 통과 못한다.
    var oneCount = binaryN.filter{$0 == "1"}.count
    
    for num in n+1...1000000 {
        let binaryNum = String(num, radix:2)
        // 꼭 배열이 아니어도 filter 걸 수 있다. 반환값은 배열.
        if binaryNum.filter({ $0 == "1" }).count == oneCount {
            answer = num
            break
        }
    }
    
    return answer
}