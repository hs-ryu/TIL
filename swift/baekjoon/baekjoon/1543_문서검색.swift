//
//  1543_문서검색.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/03/10.
//

import Foundation

var s = readLine()!
var target = readLine()!

var cnt = 0
var index = 0

// 찾고자 하는 문자열의 길이가 주어진 문자열 길이보다 길 때가있다. 이 부분 고려 안해줘서 런타임 에러 떠서 한참 고민했따. 문제 조건을 잘 읽어보자
if target.count > s.count {
    print(0)
} else {
    for i in 0...s.count-target.count {
        if index > i {
            continue
        }
        
        let start = s.index(s.startIndex, offsetBy: i)
        let end = s.index(start, offsetBy: target.count-1)

        if target == s[start...end] {
            cnt += 1
            index = i + target.count
        }
    }
    print(cnt)
}

