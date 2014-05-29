#include <stdio.h>

size_t spaces_pattern[] = {1,0,0,0,1,2,3,4,5,5,4,3,2,1,0,0,0,1};
size_t dashes_pattern[] = {0,2,3,4,4,4,3,2,0,0,2,3,4,4,4,3,2,0};
size_t pattern_len = sizeof(spaces_pattern) / sizeof(size_t);

void encode(FILE *fp){
    size_t nread, i, tempi, numdashes, patterni = 0;
    int shift;
    char *pair, temp[9];
    unsigned char buf[1024];
    // Read BUF_SIZE bytes at a time
    while ((nread = fread(buf, 1, sizeof(buf), fp)) > 0) {
        // For each byte
        for(i = 0; i < nread; ++i){
            // For each 1/2 nibble
            for(shift = 6; shift >= 0; shift -= 2){
                switch((buf[i] >> shift) & 0x3){
                    case 0x0:
                        pair = "AT";
                        break;
                    case 0x1:
                        pair = "CG";
                        break;
                    case 0x2:
                        pair = "GC";
                        break;
                    case 0x3:
                        pair = "TA";
                        break;
                }
                // Build output
                for(tempi = 0; tempi < spaces_pattern[patterni]; ++tempi)
                    temp[tempi] = ' ';
                temp[tempi++] = pair[0];
                for(numdashes = 0; numdashes < dashes_pattern[patterni]; ++numdashes, ++tempi)
                    temp[tempi] = '-';
                temp[tempi] = pair[1];
                temp[tempi+1] = '\0';
                printf("%s\n", temp);
                patterni = (patterni + 1) % pattern_len;
            }
        }
    }
}

void decode(FILE *fp){
    size_t writei = 0, patterni = 0, pos1, pos2;
    int shift = 6;
    char write_buf[1024], bin = 0;
    unsigned char read_buf[10];
    while(fgets(read_buf, sizeof(read_buf), fp) != NULL){
        // position of the first char
        pos1 = spaces_pattern[patterni];
        // position of the second char
        pos2 = pos1 + dashes_pattern[patterni] + 1;
        switch(read_buf[pos1] - read_buf[pos2]){
            case 'A' - 'T':
                //bin |= 0x0 << shift;
                break;
            case 'C' - 'G':
                bin |= 0x1 << shift;
                break;
            case 'G' - 'C':
                bin |= 0x2 << shift;
                break;
            case 'T' - 'A':
                bin |= 0x3 << shift;
                break;
            default:
                fprintf(stderr, "Input file not in valid DNA format.\n");
                return;
        }
        shift -= 2;
        // Check if we finshed constructing a byte
        if(shift < 0){
            write_buf[writei++] = bin;
            // Check if we filled the write_buf
            if(writei == sizeof(write_buf)){
                fwrite(write_buf, 1, sizeof(write_buf), stdout);
                writei = 0;
            }
            bin = 0;
            shift = 6;
        }
        patterni = (patterni + 1) % pattern_len;
    }
    // Check if we ended in the middle of constructing a byte
    if(shift != 6){
        fprintf(stderr, "Input file not in valid DNA format.\n");
        return;
    }
    // Check if we have data in the write buffer
    if(writei)
        fwrite(write_buf, 1, writei, stdout);
}

int main(int argc, char **argv){
    char *filename = NULL;
    int doencode;
    FILE *fp = NULL;

    if(argc == 2){
        filename = argv[1];
        doencode = 1;
    } else if(argc == 3 && !strcmp(argv[1], "-d")){
        filename = argv[2];
        doencode = 0;
    } else{
        fprintf(stderr, "Usage: %s [-d] file\n", argv[0]);
        return 1;
    }
    if(!(fp = fopen(filename, "r"))){
        perror(filename);
        return 1;
    }
    if(doencode)
        encode(fp);
    else
        decode(fp);

    fclose(fp);
    return 0;
}
