//
//  23827_수열.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/05/23.
//

import Foundation

var n = Int(readLine()!)!
var a:[Int] = readLine()!.split(separator: " ").map { Int($0)! }

var total:Int = a.reduce(0){ $0 + $1 }
var result = 0
for i in 0..<n {
    total -= a[i]
    result += total * a[i] % 1000000007
}
print(result % 1000000007)
