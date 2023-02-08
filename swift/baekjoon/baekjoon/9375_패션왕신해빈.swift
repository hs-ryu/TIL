//
//  9375_패션왕신해빈.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/02/08.
//

import Foundation

var t = Int(readLine()!)!

for _ in 0..<t {
    var n = Int(readLine()!)!
    var info = [String: Set<String>]()
    for _ in 0..<n {
        var input = readLine()!.split(separator: " ").map { String($0) }
        if let x = info[input[1]] {
            info[input[1]]?.insert(input[0])
        } else {
            info[input[1]] = Set(arrayLiteral: input[0])
        }
    }
    
    var result = 1
    
    for key in info.keys {
        let x = info[key]?.count
        result *= (x! + 1)
    }
    print(result - 1)
    
}
