function solution(number, k) {
    let stack = [];
    
    for (let i=0; i<number.length; i++) {
        
        let curr = number[i];
        if (stack.length === 0) {
            stack.push(curr);
            continue;
        }
        
        while (stack.at(-1) < curr && k > 0) {
            stack.pop();
            k--;
        }
        
        stack.push(curr);
    }
    
    while (k > 0) {
        stack.pop();
        k--;
    }
    
    return stack.join('');
}