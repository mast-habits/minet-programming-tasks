#include <iostream>
using namespace std;

int main() {
  int n;
  cout << "Enter the number of cubes you want to sum \n >>>>> ";
  cin >> n;
  int sum;
  int cubes[n];
  for( int i = 1; i<=n; i++ ) {
    cout << " " << i + "^3 = " + i*i*i << "\n";
    sum += i*i*i;
    cubes[i-1] = i*i*i;
  }
  cout << "\n ";
  for( int i = 0; i<n; i++){
      if(i!=n-1){
        cout << cubes[i] << " + ";
      } else {
          cout << cubes[i];
      }
  }
  cout << " = " << sum;
  cout << "\n \n The result is: " << sum;

  return 0;
}