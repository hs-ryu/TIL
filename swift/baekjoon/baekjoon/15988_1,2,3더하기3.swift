//
//  15988_1,2,3더하기3.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/07/07.
//

import Foundation
// n = 0: 0
// n = 1: 0
// n = 2: 1
// n = 3: 3
// n = 4: 7
// n = 5: 11111, 1112, 1121,1211,2111, 113, 131, 311, 14, 41, 122, 212, 221, 23, 32: 15
// n = 6: 31
// n = 7: 45
// n = 10: 274
let t = Int(readLine()!)!
for _ in 0..<t {
    let n = Int(readLine()!)!
    
    var dp = [Int](repeating: 0, count: n+1)
    for i in 1...n {
        let decimal = pow(2, i-1)
        dp[i] = (decimal as NSDecimalNumber).intValue % 1000000009
    }
    print(dp[n])
}
