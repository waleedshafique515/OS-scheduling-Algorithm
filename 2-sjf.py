# sjf

burst_time = []
wait_time = []
wait_timeotal = 0
arr = []
total_process = int(raw_input('Enter the total no of processes: '))
atime = (int(raw_input('Enter process arrival time: ')))
for i in xrange(total_process):
    arr.append([])
    arr[i].append(raw_input('Enter process number: '))
    burst_time[i].append(int(raw_input('Enter process burst time: ')))
j = 1
for i in xrange(total_process):
    post = i
    for j in xrange(total_process):
        if burst_time[j] < burst_time[post]:
            post = j
        temp = burst_time[i]
        burst_time[i] = burst_time[post]
        burst_time[post] = temp
        temp = arr[i]
        arr[i] = arr[post]
        arr[post] = temp
wait_time[0] = 0
j = 0

for i in xrange(total_process):
    wait_time[i] = 0
    for j in xrange(i):
        wait_time[i] += burst_time[i]
    wait_timeotal += wait_time[i]
print 'ProcessNumber\tArrivalTime\tBurstTime'
for i in xrange(total_process):
    print arr[i][0], '\t\t', atime, '\t\t', burst_time[i][2]

print 'Total waiting time: ', wait_timeotal
print 'Average waiting time: ', (wait_timeotal / total_process)
