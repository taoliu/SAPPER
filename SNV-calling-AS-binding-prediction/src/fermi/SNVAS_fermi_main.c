#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include "fermi.h"
#include "mag.h"

//modified from Heng Li's example.c of fermi software.

int main(int argc, char *argv[])
{
	int c, do_ec = 0, skip_unitig = 0, ec_k = -1, unitig_k = -1, do_clean = 0;
	char *seq, *qual;
	int64_t l;
	while ((c = getopt(argc, argv, "ceUk:l:")) >= 0) {
		switch (c) {
			case 'e': do_ec = 1; break;
			case 'U': skip_unitig = 1; break;
			case 'k': ec_k = atoi(optarg); break;
			case 'l': unitig_k = atoi(optarg); break;
			case 'c': do_clean = 1; break;
		}
	}
	if (optind == argc) {
		fprintf(stderr, "Local assembler for small peak regions. Output cleaned unitigs.\nUsage: SNVAS_fermi [-ceU] [-k ecKmer] [-l utgKmer] <in.fq>\n");
		return 1;
	}
	l = fm6_api_readseq(argv[optind], &seq, &qual);
	if (do_ec) fm6_api_correct(ec_k, l, seq, qual);
	if (!skip_unitig) { // construct the unitigs
		mag_t *g;
		free(qual);
		g = fm6_api_unitig(unitig_k, l, seq);
		if (do_clean) {
			magopt_t *opt = mag_init_opt();
			//opt->flag |= MOG_F_AGGRESSIVE | MOG_F_CLEAN;
			opt->flag |= MOG_F_CLEAN;
			mag_g_clean(g, opt);
			free(opt);
		}
		mag_g_print(g);
		mag_g_destroy(g);
	} else {
		fm6_api_writeseq(l, seq, qual); // then write the (possibly corrected) reads
		free(qual);
	}
	free(seq);
	return 0;
}