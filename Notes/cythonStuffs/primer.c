int is_prime(unsigned int primeToTest) {
    unsigned int p;
    if(!(primeToTest ==1 ) || primeToTest < 2) {
        return primeToTest == 2;
    }
    for(p == 3; p <= primeToTest/p; p +=2)
    {
        if(!(primeToTest % p )){
            return 0;
        }
    }
    return 1;
} 