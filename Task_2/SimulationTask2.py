import math
import random
import pandas as pd


# Initial conditions
def init():
    mc = 0
    rt_clock = 3
    non_rt_clock = 5
    n_rt = 0
    n_non_rt = 0
    server_status = 2
    scl = 4
    return mc, rt_clock, non_rt_clock, n_rt, n_non_rt, scl, server_status

# Static simulation with the initial arrival times and without the introduction of randomness
def simulation(iat_rt, iat_non_rt, st_rt, st_non_rt, master_clock, Columns):
    mc, rt_clock, non_rt_clock, n_rt, n_non_rt, scl, server_status = init()
    non_rt_queue = []
    vals = [init()]

    # Stopping condition
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
        vals.append((mc, rt_clock, non_rt_clock, n_rt, n_non_rt, scl, server_status))
        
        # To check if the server would get idle
        if scl > rt_clock and scl > non_rt_clock:
            server_status = 0

        mc = scl

    return pd.DataFrame(vals, columns=Columns)


# Add randomness based on arrival and processing time
def sample(time):
    return -1 * time * math.log(random.uniform(0, 1))


# Dynamic simulation with the initial arrival times and with the introduction of randomness
def simulation_with_randomness(iat_rt, iat_non_rt, st_rt, st_non_rt, master_clock, Columns):
    mc, rt_clock, non_rt_clock, n_rt, n_non_rt, scl, server_status = init()
    non_rt_queue = []
    vals = [init()]
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
        vals.append((mc, rt_clock, non_rt_clock, n_rt, n_non_rt, scl, server_status))

        if n_non_rt == 0 and n_rt == 0:
            server_status = 0
            scl = min(rt_clock, non_rt_clock)

        mc = scl

    return pd.DataFrame(vals, columns=Columns)


# Main function
if __name__ == '__main__':
    Columns = ["Master Clock", "RT Clock", "NON-RT Clock", "N_RT", "N_NON-RT", "SCL", "Server Status"]
    empty = pd.DataFrame([("", "", "", "", "", "", "")], columns=Columns)
    
    df1 = simulation(iat_rt=10, iat_non_rt=5, st_rt=2, st_non_rt=4, master_clock=50, Columns=Columns)
    df2 = simulation(iat_rt=5, iat_non_rt=10, st_rt=4, st_non_rt=2, master_clock=20, Columns=Columns)
    result = pd.concat([df1, empty, empty, df2])
    result.to_csv("Result_Task2-1.csv", index=False)

    df1 = simulation_with_randomness(iat_rt=10, iat_non_rt=5, st_rt=2, st_non_rt=4, master_clock=200, Columns=Columns)
    df2 = simulation_with_randomness(iat_rt=5, iat_non_rt=10, st_rt=4, st_non_rt=2, master_clock=200, Columns=Columns)
    result = pd.concat([df1, empty, empty, df2])
    result.to_csv("Result_Task2-2.csv", index=False)