#include <bits/stdc++.h>
using namespace std;

int n;              // size of a
int k;              // size of b
int prime = 101;    // prime for hashign
int base = 128;     // no of bits we need for a char
int offset;         // if offset = 100-> 9 -> 00

int decode(int i) {
    return i % n;
};

bool is_equal(string a, string b, int start) {
    int j = start;
    for (char i:b) {
        if (a[decode(j)] != i) {
            return false;
        }
        j++;
    }
    return true;
};

int hash_of_b(string b) {
    int h = 0;
    for (char i : b){
        h = (((h + prime) * base) + (int)i) % prime;
    }
    return (h + prime) % prime;
};

int hash_of_a(string a) {
    int h = 0;
    int i = 0;
    while (i < k) {
        h = (((h + prime) * base) + (int)a[decode(i)]) % prime;
        i++;
    }
    return (h + prime) % prime;
};

int offset_of(int k) {
    k = k - 1;
    int off = 1;
    for (int i = 0; i < k; i++) {
        off = (off * base) % prime;
    }
    return off;
}

int rhash(int h, char old, char newer) {
    return ((h + prime - (int)(old) * offset) * base + (int)newer) % prime;
};

int repeatedStringMatch(string a, string b) {
    n = a.size();
    k = b.size();
    offset = offset_of(k);
    
    int hash_b = hash_of_b(b);
    int rolling_hash = hash_of_a(a);

    for (int i = 0; i < n; i++) {
        cout << rolling_hash << "\n";
        if (rolling_hash == hash_b && is_equal(a, b, i)) {
            return ceil((float)((i + k) / n));
        }
        rolling_hash = rhash(rolling_hash, a[decode(i)], a[decode(i + k)]);
    }
    return -1;
};

int main() {
string c = "abcd";
string d = "cdabcdab";
cout << repeatedStringMatch(c, d);
}