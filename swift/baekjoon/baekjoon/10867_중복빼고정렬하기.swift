//
//  10867_중복빼고정렬하기.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/05/22.
//

import Foundation

var n: Int = Int(readLine()!)!
var nums:[Int] = readLine()!.split(separator: " ").map({Int($0)!})

var newNums: [Int] = Array(Set(nums)).sorted(by: { $0 < $1 })

for i in 0..<newNums.count {
    print(newNums[i], terminator: " ")
}
