# Databricks Senior Technical Solutions Engineer (Platform)
## Master Interview Preparation Plan

**Updated:** 23 November 2026  
**Target role:** Senior Technical Solutions Engineer (Platform), Databricks  
**Preparation approach:** Concept learning + hands-on labs + production troubleshooting + interview communication

---

## 1. Goal and positioning

Prepare to demonstrate strong platform troubleshooting, enterprise support, cloud infrastructure, Linux, networking, scripting, incident management and customer communication skills, while building sound fundamentals in Databricks and Apache Spark.

**Experience positioning:** Do not present Databricks architecture, Apache Spark, distributed computing or data pipeline management as professional production experience if you have not worked with them in production. Emphasize transferable experience in GCP support, cloud networking, production troubleshooting, incident ownership, root-cause analysis, customer communication and collaboration with engineering teams.

## 2. Preparation priorities

| Priority | Subject | Expected outcome |
|---|---|---|
| 1 | Linux troubleshooting | Diagnose common and advanced production OS issues using evidence |
| 2 | Networking and TCP/IP | Trace connectivity end to end and interpret packet-level symptoms |
| 3 | GCP networking and infrastructure | Troubleshoot cloud and hybrid connectivity across GCP services |
| 4 | SQL | Write and explain queries independently |
| 5 | Bash scripting | Automate checks, parse logs and handle failures safely |
| 6 | Databricks and Spark | Explain architecture and investigate common failure patterns conceptually |
| 7 | Incident management | Lead technical investigations, communicate clearly and produce useful RCAs |
| 8 | Code review | Identify correctness, security, performance and reliability issues |
| 9 | AI / GenAI | Explain core concepts, use cases, limitations and security risks |
| 10 | Other resume topics | Refresh Docker, Kubernetes, Terraform, CI/CD, AWS and databases |

The time allocation should be adjusted to the interview date and weakest areas. Do not use the old 19–20 November 2026 hourly schedule; those dates have passed.

---

# PART A — CORE TECHNICAL PREPARATION

## 3. SQL

### 3.1 Foundations
- [ ] Relational database concepts: database, table, row, column, primary key and foreign key
- [ ] Data types and constraints
- [ ] `CREATE TABLE`, `INSERT INTO`
- [ ] `SELECT *` and selecting specific columns
- [ ] `WHERE` and comparison operators
- [ ] `AND`, `OR`, `NOT`
- [ ] `IN`, `BETWEEN`, `LIKE`
- [ ] `NULL`, `IS NULL`, `IS NOT NULL`
- [ ] `UPDATE`, `DELETE`, `TRUNCATE`, `DROP`
- [ ] `ORDER BY`, `LIMIT`, `DISTINCT`

### 3.2 Aggregation and joins
- [ ] `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- [ ] `GROUP BY` and `HAVING`
- [ ] `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`
- [ ] Join keys, duplicate rows and NULL behavior
- [ ] Joins across multiple tables
- [ ] Filtering before and after aggregation
- [ ] Subqueries and correlated subqueries
- [ ] Common table expressions (CTEs)
- [ ] Window functions: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `PARTITION BY`
- [ ] Basic query-performance concepts: indexes, scans, joins and query plans

### 3.3 Practical exercises
- [ ] Create employee, department, customer and order tables
- [ ] Write at least 20 queries without copying examples
- [ ] Find duplicates and missing values
- [ ] Find the second-highest salary
- [ ] Count employees by department
- [ ] Join customers and orders with filters
- [ ] Rank employees within departments
- [ ] Explain the result and edge cases of each query

---

## 4. Bash scripting — beginner to advanced

### 4.1 Fundamentals
- [ ] Shebang and script execution
- [ ] Variables and command substitution
- [ ] Quoting, spaces and special characters
- [ ] Positional parameters: `$0`, `$1`, `$@`, `$#`
- [ ] Exit status: `$?`
- [ ] `if`, `elif`, `else`, `case`
- [ ] `for`, `while`, `until`
- [ ] Arrays and iteration
- [ ] Functions and return codes
- [ ] Arithmetic and string comparisons

### 4.2 Linux text and log processing
- [ ] `grep`, `grep -iE`, `grep -ivE`
- [ ] `awk`, `sed`, `cut`, `sort`, `uniq`, `wc`, `tr`
- [ ] `head`, `tail`, `tail -f`
- [ ] Pipes and redirection: `>`, `>>`, `2>`, `2>&1`
- [ ] `/dev/null`
- [ ] `xargs`, `tee`, `find`
- [ ] Regular expressions and timestamps

