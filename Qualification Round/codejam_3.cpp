
#include <stdio.h>      /* printf */
#include <stdlib.h>     /* strtol */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <list>
#include <iomanip>

int is_prime2(unsigned long long nb)
{
  //  for (unsigned long long i = 3; i < (sqrt(nb) + 1); i += 2)
  for (unsigned long long i = 3; i < (sqrtl(nb) + 1); i += 2)
    {
      if (nb % i == 0)
	{
	  return i;
	}
    }
  return 0;
}

std::string PrintAsBase(unsigned long long nb, int out_base)
{
  std::string result;
  int in_base = out_base;

  if(nb > 0)
    {
      for (unsigned long long in_num = nb; in_num > 0; in_num /= in_base)
	{
	  unsigned long long x = in_num % in_base;
	  if((x >= 0) and (x <= 9))
	    result += ('0' + x);
	  else
	    result += ('A' + (x - 10));
	}
      std::reverse(result.begin(), result.end());
    }
  else
    result = "0";
  return result;
}


int main()
{
  int N = 16;
  int J = 50;

  int output = 0;
  for (unsigned long long i = 0; i < (2LL << (N - 2)) && output < J; i++)
    {
      unsigned long long jam = (i << 1) + 1 + (2LL << (N - 1));
      bool flag = true;
      std::string strjam = PrintAsBase(jam, 2);
      std::list<unsigned long long> nbs;
      for (int base = 2; base <= 10; base++)
	{
	  long long nb = strtol(strjam.c_str(), NULL, base);
	  std::cout << nb << std::endl;
	  unsigned long long ntd = is_prime2(nb);
	  if (ntd == 0)
	    {
	      flag = false;
	      break;
	    }
	  nbs.push_back(ntd);
	  
	}
      if (flag)
	{
	  std::cout << strjam;
	  for (std::list<unsigned long long>::const_iterator it = nbs.begin(); it != nbs.end(); it++)
	    std::cout << " " << *it;
	  std::cout << std::endl;
	  output++;
	}
    }
  
}
