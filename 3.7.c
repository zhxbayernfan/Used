#include<stdio.h>
#include<math.h>
int main()
{
const float pi=3.14159;
float r,h,c,s1,s2,v1,v2;
scanf("r=%f,h=%f",&r,&h);
c=pi*r*2;
s1=pi*r*r;
s2=4*pi*r*r;
v1=pi*r*r*r*4/3;
v2=s1*h;
printf("��Բ�뾶Ϊr=%5.2fʱ\n",r);
printf("Բ�ܳ�Ϊc=%5.2f\nԲ���Ϊs1=%5.2f\n",c,s1);
printf("����뾶Ϊr=%5.2fʱ\n",r);
printf("Բ������Ϊs2=%5.2f\nԲ�����Ϊv1=%5.2f\n",s2,v1);
printf("��Բ������뾶Ϊr=%5.2f,Բ����Ϊh=%5.2fʱ\n",r,h);
printf("Բ�����Ϊv2=%5.2f\n",v2);
return 0;
}