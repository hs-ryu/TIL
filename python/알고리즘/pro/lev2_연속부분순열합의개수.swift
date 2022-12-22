import Foundation

func solution(_ elements:[Int]) -> Int {
    var s: Set<Int> = []
    
    // 길이가 n인 연속 부분 수열 만들기
    for i in 1..<elements.count+1 {
        // 각 인덱스로부터 n까지 더한 값 set에 넣어주기.
        for j in 0..<elements.count {
            // 이렇게 안하고 할 수 있는 방법은 없을까??
            var total = 0
            var cnt = 0
            while cnt < i {
                var temp = j + cnt
                if temp >= elements.count {
                    temp -= elements.count
                }
                total += elements[temp]
                cnt += 1
            }
            s.insert(total)
        }
    }
    return s.count
}


// 다른사람의 코드
import Foundation

func solution(_ elements:[Int]) -> Int {
    var answer = Set<Int>()

    // 재귀?
    func dfs(_ now: Int, _ num: Int, _ count: Int) {
        answer.insert(num)
        if elements.count == count { return }
        
        dfs((now + 1) % elements.count, num + elements[now % elements.count], count + 1)
    }

    for i in 0..<elements.count {
        // now = 1,2,3,4,0
        // num = 7
        // cnt = 1
        dfs((i + 1) % elements.count , elements[i], 1)
    }

    return answer.count
}