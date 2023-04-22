//
//  lev2_두원사이의정수쌍.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/04/22.
//

import Foundation

func solution(_ r1:Int, _ r2:Int) -> Int64 {
    var answer = 0
    // 최소, 최대로 가질 수 있는 Y 좌표
    var minY = r1
    var maxY = r2
    
    // 1사분면만 계산
    for i in 0..<r2 {
        while pow(Decimal(r2),2) < pow(Decimal(maxY),2) + pow(Decimal(i),2) {
            maxY -= 1
        }
        while minY-1 != 0 && pow(Decimal(r1),2) <= pow(Decimal((minY-1)),2) + pow(Decimal(i),2){
            minY -= 1
        }
        
        answer += (maxY-minY) + 1
    }
    
    
    
    return Int64(answer * 4)
}
