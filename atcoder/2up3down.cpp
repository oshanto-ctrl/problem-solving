#include<bits/stdc++.h>
using namespace std;

int main(){
	
	int x, y;
	
	cin >> x >> y;
	
	if((x < y)){
		int steps = y - x;
		if(steps <= 2){
			cout << "Yes" << "\n"; // Up
		} else{
		cout << "No" << "\n"; // Lift
		}
	} else if((x > y)){
		int steps = x - y;
		if(steps <= 3){
			cout << "Yes" << "\n"; // Down
		}else{
		cout << "No" << "\n"; // Lift
		}	
		
	} else{
		cout << "No" << "\n"; // Lift
	}
	
		
	return 0;
}








