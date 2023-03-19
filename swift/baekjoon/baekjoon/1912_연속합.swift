//
//  1912_연속합.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/03/19.
//

import Foundation

var n = Int(readLine()!)!
var nums = readLine()!.split(separator: " ").map{ Int($0)! }

var dp: [Int] = [Int](repeating: 0, count: n)
dp[0] = nums[0]

// 이전까지의 최대값과, 현재값을 더해 0보다 크다면 최신화. 근데 무작정 0보다 크다고 더한 값을 넣는게 아니라 현재값만 가지고 있을 때 더 클수 있으니까 비교해서 넣어줌.
// 0보다 작다면 현재 값 저장
for i in 1..<n {
    if dp[i-1] + nums[i] > 0 {
        dp[i] = max(dp[i-1] + nums[i], nums[i])
    } else {
        dp[i] = nums[i]
    }
}

print(dp.max()!)
