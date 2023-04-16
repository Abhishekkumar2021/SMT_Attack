#include<bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]){
    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int out;
    if(a > b)
        out = a + 5;
    else
        out = b*3;
    printf("%d\n", out);
    return 0;
}
