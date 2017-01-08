#Round Robin


number_array = []
wait_time = 0
total_process = int(raw_input('Enter the No. of Process : '))

for i in xrange(total_process):
	number_array.append([])
	print ' '
	number_array[i].append(raw_input('Enter Process Name : ' ))

	number_array[i].append(int(raw_input('Enter Arrival Time :')))

	number_array[i].append(int(raw_input('Enter Burst Time :')))

	number_array[i].append(int(raw_input('Enter Priority :')))

	print ' '

time_slice = int(raw_input('Enter the time slice for Process : '))

number_array.sort(key = lambda number_array:(number_array[1],number_array[3]))

total = 0
wait = []
finish = []
dup = []

for i in xrange(total_process):
	finish.append(0)
	total += number_array[i][2]
	dup.append(number_array[i][2])
	wait.append(0)


j = 0
l = 0


while (l<total):
	j = j % total_process
	for k in xrange(time_slice):
		if(dup[j] != 0):
			dup[j] -= 1
			l += 1
			if (dup[j] == 0):
				finish[j] = l + number_array[j][1]
				break
	j += 1




for i in xrange(total_process):
	wait[i]  = finish[i] - number_array[i][1] - number_array[i][2]

print 'Process Name \tArrival Time \t Burst Time \t  Waiting Time'
for i in xrange(total_process):
	print number_array[i][0] ,'\t\t' ,number_array[i][1] ,'\t\t', number_array[i][2], '\t\t',wait[i]
	wait_time += wait[i]

print 'Total Waiting Time : ',wait_time
print 'Average Waiting Time : ',(wait_time/total_process)
