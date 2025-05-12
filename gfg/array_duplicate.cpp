#include<bits/stdc++.h>
using namespace std;


int main() {

int n; cin >> n;

int arr[n+2];

for(int i = 0; i < n; i++) {
    cin >> arr[i];
}

map<int, int> mp;

for(int i = 0; i < n; i++) {
    mp[arr[i]]++;
}

vector<int> vec;

for(auto i : mp) {
if(i.second > 1){
    vec.push_back(i.first);
}
}

if(vec.size() > 0) {

for(int i = 0; i < vec.size(); i++){
    cout << vec[i] << " ";
} cout << "\n";
} else {
    vec.push_back(-1);

for(int i = 0; i < vec.size(); i++){
    cout << vec[i] << " ";
} cout << "\n";
}


return 0;
}
