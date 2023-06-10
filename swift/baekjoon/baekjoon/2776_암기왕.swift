//
//  2776_암기왕.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/06/10.
//

import Foundation


let t = Int(readLine()!)!

for _ in 0..<t {
    let n = Int(readLine()!)!
    var book1 = readLine()!.split(separator: " ").map{ Int($0)! }
    let m = Int(readLine()!)!
    let book2 = readLine()!.split(separator: " ").map{ Int($0)! }

    book1.sort(by: { $0 < $1 })

    for i in 0..<m {
        let find = book2[i]
        
        var l = 0
        var r = n
        
        var check = false
        while l < r {
            let middle = (l+r) / 2

            if book1[middle] == find {
                check = true
                break
            }
            
            if find < book1[middle] {
                r = middle - 1
            } else {
                l = middle + 1
            }
        }
        
        if check {
            print(1)
        } else {
            print(0)
        }
        
    }
}
