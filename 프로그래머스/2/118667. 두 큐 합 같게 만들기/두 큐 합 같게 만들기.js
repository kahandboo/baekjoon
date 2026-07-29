function solution(queue1, queue2) {
    let q1sum = queue1.reduce((sum, cur) => sum + cur, 0);
    let q2sum = queue2.reduce((sum, cur) => sum + cur, 0);
    let totalSum = q1sum + q2sum;
    let goal = totalSum / 2;
    
    if (!Number.isInteger(goal)) {
        return -1;
    }
    
    let count = 0;
    let q1idx, q2idx;
    let q1len = queue1.length;
    
    q1idx = q2idx = 0;
    
    while (q1sum != q2sum) {
        if (count > q1len * 3) return -1;
        
        if (q1sum > q2sum) {
            let popped = queue1[q1idx];
            queue2.push(popped);
            q1sum -= popped;
            q2sum += popped;
            
            q1idx++;
        } else {
            let popped = queue2[q2idx];
            queue1.push(popped);
            q1sum += popped;
            q2sum -= popped;
            
            q2idx++;
        }
        count++;
    }
    
    return count;
}