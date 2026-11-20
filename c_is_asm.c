int main(int argc, char *argv[])
{
	asm volatile(
	"mov x0,#55\n\t"
	"mov x8,#93\n\t"
	"svc #0");
	return 0;
}

