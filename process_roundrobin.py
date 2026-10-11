print("enter the process and execution time:")
pro = []
exe = []
rem = []
wait = []
trn = []
count = 0
while True:
    x = input("\nenter the process name: (to stop enter '~')")
    if x == '~':
        break
    pro.append(x)
    y = int(input("enter its execution time:"))
    exe.append(y)
    count = count + 1
quantum = int(input("\nenter time quantum: "))
i = 0
for i in range(count):
    rem.append(exe[i])
    wait.append(0)
    trn.append(0)
time = 0
avrwait = 0
avrtrn = 0
finished = 0
while finished < count:
    i = 0
    for i in range(count):
        if rem[i] > 0:
            if rem[i] > quantum:
                time = time + quantum
                rem[i] = rem[i] - quantum
            else:
                time = time + rem[i]
                wait[i] = time - exe[i]
                rem[i] = 0
                finished = finished + 1
h = 0
for h in range(count):
    trn[h] = wait[h] + exe[h]
    avrwait = avrwait + wait[h]
    avrtrn = avrtrn + trn[h]
j = 0
for j in range(count):
    print("\nwaiting time of", pro[j], "is", wait[j])
    print("turnaround time of", pro[j], "is", trn[j])
print("\naverage waiting time: ", avrwait / count, "\naverage turnaround time: ", avrtrn / count)