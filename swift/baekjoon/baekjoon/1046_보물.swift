//
//  1046_보물.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/14.
//

import Foundation

var n = Int(readLine()!)!
var a = readLine()!.split(separator: " ").map { Int($0)! }
var b = readLine()!.split(separator: " ").map { Int($0)! }

a.sort(by: {$0 < $1})
b.sort(by: {$0 > $1})

var answer = 0
for i in 0..<n {
    answer += a[i] * b[i]
}
print(answer)
