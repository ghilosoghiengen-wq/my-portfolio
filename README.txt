# Android Local Security Auditing & Vulnerability Assessment Report

## Executive Summary
This project represents a professional security auditing assessment conducted locally on an unrooted **Android (Huawei/HarmonyOS)** environment utilizing **Termux**. The primary objective was to evaluate the kernel-level isolation, look for system-wide misconfigurations (World-Writable files), and perform a local network interface audit to identify potential privilege escalation vectors (Local Root/Emulator Escape) based on real-world security standards (CIS Benchmarks & Android Security Model).

The assessment concluded that the host environment employs a highly secure **Defense-in-Depth** architecture, strictly enforcing **SELinux Mandatory Access Control (MAC)** and kernel-level mitigations, making local exploit execution from unprivileged contexts practically impossible without an unpatched memory corruption zero-day.

---

## Environment Specification
- **Host OS:** Android (Huawei EMUI / HarmonyOS Build)
- **Kernel Version:** `4.14.116`
- **Architecture:** `aarch64` (ARM 64-bit)
- **Build Type:** `user` (Production Build)
- **Auditing Environment:** Termux (Unprivileged User Context)

---

## Auditing Methodology & Scripts

The repository contains custom-built automation scripts written in Python and Bash designed to perform targeted audits without relying on generic or noisy predefined fuzzers.

### 1. Local Privilege Escalation & Property Auditor (`one_systest.py`)
This script audits critical Android system properties and deeply scans deep system directories (`/proc`, `/sys`, `/dev`, `/data/local/tmp`) for insecure file permissions.

* **Key Findings:** 
  * Dangerous properties like `ro.debuggable` were found securely set to `0` and `ro.secure` set to `1`.
  * The tool successfully flagged temporary `World-Writable` configurations under `/proc/[PID]/attr/` and `/proc/[PID]/unexpected_die_catch` owned by Root. However, deeper analysis revealed these processes were isolated within the Termux container/process namespace, preventing global system tampering.

### 2. Local Network & IPC Interface Scanner (`one_portscan.py`)
A custom TCP socket scanner optimized for Android environments to probe for risky open local ports (e.g., exposed ADB on `5555` or unauthenticated IPC bridges on port ranges `8000-8100`).

* **Key Findings:** 
  * All checked TCP ports on `127.0.0.1` returned closed/secured.
  * Attempts to audit UNIX local sockets (`/proc/net/unix`) to map inter-process communications were completely blocked by the kernel, throwing a `[Errno 13] Permission Denied` exception.

---

## Defensive Mechanisms Analyzed (Why Exploits Failed)

During the assessment, an attempt was made to reproduce and cross-compile known 2023 public exploits, such as **OverlayFS (CVE-2023-0386)**. The attempt was successfully mitigated by the kernel, failing immediately at the `unshare()` system call with an `Invalid Argument` error.

### Hardening Techniques Identified:
1. **Disabled User Namespaces (`CONFIG_USER_NS=n`):** The Huawei kernel strictly disables unprivileged user namespaces, effectively mitigating a vast majority of logic-based container-escape and local root exploits.
2. **SELinux Strict Enforcement:** The kernel proactively blocks standard apps from accessing internal sockets and sensitive diagnostic telemetry interfaces, maintaining data isolation even when processes execute in the background.

---

## Conclusion & Key Takeaways
While no actionable vulnerability was found to achieve a local root on this specific target, the assessment successfully mapped out the device's exact security posture. Proving the efficiency of built-in mitigations is as vital to a **Bug Bounty Hunter / Security Auditor** as finding a vulnerability. It confirms that the system adheres to modern hardening compliance guidelines.

### Skills Demonstrated in this Repository:
* Linux/Android Security Architecture analysis.
* Automated and manual code review of known CVEs.
* Custom automation script development using Python (Socket programming & OS interaction).
* Meticulous log analysis and technical reporting.

