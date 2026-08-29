function solution(sticker) {
    function findMaxSum(dp, isFirstStickerOff) {
        let start, end;
        
        if (isFirstStickerOff) {
            start = 2;
            end = sticker.length - 1;
            dp[0] = sticker[0];
            dp[1] = sticker[0];
        } else {
            start = 2;
            end = sticker.length;
            dp[1] = sticker[1];
        }
        
        for (let i=start; i<end; i++) {
            dp[i] = Math.max(dp[i-2] + sticker[i], dp[i-1]);
        }
        
        return Math.max(dp[sticker.length - 1], dp[sticker.length - 2]);
    }
    
    if (sticker.length === 1) return sticker[0];
    let answer = Math.max(findMaxSum(new Array(sticker.length).fill(0), false), findMaxSum(new Array(sticker.length).fill(0), true));
    
    return answer;
}