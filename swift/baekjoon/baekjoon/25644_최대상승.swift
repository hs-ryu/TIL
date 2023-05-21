//
//  25644_최대상승.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/05/21.
//

import Foundation

var n: Int = Int(readLine()!)!
var a: [Int] = readLine()!.split(separator: " ").map { Int($0)! }

var i = n-1
var j = i-1
var answer = 0
while i >= 0 && j >= 0 {
    if a[i] <= a[j] {
        i = j
        j = i-1
    } else {
        answer = max(answer, a[i]-a[j])
        j -= 1
    }
}

print(answer)
