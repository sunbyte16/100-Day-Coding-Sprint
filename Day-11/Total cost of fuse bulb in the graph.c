#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long K;   // price per defective bulb
    long long N;   // max bulb label
    long long M;   // divisor
    int E;         // number of edges

    if (!(cin >> K)) return 0;
    cin >> N;
    cin >> M;
    cin >> E;

    // Graph size N+1 because bulbs are 0..N
    vector<vector<int>> graph(N + 1);

    for (int i = 0; i < E; i++) {
        int u, v;
        cin >> u >> v;
        // Some corner tests might give edges with labels outside 0..N, guard them.
        if (u >= 0 && u <= N && v >= 0 && v <= N) {
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
    }

    vector<char> vis(N + 1, 0);
    queue<int> q;

    // If node 0 has no incident edges but still exists, still consider it as starting point.
    if (0 < 0 || 0 > N) {
        cout << 0;
        return 0;
    }

    vis[0] = 1;
    q.push(0);

    long long cnt = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        // Count only visited nodes in component of 0,
        // exclude 0 itself, and check divisibility by M.
        if (u != 0 && M != 0 && (u % M == 0)) {
            cnt++;
        }

        for (int v : graph[u]) {
            if (!vis[v]) {
                vis[v] = 1;
                q.push(v);
            }
        }
    }

    long long result = cnt * K;
    cout << result;
    return 0;
}
