import math
import random


# Initial conditions
def init():
    mc = 0
    rt_clock = 3
    non_rt_clock = 5
    n_rt = 0
    n_non_rt = 0
    server_status = 2
    scl = 4
    print(f"{mc}\t{rt_clock}\t{non_rt_clock}\t{n_rt}\t{n_non_rt}\t{scl}\t{server_status}")
    return mc, rt_clock, non_rt_clock, n_rt, n_non_rt, server_status, scl


def simulation(iat_rt, iat_non_rt, st_rt, st_non_rt, master_clock):
    mc, rt_clock, non_rt_clock, n_rt, n_non_rt, server_status, scl = init()
    non_rt_queue = []
    while mc <= master_clock:
        if rt_clock < scl:
            mc = rt_clock
            n_rt += 1
            if scl - rt_clock != 0:
                non_rt_queue.append(scl - rt_clock)
                n_non_rt += 1
            if n_rt == 1:
                rt_clock += iat_rt
                server_status = 1
                scl = mc + st_rt
                n_rt -= 1
        elif non_rt_clock < scl:
            mc = non_rt_clock
            non_rt_queue.append(st_non_rt)
            n_non_rt += 1
            non_rt_clock += iat_non_rt
            server_status = 2
            scl = mc + st_non_rt
        else:
            if mc == non_rt_clock:
                non_rt_clock += iat_non_rt
                n_non_rt += 1
                non_rt_queue.append(st_non_rt)
            elif non_rt_queue:
                n_non_rt -= 1
                server_status = 2
                scl = mc + non_rt_queue[0]
                non_rt_queue.pop(0)
        print(f"{mc}\t{rt_clock}\t{non_rt_clock}\t{n_rt}\t{n_non_rt}\t{scl}\t{server_status}")

        # To check if the server would get idle
        if n_non_rt == 0 and n_rt == 0:
            server_status = 0

        mc = scl


def sample(time):
    return -1 * time * math.log(random.uniform(0, 1))


def simulation_with_randomness(iat_rt, iat_non_rt, st_rt, st_non_rt, master_clock):
    mc, rt_clock, non_rt_clock, n_rt, n_non_rt, server_status, scl = init()
    non_rt_queue = []
    while mc <= master_clock:
        if rt_clock <= scl:
            mc = rt_clock
            n_rt += 1
            if scl - rt_clock != 0:
                non_rt_queue.append(scl - rt_clock)
                n_non_rt += 1
            if n_rt == 1:
                rt_clock = round(rt_clock + sample(iat_rt), 2)
                server_status = 1
                scl = round(mc + sample(st_rt), 2)
                n_rt -= 1
        elif non_rt_clock < scl:
            mc = non_rt_clock
            r_st_non_rt = sample(st_non_rt)
            non_rt_queue.append(r_st_non_rt)
            n_non_rt += 1
            non_rt_clock = round(non_rt_clock + sample(iat_non_rt), 2)
            server_status = 2
            scl = round(mc + r_st_non_rt, 2)
        else:
            if mc == non_rt_clock:
                non_rt_clock = round(non_rt_clock + sample(iat_non_rt), 2)
                n_non_rt += 1
                non_rt_queue.append(sample(st_non_rt))
            elif non_rt_queue:
                n_non_rt -= 1
                server_status = 2
                scl = round(mc + non_rt_queue[0], 2)
                non_rt_queue.pop(0)

        print(f"{mc}\t{rt_clock}\t{non_rt_clock}\t{n_rt}\t{n_non_rt}\t{scl}\t{server_status}")

        # To check if the server would get idle
        if n_non_rt == 0 and n_rt == 0:
            server_status = 0
            scl = min(rt_clock, non_rt_clock)

        mc = scl


# Main function
if __name__ == '__main__':
    print("Task 2.1\nSubtask 1.1\nmc\trt_clock\tnon_rt_clock\tn_rt\tn_non_rt\tscl\tserver_status")
    simulation(iat_rt=10, iat_non_rt=5, st_rt=2, st_non_rt=4, master_clock=50)
    print("\nTask 2.1\nSubtask 1.2\nmc\trt_clock\tnon_rt_clock\tn_rt\tn_non_rt\tscl\tserver_status")
    simulation(iat_rt=5, iat_non_rt=10, st_rt=4, st_non_rt=2, master_clock=20)
    print("Task 2.2\nSubtask 1.1\nmc\trt_clock\tnon_rt_clock\tn_rt\tn_non_rt\tscl\tserver_status")
    simulation_with_randomness(iat_rt=10, iat_non_rt=5, st_rt=2, st_non_rt=4, master_clock=200)
    print("\nTask 2.2\nSubtask 1.2\nmc\trt_clock\tnon_rt_clock\tn_rt\tn_non_rt\tscl\tserver_status")
    simulation_with_randomness(iat_rt=5, iat_non_rt=10, st_rt=4, st_non_rt=2, master_clock=200)
