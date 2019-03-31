#include<stdio.h>
#include<stdlib.h>
#define rot(x,k) (((x)<<(k)) | ((x)>>(32-(k))))

#define final(a,b,c) \
 { \
    c ^= b; c -= rot(b,14); \
       a ^= c; a -= rot(c,11); \
          b ^= a; b -= rot(a,25); \
             c ^= b; c -= rot(b,16); \
                a ^= c; a -= rot(c, 4); \
                   b ^= a; b -= rot(a,14); \
                      c ^= b; c -= rot(b,24); \
                       }
                        
                        typedef unsigned long Datum;
typedef unsigned int uint32;
                        #define UInt32GetDatum(X) ((Datum) (X))

                        static Datum
                        hash_uint32(uint32 k)
                        {
                            register uint32 a,
                                        b,
                                                    c;

                                                        a = b = c = 0x9e3779b9 + (uint32) sizeof(uint32) + 3923095;
                                                            a += k;

                                                                final(a, b, c);

                                                                /* report the result */
                                                                    return UInt32GetDatum(c);
                                                                    }
int get_hash_part_idx(unsigned int id, int parts){
    return hash_uint32(id)%parts;
}
