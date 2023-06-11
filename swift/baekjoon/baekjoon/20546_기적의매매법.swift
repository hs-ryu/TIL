//
//  20546_기적의매매법.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/11.
//

import Foundation

let money = Int(readLine()!)!

let price = readLine()!.split(separator: " ").map {Int($0)!}

var p1m = money
var p2m = money
var p1j = 0
var p2j = 0
var p2arr = [Int]()

for i in 0..<price.count {
    let cost = price[i]
    p1j += p1m/cost
    p1m = p1m%cost
    
    p2arr.append(cost)
    if p2arr.count >= 4 {
        // 3일 연속 하락
        if p2arr[0] > p2arr[1] && p2arr[1] > p2arr[2] {
            p2j += p2m / cost
            p2m = p2m % cost
        } else if p2arr[0] < p2arr[1] && p2arr[1] < p2arr[2] {
            p2m += p2j * cost
            p2j = 0
        }
        p2arr.removeLast()
    }
}


if p1m + price.last! * p1j > p2m + price.last! * p2j {
    print("BNP")
} else if p1m + price.last! * p1j < p2m + price.last! * p2j {
    print("TIMING")
} else {
    print("SAMESAME")
}
