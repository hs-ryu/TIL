import Foundation

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    // DFS 재귀.
    var result = 51
    func DFS(_ start: String, _ visited: [Int], _ cnt: Int) {
        // 현재 단어와 찾는 단어가 동일하면 result 갱신
        if start == target {
            if cnt < result {
                result = cnt
            }
            return
        }
        
        // 배열 한번 복사해서 쓰기. 귀찮.
        var visited = visited
        // words 배열에서 단어 하나씩 빼와서 비교
        for i in 0..<words.count {
            if visited[i] == 1 {
                continue
            }
            let tempWord = words[i]
            var diffCnt = 0
            for j in 0..<tempWord.count {
                let char = tempWord[tempWord.index(tempWord.startIndex, offsetBy: j)]
                let startChar = start[start.index(start.startIndex, offsetBy: j)]
                if startChar != char {
                    diffCnt += 1
                    if diffCnt == 2 {
                        break
                    }
                }
            }
            // 한 단어만 다르면 재귀 돌리고~
            if diffCnt != 2 {
                visited[i] = 1
                DFS(tempWord, visited, cnt + 1)
                visited[i] = 0
            }
        }
    }
    
    // 찾고자 하는 target이 words에 없으면 바로 0 리턴
    if !words.contains(target) {
        return 0
    }
    
    var visited = [Int](repeating:0, count: words.count)
    
    DFS(begin, visited, 0)

    return result
}