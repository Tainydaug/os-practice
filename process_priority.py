print("enter the process and execution time:")
pro = []
exe = []
pri = []
trn = []
count = 0
avrwait = 0
avrtrn = 0
while True:
    x = input("\nenter the process name: (to stop enter '~')")
    if x == '~':
        break
    pro.append(x)
    y = int(input("enter its execution time:"))
    exe.append(y)
    p = int(input("enter its priority (lower number = higher priority):"))
    pri.append(p)
    count = count + 1
for i in range(count - 1):
    for j in range(count - 1 - i):
        if pri[j] > pri[j + 1]:
            pri[j], pri[j + 1] = pri[j + 1], pri[j]
            exe[j], exe[j + 1] = exe[j + 1], exe[j]
            pro[j], pro[j + 1] = pro[j + 1], pro[j]
start = 0
wait = [0]
for i in range(count - 1):
    start = start + exe[i]
    wait.append(start)
for k in range(count):
    trn.append(wait[k] + exe[k])
for h in range(count):
    avrwait = avrwait + wait[h]
    avrtrn = avrtrn + trn[h]
for j in range(count):
    print("\nwaiting time of", pro[j], "is", wait[j])
    print("turnaround time of", pro[j], "is", trn[j])
print("\naverage waiting time: ", avrwait / count, "\naverage turnaround time: ", avrtrn / count)