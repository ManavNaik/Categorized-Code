#include <stdio.h>
int main()
{
 int m,n,op,a;
 printf("\nCALCULATOR \n. \n1.ADD \n2.SUBTRACT \n3.MULTIPLY \n4.DIVIDE \n \n");
 scanf("%d",&a);
 switch(a)
 {
  case 1:
printf("\n Enter any 2 number you want to ADD");
printf("\nEnter first number");
scanf("%d",&m);
printf("Enter second number");
scanf("%d",&n);
op=m+n;
printf("%d",op);
    break;
  case 2:
printf("\n Enter any 2 number you want to SUBTRACT"); 
printf("\nEnter first number");
scanf("%d",&m);
printf("Enter second number");
scanf("%d",&n);
op=m-n;
printf("%d",op);
    break;
  case 3:
  printf("\n Enter any 2 number you want to MULTIPLY");
  printf("\nEnter first number");
scanf("%d",&m);
printf("Enter second number");
scanf("%d",&n);
op=m*n;
printf("%d",op);
    break;
  case 4:
  printf("\n Enter any 2 number you want to DIVIDE");
  printf("\nEnter first number");
scanf("%d",&m);
printf("Enter second number");
scanf("%d",&n);
op=m/n;
printf("%d",op);
    break;
  case 5:
printf("\n ");
    break;
 }
return 0;
}