### 4.3 Robust scripting
- [ ] Validate input and command availability
- [ ] Handle missing files and empty results
- [ ] Use meaningful exit codes
- [ ] Understand `set -e`, `set -u`, `set -o pipefail` and their trade-offs
- [ ] Quote variables and handle filenames safely
- [ ] Add logging and timestamps
- [ ] Use traps and cleanup functions
- [ ] Avoid exposing secrets in logs or command output
- [ ] Test success, failure and edge cases

### 4.4 Practical scripts
- [ ] Log analyzer: count ERROR/WARNING/CRITICAL and show recent entries
- [ ] Server health check: CPU, memory, disk and service status
- [ ] HTTP endpoint checker using `curl`
- [ ] Multi-server reachability checker
- [ ] Disk threshold alert
- [ ] Apache service monitor and restart decision logic
- [ ] Backup verification script

---

## 5. Linux administration and troubleshooting — beginner to expert

### 5.1 Command-line foundations
- [ ] Navigation: `pwd`, `ls`, `cd`, `tree`
- [ ] File operations: `touch`, `cp`, `mv`, `rm`, `mkdir`, `rmdir`
- [ ] Reading files: `cat`, `less`, `more`, `head`, `tail`
- [ ] Search: `find`, `locate`, `grep`, `xargs`
- [ ] Text processing: `sort`, `uniq`, `cut`, `tr`, `wc`, `tee`, `awk`, `sed`
- [ ] Permissions: `chmod`, `chown`, `chgrp`, `umask`
- [ ] Identity: `id`, `whoami`, `who`, `w`, `sudo`
- [ ] Help: `man`, `--help`, `which`, `type`, `whereis`

### 5.2 Processes and CPU performance
- [ ] Load average and CPU utilization
- [ ] `uptime`, `top`, `htop`, `ps`, `pstree`
- [ ] `pgrep`, `pidof`, `pidstat`, `mpstat`
- [ ] Process states: running, sleeping, uninterruptible sleep and zombie
- [ ] `kill`, `pkill`, `killall`, `nice`, `renice`
- [ ] CPU saturation versus high load average
- [ ] Identify CPU-heavy processes and threads
- [ ] Establish a baseline and compare before/after measurements
- [ ] Investigate context switching and resource contention

### 5.3 Memory and OOM troubleshooting
- [ ] RAM, swap, virtual memory, RSS, page cache and available memory
- [ ] `free -h`, `vmstat`, `/proc/meminfo`, `pmap`
- [ ] Find memory-heavy processes using `ps` and `top`
- [ ] Kernel logs: `dmesg -T`, `journalctl -k`
- [ ] Identify OOM-killer events and killed processes
- [ ] Distinguish host-level OOM from cgroup/container memory-limit OOM
- [ ] Understand Kubernetes `OOMKilled` and exit code 137
- [ ] Investigate leaks, workload spikes and undersized limits
- [ ] Recommend profiling, workload tuning and capacity changes

### 5.4 Disk I/O and performance
- [ ] `iostat`, `iotop`, `pidstat -d`, `vmstat`
- [ ] I/O wait and device utilization concepts
- [ ] Identify processes generating high disk I/O
- [ ] Distinguish disk capacity problems from disk latency/throughput problems
- [ ] Investigate application latency caused by storage bottlenecks
- [ ] Correlate OS metrics with application logs

### 5.5 Filesystem and storage management
- [ ] Capacity: `df -h`, `du -sh`, `du -x`
- [ ] Inodes: `df -i`
- [ ] Devices and partitions: `lsblk`, `blkid`, `fdisk -l`
- [ ] Filesystem types: `df -Th`
- [ ] Mounts: `mount`, `findmnt`, `umount`, `/etc/fstab`
- [ ] LVM: `pvs`, `vgs`, `lvs`, `pvdisplay`, `vgdisplay`, `lvdisplay`
- [ ] Extend logical volumes and filesystems safely
- [ ] Filesystem checks with `fsck` only when appropriate and safely unmounted
- [ ] Deleted-but-open files: `lsof +L1`
- [ ] Read-only remounts, mount failures and permission problems
- [ ] ACLs, ownership and special permission bits

