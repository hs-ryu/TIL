//
//  1049_기타줄.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/01.
//

import Foundation

var input = readLine()!.split(separator: " ").map { Int($0)! }
var n = input[0]
var m = input[1]

var package = [Int]()
var single = [Int]()
for _ in 0..<m {
    let info = readLine()!.split(separator: " ").map{ Int($0)! }
    package.append(info[0])
    single.append(info[1])
}

var l1 = package.sorted(by: { $0 < $1 })[0]
var l2 = single.sorted(by: { $0 < $1 })[0]

var answer = 0
// 패키지가 더 비쌀때
if l1 > l2 * 6 {
    answer = l2 * n
} else {
    // 패키지가 더 싸면
    answer += (n / 6) * l1
    let mod = n % 6
    if mod * l2 > l1 {
        answer += l1
    } else {
        answer += mod * l2
    }
    
}

print(answer)
