//
//  1920_수찾기.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/03/18.
//

import Foundation

let n = Int(readLine()!)
// 그냥 Array로 하면 시간 초과난다. Set으로 O(1)로 잡아준다.
var a = Set(readLine()!.split(separator: " ").map{ Int($0)! })
let m = Int(readLine()!)
var checkList = readLine()!.split(separator: " ").map{ Int($0)! }

for num in checkList {
    if a.contains(num) {
        print(1)
    } else {
        print(0)
    }
}
