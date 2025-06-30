def solution(genres, plays):
    answer = []
    hashtable1 = {} # 각 장르별 재생수 총합
    hashtable2 = {} # 각 장르별 (고유번호, 재생수)
    for i in range(len(plays)):
        if genres[i] in hashtable2:
            hashtable2[genres[i]].append((i, plays[i]))
            hashtable1[genres[i]] += plays[i]
        else:
            hashtable2[genres[i]] = [(i, plays[i])]
            hashtable1[genres[i]] = plays[i]
            
    sortedhash = sorted(hashtable1.items(), key=lambda item: item[1], reverse=True)
    
    for key, val in sortedhash:
        data = hashtable2[key]
        
        sorted_data = sorted(data, key=lambda x: (-x[1], x[0]))
        
        if len(sorted_data) < 2:
            answer.append(sorted_data[0][0])
        else:
            answer.append(sorted_data[0][0])
            answer.append(sorted_data[1][0])
    
    
    return answer 