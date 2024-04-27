#include <stdio.h>
#include <string.h>
#define d 256
void search(char pat[], char txt[], int q)
{
int M = strlen(pat);
int N = strlen(txt);int i, j;
//p will store the hash value of the pattern.
// t will store the hash value of the current substring of the text being compared to the pattern.
// h is a variable used in the calculation of the rolling hash function
int p = 0;
int t = 0;
int h = 1;

for (i = 0; i < M - 1; i++)
h = (h * d) % q;
for (i = 0; i < M; i++) {
p = (d * p + pat[i]) % q;
t = (d * t + txt[i]) % q;
}
for (i = 0; i <= N - M; i++) {
if (p == t) {
for (j = 0; j < M; j++) {
if (txt[i + j] != pat[j])
break;
}
if (j == M)
printf("Pattern found at index %d\n", i);
}
if (i < N - M) {
t = (d * (t - txt[i] * h) + txt[i + M]) % q;
if (t < 0)
t = (t + q);}
}
}
int main()
{
char txt[100];
char pat[100];
int q;
printf("------------- RABIN-KARP ALGORITHM -------------\n\n");
printf("Enter the text: ");
scanf("%s", txt);
printf("Enter the pattern: ");
scanf("%s", pat);
printf("Enter a prime number: ");
scanf("%d", &q);
search(pat, txt, q);
return 0;
}
