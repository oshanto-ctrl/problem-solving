#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	string str;
	
	cin >> n >> str;
	
	bool check = false;
	
	for(int i = 0; i < n; i++){
		if((str[i] == 'a' && str[i+1] == 'b') || (str[i] == 'b' && str[i+1] == 'a')){
			check = true;
			break;
		}else{
			check = false;
		}
			
	}
	
	if(check){
		cout << "Yes" << "\n";
	}else{
		cout << "No" << "\n";
	}
	
	
return 0;	
}

// defabb YES
// aaaaab YES
// bbbaa YES
// bbbia NO


