//
//  lev1_삼총사.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/27.
//

import Foundation
// 단순하게, 3중 for문 돌면서 체크해보면 됨.
func solution(_ number:[Int]) -> Int {
    var result = 0
    for i in 0..<number.count-2 {
        for j in i+1..<number.count - 1{
            for k in j+1..<number.count {
                if number[i] + number[j] + number[k] == 0 {
                    result += 1
                }
            }
        }
    }
    return result
}
