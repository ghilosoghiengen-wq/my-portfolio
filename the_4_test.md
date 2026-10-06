## Phase 5: Kernel Callback Hijacking & Modprobe Path Manipulation Simulation

### 1. Conceptual Framework (Byward Execution)
To bypass the absolute hardware-enforced restrictions of the ARM64 processor at Exception Level 0 (User Space), the assessment advanced to analyzing logical subversion primitives within Exception Level 1 (Kernel Space). The target strategy shifts from executing direct unauthorized CPU code to tricking the Kernel into executing the payload on behalf of the unprivileged application, thereby rendering hardware-level constraints oblivious to the instruction.

### 2. Modprobe Path Subversion Primitives
The Linux Kernel relies on a compiled-in static memory pointer, **`modprobe_path`** (located at static offset `0xffffffff82e8a0e0` in the tested branch), to automatically spawn a user-mode helper utility under the absolute authority of **UID 0 (Root)** whenever an unknown socket protocol or unmapped hardware subsystem is requested by userland.

* **Exploitation Blueprint:**
  1. A target executable script (`trigger.sh`) is staged locally within the persistent sandbox environment to grant execution rights (`chmod 4755`) to the pre-compiled `root_shell`.
  2. Leveraging a Use-After-Free (UAF) or an out-of-bounds write primitive, the static `modprobe_path` buffer is overwritten in the kernel heap to point to our local executable script instead of `/sbin/modprobe`.
  3. A formal system request is sent by triggering an unmapped raw socket family (`socket(AF_INET, SOCK_RAW, 115)`).

### 3. Structural Analysis & Defense Assessment
During implementation on the production-grade target, the dispatching of the formal network trigger executed without causing a system panic. However, on highly secure production environments, modern kernels employ **`CONFIG_STATIC_USERMODEHELPER`** or compile `modprobe_path` as a read-only data structure (`__ro_after_init`). This acts as a complete logical mitigation, neutralizing the overwrite phase even when memory manipulation is achieved, ensuring absolute system integrity.

