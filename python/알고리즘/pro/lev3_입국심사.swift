import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    // 심사 받는 시간을 기준으로 이분탐색
    var l = 0
    // 즉 r을 제일 오래걸리는 사람이 다 심사할 경우로 초기값 설정.
    var r = times.max()! * n
    var result = 0
    while l <= r {
        // 그럼 mid는, 심사관들에게 주어진 시간!
        var mid = (l+r)/2
        var temp = 0
        for time in times {
            // 각 심사관은 mid분 만큼의 시간동안 몇명을 심사할 수 있는가?
            temp += mid / time
            if temp >= n {
                break
            }
        }
        // 심사 한 사람 수가 심사 받아야할 사람 수보다 많다면?
        if temp >= n {
            result = mid
            r = mid - 1
        }
        // 심사 한 사람 수가 심사 받아야할 사람 수보다 적다면?
        else {
            l = mid + 1
        }
    }
    
    return Int64(result)
}