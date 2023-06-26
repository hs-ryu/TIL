//
//  14889_스타트와링크.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/26.
//

import Foundation

func combi(_ idx: Int, _ a: [Int]) {
    if a.count == n/2 {
        var b:[Int] = []
        
        // 필터로 써도 됨.
        for i in 0..<n {
            if !a.contains(i) {
                b.append(i)
            }
        }
        
        var sumA = 0
        var sumB = 0
        
        for i in 0..<a.count-1 {
            for j in i..<a.count {
                sumA += arr[a[i]][a[j]]
                sumA += arr[a[j]][a[i]]
            }
        }
        
        for i in 0..<b.count-1 {
            for j in i..<b.count {
                sumB += arr[b[i]][b[j]]
                sumB += arr[b[j]][b[i]]
            }
        }
        
        let calc = abs(sumA-sumB)
        
        result = min(result,calc)
        
        return
    }
    
    var newArr:[Int] = a
    for i in idx..<n {
        newArr.append(i)
        combi(i+1, newArr)
        newArr.removeLast()
    }
}


var n: Int = Int(readLine()!)!
var arr = [[Int]]()

// 조합
for _ in 0..<n {
    let temp = readLine()!.split(separator: " ").map{ Int($0)! }
    arr.append(temp)
}

var result = 20000

combi(0, [])

print(result)
