function solution(numbers) {
    function compare(a, b) {
        const sa = String(a);
        const sb = String(b);
        
        const case1 = sa+sb;
        const case2 = sb+sa;
        
        if (Number(case1) > Number(case2)) {
            return -1;
        } else if (Number(case1) == Number(case2)){
            return 0;
        } else {
            return 1;
        }
    }
    
    numbers.sort(compare);
    
    var answer = numbers.join('');
    return answer[0] === '0' ? '0' : answer;
}