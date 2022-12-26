import Foundation


// 시간초과 걸림...
func solution(_ queue1:[Int], _ queue2:[Int]) -> Int {
    var q1 = queue1.reduce(0){$0 + $1}
    var q2 = queue2.reduce(0,+)
    var totalCount = queue1.count + queue2.count
    var sumQ = q1 + q2
    
    // 애당초에 양쪽 q의 합을 2개로 동일하게 나눌 수 없다면 의미 없다.
    var target = sumQ / 2
    if target * 2 != sumQ {
        return -1
    }
    
    var result = 0
    var queue1 = queue1
    var queue2 = queue2
    while true {
        if q1 == q2 {
            break
        }
        
        if queue1.count == 0 || queue2.count == 0 || result > totalCount * 2{
            result = -1
            break
        }
        
        if q1 > q2 {
            let x = queue1.first!
            queue1.removeFirst()
            queue2.append(x)
            q1 -= x
            q2 += x
        } else {
            let x = queue2.first!
            queue2.removeFirst()
            queue1.append(x)
            q1 += x
            q2 -= x
        }
        
        result += 1
    }
    return result
}

// 리펙토링.
func solution(_ queue1: [Int], _ queue2: [Int]) -> Int {
    var q1 = queue1.reduce(0, +)
    var q2 = queue2.reduce(0) { $0 + $1}
    let target = (q1+q2) / 2
    // ArraySlice 타입과 시간 복잡도의 관계는?
    var queue1 = queue1[queue1.indices]
    var queue2 = queue2[queue2.indices]
    var result = 0
    // 한쪽을 다 뺐는데, 답이 없으면? 그만
    while !queue1.isEmpty && !queue2.isEmpty {
        if q1 == target {
            return result
        }
        
        if q1 < target {
            let first = queue2.popFirst()!
            q1 += first
            queue1.append(first)
        } else {
            q1 -= queue1.popFirst()!
        }
        result += 1
        
    }
    return -1
}