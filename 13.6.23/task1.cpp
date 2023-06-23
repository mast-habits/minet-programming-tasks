#include <iostream>
using namespace std;

int main() {
  int n;
  cout << "How many terms of fibonacci do you want? (enter a no more than 2) \n >>>>> ";
  cin >> n;
  int a = 0;
  int b = 1;
  int c;
  int results[n];
  results[0] = a;
  results[1] = b;
  for (int i = 0; i < n; i++)
  {
    c = a+b;
    results[i+2] = c;
    a = b;
    b = c;
    cout << results[i] << "\n";
  }
  
  return 0;
}
