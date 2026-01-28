#include <bits/stdc++.h>
#include <atcoder/fenwicktree>

using namespace std;

// 1行に整数1つ
int I() {
    int x;
    cin >> x;
    return x;
}

// 1行に空白区切りの整数複数
vector<int> LI() {
    string line;
    getline(cin, line);
    istringstream iss(line);
    vector<int> result;
    int num;
    while(iss >> num) {
        result.push_back(num);
    }
    return result;
}

// 1行に文字列1つ
string S() {
    string s;
    getline(cin, s);
    return s;
}

// 1行に空白区切りの文字列複数
vector<string> LS() {
    string line;
    getline(cin, line);
    istringstream iss(line);
    vector<string> result;
    string word;
    while(iss >> word) {
        result.push_back(word);
    }
    return result;
}

int main() {
    int N = I();
    vector<int> L(N);
    for(int i = 0; i < N; i++) {
        L[i] = I();
    }

    // ここに処理を書く

    return 0;
}