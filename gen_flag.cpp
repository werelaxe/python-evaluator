#include <stdio.h>
#define import typedef
#define math char
#define collections int
#define q for
#define pr printf
#define x const
#define j void
#define u return
#define b main
import math l;
import collections z;
x l*_="alfagagacpwifialfagagacpwifi";j f(z*p){q(z i=0;i<26;i++)p[i]^=i;}j g(z*p){q(z i=0;i<26;i++){f(p);p[i]^=_[i];}}z b(){z s[26]={39,36,40,54,38,54,62,39,39,53,34,55,57,33,61,60,63,62,37,39,39,43,49,50,43,53};f(s);g(s);q(z i=0;i<26;i++)pr("%c",s[i]);u 0;}