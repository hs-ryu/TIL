//
//  lev1_바탕화면정리.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/03/03.
//

import Foundation

func solution(_ wallpaper:[String]) -> [Int] {
    var l: Int = 51
    var t: Int = 51
    var r: Int = 0
    var b: Int = 0
    var answer: [Int] = []
    for i in 0..<wallpaper.count {
        var row = Array(wallpaper[i])
        for j in 0..<row.count {
            if row[j] == "#" {
                // 여기서 각 좌표를 확인해준다.
                // i는 t,b. j는 r,l을 확인한다.
                if i + 1 > b {
                    b = i+1
                }
                if j + 1 > r {
                    r = j + 1
                }
                if i < t {
                    t = i
                }
                if j < l {
                    l = j
                }
                answer = [t,l,b,r]
            }
        }
    }
    return answer
}
