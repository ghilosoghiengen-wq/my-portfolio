#include<stdlib.h>
#include<unistd.h>
#include<string.h>

int main(int argc, char *argv[])
{
	char *buffer=(char*)malloc(7*sizeof(char));
	char *msg="لم يتم حجذ سئ من الذاكرا";
	if(buffer==NULL){
		write(1,msg,strlen(msg));
		return 1;
	}
	buffer[0]='h';
	buffer[1]='e';
	buffer[2]='l';
	buffer[3]='l';
	buffer[4]='o';
	buffer[5]='\n';
	buffer[6]='\0';
	write(1,buffer,7);
	free(buffer);
	return 0;
	
}

