#include<stdio.h>
#include<conio.h>

int main()
{
    int a[5] = {5,2,3,4,1};
    int i,j,temp;
    printf("array before sorting:- ");
    for(i=0;i<5;i++)
        printf("%d",a[i]);

    for(i=0;i<4;i++)
    {
        for(j=i+1;j<5;j++)
        {
            if(a[i]>=a[j])
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

    printf("\n");
    printf("array after sorting:- ");
    for(i=0;i<5;i++)
        printf("%d",a[i]);
}