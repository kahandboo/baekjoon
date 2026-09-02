function solution(storey) {
    let answer = 0;
    const string = String(storey);
    let carry = false;
    
    for (let i=string.length - 1; i>=0; i--) {
        let curr_string = Number(string[i]);
        
        if (carry) {
            curr_string += 1;
            carry = false;
        }
        
        if (curr_string > 5) {
            carry = true;
            answer += 10 - curr_string;
        } else if (curr_string < 5) {
            answer += curr_string;
        } else {
            answer += curr_string;
            
            if (i>0) {
                let next_string = Number(string[i-1]);
                
                if (next_string >= 5) {
                    carry = true;
                }
            }
        }        
    }
    
    if (carry) {
        answer += 1;
    }
    
    return answer;
}