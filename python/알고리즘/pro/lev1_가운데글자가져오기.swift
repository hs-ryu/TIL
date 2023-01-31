func solution(_ s:String) -> String {
    var result = ""
    if s.count % 2 == 1 {
        var center = s.index(s.startIndex, offsetBy: s.count/2)
        result = String(s[center])
    } else {
        var centerPast = s.index(s.startIndex, offsetBy: s.count/2-1)
        var center = s.index(s.startIndex, offsetBy: s.count/2)
        
        result = String(s[centerPast]) + String(s[center])
    }
    return result
}


// 이런 풀이도 있넹
func solution(_ s:String) -> String {
    if Array(s).count % 2 == 0 {
        return String(Array(s)[(s.count/2)-1...(s.count/2)])
    }else{
        return String(Array(s)[s.count/2])
    }
}