//
//  lev2_당구연습.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/04/23.
//

import Foundation

func solution(_ m:Int, _ n:Int, _ startX:Int, _ startY:Int, _ balls:[[Int]]) -> [Int] {
    var answer: [Int] = []
    for ball in balls {
        
        var result = 0
        var dX = startX-ball[0]
        var dY = startY-ball[1]
        // 각각의 쿠션
        var l = pow(Float((startX + ball[0])),2) + pow(Float(dY),2)
        var r = pow(Float((m - startX + m - ball[0])),2) + pow(Float(dY),2)
        var t = pow(Float(dX),2) + pow(Float((n - startY + n - ball[1])),2)
        var b = pow(Float(dX),2) + pow(Float((startY + ball[1])),2)
        // print(l,r,t,b)
        
        // 근데, 이거 바로 비교하면 안되고, 벽에 맞기 전에 공에 먼저 맞는 경우가 있으니 고려해줘야함.
        // dX가 같을때, 즉 Y 축으로 같은 선상일 때
        if dX == 0 {
            // 시작 공이 목표 Y보다 크다면 -> 아래 쿠션 안된다.
            if dY > 0 {
                result = [Int(l),Int(r),Int(t)].min()!
            } else {
                result = [Int(l),Int(r),Int(b)].min()!
            }
        } else if dY == 0 {
            if dX > 0 {
                result = [Int(r),Int(t),Int(b)].min()!
            } else {
                result = [Int(l),Int(t),Int(b)].min()!
            }
        } else {
            result = [Int(r),Int(l),Int(t),Int(b)].min()!
        }
        answer.append(result)
    }
    return answer
}
