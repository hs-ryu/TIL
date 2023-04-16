//
//  lev1_공원산책.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/04/16.
//

import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
    let dr = [-1,1,0,0]
    let dc = [0,0,-1,1]
    
    func findDirection (_ d: String) -> Int {
        switch d {
            case "N": return 0
            case "S": return 1
            case "W": return 2
            case "E": return 3
            default: return 0
        }
    }
    
    func move(_ sr: Int, _ sc: Int) -> [Int]{
        var cr = sr
        var cc = sc
        // 돌면서 갈 수 있는지 확인한다.
        for i in 0..<routes.count {
            var command = routes[i].split(separator:" ")
            var d = findDirection(String(command[0]))
            var cnt = Int(command[1])!
            var tempR = cr
            var tempC = cc
            var goFlag = true
            
            for _ in 1...cnt {
                var nr = tempR + dr[d]
                var nc = tempC + dc[d]
                if 0 <= nr && nr < arr.count && 0 <= nc && nc < arr[0].count && arr[nr][nc] != "X" {
                    tempR = nr
                    tempC = nc
                } else {
                    goFlag = false
                    break
                }
            }
            
            if goFlag == true {
                cr = tempR
                cc = tempC
            }
        }
        return [cr,cc]
    }
    
    // 배열을 내가 조작하기 쉽도록 변환한다. 인덱싱 용이하도록
    var arr: [[String]] = []
    for i in 0..<park.count {
        let temp = park[i]
        let str = temp.map { String($0) }
        arr.append(str)
    }
    
    var sr:Int = 0
    var sc:Int = 0
    for i in 0..<arr.count {
        for j in 0..<arr[i].count {
            if arr[i][j] == "S" {
                sr = i
                sc = j
                break
            }
        }
    }
    var answer = move(sr,sc)
    
    return answer
}
