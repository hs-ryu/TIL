//
//  lev2_무인도여행.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/09.
//

import Foundation
// BFS !
func solution(_ maps:[String]) -> [Int] {
    let dr = [-1,1,0,0]
    let dc = [0,0,-1,1]
    
    func BFS(_ r: Int , _ c: Int) -> Int {
        var cnt = Int(newMaps[r][c])!
        var q = [[r,c]]
        while q.count != 0 {
            let temp = q.removeLast()
            let cr = temp[0]
            let cc = temp[1]
            for i in 0..<4 {
                let nr = cr + dr[i]
                let nc = cc + dc[i]
                if (0 <= nr && nr < maps.count ) && (0 <= nc && nc < maps[0].count) {
                    if visited[nr][nc] == 0 && newMaps[nr][nc] != "X"{
                        visited[nr][nc] = 1
                        cnt += Int(newMaps[nr][nc])!
                        q.append([nr,nc])
                    }
                }
            }
        }
        return cnt
    }
    
    var visited = [[Int]](repeating: [Int](repeating: 0,count:maps[0].count), count: maps.count)
    var newMaps = [[String]]()
    for i in 0..<maps.count {
        var x = maps[i].map{String($0)}
        newMaps.append(x)
    }
    var answer = [Int]()
    for i in 0..<maps.count {
        for j in 0..<maps[0].count {
            if visited[i][j] == 0 && newMaps[i][j] != "X"{
                visited[i][j] = 1
                let x = BFS(i,j)
                answer.append(x)
            }
        }
    }
    if answer.count == 0 {
        answer.append(-1)
    } else {
        answer.sort()
    }
    
    return answer
}
