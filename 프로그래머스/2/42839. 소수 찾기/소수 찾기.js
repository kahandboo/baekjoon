function solution(numbers) {
    function getPermutations(arr) {
        function recursion(n, box, visited) {
            if (box.length == n) {
                permutations.push(Number(box.join("")));
                return;
            }
            for (let i=0; i<arr.length; i++) {
                if (!visited[i]) {
                    box.push(arr[i]);
                    visited[i] = true;
                    recursion(n, box, visited);
                    
                    box.pop();
                    visited[i] = false;
                }
            }
        }
        let permutations = [];
        for (let i=1; i<=arr.length; i++) {
            let visited = Array(arr.length).fill(false);
            recursion(i, [], visited);
        }
        
        return permutations;
    }
    
    function isPrime(num) {
        if (num < 2) {
            return false;
        }
        
        for(let i=2; i<=Math.floor(Math.sqrt(num)); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    let nums = numbers.split("");
    let primes = new Set();
    var answer = 0;
    let permutations = getPermutations(nums);
    
    permutations.forEach((permutation) => {
        if (isPrime(permutation) && !primes.has(permutation)) {
            answer++;
            primes.add(permutation);
        }
    });
    
    return answer;
}