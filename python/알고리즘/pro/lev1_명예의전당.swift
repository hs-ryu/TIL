import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var arr = [Int]()
    var result = [Int]()
    
    for (idx, num) in score.enumerated() {
        if arr.count < k {
            arr.append(num)
            arr.sort(by: >)
            result.append(arr[arr.endIndex-1])
        } else {
            var x = 0
            for i in 0..<k {
                if num > arr[i] {
                    arr.insert(num, at: i)
                    arr.removeLast()
                    result.append(arr[arr.endIndex-1])
                    x = 1
                    break
                }
            }
            if x == 0 {
                result.append(arr[arr.endIndex-1])
            }
            
        }
    }
    return result
}