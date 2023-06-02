//
//  2740_행렬곱셈.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/02.
//

import Foundation

var matrixA = readLine()!.split(separator: " ").map { Int($0)! }
let n = matrixA[0]
let m = matrixA[1]

var A = [[Int]]()

for _ in 0..<n {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    A.append(row)
}

var matrixB = readLine()!.split(separator: " ").map { Int($0)! }

let k = matrixB[1]
var B = [[Int]]()
for _ in 0..<m {
    let row = readLine()!.split(separator: " ").map { Int($0)! }
    B.append(row)
}

// n = 4, k = 3 -> 4행 3열
var result = [[Int]]()

for p in 0..<n {
    result.append([])
    for i in 0..<k {
        var s = 0
        for j in 0..<m {
            s += A[p][j] * B[j][i]
        }
        result[p].append(s)
    }
}
for i in 0..<result.count {
    print(result[i].map{ String($0) }.joined(separator: " "))
}
