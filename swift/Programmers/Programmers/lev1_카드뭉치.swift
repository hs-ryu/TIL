//
//  lev1_카드뭉치.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/16.
//

import Foundation

func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    var p1 = 0
    var p2 = 0
    var check = true
    
    for i in 0..<goal.count {
        var s1 = cards1[p1]
        var s2 = cards2[p2]
        
        if (s1 == goal[i]) {
            if (p1 < cards1.count-1) {
                p1 += 1
            }
        } else if (s2 == goal[i]) {
            if (p2 < cards2.count-1) {
                p2 += 1
            }
        } else {
            check = false
            break
        }
        
    }
    
    var result = "Yes"
    if (check == false) {
        result = "No"
    }
    
    
    return result
}
