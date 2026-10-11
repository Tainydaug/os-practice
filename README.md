# OS Practice

Operating systems practice programs: four CPU scheduling algorithms in Python and a POSIX file I/O demo in C.

## CPU scheduling (Python)

Each program asks for process names and burst (execution) times, then prints the waiting time and turnaround time of every process plus the averages. Enter `~` as the process name to stop adding processes.

| File | Algorithm | Notes |
|---|---|---|
| `process_fcfs.py` | First Come First Served | Runs processes in the order entered |
| `process_short.py` | Shortest Job First (non-preemptive) | Sorts by burst time, shortest first |
| `process_priority.py` | Priority scheduling (non-preemptive) | Lower number means higher priority |
| `process_roundrobin.py` | Round Robin | Asks for a time quantum |

**Assumption:** every process arrives at time 0.

### Run

```
python process_fcfs.py
```

### Example (FCFS, processes P1=5, P2=3, P3=8)

| Process | Waiting | Turnaround |
|---|---|---|
| P1 | 0 | 5 |
| P2 | 5 | 8 |
| P3 | 8 | 16 |

Average waiting time 4.33, average turnaround time 9.67.

### Same processes under the other algorithms

| Algorithm | Avg waiting | Avg turnaround |
|---|---|---|
| FCFS | 4.33 | 9.67 |
| SJF | 3.67 | 9.0 |
| Priority (P1=2, P2=1, P3=3) | 3.67 | 9.0 |
| Round Robin (quantum 2) | 7.0 | 12.33 |

SJF gives the lowest average waiting time here, which matches the theory. Round Robin has a higher average wait but shares the CPU fairly.

### Formulas used

- Turnaround time = completion time - arrival time
- Waiting time = turnaround time - burst time

## POSIX file I/O (C)

`posix_file_io.c` uses system calls directly: it creates `demo.txt` and writes to it, reads it back, then copies it to `demo_copy.txt` in small chunks.

```
gcc posix_file_io.c -o posix_file_io
./posix_file_io
```

Output:
```
File descriptor: 3
Read 27 bytes: Hello from POSIX file I/O!
Copied 27 bytes
```

Works on Linux, macOS, or WSL on Windows. The file descriptor is 3 because 0, 1, and 2 are already taken by standard input, output, and error.

## Limitations

- Scheduling programs assume arrival time 0 and no I/O waits.
- Non-preemptive SJF and priority can starve long or low-priority jobs.
- Basic input handling: entering text where a number is expected will crash the program.

## Author

Tanishq Gyaneshwar Dhoke ([@Tainydaug](https://github.com/Tainydaug))
