//
//  16194_카드구매하기.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/02/06.
//

import Foundation

var n = Int(readLine()!)!
var p = readLine()!.split(separator: " ").map{ Int($0)! }
p.insert(0, at: 0)
var dp = [Int]()
for _ in 0...n {
    dp.append(0)
}

for i in 1...n {
    dp[i] = p[i]
    for j in 1...i {
        dp[i] = min(dp[i],dp[i-j] + dp[j])
    }
}
print(dp[n])
