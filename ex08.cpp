#include<stdio.h>
 
int main()
{
	int i,j,k,n,a[30];
	printf("amount of elements of the array");
	scanf("%d",&n);
	printf("\nenter the numbers of the array\n");
	
	for(i=0;i<n;++i)
		scanf("%d",&a[i]);
		
	for(i=0;i<n;++i)
		for(j=i+1;j<n;)
		{
			if(a[i]==a[j])
			{
				for(k=j;k<n-1;++k)
					a[k]=a[k+1];
					
				--n;
			}
			else
				++j;
		}
	
	printf("\n");
	for(i=0;i<n;++i)
		printf("%d ",a[i]);
 
	return 0;
}