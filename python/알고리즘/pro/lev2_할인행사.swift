import Foundation

func solution(_ want:[String], _ number:[Int], _ discount:[String]) -> Int {
    var wantInfo = Dictionary<String,Int>()
    var sellInfo = [String:Int]()
    var result = 0
    for i in 0..<want.count {
        wantInfo[want[i]] = number[i]
    }
    
    for i in 0..<discount.count {
        if i < 10 {
            if let temp = sellInfo[discount[i]] {
                sellInfo[discount[i]]! += 1
            } else {
                sellInfo[discount[i]] = 1
            }
        } else {
            if let temp = sellInfo[discount[i-10]] {
                sellInfo[discount[i-10]]! -= 1
                if sellInfo[discount[i-10]] == 0 {
                    sellInfo.removeValue(forKey: discount[i-10])
                }
            }
            if let temp = sellInfo[discount[i]] {
                sellInfo[discount[i]]! += 1
            } else {
                sellInfo[discount[i]] = 1
            }
        }
        
        var yes = 0
        // 확인하기.
        for w in wantInfo.keys {
            if let temp = sellInfo[w] {
                if wantInfo[w] == temp {
                    continue
                } else {
                    yes = 1
                    break
                }
            } else {
                yes = 1
                break
            }
        }
        
        if yes == 0 {
            result += 1
        }
        
    }
    
    return result
}

// 다른 사람의 풀이

import Foundation

func solution(_ want:[String], _ number:[Int], _ discount:[String]) -> Int {
    var answer = 0

    // 2중 배열. discount.count < 100,000
    // * 10 -> 최대 1,000,000만번. 나도 마찬가지네?
    for i in 0..<(discount.count - 9) {
        var temp = Array(repeating: 0, count: want.count)
        for j in i..<(i + 10) {
            if let idx = want.firstIndex(of: discount[j]) {
                temp[idx] += 1
            }
        }
        // 그냥 배열 비교해버리네. 괜찮네.
        if number == temp {
            answer += 1
        }
    }

    return answer
}