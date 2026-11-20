#include<unistd.h>

int main(int argc, char *argv[])
{
register long reslt asm("x2");
asm volatile(
"mov x0,#67\n\t"
"mov x1,#11\n\t"
"add %0,x0,x1\n\t"
:"=r" (reslt)
:
:"x0","x1"
);

char text[3];
text[0]=(reslt/10)+'0';
text[1]=(reslt%10)+'0';
text[2]='\n';

write(1,text,3);
return 0;

}
