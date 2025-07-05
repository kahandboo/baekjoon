function solution(participant, completion) {
    dupcheck = {};
    participant.forEach(num => dupcheck[num] = (dupcheck[num] || 0) + 1);
    completion.forEach(n => dupcheck[n]--);
    
    const answer = Object.keys(dupcheck).find(name => dupcheck[name] > 0);
    return answer;
}