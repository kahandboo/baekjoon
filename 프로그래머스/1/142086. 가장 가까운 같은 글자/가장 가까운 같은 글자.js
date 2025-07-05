function solution(s) {
    let arr = s.split("");
    let answer = [];
    let dict = {};
    arr.forEach((str, idx) => {
        if (dict.hasOwnProperty(str)) {
            answer.push(idx - dict[str]);
            dict[str] = idx;
        }
        else {
            answer.push(-1)
            dict[str] = idx
        } 
    })

    return answer;
}