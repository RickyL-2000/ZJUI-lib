#include <stdio.h>

int
main ()
{
    unsigned int S3 = 0; /* state bits for counter with serial gating */
    unsigned int S2 = 0;
    unsigned int S1 = 0;
    unsigned int S0 = 0;
    unsigned int G2;     /* helper variables for serial gating */
    unsigned int G1;
    unsigned int G0;
    unsigned int P3 = 0; /* state bits for counter with parallel gating */
    unsigned int P2 = 0;
    unsigned int P1 = 0;
    unsigned int P0 = 0;
    int i;

    /* Print header for output. */
    printf ("cycle serial parallel\n");

    /* Simulate 16 cycles. */
    for (i = 0; 16 > i; i = i + 1) {
        
	/* Print counter state. */
	printf ("%4d   %d%d%d%d     %d%d%d%d\n", 
		i, S3, S2, S1, S0, P3, P2, P1, P0);

	/* Calculate serial AND gate outputs. */
	G0 = S0;
	G1 = (G0 & S1);
	G2 = (G1 & S2);

        /* Advance serial counter. */
	S0 = (S0 ^ 1);
	S1 = (S1 ^ G0);
	S2 = (S2 ^ G1);
	S3 = (S3 ^ G2);

	/* Advance parallel counter. */
	P0 = (P0 ^ 1);
	P1 = (P1 ^ P0);
	P2 = (P2 ^ (P1 & P0));
	P3 = (P3 ^ (P2 & P1 & P0));
    }

    return 0;
}
