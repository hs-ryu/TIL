import Foundation

func solution(_ A: [Int])->Int {
    var lightCount: Int = 0
    var count: Int = 1
    var lastNum: Int = 1

    for num in A {
        if count == num {
            lightCount += 1
            count = lastNum + 1
            lastNum = count
        }
        else if lastNum < num {
            lastNum = num
        }
    }

    return lightCount
}

var x = solution([5,3,2,1,4])
print(x)