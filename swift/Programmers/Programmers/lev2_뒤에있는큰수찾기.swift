//
//  lev2_뒤에있는큰수찾기.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/14.
//

import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var answer = [Int](repeating: -1, count: numbers.count)
    var stack = [Int]()
    for i in 0..<numbers.count {
        
        while stack.count != 0  && numbers[stack.last!] < numbers[i] {
            var temp = stack.removeLast()
            answer[temp] = numbers[i]
        }
        stack.append(i)
    }
    return answer
}
