//
//  lev1_크기가작은부분문자열.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/15.
//

import Foundation

func solution(_ t:String, _ p:String) -> Int {
    var length = p.count
    var tList = Array(t).map{ String($0) }
    var answer = 0
    for i in 0..<t.count-length+1 {
        var temp = ""
        for j in 0..<length {
            temp += tList[i+j]
        }
        var number = Int(temp)!
        if number <= Int(p)! {
            answer += 1
        }
    }
    
    
    
    return answer
}
