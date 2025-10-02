#include <bits/stdc++.h>
using namespace std;

// Функція визначає день тижня за алгоритмом Zeller’s Congruence
// Повертає 0=Нд, 1=Пн, ..., 6=Сб
int day_of_week(int y, int m, int d) {
    if(m < 3) { m += 12; y--; }
    int K = y % 100;
    int J = y / 100;
    int h = (d + 13*(m+1)/5 + K + K/4 + J/4 + 5*J) % 7;
    return ((h + 6) % 7); // приводимо: 0=Нд, ..., 5=Пт, 6=Сб
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int K; cin >> K;
    long long ans = 0;
    while(K--){
        int A,B; cin >> A >> B;
        for(int year=A; year<=B; year++){
            for(int month=1; month<=12; month++){
                if(day_of_week(year, month, 13) == 5) // 5=П'ятниця
                    ans++;
            }
        }
    }
    cout << ans << "\n";
    return 0;
}
