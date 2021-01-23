def solution(bridge_length, weight, truck_weights):
    bridgetruck = 0
    sec = 0
    bridgetimer = []
    while len(bridgetimer) !=0 or len(truck_weights) !=0:
            for j in range(len(bridgetimer)):
                bridgetimer[j][1] -= 1
            if len(bridgetimer) > 0 and bridgetimer[0][1] == 0:
                bridgetruck -= bridgetimer[0][0]
                del bridgetimer[0]
            if(len(truck_weights) > 0 and bridgetruck + truck_weights[0] <= weight):
                bridgetruck += truck_weights[0]
                bridgetimer.append([truck_weights[0], bridge_length])
                del truck_weights[0]
            sec +=1
            
    return sec