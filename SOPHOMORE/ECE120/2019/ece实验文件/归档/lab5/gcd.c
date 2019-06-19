#include <stdio.h>


// Calculate the Greatest Common Denominator/Divisor (GCD) of two
// positive integers extA and extB.
// NOTE: LIKELY TO TERMINATE IF EITHER VALUE IS 0 

unsigned int 
extOut (unsigned int extA, unsigned int extB)
{
    unsigned int A = extA;
    unsigned int B = extB;
    unsigned int C;
    unsigned int OUT;
    unsigned int swap;

    // Find the minimum of A and B and set A to the larger of the two,
    // and B to the smaller of the two.
    if (A < B) {
    	swap = A;
	A = B;
	B = swap;
    }

    // Set C to the remainder of A divided by B.  If C is zero, stop.
    // The GCD is B.  Otherwise, copy B to A and C to B, then start
    // over.
    for (C = A % B; 0 != C; C = A % B) {
        A = B;
	B = C;
    }

    // The GCD is B.  Return it.
    OUT = B;
    return OUT;
}


// Allow the user to specify two numbers.  Calculate the GCD of those
// two numbers and print it.
int
main (int argc, const char* const argv[])
{
    unsigned int one;
    unsigned int two;
    char         trash[2];

    if (3 > argc || 1 != sscanf (argv[1], "%u%1s", &one, trash) ||
	1 != sscanf (argv[2], "%u%1s", &two, trash) ||
	0 == one || 0 == two) { 
        fprintf (stderr, "syntax: %s <n1> <n2>\n        (both >0)\n", argv[0]);
	return 2;
    }

    printf ("GCD(%u,%u) is %u.\n", one, two, extOut (one, two));

    return 0;
}
