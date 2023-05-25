//
//  25497_기술연계마스터임스.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/05/25.
//

import Foundation

var n: Int = Int(readLine()!)!
var stack:[Character] = []
var str:[Character] = Array(readLine()!)
var answer = 0
for i in 0..<str.count {
    var temp = str[i]
    
    if temp == "L" {
        stack.append(contentsOf: "L")
    } else if temp == "S" {
        stack.append(contentsOf: "S")
    } else if temp == "R" {
        var x = stack.popLast()
        if let p = x {
            if p == "L" {
                answer += 1
            }
        }
    } else if temp == "K" {
        var x = stack.popLast()
        if let p = x {
            if p == "S" {
                answer += 1
            }
        }
    } else {
        answer += 1
    }
}
print(answer)
