import Foundation
// 효율 0점 풀이.
func solution(_ stones:[Int], _ k:Int) -> Int {
    // n^2 시간초과임.
    // k 구간의 최대값? -> k 구간이 다 0 이하가 되어 버리면 못건넌다. -> 최대값이 즉 갈 수 있는 사람들이 된다.
    var result = 200000001
    var maxValue = 0
    var slice = [Int]()
    
    for i in 0..<stones.count {
        if i < k {
            slice.append(stones[i])
        } else {
            // 그냥 맥시멈 때리면 시간초과 안날까?
            if let sliceMax = slice.max() {
                if sliceMax < result {
                    result = sliceMax
                }
            }
            slice.removeFirst()
            slice.append(stones[i])
        }
    }
    
    // 한번 더 체크해줘야할듯. stones의 길이가 굉장히 짧을수도 있기 때문임.
    if let sliceMax = slice.max() {
        if sliceMax < result {
            result = sliceMax
        }
    }
    
    return result
}



import Foundation

func solution(_ stones:[Int], _ k:Int) -> Int {
    // 이분탐색. 건널수 있는 인원을 가지고 탐색한다.
    var l = 1
    var r = 200000000
    while l <= r {
        var mid = (l+r)/2
        var cnt = 0
        // cnt가 k보다 작은 경우는 끝까지 돌텐데, 이게 왜 효율성이 높은거지?
        for i in 0..<stones.count {
            if stones[i] - mid <= 0 {
                cnt += 1
            } else {
                cnt = 0
            }
            if cnt >= k {
                break
            }
        }
        if cnt >= k {
            r = mid - 1
        } else {
            l = mid + 1
        }
    }
    return l
}