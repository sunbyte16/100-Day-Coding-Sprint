#include <bits/stdc++.h>
using namespace std;

struct State {
    int x, y, d;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;

    vector<string> grid(N);
    for (int i = 0; i < N; i++) {
        cin >> grid[i];
    }

    int Sx, Sy, Tx, Ty;
    cin >> Sx >> Sy >> Tx >> Ty;

    // Convert to 0-based indexing
    Sx--; Sy--;
    Tx--; Ty--;

    // visited[x][y][cooldown]
    vector<vector<vector<bool>>> visited(
        N, vector<vector<bool>>(M, vector<bool>(K + 1, false))
    );

    queue<State> q;
    q.push({Sx, Sy, K});   // start with no active echo
    visited[Sx][Sy][K] = true;

    int steps = 0;

    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    while (!q.empty()) {
        int sz = q.size();
        while (sz--) {
            State cur = q.front();
            q.pop();

            int x = cur.x;
            int y = cur.y;
            int d = cur.d;

            if (x == Tx && y == Ty) {
                cout << steps << "\n";
                return 0;
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M)
                    continue;
                if (grid[nx][ny] == 'T')
                    continue;

                // If echo cooldown active, empty cells are blocked
                if (d < K && grid[nx][ny] == '.')
                    continue;

                int nd;
                if (grid[nx][ny] == 'E')
                    nd = 0;
                else
                    nd = min(K, d + 1);

                if (!visited[nx][ny][nd]) {
                    visited[nx][ny][nd] = true;
                    q.push({nx, ny, nd});
                }
            }
        }
        steps++;
    }

    cout << -1 << "\n";
    return 0;
}
