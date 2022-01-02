#include <bits/stdc++.h>
using namespace std;

int decode(int i, int n) {
    return i % n;
};

bool is_equal(string a, string b, int start) {
    int n = a.size();
    int j = start;
    for (char i:b) {
        if (a[decode(j, n)] != i) {
            return false;
        }
        j++;
    }
    return true;
};

int hash_of_b(string b) {
    int h = 0;
    for (char i : b){
        h = h + (int)i;
    }
    return h;
};

int sum_of_a(string a, int k, int n) {
    int h = 0;
    int i = 0;
    while (i < k) {
        h = h + (int)a[decode(i, n)];
        i++;
    }
    return h;
};

int rsum(int h, char old, char newer) {
    return h - (int)old + (int)newer;
};

int repeatedStringMatch(string a, string b) {
    int n = a.size();
    int k = b.size();
    
    int sum_b = hash_of_b(b);
    int rolling_sum= sum_of_a(a, k, n);

    for (int i = 0; i < n; i++) {
        cout << rolling_sum << "\n";
        if (rolling_sum == sum_b && is_equal(a, b, i)) {
            return ceil((float)((i + k) / n));
        }
        rolling_sum = rsum(rolling_sum, a[decode(i, n)], a[decode(i + k, n)]);
    }
    return -1;
};

int main() {
string c = "abcd";
string d = "cdabcdab";
cout << repeatedStringMatch(c, d);
}