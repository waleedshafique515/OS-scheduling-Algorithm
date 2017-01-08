# Fcfs
number_array = []
waiting_time = 0
total_process = int(raw_input('Total no of processes: '))

for i in xrange(total_process):
    number_array.append([])
    number_array[i].append(raw_input('Process Name: '))
    number_array[i].append(int(raw_input('Arrival time: ')))
    waiting_time += number_array[i][1]
    number_array[i].append(int(raw_input('Burst Time: ')))

number_array.sort(key=lambda number_array: number_array[1])

print 'Name\tArrivalTime\tBurstTime'
for i in xrange(total_process):
    print number_array[i][0], '\t\t', number_array[i][1], '\t\t', number_array[i][2]

print 'Waiting time: ', waiting_time
print 'Average waiting time: ', (waiting_time / total_process)
