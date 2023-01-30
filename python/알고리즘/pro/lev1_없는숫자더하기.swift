import Foundation

func solution(_ numbers:[Int]) -> Int {
    var result = 0
    let x = Set(numbers)
    
    for i in 0..<10 {
        if !x.contains(i){
            result += i
        }
    }
    return result
}