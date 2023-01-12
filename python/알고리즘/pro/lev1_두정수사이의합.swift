import Foundation

func solution(_ a:Int, _ b:Int) -> Int64 {
    var result = 0
    var m1 = max(a,b)
    var m2 = min(a,b)
    
    
    for i in m2...m1 {
        result += i
    }
    
    return Int64(result)
}