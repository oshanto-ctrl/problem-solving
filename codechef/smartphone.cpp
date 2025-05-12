#include<bits/stdc++.h>
using namespace std;
typedef long long ll;



ll getRev(vector<ll>arr, ll n){
		ll maxRev = 0;
		sort(arr.begin(), arr.end(), greater<ll>());
		
		for(ll i = 0; i < n; i++){
			
			ll rev = arr[i]* (i+1);
			maxRev = max(maxRev, rev);
		}
		
	return maxRev;
		
}



// Driver
int main(){
	
	ll n;
	cin >> n;
	
	vector<ll>arr;
	
	for(ll i = 0; i < n; i++){
		ll a;
		cin >> a;
		arr.push_back(a);
	}
	
	ll result = getRev(arr, n);
	cout << result << "\n";
	
	return 0;
}
