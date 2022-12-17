import Foundation

func solution(_ k:Int, _ d:Int) -> Int64 {
    var answer = 0
    
    for i in stride(from: 0, through: d, by: k) {
        let x = sqrt(pow(Double(d),2) - pow(Double(i),2))
        answer += Int(floor(Double(x)/Double(k))) + 1
    }
    return Int64(answer)
}