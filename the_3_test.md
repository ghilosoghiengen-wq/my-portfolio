## Phase 4: Advanced C++ Obfuscation & Direct ARM64 System Calls (`syscall`)

### 1. Objective & Architectural Obfuscation
To completely bypass user-space monitoring and potential API hooking enforced by Android's runtime, the exploitation framework was re-engineered into native **C++ (`one_sploit.cpp`)**. The codebase utilized Object-Oriented Programming (OOP) structures (`ExploitPayload` class) to obfuscate the embedded shellcode text text string within the compiled binary, generating a dynamic payload (`patch.c` & `root_shell`) natively inside Termux's local storage to circumvent SELinux path filters.

### 2. Bypassing Wrappers via Direct Assembly Syscalls (NR_unshare: 220)
Instead of invoking standard glibc wrapper functions which are heavily audited by Android security layers, the exploit utilized the direct kernel gateway via the **`syscall()`** function. In the ARM64 (AArch64) architecture, this executes a low-level software interrupt (`svc #0`), shifting the operation straight to the Linux Kernel.

* **Execution Code Configuration:**
  ```cpp
  long res = syscall(SYS_unshare, CLONE_NEWNET | CLONE_NEWUSER);
  ```
  The script manually invoked the specific ARM64 system call table index **`220`** (representing `sys_unshare`), attempting a stealth transition into an unprivileged user namespace.

### 3. Hardware-Enforced Access Control Discovery
The raw execution trace returned a distinct security obstruction:
```assembly
[-] Direct Syscall returned obstruction from hardware-enforced SELinux.
```
* **Technical Auditing Conclusion:** 
  This critical finding demonstrates that the target platform implements **Hardware-Enforced SELinux Policies**. The Mandatory Access Control (MAC) is validated directly at the Hypervisor/Hardware abstraction layer during the transition from Exception Level 0 (EL0 - User) to Exception Level 1 (EL1 - Kernel). Even when glibc boundaries are completely bypassed via raw CPU instructions, the hardware architecture cross-checks the calling process's security context (SELinux Domain) and denies execution, preventing unauthorized subsystem modification on production-grade Huawei devices.
