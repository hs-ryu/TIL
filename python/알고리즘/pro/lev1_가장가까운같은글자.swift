import Foundation

func solution(_ s:String) -> [Int] {
    var dict = Dictionary<Character, Int>()
    var result = [Int]()
    
    for (index, string) in s.enumerated() {
        if let prevIndex = dict[string] {
            result.append(index-prevIndex)
        } else {
            result.append(-1)
        }
        dict[string] = index
    }
    
    // var dict = [String: Int]() 요론 식도 가능.
    // 딕셔너리에 value에 여러 타입을 넣고 싶으면 Any 타입으로 선언
    // 키값에 Any 타입 집어 넣으면 Hashble 하지 않아 에러남!
    
    return result
}