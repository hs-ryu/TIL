import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var list = [String:Int]()
    var result = [Int]()
    var list_detail = [String:[[Int]]]()
    
    for i in 0..<genres.count {
        if let x = list[genres[i]] {
            list[genres[i]]! += plays[i]
            list_detail[genres[i]]!.append([i,plays[i]])
        } else {
            list[genres[i]] = plays[i]
            list_detail[genres[i]] = [[i,plays[i]]]
        }
        
    }
    
    var arrayList = [[Any]]()
    for key in list.keys {
        arrayList.append([key ,list[key]!])
    }
    
    var arr = arrayList.sorted { $0[1] as! Int > $1[1] as! Int }

    for i in 0..<arr.count {
        var temp_genre = arr[i][0]
        var temp_songs = list_detail[temp_genre as! String]!
        temp_songs.sort { $0[1] == $1[1] ? $0[0] < $1[0] : $0[1] > $1[1] }
        result.append(temp_songs[0][0])
        if temp_songs.count > 1 {
            result.append(temp_songs[1][0])
        }
    }
    
    return result
}