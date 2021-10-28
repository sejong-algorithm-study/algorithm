#include <iostream>
using namespace std;

#define MAX 200
long long arr[MAX + 1][MAX + 1];
long long Sum(int c, int r)
{
    long long ans = 0;
    for(int i = 0 ; i <= c ; i++)
        ans += arr[i][r - 1];
    return ans;
}

int main(void)
{
    int n, k;
    cin >> n >> k;
    
    for (int i = 0 ; i < k ; i++)
        arr[0][i] = 1;
    for (int i = 1 ; i <= n ; i++)
    {
        for (int j = 1 ; j <= k ; j++)
        {
            if (j == 1)
                arr[i][j] = 1;
            else   
                arr[i][j] = Sum(i, j)%1000000000;
        }
    }
    cout << arr[n][k];
    
}