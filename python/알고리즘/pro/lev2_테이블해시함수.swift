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