#include <stdio.h>
int main() {
	int a = 2;
	int b = 2;
	int c = a + b;

	printf("C says: Hello, World!\n");
	printf("%d + %d = %d\n",a,b,c);

	char user[][5] = {"User1", "User2", "User3"};
	int listOfUsers; 
	for (listOfUsers = 0; listOfUsers < 3; listOfUsers++) {
		printf("%s\n", user[listOfUsers]);	
	}
	return 0;
}


