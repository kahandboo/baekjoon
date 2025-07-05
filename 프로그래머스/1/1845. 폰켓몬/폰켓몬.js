function solution(nums) {
    let poketmon = {};
    nums.forEach(n => poketmon[n] = (poketmon[n]||0) + 1);
    let pickPoketmon = nums.length / 2;
    let breedNum = Object.keys(poketmon).length;
    
    if (pickPoketmon > breedNum) return breedNum;
    else return pickPoketmon;
}