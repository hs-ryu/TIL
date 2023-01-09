import Foundation

// 파이썬으로 풀었던 문제.
// 포인터 2개 활용해서 left를 줄여나가고, right를 늘려나가며 체크.
// O(n+m) 정도 될듯
func solution(_ s:String) -> Int {
    func palindrome(_ st: String, _ l: Int, _ r: Int) -> Int {
        var length = 0
        var r = r
        var l = l
        var st = Array(st)
        if r - l == 1 {
            length = 0
        } else {
            length = 1
        }
        
        while l >= 0 && r < st.count {
            if st[l] == st[r] {
                l -= 1
                r += 1
                length += 2
            } else {
                break
            }
        }
        return length
    }
    
    var answer = 0
    
    if s.count == 1 {
        return 1
    }
    
    for i in 0..<s.count {
        let p1 = palindrome(s,i,i+1)
        let p2 = palindrome(s,i,i+2)
        answer = max(p1,p2,answer)
    }

    return answer
}