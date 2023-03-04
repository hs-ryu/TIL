//
//  lev2_덧칠하기.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/03/04.
//

import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {
    var answer = 0
    var painted = 0
    for i in 0..<section.count {
        if section[i] > painted {
            painted = section[i] + m - 1
            answer += 1
        }
    }
    
    
    return answer
}
