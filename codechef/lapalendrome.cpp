#include<bits/stdc++.h>
using namespace std;

// Check equal frequency
bool equalFreq(string f, string l){
		unordered_map<char, int> ff, fl;
		
		for(char ch : f){
			ff[ch]++;
		}
		
		for(char ch : l){
			fl[ch]++;
		}
		
	return ff == fl;
}

// Check equal characters
bool equalChar(string f, string l){
	string sorted_f = f;
	string sorted_l = l;
	
	sort(sorted_f.begin(), sorted_f.end());
	sort(sorted_l.begin(), sorted_l.end());
	
	return sorted_f == sorted_l;
}

// odd string checker
void odd(string str, int n){
	string f = "";
	string l = "";
	
	
	for(int i = 0; i < n/2; i++){
		f += str[i];
	}
	
	for(int i = (n/2)+1; i < n; i++){
		l += str[i];
	}
	
	// cout << "First " << f << "\n";
	// cout << "Last " << l << "\n";
	
	if(equalChar(f, l) && equalFreq(f, l)){
		cout << "YES\n";
	}else{
		cout << "NO\n";
	}
}

// even string checker
void even(string str, int n){
	string f = "";
	string l = "";
	
	for(int i = 0; i < n / 2; i++){
		f += str[i];
	}
	
	for(int i = n / 2; i < n; i++){
		l += str[i];
	}
	
	
	// cout << "First " << f << "\n";
	// cout << "Last " << l << "\n";
	
	if(equalChar(f, l) && equalFreq(f, l)){
		cout << "YES\n";
	}else{
		cout << "NO\n";
	}
	
}

// Driver

int main(){
	
	int t;
	cin >> t;
	
	while(t--){
		string str;
		cin >> str;
		
		int n = str.size();
		
		if(n%2 != 0){
			odd(str, n);
		}else{
			even(str, n);
		}
		
	}
	
	return 0;
}























