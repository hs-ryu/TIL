//
//  lev2_광물캐기.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/04/18.
//

import Foundation


// 한 곡괭이 당 5개 광물 캘 수 있다. -> 5개씩 끊자. 그러고 다이아, 철, 돌 각각의 피로도를 계산해서 배열에 넣기.
// 근데, 광물의 수가 곡괭이 * 5 보다 많을 수 있으니까, 짤라 줘야함.
// 다 돼면 정렬해서 피로도 높은것 부터 다이아 -> 철 -> 돌 곡괭이를 써서 처리.
func solution(_ picks:[Int], _ minerals:[String]) -> Int {
    
    var i = 0
    var info: [[Int]] = []
    
    var totalPicks = 0
    for cnt in picks {
        totalPicks += cnt
    }
    
    while (i + 5 < minerals.count) {
        // 각각 다이아, 철, 돌로 캤을때
        var temp: [Int] = [0,0,0]
        
        for j in 0..<5 {
            if minerals[i+j] == "diamond" {
                temp[0] += 1
                temp[1] += 5
                temp[2] += 25
            } else if minerals[i+j] == "iron" {
                temp[0] += 1
                temp[1] += 1
                temp[2] += 5
            } else if minerals[i+j] == "stone" {
                temp[0] += 1
                temp[1] += 1
                temp[2] += 1
            }
        }
        info.append(temp)
        i += 5
    }
    if i != minerals.count {
        var temp: [Int] = [0,0,0]
        for k in i..<minerals.count {
            if minerals[k] == "diamond" {
                temp[0] += 1
                temp[1] += 5
                temp[2] += 25
            } else if minerals[k] == "iron" {
                temp[0] += 1
                temp[1] += 1
                temp[2] += 5
            } else if minerals[k] == "stone" {
                temp[0] += 1
                temp[1] += 1
                temp[2] += 1
            }
        }
        info.append(temp)
    }
    
    while totalPicks < info.count {
        info.removeLast()
    }
    info.sort{($0[2], $0[1], $0[0]) > ($1[2], $1[1], $1[0])}
    
    
    var result = 0
    var t = picks
    for i in 0..<info.count {
        if t[0] != 0 {
            result += info[i][0]
            t[0] -= 1
        } else if t[1] != 0 {
            result += info[i][1]
            t[1] -= 1
        } else if t[2] != 0 {
            result += info[i][2]
            t[2] -= 1
        }
    }
    
    return result
}
