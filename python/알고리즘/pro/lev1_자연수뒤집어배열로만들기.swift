
// 쉽당
func solution(_ n:Int64) -> [Int] {
    var s = String(n)
    var a = Array(s)
    a.reverse()
    // String으로 감싸는 이유 -> Array(s)의 속성값 하나하나가 Character 타입이라, Int변환이 안된다.
    var b = a.map { Int(String($0))! }
    
    return b
}