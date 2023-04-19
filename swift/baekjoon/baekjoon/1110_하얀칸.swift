//
//  1110_하얀칸.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/04/19.
//

import Foundation

var result = 0
for i in 0..<8 {
    var input = Array(readLine()!).map{String($0)}
    // 홀수 줄은 1번이 흰색
    if i % 2 == 1 {
        for j in stride(from: 1, to: 8, by: 2) {
            if input[j] == "F" {
                result += 1
            }
        }
    } else {
        for j in stride(from: 0, to: 8, by: 2) {
            if input[j] == "F" {
                result += 1
            }
        }
    }
}
print(result)
