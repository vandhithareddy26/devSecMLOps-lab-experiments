# devSecMLOps-lab-experiments
# DevSecMLOps Lab Experiments

A collection of laboratory experiments exploring security practices for machine learning operations (MLOps), including role-based access control, deployment authorization, runtime monitoring, static application security testing, and vulnerability remediation.

**GitHub Repository:** https://github.com/vandhithareddy26/devSecMLOps-lab-experiments

## Experiments

### Experiment 6: ML Pipeline with Role-Based Access Control (RBAC)

**Objective:** Implement role-based access control to protect operations in an ML pipeline.

**Key features:**
- Defines roles such as Data Engineer, Data Scientist, ML Engineer, Admin, and Viewer.
- Assigns permissions to different pipeline operations.
- Uses a decorator to enforce access permissions.
- Records access attempts in an audit log.
- Demonstrates authorized and unauthorized operations.
- Includes deployment authorization and runtime security monitoring.

**Files:**
- `Experiment6/Experiment6/exp6_rbac.py` — RBAC implementation and audit logging.
- `Experiment6/Experiment6/deploy_monitor.py` — deployment authorization, monitoring, and security event logging.
- `Experiment6/Experiment6/experiment6.html` — experiment presentation page.

### Experiment 8: Vulnerability Scanning in the ML Pipeline

**Objective:** Demonstrate how insecure Python code can be identified and remediated using Static Application Security Testing (SAST).

**Key features:**
- Demonstrates unsafe pickle deserialization.
- Identifies risks associated with `subprocess` calls using `shell=True`.
- Demonstrates the use of a weak MD5 hash.
- Shows the risk of hard-coded credentials.
- Provides a fixed version illustrating safer alternatives.
- Describes a workflow involving security scanning, remediation, and re-scanning.

**Files:**
- `Experiment8/Experiment8/exp8_vuln_sample.py` — deliberately vulnerable example for controlled security analysis.
- `Experiment8/Experiment8/exp8_fixed_sample.py` — example of remediation.
- `Experiment8/Experiment8/experiment8.html` — experiment presentation page.

## Technologies and Concepts

- Python
- Role-Based Access Control (RBAC)
- Secure ML deployment
- Audit logging and runtime monitoring
- Static Application Security Testing (SAST)
- Bandit vulnerability scanning
- Secure deserialization
- Command execution safety
- Cryptographic hashing
- Credential management

## Getting Started

### Prerequisites

- Python 3
- A terminal or command prompt
- Bandit, if you want to perform the vulnerability scan described in Experiment 8

### Run Experiment 6

Navigate to the experiment directory:

```bash
cd Experiment6/Experiment6
python exp6_rbac.py
```

To run the deployment and monitoring example:

```bash
python deploy_monitor.py
```

### Run Experiment 8

Navigate to the experiment directory:

```bash
cd Experiment8/Experiment8
python exp8_vuln_sample.py
```

Run the remediated example:

```bash
python exp8_fixed_sample.py
```

**Security note:** The vulnerable sample intentionally contains insecure patterns for educational analysis. Do not use it with untrusted files, real credentials, or production systems.

### Optional: Run Bandit

Install Bandit:

```bash
python -m pip install bandit
```

Scan the vulnerable example:

```bash
bandit exp8_vuln_sample.py
```

Scan the remediated example:

```bash
bandit exp8_fixed_sample.py
```

Review the reported findings and verify the results against the actual code. The presence or absence of a finding depends on the scanner version and its configuration.

## Learning Outcomes

After working through these experiments, students can explore:

1. How access permissions can protect ML pipeline operations.
2. How audit logs help record authorization decisions.
3. Why deployment authorization and runtime monitoring matter.
4. How static analysis can identify insecure coding patterns.
5. How remediation can improve code security.
6. Why secure credential handling and safer command execution are important in MLOps.

## Disclaimer

These experiments are intended for educational and laboratory use. The vulnerable code is included to demonstrate security risks and should not be used in production environments.

## Author

**Vandhitha Reddy**

GitHub: https://github.com/vandhithareddy26
