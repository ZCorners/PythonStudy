# coding=utf-8

# 初始化数据
states_need = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {'kone': set(['id', 'nv', 'ut']),
            'ktwo': set(['wa', 'id', 'mt']),
            'kthree': set(['or', 'nv', 'ca']),
            'kfour': set(['nv', 'ut']),
            'kfive': set(['ca', 'az'])}

final_stations = set()

while states_need:
    best_stations = None
    state_covered = set()
    for station, states in stations.items():
        covered = states_need & states
        if len(covered) > len(state_covered):
            best_stations = station
            state_covered = covered
    final_stations.add(best_stations)
    states_need -= state_covered


print final_stations