#include<bits/stdc++.h>
using namespace std;

int main(){
	int n, x;
	cin >> n >> x;
	
	int arr[n+2];
	int s = 0;
	
	for(int i = 0; i < n; i++){
		cin >> arr[i];
		if(arr[i] <= x){
			s += arr[i];
		}
	}
	
	cout << s << "\n";
	
	
	
	
return 0;	
}
