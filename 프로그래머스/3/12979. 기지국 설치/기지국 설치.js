function solution(n, stations, w) {
    var answer = 0;
    let idx = 1;    
    
    for (let station of stations) {        
        let empty = station - idx - w;
        idx = station + w + 1;
        if (empty < 1) {
            continue;
        }
        
        answer += Math.ceil(empty/(2*w+1));
    }
    
    
    if (idx <= n) {
        let empty = n - idx + 1;
        answer += Math.ceil(empty/(2*w+1));
    }

    return answer;
}