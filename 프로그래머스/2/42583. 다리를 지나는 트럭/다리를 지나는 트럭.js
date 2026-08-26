function solution(bridge_length, weight, truck_weights) {
    let second = 0;
    let bridge = new Array(bridge_length).fill(0);
    let idx = 0;
    let current_weight = 0;
    
    while (idx < truck_weights.length) {
        second++;
        current_weight -= bridge.shift();
        
        let truck = truck_weights[idx];
        if (idx < truck_weights.length && current_weight + truck <= weight) {
            current_weight += truck;
            bridge.push(truck);
            idx++;
        } else {
            bridge.push(0);
        }
    }
    
    let bridge_idx = bridge.length - 1;
    while (bridge[bridge_idx] == 0 && bridge_idx >= 0) {
        bridge_idx--;
    }
    
    second += bridge_idx + 1;
    
    return second;
}