### 5.6 Linux boot and startup troubleshooting
- [ ] BIOS/UEFI, bootloader, kernel, initramfs and systemd sequence
- [ ] GRUB entries and kernel parameters
- [ ] systemd targets and unit dependencies
- [ ] `systemctl status`, `systemctl --failed`, `systemctl list-units`
- [ ] Boot logs: `journalctl -b`, `journalctl -b -1`, `dmesg`
- [ ] Emergency and rescue modes
- [ ] `/etc/fstab` errors and missing mount dependencies
- [ ] Kernel panic, initramfs issues and root filesystem mount failures
- [ ] Practise recovery only on a disposable VM or snapshot

### 5.7 Services, logs and system administration
- [ ] `systemctl`, `service`, `journalctl`, `/var/log`
- [ ] `cron`, `crontab`, `at`
- [ ] Debian/Ubuntu packages: `apt`, `dpkg`
- [ ] SSH, SCP, SFTP and authentication logs
- [ ] Time and NTP: `date`, `timedatectl`, chrony concepts
- [ ] Kernel and OS: `uname -a`, `hostnamectl`, `lsmod`, `modinfo`
- [ ] Limits: `ulimit`, PAM limits and systemd resource controls
- [ ] Apache service status and configuration validation
- [ ] Apache access/error logs, listeners and process checks

### 5.8 Advanced diagnostics
- [ ] `lsof`, `/proc`, `/sys`
- [ ] `strace` for system-call troubleshooting
- [ ] File descriptors and process limits
- [ ] Core dumps and crash basics
- [ ] Correlate logs, metrics and process state
- [ ] Build a timeline and verify recovery after remediation

---

## 6. Linux networking and end-to-end connectivity

### 6.1 Linux network commands
- [ ] Interfaces and addresses: `ip addr`, `ip link`
- [ ] Routes and rules: `ip route`, `ip rule`
- [ ] Neighbours: `ip neigh`
- [ ] Sockets/listeners: `ss -tulpen`, `ss -s`
- [ ] DNS: `dig`, `nslookup`, `host`, `getent hosts`
- [ ] Resolver configuration: `/etc/resolv.conf`
- [ ] Connectivity: `ping`, `tracepath`, `traceroute`, `mtr`
- [ ] TCP tests: `nc`, `ncat`, `curl`
- [ ] HTTP/TLS: `curl -v`, `openssl s_client`
- [ ] Packet capture: `tcpdump`
- [ ] Firewall: `iptables`, `nft`, `ufw`
- [ ] Interface counters: `ip -s link`, `ethtool -S`
- [ ] Process/socket mapping: `ss -plant`, `lsof -i`
- [ ] NetworkManager and systemd-networkd concepts

### 6.2 Server-to-internet troubleshooting
- [ ] Confirm application process and local listening socket
- [ ] Verify interface, IP, subnet and default route
- [ ] Test DNS resolution separately from direct-IP connectivity
- [ ] Validate TCP handshake and destination port
- [ ] Check routing and next-hop selection
- [ ] Inspect host firewall and egress rules
- [ ] Check NAT/SNAT and return-path behavior
- [ ] Validate proxy configuration and TLS handshake
- [ ] Investigate MTU and Path MTU Discovery
- [ ] Capture packets and identify where traffic stops

### 6.3 Server-to-server troubleshooting
- [ ] Verify source/destination IP, route and interface
- [ ] Confirm destination process is listening on the expected address/port
- [ ] Test DNS and direct-IP connectivity separately
- [ ] Validate host and cloud firewall rules
- [ ] Check VPC routes, peering, VPN or Interconnect path
- [ ] Validate symmetric routing and return path
- [ ] Distinguish timeout, refused, reset and unreachable errors
- [ ] Compare packet captures at both endpoints

### 6.4 OSI and TCP/IP end to end
- [ ] OSI layers 1–7 and practical examples
- [ ] TCP/IP model and OSI mapping
- [ ] Encapsulation and decapsulation
- [ ] Ethernet, MAC addresses, ARP and VLANs
- [ ] IP addressing, CIDR, subnetting and routing
- [ ] TCP three-way handshake, sequence numbers, ACKs and retransmissions
- [ ] TCP flags: SYN, ACK, FIN and RST
- [ ] UDP and common use cases
- [ ] DNS resolution flow
- [ ] HTTP/HTTPS, TLS handshake, certificates and SNI
- [ ] MTU, MSS, fragmentation and Path MTU Discovery
- [ ] NAT, SNAT, DNAT and connection tracking
- [ ] Load balancing and health checks
- [ ] Packet loss, latency, jitter, throughput and congestion
- [ ] Read packet captures and correlate client, server and network observations

