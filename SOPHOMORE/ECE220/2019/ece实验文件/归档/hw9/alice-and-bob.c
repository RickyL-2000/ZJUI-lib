#include <stdio.h>

int
main ()
{
    int room_number   = 0;	/* These variables represent FSM state. */
    int have_password = 0;
    int hacked_router = 0;
    int game_won      = 0;

    int choice;			/* Holds the user's choice of action. */

    printf ("Now in your junior year at Illinois, you have taken a 3-bedroom apartment\n");
    printf ("with your friends, security experts Alice and Bob.  It's Friday night, and\n");
    printf ("you really want to watch a movie, but you can't get enough network\n");
    printf ("bandwidth for high resolution.  Alice and Bob, while otherwise reasonable\n");
    printf ("people, own the network router, and have set a fixed sharing policy that\n");
    printf ("allows you only one-third of the bandwidth, even when they are out.\n");
    printf ("So outrageous.  You will need to take matters into your own hands.\n\n");

    printf ("<< STARTING THE GAME >>\n\n");

    for (; 0 == game_won; ) {
        if (0 == room_number) {
	    printf ("You are in your bedroom.  The ambience is perfect");
	    if (0 == hacked_router) {
		printf (", but you know that\n");
		printf ("as soon as you settle down to watch your movie, the bandwidth cap\n");
		printf ("will kick in.\n\n");
	    } else {
		printf (".\n\n");
	    }
	    printf ("Type 1 to head out into the common room.\n");
	    if (0 != hacked_router) {
	        printf ("Type 2 to watch your movie.\n");
	    }
	} else if (1 == room_number) {
	    printf ("You are in the common room.  Huge piles of dirty dishes glare at you\n");
	    printf ("from near the sink.  Maybe you should give up on the movie and just\n");
	    printf ("spend your Friday night washing dishes?  Nah, it's someone else's turn\n");
	    printf ("this time.\n\n");
	    printf ("Type 1 to head for your bedroom.\n");
	    printf ("Type 2 to go to Alice's room.\n");
	    printf ("Type 3 to enter Bob's room.\n");
	} else if (2 == room_number) {

	    printf ("You stand in Alice's bedroom.  Books on the last 50 years of security\n");
	    printf ("protocols, networking, distributed systems, and cryptography compete\n");
	    printf ("for space on her bookshelf.  Her matte black laptop beckons to you from\n");
	    printf ("the top of her desk.\n\n");

	    if (0 != hacked_router) {
		printf ("The router has recently been upgraded to allow dynamic sharing.  You\n");
		printf ("worry briefly about whether you left fingerprints on the laptop's keys.\n\n");
	    } else {
		printf ("Alice and Bob keep the router in this room.  You know that Alice leaves a\n");
		printf ("connection open from her laptop to the router's administrator account");
		if (0 == have_password) {
		    printf (",\nbut you have no way to log in to the laptop.\n\n");
		} else {
		    printf (".\n\n");
		}
	    }

	    printf ("Type 1 to return to the safety of the common room.\n");

	    if (0 == hacked_router && 0 != have_password) {
		printf ("Type 2 if you dare to try using what you found in Bob's room.\n");
	    }

	} else if (3 == room_number) {
	    printf ("Bob's room is really messy.  Dirty clothes are scattered over everything,\n");
	    printf ("from the stacks of detailed notes on security breeches and exploits to\n");
	    printf ("the open spaces between computers in his personal rack.  Even his dresser,\n");
	    printf ("where he presumably keeps his clean clothes, has dirty clothes piled on\n");
	    printf ("top of it.  Oh, and some really, really old pizza!\n\n");

	    if (0 == have_password) {
		printf ("You notice a scrap of paper peeking out at you from the pocket of a\n");
		printf ("sweaty shirt.  Is that a password???  Silly Bob!\n");
	    } else {
		printf ("The scrap of paper seems to be back where it was before you read it.\n");
	    }
	    printf ("\nType 1 to escape the mess and return to the common room.\n");
	    if (0 == have_password) {
	        printf ("Type 2 to read the curious scrap of paper.\n");
	    }
	}

	printf ("\nYour choice: ");
	if (1 != scanf ("%d", &choice)) {
	    printf ("\nAre you trying to break the game?  Nice try.\n");
	    return 3;
	}

	printf ("\n");
	if (0 == room_number) {
	    if (1 == choice) { 
		room_number = 1; 
	    } else if (2 == choice && 0 != hacked_router) {
		game_won = 1;
	    } else {
	        printf ("Unrecognized choice.\n\n");
	    }
	} else if (1 == room_number) {
	    if (1 == choice) {
	        room_number = 0;
	    } else if (2 == choice) {
	        room_number = 2;
	    } else if (3 == choice) {
	        room_number = 3;
	    } else {
	        printf ("Unrecognized choice.\n\n");
	    }
	} else if (2 == room_number) {
	    if (1 == choice) {
	        room_number = 1;
	    } else if (0 != have_password && 0 == hacked_router && 
	    	       2 == choice) {
	        hacked_router = 1;
	    } else {
	        printf ("Unrecognized choice.\n\n");
	    }
	} else if (3 == room_number) {
	    if (1 == choice) {
	        room_number = 1;
	    } else if (0 == have_password && 2 == choice) {
	        have_password = 1;
	    } else {
	        printf ("Unrecognized choice.\n\n");
	    }
	}
    }

    printf ("You settle down comfortably on your bed, press \"Play\" to start\n");
    printf ("the movie, and lay back to enjoy it.  Congratulations!\n\n");
    printf ("<< ENDING THE GAME >>\n\n");

    return 0;
}

