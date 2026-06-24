function solution(s) {
    let splitted = s.split(' '); 
    let answer = [];
    
    for (const str of splitted) {
        if (str === '') {
            answer.push('');
            continue;
        }
        
        let changedStr = '';
        const isAlphabet = /^[a-zA-Z]+$/.test(str[0]);
        
        if (isAlphabet) {
            changedStr += str[0].toUpperCase();
            changedStr += str.slice(1).toLowerCase();
        } else {
            changedStr += str.toLowerCase();
        }
        
        answer.push(changedStr);
    }
    
    return answer.join(' ');
}