//
//  15489_파스칼삼각형.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/02/07.
//

import Foundation

var input = readLine()!.split(separator: " ").map{ Int($0)! }

var arr = [[Int]](repeating: [Int](repeating: 1, count: 31), count: 31)
for i in 0..<31{
    for j in 0...i {
        if j-1 >= 0 && i != j {
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        }
    }
}
var result = 0
for i in input[0]-1..<input[0]-1+input[2] {
    for j in input[1]-1..<i-input[0]+input[1]+1 {
        result += arr[i][j]
    }
}
print(result)
