//
//  1388_바닥장식.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/06.
//

import Foundation


let dr = [-1,1,0,0]
let dc = [0,0,-1,1]

func search(_ i: Int, _ j: Int) {
    var q = [[i,j]]
    if arr[i][j] == "-" {
        while q.count > 0 {
            let temp = q.removeLast()
            let cr = temp[0]
            let cc = temp[1]
            for k in 2..<4 {
                let nc = cc + dc[k]
                if 0 <= nc && nc < m && arr[cr][nc] == "-" {
                    if visited[cr][nc] == 0 {
                        q.append([cr,nc])
                        visited[cr][nc] = 1
                    }
                }
            }
        }
    } else {
        while q.count > 0 {
            let temp = q.removeLast()
            let cr = temp[0]
            let cc = temp[1]
            for k in 0..<2 {
                let nr = cr + dr[k]
                if 0 <= nr && nr < n && arr[nr][cc] == "|" {
                    if visited[nr][cc] == 0 {
                        q.append([nr,cc])
                        visited[nr][cc] = 1
                    }
                    
                }
            }
        }
    }
    result += 1
}



var input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0]
let m = input[1]

var arr = [[Character]]()
var result = 0
for _ in 0..<n {
    let temp = Array(readLine()!)
    arr.append(temp)
}

var visited = [[Int]](repeating: [Int](repeating: 0, count: m), count: n)

for i in 0..<n {
    for j in 0..<m {
        if visited[i][j] == 0 {
            search(i, j)
        }
    }
}

print(result)
