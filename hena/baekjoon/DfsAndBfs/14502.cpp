#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
#define MAX 8
bool visited[MAX][MAX];
int graph[MAX][MAX];
vector<pair<int, int>> v;
int SafeAreaCount;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void init()
{
    for (int i = 0 ; i < n ; i++)
    {
        for (int j = 0 ; j < m ; j++)
        {
            visited[i][j] = false;
        }
    }
}

void CountingSafeArea()
{
    int cnt = 0;
    for (int i= 0 ; i < n ; i++)
    {
        for (int j = 0 ; j < m ; j++)
        {
            if (graph[i][j] == 0 && !visited[i][j])
                cnt++;
        }
    }
    if (SafeAreaCount < cnt)
        SafeAreaCount = cnt;
}

void BFS()
{
    queue<pair<int, int>> q;
    init();
    for (int i = 0 ; i < v.size() ; i++){
        int x = v[i].first;
        int y = v[i].second;
        q.push({x, y});
    }
    
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0 ; i < 4 ; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0  || ny >=m)
                continue;
            if (!visited[nx][ny] && graph[nx][ny] == 0)
            {
                visited[nx][ny] = true;
                q.push({nx,ny});
            }
        }
    }
    CountingSafeArea();
    
}

void recursive(int x, int y, int cnt)
{
    if (cnt == 3)
    {
        BFS();
        // print();
        return ;
    }
    for (int i = x ; i < n ; i++)
    {
        for (int j = 0 ; j < m ; j++)
        {
            if (graph[i][j] == 0)
            {
                graph[i][j] = 1;
                recursive(i, j, cnt + 1);
                graph[i][j] = 0;
            }
        }
    }
}

void find()
{
    for (int i = 0 ; i < n ; i++)
    {
        for (int j = 0 ; j < m ; j++)
        {
            if (graph[i][j] == 2)
                v.push_back({i, j});
        }
    }
    // for (int i = 0 ; i < v.size() ; i++)
    //     cout << v[i].first << v[i].second << ' ';
}
void input()
{
    cin >> n >> m;
    for (int i = 0 ; i < n ; i++)
    {
        for (int j = 0 ; j < m ; j++)
        {
            cin >>graph[i][j];
        }
    }
}
int main()
{
    input();
    find();
    recursive(0,0,0);  
    cout << SafeAreaCount;
}