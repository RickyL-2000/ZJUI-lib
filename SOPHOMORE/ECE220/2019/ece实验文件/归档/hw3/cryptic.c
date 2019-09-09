#include <stdint.h>
#include <stdio.h>

int
main ()
{
    char id[16];
    uint32_t hash = 0;
    char* s;
    char key[10];
    int32_t val;
    int32_t i;
    
    printf ("Please type your campus ID number: ");
    if (1 != scanf ("%15s", id)) {
        printf ("Invalid.  Type a longer ID.\n");
	return 3;
    }

    for (s = id; '\0' != *s; s++) {
        hash ^= ((hash << 5) + (*s << 3) + *s);
    }

    printf ("ID   : \"%s\"\n", id);
    printf ("hash : %08X\n", hash);

    for (i = 0; 10 > i; i++) {
        val = (hash & 0x1F);
	hash >>= 5;
	key[i] = 'A' + val - (25 < val) * 43;
    }
    key[9] = '\0';
    printf ("key  : %s\n", key);
    
    return 0;
}

