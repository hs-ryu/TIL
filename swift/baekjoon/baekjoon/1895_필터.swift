//
//  1895_필터.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/03/17.
//

import Foundation

var input = readLine()!.split(separator: " ").map{ Int($0)! }
var (r,c) = (input[0], input[1])

var arr: [[Int]] = []
for _ in 0..<r {
    let row = readLine()!.split(separator: " ").map{ Int($0)! }
    arr.append(row)
}
var t = Int(readLine()!)!

var new_arr: [Int] = []

for i in 0..<r-2{
    for j in 0..<c-2 {
        var temp: [Int] = [arr[i][j], arr[i][j+1], arr[i][j+2], arr[i+1][j], arr[i+1][j+1], arr[i+1][j+2], arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]
        temp.sort()
        new_arr.append(temp[4])
    }
}

var result = 0
for num in new_arr {
    if num >= t {
        result += 1
    }
}
print(result)
