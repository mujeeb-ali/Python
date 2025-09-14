#include<iostream>
using namespace std;
   int add(int a,int b){
        int c = a+b;
        return c;
    }

void printFibonacci(int n) {
    int a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        std::cout << a << " ";
        int next = a + b;
        a = b;
        b = next;
    }
    std::cout << std::endl;
}

    int main(){

// int a = add(5,7);
//  cout<<a;

// cout<<"Hey";
// Function to print Fibonacci series up to n terms
printFibonacci(10);

    return 0;
}