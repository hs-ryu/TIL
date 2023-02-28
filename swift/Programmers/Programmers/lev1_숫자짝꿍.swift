//
//  lev1_숫자짝꿍.swift
//  Programmers
//
//  Created by ryu hyunsun on 2023/02/28.
//

import Foundation

func solution(_ X:String, _ Y:String) -> String {
    var xDic = [String:Int]()
    var xList = Array(X)
    for i in 0..<xList.count {
        if let k = xDic[String(xList[i])] {
            xDic[String(xList[i])]! += 1
        } else {
            xDic[String(xList[i])] = 1
        }
    }
    
    var yDic = [String:Int]()
    var yList = Array(Y)
    for i in 0..<yList.count {
        if let k = yDic[String(yList[i])] {
            yDic[String(yList[i])]! += 1
        } else {
            yDic[String(yList[i])] = 1
        }
    }
    
    var result: [String] = []
    // 공통 찾기. x,y중 하나만 하면 됨.
    for x in xDic {
        var cnt = 0
        if let yValue = yDic[x.key] {
            if x.value >= yValue {
                cnt = yValue
            } else {
                cnt = x.value
            }
        }
        for i in 0..<cnt {
            result.append(x.key)
        }
    }
    // 여기서 result가 비어있으면 걸러내는데? 왜 인덱싱 에러가 뜨는걸까. 자릿수.....? x,y의 길이가 너무 길어서?
    if result.isEmpty {
        return "-1"
    }
    
    var answer = ""
    result.sort(by: { Int64($0)! > Int64($1)! })
    // 공통 찾아서 sort 해버리기
    // 그 담에 합치기.
    for i in 0..<result.count {
        answer.append(result[i])
    }
    
    return String(Int64(answer)!)
}
