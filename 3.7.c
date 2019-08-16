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
printf("当圆半径为r=%5.2f时\n",r);
printf("圆周长为c=%5.2f\n圆面积为s1=%5.2f\n",c,s1);
printf("当球半径为r=%5.2f时\n",r);
printf("圆球表面积为s2=%5.2f\n圆球体积为v1=%5.2f\n",s2,v1);
printf("当圆柱底面半径为r=%5.2f,圆柱高为h=%5.2f时\n",r,h);
printf("圆柱体积为v2=%5.2f\n",v2);
return 0;
}