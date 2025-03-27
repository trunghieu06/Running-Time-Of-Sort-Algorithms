#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

mt19937 rd(chrono::steady_clock::now().time_since_epoch().count());
ll rand(ll l, ll r) { return uniform_int_distribution<ll>(l, r)(rd); }

string intToString(int n) {
    return to_string(n);
}

void genRandomArray(int n) {
    string filename = "./random_arr/n" + intToString(n) + ".txt";
    ofstream fo(filename);
    fo << n << '\n';
    for (int i = 1; i <= n; ++i) {
        fo << rand(-1e4, 1e4) << ' ';
    }
    fo.close();
}

void genIncreasingArray(int n) {
    string filename = "./increasing_arr/n" + intToString(n) + ".txt";
    ofstream fo(filename);
    fo << n << '\n';
    int a[n];
    for (int i = 0; i < n; ++i) {
        a[i] = rand(-1e4, 1e4);
    }
    sort(a, a + n);
    for (int i = 0; i < n; ++i) {
        fo << a[i] << ' ';
    }
    fo.close();
}

void genDecreasingArray(int n) {
    string filename = "./decreasing_arr/n" + intToString(n) + ".txt";
    ofstream fo(filename);
    fo << n << '\n';
    int a[n];
    for (int i = 0; i < n; ++i) {
        a[i] = rand(-1e4, 1e4);
    }
    sort(a, a + n, greater<int>());
    for (int i = 0; i < n; ++i) {
        fo << a[i] << ' ';
    }
    fo.close();
}

void genNearlySortedArray(int n) {
    string filename = "./nearly_sorted_arr/n" + intToString(n) + ".txt";
    ofstream fo(filename);
    fo << n << '\n';
    int a[n];
    for (int i = 0; i < n; ++i) {
        a[i] = rand(-1e4, 1e4);
    }
    sort(a, a + n);
    int swappedPairs = n / 100;
    while (swappedPairs) {
        int i, j;
        do {
            i = rand(0, n);
            j = rand(0, n);
        } while (i == j);
        swap(a[i], a[j]);
        swappedPairs -= 1;
    }
    for (int i = 0; i < n; ++i) {
        fo << a[i] << ' ';
    }
    fo.close();
}

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int listOfLen[7] = {100, 500, 1000, 2000, 3000, 4000, 5000};
    for (int i = 0; i < 7; ++i) {
        genRandomArray(listOfLen[i]);
    }
    for (int i = 0; i < 7; ++i) {
        genIncreasingArray(listOfLen[i]);
    }
    for (int i = 0; i < 7; ++i) {
        genDecreasingArray(listOfLen[i]);
    }
    for (int i = 0; i < 7; ++i) {
        genNearlySortedArray(listOfLen[i]);
    }
    return 0;
}