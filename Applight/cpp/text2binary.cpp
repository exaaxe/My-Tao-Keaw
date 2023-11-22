#include <iostream>
#include <bitset>
#include <string>

using namespace std;

int main() {
    string text;
    cout << "Enter text to convert to binary: ";
    getline(cin, text);

    cout << "Binary representation: ";
    for (char c : text) {
        cout << bitset<8>(c) << " ";
    }
    cout << endl;

    return 0;
}