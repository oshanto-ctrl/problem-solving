#include<bits/stdc++.h>
using namespace std;

int main(){
	
	int t;
	cin >> t;
	
	while(t--){
		
	string cf = "codeforces";
	bool check = false;
	char c;
	
	cin >> c;
	
	for(int i = 0; i < 10; i++){
		if(cf[i] == c){
			check = true;
			break;
		}
	}
		
		if(check){
			cout << "YES" << "\n";
		} else{
			cout << "NO" << "\n";
		}

}
	
	
	return 0;
}
