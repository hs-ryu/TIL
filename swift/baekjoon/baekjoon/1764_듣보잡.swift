//
//  1764_듣보잡.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/03/14.
//

import Foundation

var input = readLine()!.split(separator: " ").map{ Int($0)! }
var (n,m) = (input[0],input[1])

var result: [String] = []
var nDic: Set<String> = []
var mDic: Set<String> = []
for _ in 0..<n {
    let s = readLine()!
    nDic.insert(s)
}

for _ in 0..<m {
    let s = readLine()!
    mDic.insert(s)
}

for s in nDic {
    if mDic.contains(s) {
        result.append(s)
    }
}
result.sort(by: {$0 < $1})
print(result.count)
for r in result {
    print(r)
}
