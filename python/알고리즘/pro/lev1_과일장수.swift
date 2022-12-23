import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    var score = score.sorted{ $0 > $1 }
    var result = 0
    
    var i = 0
    var minV = 10
    var cnt = 0
    while i < score.count {
        cnt += 1
        if minV > score[i] {
            minV = score[i]
        }
        
        if cnt == m {
            result += minV * m
            cnt = 0
            minV = 10
        }
        i += 1
    }
    
    return result
}

// 리팩토링
import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    let s = score.sorted(by: >)
    // let s = score.sorted{ $0 > $1 }
    return stride(from: m-1, to: score.count, by: m)
        .reduce(0) { $0 + s[$1] * m }
}