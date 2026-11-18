# Bash Scripting for DevOps – 30-Day Learning Roadmap

**Goal:** Become confident in writing Bash scripts for Linux administration, cloud operations, and DevOps automation.

**Duration:** 30 Days
**Daily Commitment:** 1 Hour
**Focus:** Hands-on scripting, troubleshooting, and interview preparation.

---

## Learning Progress Tracker

Update the checkboxes as you complete each day.

### Week 1 – Bash Fundamentals

| Day | Topic                               | Practical Assignment                      | Status |
| --- | ----------------------------------- | ----------------------------------------- | ------ |
| 01  | Arrays and indexing                 | Create and iterate through a server array | [ ]    |
| 02  | Arithmetic and counters             | Count successful and failed server checks | [ ]    |
| 03  | Conditions and pattern matching     | Identify servers using name patterns      | [ ]    |
| 04  | For loops                           | Check multiple servers using a loop       | [ ]    |
| 05  | While loops                         | Implement retry logic for failed servers  | [ ]    |
| 06  | Functions                           | Create reusable server-check functions    | [ ]    |
| 07  | Function arguments and return codes | Return success or failure from functions  | [ ]    |

### Week 2 – Intermediate Bash

| Day | Topic                       | Practical Assignment                    | Status |
| --- | --------------------------- | --------------------------------------- | ------ |
| 08  | Command-line arguments      | Accept server names as script arguments | [ ]    |
| 09  | Exit status                 | Handle successful and failed commands   | [ ]    |
| 10  | Command substitution        | Capture system information in variables | [ ]    |
| 11  | Grep                        | Filter ERROR and WARNING logs           | [ ]    |
| 12  | AWK fundamentals            | Extract fields from application logs    | [ ]    |
| 13  | AWK calculations            | Calculate error counts and percentages  | [ ]    |
| 14  | Sed and regular expressions | Search and replace log content          | [ ]    |

### Week 3 – Linux Administration and Automation

| Day | Topic                       | Practical Assignment                        | Status |
| --- | --------------------------- | ------------------------------------------- | ------ |
| 15  | Linux text utilities        | Practice cut, sort, uniq, wc, head and tail | [ ]    |
| 16  | File and directory handling | Check files, directories and permissions    | [ ]    |
| 17  | Redirection and pipelines   | Redirect output and error messages          | [ ]    |
| 18  | Error handling              | Implement safe script execution and traps   | [ ]    |
| 19  | Debugging                   | Practice bash -n, bash -x and ShellCheck    | [ ]    |
| 20  | Processes and cron          | Automate a recurring monitoring task        | [ ]    |
| 21  | Disk monitoring             | Create a disk usage alert script            | [ ]    |

### Week 4 – DevOps Automation Projects

| Day | Topic                     | Practical Assignment                        | Status |
| --- | ------------------------- | ------------------------------------------- | ------ |
| 22  | CPU and memory monitoring | Generate a Linux health report              | [ ]    |
| 23  | Server availability       | Build a multi-server monitoring script      | [ ]    |
| 24  | Log analysis              | Build an application log analyser           | [ ]    |
| 25  | Backup automation         | Create and verify timestamped backups       | [ ]    |
| 26  | Docker automation         | Automate container status checks            | [ ]    |
| 27  | Kubernetes automation     | Automate cluster and pod health checks      | [ ]    |
| 28  | Integrated toolkit        | Combine monitoring scripts into one toolkit | [ ]    |
| 29  | Interview assessment      | Solve timed Bash coding challenges          | [ ]    |
| 30  | Capstone project          | Build a complete DevOps automation toolkit  | [ ]    |

---

## Daily Study Routine

| Duration   | Activity                    |
| ---------- | --------------------------- |
| 15 minutes | Learn concepts              |
| 10 minutes | Review examples             |
| 25 minutes | Write scripts independently |
| 10 minutes | Debug and review code       |

## Hands-on Projects

### 1. Server Availability Monitor

- Maintain a list of servers.
- Check availability using ping.
- Count UP and DOWN servers.
- Calculate availability percentage.
- Generate a monitoring report.

### 2. Linux System Health Monitor

- Capture hostname and timestamp.
- Monitor CPU and memory.
- Check disk utilization.
- Identify high-resource processes.
- Generate a health report.

### 3. Application Log Analyser

- Check whether the log file exists.
- Count ERROR and WARNING entries.
- Display the last 10 errors with timestamps.
- Handle missing or empty log files.
- Generate a summary.

### 4. Backup Automation

- Create timestamped backups.
- Verify archive creation.
- Implement backup retention.
- Test restoration.

### 5. DevOps Automation Toolkit

- Docker container status checks.
- Kubernetes pod health checks.
- Server availability monitoring.
- Linux resource monitoring.
- Application log analysis.

---

## Interview Preparation Checklist

- [ ] Explain the Bash shebang.
- [ ] Difference between `$@` and `$*`.
- [ ] Explain Bash arrays and indexing.
- [ ] Difference between `[ ]` and `[[ ]]`.
- [ ] Explain `$?` and exit codes.
- [ ] Explain `&&`, `||` and pipelines.
- [ ] Explain `2>/dev/null`.
- [ ] Explain `grep`, `awk` and `sed`.
- [ ] Explain `set -euo pipefail`.
- [ ] Explain functions and arguments.
- [ ] Explain retry logic.
- [ ] Explain traps and signals.
- [ ] Debug a failing Bash script.
- [ ] Write a server monitoring script.
- [ ] Automate Docker and Kubernetes checks.

---

## Current Skill Assessment

| Skill                   | Current Level             |
| ----------------------- | ------------------------- |
| Variables               | Beginner                  |
| Arrays                  | Beginner – needs practice |
| For loops               | Beginner                  |
| If/Else                 | Beginner                  |
| Pattern matching        | Needs reinforcement       |
| Counters and arithmetic | In progress               |
| Ping monitoring         | Basic                     |
| Grep                    | Basic                     |
| AWK                     | Beginner                  |
| Functions               | To learn                  |
| Error handling          | To learn                  |
| DevOps automation       | To practice               |

## Learning Rules

1. Write code independently before checking solutions.
2. Practise every topic with real examples.
3. Debug mistakes instead of immediately copying corrected code.
4. Commit completed exercises to GitHub.
5. Maintain notes for commands and concepts.
6. Complete the practical assignment before moving to the next topic.

## Repository Structure

```text
bash-devops-learning/
├── README.md
├── day-01-arrays/
├── day-02-counters/
├── day-03-conditions/
├── day-04-for-loops/
├── day-05-while-loops/
├── day-06-functions/
├── day-07-return-codes/
├── week-2/
├── week-3/
├── week-4/
└── projects/
    ├── server-monitor/
    ├── linux-health-monitor/
    ├── log-analyser/
    ├── backup-automation/
    └── devops-toolkit/
```

---

**Final Objective:** Build the ability to independently write, troubleshoot, and explain Bash automation scripts used in real-world DevOps and Cloud Engineering environments.
