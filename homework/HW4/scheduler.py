import sys
import copy
import pprint

from scheduling_algos import fcfs, sjf, rr

pp = pprint.PrettyPrinter(indent=4)

processes = {
    1: [0, 5],
    2: [2, 3],
    3: [1, 24]
}


def schedule(processes, algo=fcfs):
    return algo(copy.deepcopy(processes))


def evaluate(scheduled_processes):
    waiting_time = 0
    turnaround_time = 0
    response_time = 0

    for k, v in scheduled_processes.items():
        turnaround_time += v[-1][1]
        response_time += v[0][0]-processes[k][0]
        waiting_time += v[0][0]-processes[k][0]+compute_waiting_time(v)

    print("""
        waiting time: %0.2f
        turnaround time: %0.2f
        response_time: %0.2f
        throughput: %0.2f
        """ % (waiting_time/len(processes), turnaround_time/len(processes), 
        response_time/len(processes), len(scheduled_processes)/len(processes)))


def compute_waiting_time(ll):
    t = 0
    for i in range(len(ll)-1):
        t += ll[i+1][0]-ll[i][1] 
    return t


if __name__=="__main__":
    algorithms = [fcfs, sjf, rr]

    for algo in algorithms:
        print("Algorithm %s" % (algo.__name__))
        result = schedule(processes, algo)
        pp.pprint(result)
        evaluate(result) 
