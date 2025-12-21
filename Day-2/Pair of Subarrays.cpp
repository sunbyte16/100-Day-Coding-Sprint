#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<long long> A(N + 1), prefix(N + 1, 0);
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
        prefix[i] = prefix[i - 1] + A[i];
    }

    // sum -> list of (L, R)
    unordered_map<long long, vector<pair<int,int>>> mp;

    for (int L = 1; L <= N; L++) {
        for (int R = L; R <= N; R++) {
            long long s = prefix[R] - prefix[L - 1];
            mp[s].push_back({L, R});
        }
    }

    long long ans = 0;

    for (auto &entry : mp) {
        auto &v = entry.second;

        // Sort by ending index
        sort(v.begin(), v.end(),
             [](auto &a, auto &b) {
                 return a.second < b.second;
             });

        int m = v.size();
        for (int i = 0; i < m; i++) {
            for (int j = i + 1; j < m; j++) {
                if (v[i].second < v[j].first) {
                    ans++;
                }
            }
        }
    }

    cout << ans << '\n';
    return 0;
}
