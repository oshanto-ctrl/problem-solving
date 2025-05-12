#include<bits/stdc++.h>
using namespace std;

int main() {
    /*
        Problem Link:
        https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/bubble-sort-15-8064c987/
    */

    int n; cin >> n;

    int arr[n+2];

    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Bubble Sort to count swap
    int swap_count = 0;
    bool swapped = true;

    while(swapped) {

        swapped = false;
        swap_count++;

        for(int i = 0; i < n - 1; i++) {
            if(arr[i] > arr[i+1]) {
                swap(arr[i], arr[i+1]);
                swapped = true;
            }
        }
        n--;
    }


    // Print out the swap count
    cout << swap_count << "\n";



return 0;
}