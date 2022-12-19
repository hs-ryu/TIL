import Foundation

func solution(_ topping:[Int]) -> Int {
    var x_cnt = 0
    var y_cnt = 0
    var result = 0
    
    var x_dict = [Int:Int]()
    var y_dict = [Int:Int]()
    
    for i in 0..<topping.count {
        if let y = y_dict[topping[i]] {
            y_dict[topping[i]]! += 1
        } else {
            y_dict[topping[i]] = 1
            y_cnt += 1
        }
    }
    
    for i in 0..<topping.count {
        if let x = x_dict[topping[i]] {
            x_dict[topping[i]]! += 1
        } else {
            x_dict[topping[i]] = 1
            x_cnt += 1
        }
        

        // 딕셔너리에서 key 제거하기 -> removeValue(forKey: ~~)
        // 혹시 기억 안나면??? 해당 키값 nil로 만들어주기. <- 근데 이건 확실할 때만 사용할 수 있을듯.
        if let y = y_dict[topping[i]] {
            y_dict[topping[i]]! -= 1
            if y_dict[topping[i]] == 0 {
                y_dict.removeValue(forKey: topping[i])
                y_cnt -= 1
            }
        }
        
        if x_cnt == y_cnt {
            result += 1
        }
        
    }
    return result
}