/*									tab:8
 *
 * signals.c - validate functional form of lab outputs A and P
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
 * Creation Date:   8 February 2017
 * Filename:	    signals.c
 * History:
 *	SL	1	8 February 2017
 *		First written.
 */


#include <stdio.h>


int main ()
{
    unsigned int S2; /* FSM state variables */
    unsigned int S1;
    unsigned int S0;
    unsigned int A; /* output variables for SOP/POS */
    unsigned int P;
    unsigned int A_n; /* output variables for NAND/NOR */
    unsigned int P_n;

    /* Print a header for the truth table. */
    printf (" S2 S1 S0 | A P | A_n P_n\n");
    printf ("----------+-----+---------\n");

    /* Loop over all input combinations. */
    for (S2 = 0; 1 >= S2; S2 = S2 + 1) {
        for (S1 = 0; 1 >= S1; S1 = S1 + 1) {
            for (S0 = 0; 1 >= S0; S0 = S0 + 1) {

                /*
                 * Only print combinations for which
                 * outputs A and P are defined.
                 */
                if (1 != S1 || 1 != S0) {

                    /*
                     * Calculate the outputs as SOP or POS using AND, OR,
                     * and NOT.  Discard all but the low bit from
                     * the logic expressions by bitwise ANDing with 1.
                     */
                    /* WRITE CODE HERE USING SOP OR POS FORMS */
                    A = (S2|(~S0))&(((~S2)|(~S1))&0x1);
                    P = (S2|S1)&(S0|(~S2));

                    /*
                     * Calculate the outputs using only NAND, NOR,
                     * and NOT.  Note that you must construct these
                     * operators from AND, OR, and NOT in C.  For
                     * example, A NAND B is written as (~(A & B)).
                     * Discard all but the low bit from the logic
                     * expressions by bitwise ANDing with 1.
                     */
                    /* WRITE CODE HERE USING NAND OR NOR FORMS */
                    A_n = (~((~(S2|(~S0)))|(~((~S2)|(~S1)))))&0x1;
                    P_n = (~((~(S2|S1))|(~(S0|(~S2)))))&0x1;

                    /* Print a row of the truth table. */
                    printf ("  %d  %d  %d | %d %d |  %d   %d\n",
                            S2, S1, S0, A, P, A_n, P_n);
                }
            }
        }
    }

    /* Success! */
    return 0;
}
