//
//  1660_캡틴이다솜.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/03/16.
//

import Foundation

// dp 문제.
var n = Int(readLine()!)!
var num: Int = 0
var i: Int = 1
var arr: [Int] = []

while n > num {
    num += (i * (i+1)) / 2
    arr.append(num)
    i += 1
}

var dp: [Int] = [Int](repeating: 300001, count: n+1)

for i in 1...n {
    for number in arr {
        if number == i {
            dp[i] = 1
            break
        }
        else if number > i {
            break
        }
        dp[i] = min(dp[i], 1+dp[i-number])
    }
}
print(dp[n])
