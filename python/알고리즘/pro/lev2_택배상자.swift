import Foundation

func solution(_ order:[Int]) -> Int {
    var result = 0
    var now = 1
    var i = 0
    var stack = [Int]()
    let length = order.count
    while i < length {
        // 현재 보고 있는 수가 해당 순서와 같다면
        if now == order[i] {
            result += 1
            i += 1
            now += 1
        } else {
            // stack에서 일단 확인해야한다.
            if stack.count != 0 {
                // 배열.last 는 옵셔널 값을 반환한다. 옵셔널 바인딩 해줘야한다.
                if stack.last! == order[i] {
                    stack.removeLast()
                    result += 1
                    i += 1
                } else {
                    // stack의 끝이랑 다르면? stack에 추가.
                    if now >= length {
                        break
                    }
                    stack.append(now)
                    now += 1
                }
            } else {
                stack.append(now)
                now += 1
            }
        }
    }
    return result
}


// 리펙토링
func solution(_ order:[Int]) -> Int {
    var idx = 0
    var stack = [Int]()
    // 그냥 아싸리 스택에 무조건 다 집어넣고. 빼면서 확인하면 된다.
    for i in 1...order.count {
        stack.append(i)

        while !stack.isEmpty {
            if stack.last! == order[idx] {
                stack.removeLast()
                idx += 1
                continue
            }
            break
        }
    }

    return idx
}