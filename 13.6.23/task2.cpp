#include <iostream>
using namespace std;

int main() {
  int n;
  cout << "How many lines of * do you want? \n";
  cin >> n;
  int x = 1;
  for(int i = 0; i<n; i++){
  	for(int j = 0; j<i+1; j++) {
  	    cout << "*";
  	}
  	cout << "\n";
  }
  return 0;
}
