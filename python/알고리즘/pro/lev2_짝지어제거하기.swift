import Foundation

func solution(_ s:String) -> Int{
    var answer:Int = -1

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    var i = 0
    var sArray = Array(s)
    var stack = [Character]()
    while i < sArray.count {
        if stack.count != 0 {
            // last로 마지막 놈을 가져오거나
            // endIndex - 1로 인덱싱 하거나
            // count - 1로 인덱싱 하거나
            if stack.last! == sArray[i] {
                stack.removeLast()
            } else {
                stack.append(sArray[i])
            }
        } else {
            stack.append(sArray[i])
        }
        i += 1
    }
    if stack.count == 0 {
        answer = 1
    } else {
        answer = 0
    }

    return answer
}