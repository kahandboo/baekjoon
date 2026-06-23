function solution(priorities, location) {
    let queue = [];
    let answer = 1;
    priorities.forEach((priority, idx) => {
        queue.push([priority, idx]);
    });
    
    while (true) {
        let [val, idx] = queue.shift();
        const hasBiggerVal = queue.some(q => q[0] > val);
        
        if (hasBiggerVal) {
            queue.push([val, idx]);
        } else {
            if (idx == location) {
                return answer;
            }
            answer += 1;
        }
    }
}