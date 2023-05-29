//
//  25497_기술연계마스터임스.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/05/25.
//

import Foundation

var n: Int = Int(readLine()!)!
var str:[Character] = Array(readLine()!)
var lCnt = 0
var sCnt = 0
var answer = 0
for i in 0..<str.count {
    var temp = str[i]
    if temp == "L" {
        lCnt += 1
    } else if temp == "S" {
        sCnt += 1
    } else if temp == "R" {
        if lCnt > 0 {
            answer += 1
            lCnt -= 1
        } else {
            break
        }
    } else if temp == "K" {
        if sCnt > 0 {
            answer += 1
            sCnt -= 1
        } else {
            break
        }
    } else {
        answer += 1
    }
    
}
print(answer)