---

## 7. GCP networking and infrastructure — end to end

### 7.1 GCP network services
- [ ] VPCs, subnetworks, regional scope and global VPC concepts
- [ ] Primary and secondary IP ranges
- [ ] Static and dynamic routes; route priority and dynamic routing mode
- [ ] VPC firewall rules and hierarchical firewall policies
- [ ] Cloud NAT and Public NAT
- [ ] Cloud Router, BGP, route advertisements and learned routes
- [ ] HA VPN, tunnels, BGP and troubleshooting
- [ ] Cloud Interconnect, VLAN attachments, BGP and redundancy
- [ ] VPC Network Peering and route-exchange limitations
- [ ] Private Service Access (PSA)
- [ ] Private Service Connect (PSC)
- [ ] Private Google Access and Private Google APIs
- [ ] Cloud DNS, forwarding/peering zones and DNS policies
- [ ] Application Load Balancers and Network Load Balancers
- [ ] Backend services, health checks, instance groups, NEGs and serverless NEGs
- [ ] GKE networking: VPC-native clusters, Pod/Service ranges, Services, Ingress/Gateway and NetworkPolicy
- [ ] Shared VPC and service-project dependencies
- [ ] Network Intelligence Center, Connectivity Tests, VPC Flow Logs and packet mirroring

### 7.2 End-to-end GCP connectivity paths
- [ ] VM to internet through Cloud NAT
- [ ] VM-to-VM in the same VPC and across subnets
- [ ] VM-to-VM across VPC peering
- [ ] On-premises to GCP over HA VPN
- [ ] On-premises to GCP over Cloud Interconnect
- [ ] Workloads to Google APIs using Private Google Access or PSC
- [ ] Workloads to managed services using PSA or PSC
- [ ] Load balancer to VM/NEG backend
- [ ] GKE Pod to internet, VM, Google API and private service
- [ ] Shared VPC service-project connectivity
- [ ] Hybrid and multi-VPC routing and return-path validation

### 7.3 Complex GCP network and infrastructure incidents
- [ ] VM internet failure: trace DNS, route, firewall, NAT and return path
- [ ] VM-to-VM timeout: inspect routes, firewall, listener and packet captures
- [ ] Unhealthy load-balancer backend: health-check source ranges, firewall, backend, port and application response
- [ ] HTTP 502/503/504: isolate frontend, proxy, backend reachability, timeout and application health
- [ ] Cloud NAT port exhaustion/allocation errors: NAT metrics, logs, port allocation and connection patterns
- [ ] PSA allocated-range exhaustion and Service Networking provisioning failures
- [ ] PSC endpoint failure: endpoint, forwarding rule, DNS, producer acceptance and routing/firewall design
- [ ] VPN tunnel up but traffic failing: BGP, route exchange, firewall and return route
- [ ] Interconnect BGP/route issue: VLAN attachment, peer ASN, learned/advertised routes and redundancy
- [ ] Asymmetric routing, overlapping CIDRs and route priority
- [ ] GKE Pod IP exhaustion and secondary-range utilization
- [ ] GKE DNS, NodeLocal DNSCache, kube-dns and NetworkPolicy issues
- [ ] MTU mismatch and fragmentation across VPN, Interconnect or overlay paths
- [ ] Shared VPC IAM and network attachment/configuration issues
- [ ] Firewall policy precedence and effective-rule troubleshooting
- [ ] Correlate VPC Flow Logs, Cloud Logging, Monitoring, Connectivity Tests and packet captures
- [ ] Build incident timeline, determine blast radius, isolate fault domain and document RCA/prevention

---

# PART B — ROLE-SPECIFIC PREPARATION

## 8. Databricks and Apache Spark fundamentals

### 8.1 Databricks platform
- [ ] Databricks architecture and workspace fundamentals
- [ ] Lakehouse architecture
- [ ] Delta Lake and transaction log concepts
- [ ] Unity Catalog and data governance
- [ ] Databricks SQL
- [ ] Compute and cluster concepts
- [ ] Jobs and workflow fundamentals
- [ ] Object storage access, identity and permissions

### 8.2 Apache Spark
- [ ] Driver, executors and cluster manager concepts
- [ ] Jobs, stages and tasks
- [ ] Transformations and actions
- [ ] Lazy evaluation
- [ ] Partitions and parallelism
- [ ] Shuffle and data movement
- [ ] Data skew and partition imbalance
- [ ] Caching and persistence basics
- [ ] Driver OOM versus executor OOM
- [ ] Failed tasks, retries and executor loss
- [ ] Slow jobs and long-running stages
- [ ] Cluster startup and autoscaling issues

