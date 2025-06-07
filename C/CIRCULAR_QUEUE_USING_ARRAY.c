// CIRCULAR QUEUE USING ARRAY
#include<stdio.h>
#define MAX 4
struct queue{
int a[MAX];
int f,r;
}q;
void cin(struct queue *q,int num){
if((q->f==q->r+1)||(q->f==0 && q->r==MAX-1)){
printf("\nQueue Overflow\nElement %d Cannot be able to insert in Queue\n\n",num);
return ;
}
printf("Element Inserted: %d\n",num);
if(q->r==MAX-1){
q->r=0;
}else{
q->r++;
q->a[q->r]=num;
if(q->f==-1)
q->f=0;
}
}
void c_delete(struct queue *q){
if(q->f==-1){
printf("\n\nQueue Underflow\nElement can not be able to delete further anymore\n\n");
return ;
}
printf("\nNumber Deleted: %d",q->a[q->f]);
q->a[q->f]=0;
if(q->f==q->r)
q->f=q->r=-1;
else{

if(q->f==MAX-1)
q->f=0;
else
q->f++;
}
}
int main(){
q.f=-1;
q.r=-1;
cin(&q,90);
cin(&q,95);
cin(&q,98);
cin(&q,99);
cin(&q,100);
for(int i=0;i<=MAX;i++){
c_delete(&q);
}
return 0;
}