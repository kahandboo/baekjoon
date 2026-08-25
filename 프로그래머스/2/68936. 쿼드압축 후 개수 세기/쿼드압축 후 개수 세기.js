function solution(arr) {
    let zero_count = 0;
    let one_count = 0;
    
    function isCompressible(rStart, cStart, len) {
        const target = arr[rStart][cStart];

        for (let i=rStart; i < rStart + len; i++) {
            for (let j=cStart; j < cStart + len; j++) {
                if (arr[i][j] !== target) return false;
            }
        }
        return true;
    } 

    function makeQuadTree(rStart, cStart, len) {
        if (isCompressible(rStart, cStart, len)) {
            if (arr[rStart][cStart] == 0) {
                zero_count++;
            } else {
                one_count++;
            }
            
            return;
        } else {
            const half = len / 2;
            makeQuadTree(rStart, cStart, half);
            makeQuadTree(rStart, cStart + half, half);
            makeQuadTree(rStart + half, cStart, half);
            makeQuadTree(rStart + half, cStart + half, half);
        }
    }
    
    makeQuadTree(0, 0, arr.length);
    
    return [zero_count, one_count];
}