### 8.3 Databricks incident scenarios
- [ ] Job fails during startup
- [ ] Job is running slowly
- [ ] Executor lost during execution
- [ ] Driver or executor runs out of memory
- [ ] Data skew causes a few tasks to run much longer
- [ ] Cluster fails to start or scale
- [ ] Workload cannot access object storage
- [ ] Permissions or catalog access fail
- [ ] Network or DNS prevents access to a dependency

### 8.4 AI and data platform products
- [ ] Genie
- [ ] MLflow
- [ ] Mosaic AI
- [ ] AutoML
- [ ] Model Serving

**Preparation note:** Learn the architecture and troubleshooting vocabulary. Clearly distinguish hands-on lab experience, conceptual understanding and professional production experience.

---

## 9. Incident management and customer communication

- [ ] P0/P1 triage, severity, impact and scope
- [ ] Incident commander, technical leads and communication channels
- [ ] Timestamped incident timeline
- [ ] Separate mitigation, recovery and root-cause investigation
- [ ] Form hypotheses and test them with evidence
- [ ] Customer updates at agreed intervals
- [ ] War rooms and cross-functional escalation
- [ ] RCA: impact, trigger, root cause, contributing factors and corrective actions
- [ ] Preventive actions, owners and validation
- [ ] Mentor junior engineers and create knowledge-base content
- [ ] Explain uncertainty without speculation
- [ ] Communicate technical findings to technical and non-technical audiences

### Incident response structure to practise

1. **Impact:** What is broken, who is affected and since when?
2. **Scope:** Is the issue isolated or widespread?
3. **Evidence:** What do logs, metrics, traces and packet captures show?
4. **Hypothesis:** Which layer or component is most likely responsible?
5. **Mitigation:** What safe action can restore service?
6. **Root cause:** What actually caused the incident?
7. **Prevention:** What change reduces recurrence?

---

## 10. Code review

- [ ] Understand unfamiliar code before changing it
- [ ] Identify syntax and logical errors
- [ ] Review variable handling and input validation
- [ ] Check error handling and exit codes
- [ ] Identify security issues and secret exposure
- [ ] Check performance and reliability
- [ ] Review SQL queries
- [ ] Review Bash and Python scripts
- [ ] Check logging, retries and cleanup
- [ ] Explain a code change and its trade-offs clearly

---

## 11. AI and GenAI

- [ ] AI, ML and GenAI differences
- [ ] LLMs, tokens and context windows
- [ ] Prompt engineering
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Embeddings and vector databases
- [ ] AI agents and tool calling
- [ ] Hallucinations and model limitations
- [ ] Prompt injection and data leakage risks
- [ ] Guardrails and responsible AI
- [ ] Model evaluation and observability
- [ ] AI-assisted code review
- [ ] Mosaic AI fundamentals

---

## 12. Other resume topics

### Cloud and DevOps
- [ ] GCP core services and architecture
- [ ] AWS core services and networking concepts
- [ ] Docker images, containers and registries
- [ ] Kubernetes workloads, Services, probes and troubleshooting
- [ ] Terraform state, providers, modules and plan/apply workflow
- [ ] Jenkins and GitHub Actions
- [ ] Cloud Build and CI/CD
- [ ] Linux administration and shell scripting
- [ ] Databases and virtualization fundamentals

---

# PART C — HANDS-ON LABS AND INTERVIEW PRACTICE

## 13. Practical lab scenarios

Use the Debian VM with Apache behind the GCP Global Load Balancer as a safe practice environment. Use test resources and snapshots for disruptive experiments.

### Linux labs
- [ ] Inspect system load, CPU, memory and processes
- [ ] Generate controlled CPU load and observe the impact
- [ ] Identify a memory-heavy process
- [ ] Investigate disk usage and inode utilization
- [ ] Find a deleted-but-open file
- [ ] Diagnose a stopped Apache service
- [ ] Inspect boot and service logs

### Linux networking labs
- [ ] Identify IP, interface and default route
- [ ] Check DNS resolution
- [ ] Check whether a service is listening
- [ ] Test TCP connectivity to a port
- [ ] Trace a route to a destination
- [ ] Capture a successful and failed connection with `tcpdump`
- [ ] Compare client-side and server-side evidence

