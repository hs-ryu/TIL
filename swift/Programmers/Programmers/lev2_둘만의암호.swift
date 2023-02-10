//
//  lev2_둘만의암호.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/10.
//

import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    
    var answer = ""
    var s_list = s.map { String($0) }
    var skip_list = skip.map{ String($0) }
    var skip_set = Set<Int>()
    for x in skip_list {
        skip_set.insert(Int(UnicodeScalar(x)!.value))
    }
    // 문자 -> 아스키코드 변환
    // print(Int(UnicodeScalar("a").value))
    // 아스키코드 -> 문자로 변환
    // print(String(UnicodeScalar(65)))
    for i in 0..<s.count {
        var temp = Int(UnicodeScalar(s_list[i])!.value)
        var k = 0
        while k < index {
            if !skip_set.contains(temp) {
                k += 1
            }
            temp += 1
            if temp == 123 {
                temp = 97
            }
        }
        var new_str = String(UnicodeScalar(temp)!)
        answer += new_str
    }
    
    
    return answer
}
