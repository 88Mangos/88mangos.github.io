#include <iostream>

using namespace std;

int main(){
    int N = 5;
    int M[N][2] = {
        {-14,12},
        {4,1},
        {30,0},
        {20,-11},
        {-7,-6}
    };

    float A = 0.5;

    long sum1 = 0;
    for (int i=1;i<=N;i++){
        sum1 += M[(i-1)][0] * M[((i)%N)][1];
    }
    cout << sum1 << endl;
    long sum2 = 0;
    for (int i=1;i<=N;i++){
        sum2 += M[(i-1)][1] * M[((i)%N)][0];
    }
    cout << sum2 << endl;
    A *= abs(sum1 - sum2);
    cout << "A: " << A << endl;
}