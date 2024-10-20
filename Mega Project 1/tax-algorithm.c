//Project made by Sumit Kudalkar
#include <stdio.h>

int main()

{
    int income;
    float tax;
    printf("enter your income : \n");
    scanf("%d", &income);

    if (income > 300000 && income <= 600000)
    {
        tax = 0.05;
        printf("the payable tax is : \n %.2f", 0.05 * (income - 300000));
    }

    else if (income > 600000 && income <= 900000)
    {
        tax = 0.10;
        printf("the payable tax is : \n %.2f", 0.05 * (600000 - 300000) + 0.10 * (income - 600000));
    }

    else if (income > 900000 && income <= 1200000)
    {
        tax = 0.15;
        printf("the payable tax is : \n %.2f", 0.05 * (600000 - 300000) + 0.10 * (900000 - 600000) + 0.15 * (income - 900000));
    }
    
    else if (income > 1200000 && income <= 1500000)
    {
        tax = 0.20;
        printf("the payable tax is : \n %.2f", 0.05 * (600000 - 300000) + 0.10 * (900000 - 600000) + 0.15 * (1200000 - 900000) + 0.20 * (income - 1200000));
    }
    
    else if (income > 1500000)
    {
        tax = 0.30;
        printf("the payable tax is : \n %.2f", 0.05 * (600000 - 300000) + 0.10 * (900000 - 600000) + 0.15 * (1200000 - 900000) + 0.20 * (1500000 - 1200000) + 0.30 * (income - 1500000));
    }
    
    else
    {
        printf("no tax required \n");
    }
    
    return 0;
}

