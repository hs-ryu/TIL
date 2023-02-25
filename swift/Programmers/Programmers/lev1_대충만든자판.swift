//
//  lev1_대충만든자판.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/25.
//

import Foundation

func solution(_ keymap:[String], _ targets:[String]) -> [Int] {
    var x = [Character:Int]()
    var answer = [Int]()
    for i in 0..<keymap.count {
        var temp = Array(keymap[i])
        for j in 0..<temp.count {
            if let s = x[temp[j]] {
                if s > j {
                    x[temp[j]] = j
                }
            } else {
                x[temp[j]] = j
            }
        }
    }
    
    for i in 0..<targets.count {
        var temp = Array(targets[i])
        var cnt = 0
        
        for j in 0..<temp.count {
            if let s = x[temp[j]] {
                cnt += s+1
            } else {
                cnt = -1
                break
            }
        }
        answer.append(cnt)
    }
    
    
    return answer
}
