import Foundation

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    var dic = Dictionary<Int,Int>()
    for i in 0..<tangerine.count {
        if let x = dic[tangerine[i]] {
            dic[tangerine[i]]! += 1
        } else {
            dic[tangerine[i]] = 1
        }
    }
    
    var arr = [Int]()
    for (key,value) in dic {
        arr.append(value)
    }
    
    arr.sort(by:>)
    var result = 0
    var cnt = 0
    for i in 0..<arr.count {
        cnt += arr[i]
        result += 1
        if cnt >= k {
            break
        }
    }
    return result
}