# srem_timef

arrival_time = [];
burst_time = [];
rem_time = [];
sum_wait = 0;
sum_turnaround = 0
n = int(raw_input("Enter number of Process : "))
i = 0
while i < n:
    print  "For process :", i + 1
    arrival_time.append(int(raw_input("Enter arrival time of process :")))
    burst_time.append(int(raw_input("Enter burst time of process :")))
    rem_time.append(burst_time[i])
    i += 1

print "\n\nProcess\t|Turnaround Time| Waiting Time\n"
rem_time.append(99999)
time = 0;
remain = 0;
j = i
while remain != n:
    smallest = j
    i = 0;
    while i < n:
        if arrival_time[i] <= time and rem_time[i] < rem_time[smallest] and rem_time[i] > 0:
            smallest = i
        i += 1
    rem_time[smallest] -= 1
    if rem_time[smallest] == 0:
        remain += 1
        endTime = time + 1
        print smallest + 1, "\t", "\t", endTime - arrival_time[smallest], "\t", "\t", endTime - burst_time[smallest] - arrival_time[smallest]
        sum_wait += endTime - burst_time[smallest] - arrival_time[smallest]
        sum_turnaround += endTime - arrival_time[smallest]
    time += 1
print "\nAverage waiting time = ", sum_wait * 1.0 / n
print "Average Turnaround time = ", sum_turnaround * 1.0 / 5

