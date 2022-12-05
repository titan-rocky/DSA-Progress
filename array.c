#include<stdio.h>

int main()
{
	//pgm1
	long int arr[6]={3,14,55523,65536,1241153,1622221};
	int len_arr=sizeof(arr)/sizeof(arr[0]);
	int i;long int max=arr[0];
	for (i=1;i<len_arr;i++)
	{	
		if (max<arr[i])
		{
			max=arr[i];
		}


	}
	printf("Maximum = %ld\n",max);



	//pgm2
	//insertion_sort

	for (i=0;i<len_arr;i++)
	{
		long int key=arr[i];
		int index=0;
		while (index>=0 && key>arr[i])
		{
			arr[i]=arr[i-1];
			i-=1;
		}
		arr[i]=key;
	}

	printf("Sorted array = ");
	for (i=0;i<len_arr;i++)
	{

		printf("%ld ",arr[i]);

	}



	//pgm3
	//sorted array

	for (i=0;i<len_arr;i++)
	{
		
		
	}

	return 0;
}