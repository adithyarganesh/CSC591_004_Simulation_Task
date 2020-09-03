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
            if scl-rt_clock != 0:
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
        if scl > rt_clock and scl > non_rt_clock:
            server_status = 0
        mc = scl

# Main function
if __name__ == '__main__':
    print("Task 1.1\nmc\trt_clock\tnon_rt_clock\tn_rt\tn_non_rt\tscl\tserver_status")
    simulation(iat_rt=10, iat_non_rt=5, st_rt=2, st_non_rt=4, master_clock=50)
    print("\nTask 1.2\nmc\trt_clock\tnon_rt_clock\tn_rt\tn_non_rt\tscl\tserver_status")
    simulation(iat_rt=5, iat_non_rt=10, st_rt=4, st_non_rt=2, master_clock=20)