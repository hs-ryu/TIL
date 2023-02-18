//
//  lev2_숫자변환하기.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/17.
//

import Foundation
// dp? BFS?
// 아래처럼 풀면 시간초과 난다. 적당한 조건으로 추가하지 말아야할듯?
func solution(_ x:Int, _ y:Int, _ n:Int) -> Int {
    var q = [[Int]]()
    
    q.append([x,0])
    
    var result = -1
    while q.count > 0 {
        var temp = q.removeFirst()
        var v = temp[0]
        var c = temp[1]
        
        if v == y {
            result = c
            break
        }
        
        if v * 2 <= y {
            q.append([v * 2, c + 1])
        }
        if v * 3 <= y {
            q.append([v * 3, c + 1])
        }
        if v + n <= y {
            q.append([v + n, c + 1])
        }
    }
    
    return result
}


import Foundation
// 얘도 시간초과.
func solution(_ x:Int, _ y:Int, _ n:Int) -> Int {
    var q = [[Int]]()
    var visited = [Int](repeating:0, count:100000000)
    q.append([x,0])
    
    var result = -1
    while q.count > 0 {
        var temp = q.removeFirst()
        var v = temp[0]
        var c = temp[1]
        
        if v == y {
            result = c
            break
        }
        
        if v * 2 <= y && visited[v * 2] == 0 {
            visited[v * 2] = 1
            q.append([v * 2, c + 1])
        }
        if v * 3 <= y && visited[v * 3] == 0 {
            visited[v * 2] = 1
            q.append([v * 3, c + 1])
        }
        if v + n <= y && visited[v + n] == 0 {
            visited[v * 2] = 1
            q.append([v + n, c + 1])
        }
    }
    
    return result
}
