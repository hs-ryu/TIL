//
//  2485_가로수.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/10.
//

import Foundation

func findGCD(_ x: Int, _ y: Int) -> Int {
    if (y == 0) {
        return x
    } else {
        return findGCD(y, x % y)
    }
}

let n = Int(readLine()!)!

var trees=[Int]()

for _ in 0..<n {
    trees.append(Int(readLine()!)!)
}

var arr = [Int]()
for i in 1..<n {
    arr.append(trees[i]-trees[i-1])
}

var gcm = arr[0]

for i in 1..<arr.count {
    gcm = findGCD(gcm, arr[i])
}

var answer = 0
for a in arr {
    answer += (a / gcm) - 1
}
print(answer)
