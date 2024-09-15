"""CPU Scheduling Algorithm that schedules processes basing on First Come, First Server paradigm"""
def set_cpu_bursts():
    procs_num = int(input("Numero dei processi: "))
    cpu_burst_list = []
    for i in range(procs_num):
        print(f"CPU burst del processo P{i+1}")
        cpu_burst = int(input(" "))
        cpu_burst_list.append(cpu_burst)
    return cpu_burst_list, procs_num

def gantt_diagram(cpu_burst_list, procs_num):
    print("Diagramma di Gantt:")
    for i in range(procs_num):
        print(f"P{i+1}({cpu_burst_list[i]}) ", end="")

def main():
    [list, procs] = set_cpu_bursts()
    gantt_diagram(list, procs)

main()