### GCP labs
- [ ] Trace VM-to-internet connectivity through Cloud NAT
- [ ] Troubleshoot VM-to-VM connectivity
- [ ] Investigate an unhealthy load-balancer backend
- [ ] Inspect health-check and backend behavior
- [ ] Review VPC Flow Logs and Connectivity Tests
- [ ] Review Cloud NAT metrics and logs
- [ ] Trace a GKE Pod connectivity path
- [ ] Draw a hybrid VPN/Interconnect packet path

### Safety
Do not run destructive filesystem, firewall, routing or boot-recovery commands on production systems. Avoid unbounded stress tests. Use a disposable lab VM, snapshots, controlled duration and a rollback plan.

---

## 14. Interview question bank

### Linux
- How do you investigate a Linux server with high CPU?
- What is the difference between load average and CPU utilization?
- How do you troubleshoot memory exhaustion and OOM kills?
- A filesystem shows 100% usage. What do you check?
- `df` shows full disk but `du` does not. Why might that happen?
- A Linux VM fails to boot. How do you investigate?
- Apache is active but the application is unreachable. What do you check?

### Networking
- Explain what happens when a server connects to an HTTPS endpoint.
- How do you troubleshoot a server that cannot access the internet?
- How do you investigate a TCP connection timeout?
- What is the difference between connection refused and connection timed out?
- Explain TCP three-way handshake and retransmissions.
- How do you use `tcpdump` to locate packet loss?
- What happens when MTU is mismatched?

### GCP
- A VM cannot access the internet through Cloud NAT. How do you investigate?
- A load balancer reports an unhealthy backend. What do you check?
- A VPN tunnel is up but traffic does not pass. What next?
- How do you troubleshoot BGP route advertisement issues?
- What is the difference between PSA and PSC?
- How do you investigate PSA range exhaustion?
- A GKE cluster cannot allocate Pod IPs. What do you inspect?
- How do you investigate asymmetric routing?

### Databricks and Spark
- Explain Spark driver, executors, jobs, stages and tasks.
- What causes a Spark job to run slowly?
- What is a shuffle?
- What is data skew?
- How would you distinguish driver OOM from executor OOM?
- What would you investigate if a cluster fails to start?
- How would you approach an object-storage access failure?

### Incident management
- Describe a high-severity incident you handled.
- How do you prioritize mitigation versus root-cause analysis?
- How do you communicate during an ongoing outage?
- How do you handle disagreement during a war room?
- What should a useful RCA contain?
- How do you prevent recurrence?

---

## 15. Study method

For each topic, follow this cycle:

1. **Understand:** Learn the concept from first principles.
2. **Commands:** Learn command syntax and interpret real output.
3. **Lab:** Reproduce the issue safely in a test environment.
4. **Troubleshoot:** Follow evidence across application, OS, network and cloud layers.
5. **Explain:** State impact, findings, root cause, mitigation and prevention.
6. **Interview:** Solve a scenario aloud and explain why each diagnostic step matters.

Use one practical task at a time. Do not move to the next exercise until you can explain the current result and the reason behind each diagnostic step.

---

## 16. Final readiness checklist

### Technical
- [ ] I can write SQL queries independently and explain their output.
- [ ] I can write and troubleshoot Bash scripts.
- [ ] I can investigate Linux CPU, memory, OOM, disk, filesystem, boot and service issues.
- [ ] I can troubleshoot server-to-internet and server-to-server connectivity.
- [ ] I can explain OSI, TCP/IP, DNS, TCP handshake, routing, NAT, TLS and MTU.
- [ ] I can explain GCP VPC, Cloud NAT, Cloud Router, VPN, Interconnect, PSC, PSA, DNS, load balancing and GKE networking.
- [ ] I can investigate complex GCP incidents using logs, metrics, flow logs and packet captures.
- [ ] I can explain Databricks and Spark fundamentals accurately.
- [ ] I can review short Bash, Python and SQL code samples.
- [ ] I can explain core AI/GenAI concepts and risks.

### Senior support engineering
- [ ] I can structure a P0/P1 investigation.
- [ ] I can establish impact and scope.
- [ ] I can communicate concise customer updates.
- [ ] I can coordinate technical escalations and war rooms.
- [ ] I can produce an evidence-based RCA.
- [ ] I can propose preventive actions and validate them.
- [ ] I can explain my own experience with specific examples.
- [ ] I have completed at least one mock interview.

---

**Preparation principle:** Prioritize practical understanding, evidence-based troubleshooting, clear communication and honest representation of experience.
