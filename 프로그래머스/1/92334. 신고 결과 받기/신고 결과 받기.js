function solution(id_list, report, k) {
    let idObject = {};
    let nugutonugu = {};
    id_list.forEach((id) => {
        idObject[id] = 0;
        nugutonugu[id] = new Set();
    });

    report.forEach(entry => {
        let [reporter, reported] = entry.split(" ");

        if (!nugutonugu[reporter].has(reported)) {
            nugutonugu[reporter].add(reported);
            idObject[reported] += 1;
        }
    });
    
    let stopped = [];
    for (let id in idObject) {
        if (idObject[id] >= k) {
            stopped.push(id);
        }
    }

    let answer = id_list.map(user => {
        let count = 0;
        stopped.forEach(s => {
            if (nugutonugu[user].has(s)) count += 1;
        });
        return count;
    });

    return answer;
}