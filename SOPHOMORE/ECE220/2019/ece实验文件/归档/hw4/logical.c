/*									tab:8
 *
 * logical.c - print a 3-variable truth table
 *
 * "Copyright (c) 2017 by Steven S. Lumetta."
 *
 * Permission to use, copy, modify, and distribute this software and its
 * documentation for any purpose, without fee, and without written agreement is
 * hereby granted, provided that the above copyright notice and the following
 * two paragraphs appear in all copies of this software.
 * 
 * IN NO EVENT SHALL THE AUTHOR OR THE UNIVERSITY OF ILLINOIS BE LIABLE TO 
 * ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL 
 * DAMAGES ARISING OUT  OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, 
 * EVEN IF THE AUTHOR AND/OR THE UNIVERSITY OF ILLINOIS HAS BEEN ADVISED 
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 * 
 * THE AUTHOR AND THE UNIVERSITY OF ILLINOIS SPECIFICALLY DISCLAIM ANY 
 * WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF 
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE SOFTWARE 
 * PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND NEITHER THE AUTHOR NOR
 * THE UNIVERSITY OF ILLINOIS HAS ANY OBLIGATION TO PROVIDE MAINTENANCE, 
 * SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS."
 *
 * Author:	    Steve Lumetta
 * Version:	    1
 * Creation Date:   25 January 2017
 * Filename:	    logical.c
 * History:
 *	SL	1	25 January 2017
 *		First written.
 */


#include <stdio.h>


int
main ()
{
    unsigned int A; /* input variables */
    unsigned int B;
    unsigned int C;
    unsigned int Q; /* output variables */
    unsigned int R;

    /* Print a header for the truth table. */
    printf (" A B C | Q R\n");
    printf ("-------+-----\n");

    /* Loop over all input combinations. */
    for (A = 0; 1 >= A; A = A + 1) {
	for (B = 0; 1 >= B; B = B + 1) {
	    for (C = 0; 1 >= C; C = C + 1) {

		/*
		 * Calculate the output Q.  Discard all but the low bit from 
		 * the logic expression by bitwise ANDing with 1.
		 */
		Q = (((A & B) ^ (A & (~C)) ^ ((~B) & (~C))) & 1);

		/*
		 * Calculate the output R.  You must rewrite this 
		 * calculation to use only the input variables and
		 * the functions AND, OR, and NOT.
		 */
		 R= (A & B & C)|((~A) & (~B) & (~C) & 1);

		/* Print a row of the truth table. */
	        printf (" %d %d %d | %d %d\n", A, B, C, Q, R);
	}
	    }
	}

	
	
    /* Success! */
    return 0;
}

