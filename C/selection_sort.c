#include<stdio.h>
#include<conio.h>
int main()
{
    int a[5]={5,4,3,2,1};
    int i,k,temp;
    printf("array before sorting :- ");
    for(i=0;i<5;i++)
        printf("%d",a[i]);
    // selection sorting
    for(i=0;i<4;i++)
    {
        for(k=i+1;k<5;k++)
        {
            if(a[i]>=a[k])
            {
               temp = a[i];
               a[i] = a[k];
               a[k] = temp; 
            }
        }
    }
    printf("\n");
    printf("array after sorting :- ");
    for(i=0;i<5;i++)
        printf("%d",a[i]);
    getch();    
}