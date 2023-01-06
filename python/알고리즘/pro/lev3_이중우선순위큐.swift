import Foundation

func solution(_ operations:[String]) -> [Int] {
    var q = [Int]()
    for i in 0..<operations.count {
        
        let x = operations[i].split(separator:" ")
        let oper = x[0]
        let num = Int(x[1])
        if oper == "I" {
            q.append(num!)
            
        } else if oper == "D" && !q.isEmpty {
            if num == -1 {
                q.removeFirst()
            } else {
                q.removeLast()
            }
        }
        // 여기서 계속 정렬하는게 좀 그렇다.
        // 시간초과는 안나는데, 너무 비효율적인듯
        q.sort(by: {$0 < $1})
    }
    var result = [Int]()
    if q.count >= 1 {
        result = [q.last!, q.first!]
    } else {
        result = [0,0]
    }
    
    return result
}