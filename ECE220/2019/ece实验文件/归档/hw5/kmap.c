#include <stdio.h>

int main ()
{
    unsigned int a, b, c, d;
    unsigned int f;

    /* Print header for K-map. */
    printf("          bc      \n");
    printf("      00 01 11 10 \n");
    printf("    +-------------\n");

    /* row-printing loop */
    for (a = 0; 2 > a; a = a + 1) {

        printf ("a=%d | ",a);

        /* Loop over input variable b in binary order. */
        for (b = 0; 2 > b; b = b + 1) {

            /* Loop over d in binary order. */
            for (d = 0; 2 > d; d = d + 1) {

                /* Use variables b and d to calculate *
                 * input variable c (iterated in      *
                 * Gray code order).                  */
                /* CALCULATE C HERE. */
		c=b^d;
                /* Calculate and print one K-map entry *
                 * (function f(a,b,c) ).               */
                /* INSERT CODE HERE. */
		f=(a&b&(~c))|c&(~a|~b)|((~b)&(~c)&1);
		printf("%d  ",f);
            }
        }

        /* End of row reached: print a newline character. */
        printf ("\n");
    }

    return 0;
}

