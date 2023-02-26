//
//  lev1_콜라문제.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/26.
//

import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var result = 0
    var cnt = n
    
    // 심플하게 이렇게 풀 수 도 있지만, 몫으로 연산하는게 훨씬 더 효율적일 것임.
    while cnt >= a {
        cnt -= a
        result += b
        cnt += b
    }
    return result
}
