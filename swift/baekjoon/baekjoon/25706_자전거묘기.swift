//
//  25706_자전거묘기.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/05/31.
//

import Foundation

var n: Int = Int(readLine()!)!
var h: [Int] = readLine()!.split(separator: " ").map{Int($0)!}
var dp = [Int](repeating: 1, count: n)

// 거꾸로 계산하고 싶다 -> reversed 쓰자. stride보단 이게 편할듯.
for i in (0..<n-1).reversed() {
    if h[i] == 0 {
        dp[i] += dp[i+1]
    } else {
        // n = 10
        // 3번째 값 : 5
        if i + h[i] + 1 < n {
            dp[i] += dp[i+h[i]+1]
        }
    }
}
print(dp.map{String($0)}.joined(separator: " "))
