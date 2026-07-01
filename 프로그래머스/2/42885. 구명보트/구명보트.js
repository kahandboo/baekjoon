function solution(people, limit) {
    var answer = 0;
    people.sort((a, b) => a - b);
    let left = 0;
    let right = people.length - 1;
    
    while (left <= right) {
        let lightPerson = people[left];
        let heavyPerson = people[right];
        let totalWeight = lightPerson + heavyPerson;
        
        if (totalWeight <= limit) {
            left++;
            right--;
        } else {
            right--;
        }
        answer += 1;
    }
    return answer;
}