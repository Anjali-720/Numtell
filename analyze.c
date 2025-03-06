#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}

bool is_armstrong(int n) {
    int original = n, sum = 0, digits = 0;
    while (original != 0) {
        digits++;
        original /= 10;
    }
    original = n;
    while (original != 0) {
        int digit = original % 10;
        sum += pow(digit, digits);
        original /= 10;
    }
    return sum == n;
}

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);

    printf("Even/Odd: %s\n", (number % 2 == 0) ? "Even" : "Odd");
    printf("Prime: %s\n", is_prime(number) ? "Yes" : "No");
    printf("Armstrong: %s\n", is_armstrong(number) ? "Yes" : "No");
    printf("Square: %d\n", number * number);
    printf("Cube: %d\n", number * number * number);
    printf("Binary: ");
    for (int i = 31; i >= 0; i--) {
        printf("%d", (number >> i) & 1);
    }
    printf("\n");
    return 0;
}
