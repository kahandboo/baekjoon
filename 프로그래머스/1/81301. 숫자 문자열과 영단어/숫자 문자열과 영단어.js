function solution(s) {
    
    let strToNum = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    };
    
    for (let key in strToNum) {
        s = s.replaceAll(key, strToNum[key]);
        }
    return Number(s);
}