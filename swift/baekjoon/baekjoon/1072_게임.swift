//
//  1072_게임.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/07/09.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
var x = input[0]
var y = input[1]

let z = (y * 100) / x
var result = -1
if z >= 99 {
    print(result)
}
else {
    var l = 0
    var r = 1000000000
    
    while l <= r {
        var m = (l + r) / 2
        var temp = (100 * (y + m)) / (x+m)
        if z >= temp {
            result = m + 1
            l = m + 1
        } else {
            r = m - 1
        }
    }
    print(result)
}
