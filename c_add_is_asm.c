int main(int argc, char *argv[])
{
	asm volatile(
	"mov x0,#40\n\t"
	"add x0,x0,#20\n\t"
	"mov x8,#93\n\t"
	"svc #0\n\t");
	return 0;
}

