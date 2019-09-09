;decription part
;Firstly, this program calculate the memory location through X,Y
;Secondly, read the value T in this memory location.
;Thirdly, calculate V through expression and store V into this memory location
;X through 0 to 78, when X reset to 0, Y add 1
;when y=24, x=78, end this part
;R0	X
;R1	Y
;R2	x5000 or (S AND x000F)
;R3	T
;R4	S or -78
;R5	Q or 79
;R6	temporary register or V
;screen-drawing part 
;read value V stored in 1975 consecutive memory location starting at x5000 and print out 
;each value V respectively
;R0	V or line breaker
;R1	X 
;R2	Y
;R3	memory location
;R4	-78
;R5	79
;R6	temporary register
	
	.ORIG x3000
	AND R0,R0,#0	;R0 store X
	AND R1,R1,#0	;R1 store Y
;calculate memory location and read T
START	LD R6,NUMONE	;R6 store 79
	LD R2,ADDRONE	;R2 store x5000
	ADD R2,R2,R0	;add X
LOOPA	ADD R2,R2,R1	;add 79*Y
	ADD R6,R6,#-1	;
	BRp LOOPA	;R2 store x5000+X+79*Y
	ST R2,ADDRTWO	;store x5000+X+79*Y into x4000
	LDR R3,R2,#0	;R3 store T

;Calculate S
	NOT R4,R0	;
	NOT R5,R3	;
	AND R4,R4,R3	;
	AND R5,R5,R0	;
	ADD R4,R4,R5	;R4 store S

;Calculate Q
	ADD R5,R1,R1	;
	ADD R5,R5,R0	;
REMAIN	ADD R5,R5,#-10	;
	BRzp REMAIN	;
	ADD R5,R5,#10	;
	ADD R5,R5,#7	;R5 store Q

;Calculate V
	AND R2,R4,#15	;R2 store (S AND x000F)
	AND R3,R3,#0	;clear R3
SHIFT	ADD R3,R3,#1	;calculate S>>4
	ADD R4,R4,#-16	;
	BRzp SHIFT	;
	ADD R3,R3,#-1	;R3 store (S>>4)
	AND R6,R6,#0	;clear R6
MULT	ADD R6,R3,R6	;Calculate (S>>4)*Q,stre in R6
	ADD R5,R5,#-1	;
	BRp MULT	;
	ADD R6,R6,R2	;R6 store V

;Store V to original memory
	LD  R2,ADDRTWO	;
	STR R6,R2,#0	;store V into (x5000+X+79*Y)

;judge if X or Y is in edge
	LD R4,NUMTWO	;R4 store -78
	LD R5,NUMONE	;R5 store 79
	ADD R0,R0,R4	;
	BRzp NEXT	;if X =78, reset X = 0, go to calculate Y
	ADD R0,R0,R5	;
	BRnzp START	;X through 0 to 78
NEXT	ADD R6,R1,#-12	;judge whether Y is equal to 24, if true, go to screen-drawing part 
	ADD R6,R6,#-12	;
	BRzp PSCR	;
	ADD R1,R1,#1	;Y add 1
	BRnzp START	;Y through 0 to 24 

;screen-drawing part 
PSCR 	AND R1,R1,#0	;R1 store X
	AND R2,R2,#0	;R2 store Y
STARTB	LD  R3,ADDRONE	;R3 store x5000
	LD  R6,NUMONE	;R6 store 79
	ADD R3,R3,R1	;add X
LOOPB	ADD R3,R3,R2	;add 79*Y
	ADD R6,R6,#-1	;
	BRp LOOPB	;R3 store x5000+X+79*Y
	LDR R0,R3,#0	;load mem[x5000+X+79*Y] into R0
	TRAP x21	;print out 

;judge if X or Y is in edge
	LD R4,NUMTWO	;R4 store -78
	LD R5,NUMONE	;R5 store 79
	ADD R1,R1,R4	;X through 0 to 78
	BRzp NEXTB	;if X =78, reset X = 0, go to calculate Y
	ADD R1,R1,R5	;
	BRnzp STARTB	;X through 0 to 78
NEXTB	LD R0,LINE	;
	TRAP x21	;when X reset to 0, print line breaker.
	ADD R6,R2,#-12	;judge whether Y is equal to 24, if true, stop the program
	ADD R6,R6,#-12	;
	BRzp DONE	;
	ADD R2,R2,#1	;Y add 1
	BRnzp STARTB	;Y through 0 to 24

;DATA	
ADDRONE	.FILL x5000	;
ADDRTWO	.FILL x4000	;	
NUMONE	.FILL x004F	;79
NUMTWO	.FILL xFFB2	;-78
LINE	.FILL x000A	;

;STOP
DONE	TRAP x25
	.END
