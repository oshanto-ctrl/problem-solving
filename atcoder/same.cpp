#include<bits/stdc++.h>
using namespace std;


bool checkSame(int arr[], int n){
	
	if(n <= 1){
		return true;
	}
	
	int fl = arr[0];
	
	for(int i = 1; i < n; i++){
		if(arr[i] != fl){
			return false;
		}
	}
	
	return true;
}


int main() {
	
	int n;
	
	cin >> n;
	
	int arr[n+2];
	
	for(int i = 0; i < n; i++){
		cin >> arr[i];
	}
	
	if(checkSame(arr, n)){
		cout << "Yes" << "\n";
	} else{
		cout << "No" << "\n";
	}
	
	
	return 0;
}


















