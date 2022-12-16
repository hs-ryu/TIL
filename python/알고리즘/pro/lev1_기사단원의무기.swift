import Foundation

// 약수를 확인하는 함수.
// 원래는 절반까지만 반복문을 돌았지만 그것도 필요없다. 제곱근만큼만 돌고
// 그 값으로 다시 체크해주면됨.
func check(x: Int) -> Int {
    var divArr = [Int]()
    for i in 1..<Int(sqrt(Double(x)))+1 {
        if x % i == 0 {
            divArr.append(i)
            var p = pow(Double(i),2)
            if p != Double(x) {
                divArr.append(x / i)
            }
        } 
    }
    
    return divArr.count
}

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    var divArr = [Int]()
    var result = 0
    
    for i in 1..<number+1 {
        let weapon = check(x:i)
        if weapon > limit {
            divArr.append(power)
            result += power
        } else {
            divArr.append(weapon)
            result += weapon
        }
    }
    return result
}