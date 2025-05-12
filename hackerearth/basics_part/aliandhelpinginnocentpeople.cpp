#include<bits/stdc++.h>
using namespace std;


int main() {

/*
    012345678
    DDXDDD-DD

    // Valid Case
    tag[2] is consonant = Valid
    tag[0, 1, 3, 4, 5, 6, 8] if any consecuitive sum is even = Valid
    i+1 (+) i (%) 2
    22X222-22 => Valid


    // Invalid Case
    tag[2] is vowel = Invalid
    tag[0, 1, 3, 4, 5, 6, 8] if any consecuitive sum is odd = Invalid
    Sample:     12X345-67 => Invalid

*/

    string tag;
    cin >> tag;

    bool isCharOkay = true;
    char ch = tag[2];

    if(ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U' || ch == 'Y') {
        isCharOkay = false;
    }

    bool isSumOkay = true;
    int n = tag.size();

    vector<int>vec;

    for(int i = 0; i < n; i++){
          if(i == 2 || i == 6) {
            i++;
        }

        vec.push_back(tag[i]-'0');
    }

    int vs = vec.size();

    for(int i = 0; i < vs; i++) {
        if((vec[i+1] + vec[i])&1){
            isSumOkay = false;
            break;
        } else{
            isSumOkay = true;
        }
    }




    if(isSumOkay && isCharOkay) {
        cout << "valid" << "\n";
    } else {
    cout << "invalid" << "\n";
    }





return 0;
}

/*

   // 2 and 6 = ignore
    for(int i = 0; i < n; i++) {
        if(i == 2 || i == 6) {
            i++;
        }

        int sum = 0;
        sum = tag[i+1]-'0' + tag[i]-'0';
        printf("i = %d ---- tag[i+1] %c ---- tag[i] %c --- sum %d\n", i, tag[i+1], tag[i], sum);
        if(sum&1){
            isSumOkay = false;
            break;
        }


    }


*/
