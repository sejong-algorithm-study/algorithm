#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 20
using namespace std;


int Array[MAX][MAX];
vector <int> commands;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};


bool ispossible(int x, int y, int n, int m)
{
    if (x < 0 || x >= n || y < 0 || y >= m)
        return false;
    return true;
}

void change(int *top, int *down, int *front, int * back, int * left, int * right, int dir, int x, int y)
{
    int tmp;
    if (dir == 1){
        tmp = *top;*top = *left;*left = *down;*down = *right;*right = tmp;
    }
    else if (dir == 2){
        tmp = *top;*top = *right;*right = *down;*down = *left;*left = tmp;
    }
    else if (dir == 3){
        tmp = *top;*top = *back;*back = *down;*down = *front;*front = tmp;
    }
    else if (dir == 4){
        tmp = *top;*top = *front;*front = *down;*down = *back;*back = tmp;
    }
    if (Array[x][y])
    {
        *down = Array[x][y];
        Array[x][y] = 0;
    }
    else
        Array[x][y] = *down;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n, m, x, y, k;
    cin >> n >> m >> x >> y >> k;

    //입력
    for (int i = 0 ; i < n ; i++)
    {
        for (int j = 0 ; j < m ; j++)
        {   
            int num;
            cin >> num;
            Array[i][j] = num;
        }
    }

    //명령어 입력
    for (int i = 0 ; i < k ; i++){
        int num;
        cin >> num;
        commands.push_back(num);
    }
    
    int top = 0, down = 0, front = 0, back = 0, left = 0, right = 0;
    for (int i = 0 ; i < k ; i++){
        int nx = x + dx[commands[i] - 1];
        int ny = y + dy[commands[i] - 1];
        if (!ispossible(nx, ny, n, m))
            continue;
        
        change(&top, &down, &front, &back, &left, &right, commands[i], nx, ny);
        cout << top << '\n';
        x = nx;
        y = ny;
    }
}