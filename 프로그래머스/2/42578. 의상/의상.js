
function solution(clothes) {
        
    let crib = {};
    for (let i=0; i < clothes.length; i++){
        if (crib.hasOwnProperty(clothes[i][1])) crib[clothes[i][1]].push(clothes[i][0]);
        else crib[clothes[i][1]] = [clothes[i][0]];
    }
    
      let count = 1;
      for (let key in crib) {
        count *= (crib[key].length + 1);
      }
    
    return count - 1;
}