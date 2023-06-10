//
//  1544_사이클단어.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/10.
//

import Foundation

var n = Int(readLine()!)!

func isCycle(newStr: String) -> Bool {
    for s in answer {
        if s.count == newStr.count && String(s + s).range(of: newStr) != nil {
            return true
        }
    }
    return false
}

var answer = [String]()

for _ in 0..<n {
    let str = readLine()!
    
    if !isCycle(newStr: str) {
        answer.append(str)
    }
}

print(answer.count)
