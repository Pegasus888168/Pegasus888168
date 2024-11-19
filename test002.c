#include <iostream>
using namespace std;

int main() 
{ 
    int input = 0; 
    cout << "輸入整數："; 
    cin >> input; 
    if(input % 2) {
        cout << input << " 為奇數" << endl; 
    }
    else { 
        cout << input << " 為偶數" << endl; 
    }
    return 0;
}
