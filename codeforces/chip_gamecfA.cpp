
// https://codeforces.com/contest/1719/problem/A


#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(){

ll t;

cin >> t;

while(t--){
    int n, m;

    int x = 0;

    cin >> n >> m;

    x = (n + m);

    if(x&1){
        cout << "Burenka" << "\n";
    }else{
        cout << "Tonya" << "\n";
    }
}


return 0;
}








