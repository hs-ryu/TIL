//
//  15654_N과M.swift
//  baekjoon
//
//  Created by ryu hyunsun on 2023/07/02.
//

// 순열
import Foundation

var input: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
var n: Int = input[0]
var m: Int = input[1]
var nums: [Int] = readLine()!.split(separator: " ").map { Int($0)! }
nums.sort(by: { $0 < $1 })

var check = [Int](repeating: 0, count: n)

func permutation(_ cnt:Int, _ temp: [Int]){
    if cnt == m {
        print(temp.map({ String($0) }).joined(separator: " "))
        return
    }
    var x = temp
    for i in 0..<n{
        if check[i] == 0 {
            check[i] = 1
            x.append(nums[i])
            permutation(cnt+1, x)
            check[i] = 0
            x.removeLast()
        }
    }
}

permutation(0, [])
