import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var result = 0
    var a = a.sorted(by: {$0 > $1})
    var b = b.sorted(by: {$0 > $1})

    var j = 0
    // a,b를 내림차순 정리.
    // 예를들어, a의 1번과 b의 1번을 비교했을때 a의 1번이 b의 1번보다 작으면? -> b가 이긴다. b의 다음 놈을 체크한다.
    // 반대로, a의 1번이 b의 1번보다 크다? -> a가 이긴다. 그럼 어차피 a가 이기는거니까, a의 2번과 b의 1번을 비교한다. 계속 이런식으로 굳.
    
    for i in 0..<a.count {
        if a[i] < b[j] {
            j += 1
            result += 1
        }
    }
    
    return result
}