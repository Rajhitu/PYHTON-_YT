#include <bits/stdc++.h>
using namespace std;
int main()
{

    string s1, s2;

    cin >> s1>>s2;
    int *a, *b, *c;
    a = new int[ s1.length()];
    b = new int[ s2.length()];
    c = new int[max(s1.length(), s2.length())];

    for (int i = 0; i < s1.length(); i++)
    {
        a[i] = s1[i] - '0';
    }
    for (int i = 0; i < s2.length(); i++)
    {
        b[i] = s2[i] - '0';
    }

    int j = s1.length();
    int k = s2.length();
    int i = sizeof(c) / sizeof(int);
    int carry=0;
  
        while (k >= 0 && j >= 0)
        {
            if (a[j] + b[k] > 9)
            {       
            //    if(carry==1)
            //    {

            //     c[i] = ((a[j--] + b[k--]) % 10)+1;
            //     carry--;
                
            //    }
            //    else
               {

                  c[i--] = (a[j--] + b[k--]) ;
               }
                
                
                
            }
            else
            {   
            //     if(carry==1)
            //     {
            //         c[i] = a[j--] + b[k--]+1;
            //         carry=0;

            //     }
            //     else
                {
                    c[i--] = a[j--] + b[k--];
                }
              
            }
        }
    

    for (int i = 0; i < sizeof(c) / sizeof(int); i++)
    {
        cout << c[i];
    }

    return 0;
}