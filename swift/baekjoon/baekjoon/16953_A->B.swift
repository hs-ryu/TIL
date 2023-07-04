//
//  16953_A->B.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/07/04.
//

import Foundation

func bfs(_ x: Int) -> Int {
    
    var q = [[x,0]]
    var result = -1
    while q.count != 0 {
        var temp = q.removeLast()
        if temp[0] * 2 == b || Int(String(temp[0]) + "1")! == b {
            result = temp[1] + 2
            break
        }
        
        if temp[0] * 2 < b {
            q.append([temp[0]*2,temp[1]+1])
        }
        let st = String(temp[0]) + "1"
        if Int(st)! < b {
            q.append([Int(st)!, temp[1]+1])
        }
        
    }
    return result
    
}


var input = readLine()!.split(separator: " ").map{ Int($0)! }
let a = input[0]
let b = input[1]

var result = bfs(a)
print(result)
