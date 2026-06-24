function solution(s) {
    let splitted = s.split(' ');
    let max_num = -Infinity;
    let min_num = Infinity;
    splitted.forEach((str) => {
        let num = Number(str);
        if (num > max_num) {
            max_num = num;
        }
        if (num < min_num) {
            min_num = num;
        }
    });
    
    return min_num.toString() + ' ' + max_num.toString();
}