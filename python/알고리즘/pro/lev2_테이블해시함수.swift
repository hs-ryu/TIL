import Foundation

func solution(_ data:[[Int]], _ col:Int, _ row_begin:Int, _ row_end:Int) -> Int {
    var result = 0
    // 구체적이지만 너무 길다. 좀 더 짧게하는 방법은 없나?
    let x = data.sorted{ (a, b) -> Bool in 
        if a[col-1] == b[col-1] { return a[0] > b[0] }
        return a[col-1] < b[col-1]
    }
    var arr = [Int]()
    for i in row_begin...row_end {
        var temp = 0
        for j in 0..<x[i-1].count {
            temp += x[i-1][j] % i
        }
        arr.append(temp)
    }
    
    // 정수값에서 바로 XOR 연산 되는거. 
    result = arr[0]
    for i in 1..<arr.count {
        result ^= arr[i]
    }
    
    return result
}


// 다른 사람의 풀이

import Foundation

func solution(_ data:[[Int]], _ col:Int, _ row_begin:Int, _ row_end:Int) -> Int {
    // 조건 2가지일때 -> 3항 연산자. 이거 괜찮네.
    var data = data.sorted { $0[col-1] == $1[col-1] ? $0[0] > $1[0] : $0[col-1] < $1[col-1] }
    var numbers = [Int]()
    // 맵 함수로 배열 다시 만들어 주고 -> reduce로 합쳐주고 numbers에 넣어주기.
    for mod in row_begin-1...row_end-1 { numbers.append(data[mod].map { $0 % (mod + 1) }.reduce(0, +)) }
    // reduce 함수에 바로 xor해주는거. 넘 좋다.
    return numbers.reduce(0, ^)
}
