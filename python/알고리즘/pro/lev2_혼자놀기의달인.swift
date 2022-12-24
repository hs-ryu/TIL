import Foundation

func solution(_ cards:[Int]) -> Int {
    var result = [[Int]]()
    var visited = [Int](repeating: 0, count: cards.count)
    
    for i in 0..<cards.count {
        if visited[cards[i]-1] == 0 {
            var temp = Set<Int>()
            var nextCard = cards[i]
            while visited[nextCard-1] == 0 {
                visited[nextCard-1] = 1
                if temp.contains(nextCard) {
                    break
                }
                temp.insert(nextCard)
                nextCard = cards[nextCard-1]
            }
            var tempArray = Array(temp)
            result.append(tempArray)
        }
    }
    result.sort { $0.count > $1.count }

    return result.count > 1 ? result[0].count * result[1].count : 0
}