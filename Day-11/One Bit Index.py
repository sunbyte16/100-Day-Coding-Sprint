#include <bits/stdc++.h>
using namespace std;

bool isPowerOfTwo(long long x) {
    return x > 0 && (x & (x - 1)) == 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    if (!(cin >> N)) return 0;
    long long prefSum = 0;
    int goodCount = 0;

    for (int i = 0; i < N; ++i) {
        long long v;
        cin >> v;
        prefSum += v;
        if (isPowerOfTwo(prefSum)) {
            goodCount++;
        }
    }

    cout << goodCount << "\n";
    return 0;
}
