#include<stdio.h>
#include<conio.h>
int main()
{
    int a[5]={5,4,3,2,1};
    int i,j,k,temp;
    printf("array before sorting :- ");
    for(i=0;i<5;i++)
        printf("%d",a[i]);
    // insertion sorting     
    for(j=0;j<i;j++)
    {
        if(a[j]>a[i])
        {
            temp = a[j];
            a[j] = a[i];
            for(k=i;k>j;k--)
            a[k] = a[k-1];
            a[k+1] = temp;
        }
    }
    printf("\n");
    printf("array after sorting :- ");
    for(i=0;i<5;i++)
        printf("%d",a[i]);
    getch();    
}