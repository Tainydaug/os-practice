print("enter the process and execution time:")
pro = []
exe = []
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
    count = count + 1    
start = 0
i = 1
wait = [0]
for i in range(count-1):
     start = start + exe[i]
     wait.append(start)
k = 0
for k in range(count):     
     trn.append(wait[k] + exe[k])
h = 0
for h in range(count):
    avrwait = avrwait + wait[h]
    avrtrn = avrtrn + trn[h] 
j = 0     
for j in range(count):
    print("\nwaiting time of",pro[j],"is",wait[j])
    print("turnaround time of",pro[j],"is",trn[j])
print("\naverage waiting time: ",avrwait/count,"\naverage turnaround time: ",avrtrn/count)
    
         

             
    
    
    
    