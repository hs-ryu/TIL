//
//  lev3_연속펄스부분수열의합.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/03/05.
//

import Foundation

func solution(_ sequence:[Int]) -> Int64 {
    var dpPlus: [Int] = [Int](repeating:0, count:sequence.count)
    var dpMinus: [Int] = [Int](repeating:0, count:sequence.count)
    var flag = 1
    
    dpPlus[0] = sequence[0]
    dpMinus[0] = sequence[0] * (-1)
    
    for i in 1..<sequence.count {
        flag *= -1
        dpPlus[i] = max(dpPlus[i-1] + sequence[i] * flag, sequence[i] * flag)
        dpMinus[i] = max(dpMinus[i-1] + sequence[i] * flag * -1, sequence[i] * flag * -1)
    }
    var answer = Int64(max(dpPlus.max()!,dpMinus.max()!))
    
    return answer
}
