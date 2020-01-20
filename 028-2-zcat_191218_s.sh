#3_x02
cd /haplox/users/zhx/104DATAall/191218YKY/needmerge/22660-22171/
ossutil cp oss://sz-haploXseq/rawFQ/'2019'04/190402_A00250_0119_AHJJ5TDSXX_clinical/S071_SZ20190330013PET-e_ffpe'#'dna_wEspluS_22171_S21_L004_R1_001.fastq.gz ./''
ossutil cp oss://sz-haploXseq/rawFQ/'2019'04/190402_A00250_0119_AHJJ5TDSXX_clinical/S071_SZ20190330013PET-e_ffpe'#'dna_wEspluS_22171_S21_L004_R2_001.fastq.gz ./''
ossutil cp oss://sz-haploXseq/rawFQ/'2019'04/190407_A00250_0120_BHJWVLDSXX_clinical/S068_SZ20190330013PET-e_ffpe'#'dna_wEspluS_22660_S53_L002_R1_001.fastq.gz ./''
ossutil cp oss://sz-haploXseq/rawFQ/'2019'04/190407_A00250_0120_BHJWVLDSXX_clinical/S068_SZ20190330013PET-e_ffpe'#'dna_wEspluS_22660_S53_L002_R2_001.fastq.gz ./''
#finished!
zcat S068_SZ20190330013PET-e_ffpe'#'dna_wEspluS_22660_S53_L002_R1_001.fastq.gz S071_SZ20190330013PET-e_ffpe'#'dna_wEspluS_22171_S21_L004_R1_001.fastq.gz >merge_22171_R1.fastq && gzip merge_22171_R1.fastq
#finished! 
zcat S068_SZ20190330013PET-e_ffpe'#'dna_wEspluS_22660_S53_L002_R2_001.fastq.gz S071_SZ20190330013PET-e_ffpe'#'dna_wEspluS_22171_S21_L004_R2_001.fastq.gz >merge_22171_R2.fastq && gzip merge_22171_R2.fastq
#doing... 

#4_x02
cd /haplox/users/zhx/104DATAall/191218YKY/needmerge/21812-24629
ossutil cp oss://sz-haploXres/haplox/hapYun/'2019'12/tmp_workflow_repaq-xz-rawFQ_1_'2019'_12_18_21812/tmp/repaq-xz-rawfq_node_2/ ./''
rm S092_SZ20190326026WHB-b_g'#'dna_wEspluS_21812_S15_L004.rFQ
ossutil cp oss://sz-haploXseq/rawFQ/'2019'05/190502_A00250_0127_BHJY5VDSXX_clinical/S009_SZ'2019'0326026WHB-b_g'#'dna_wEspluS_24629_S3_L003_R1_001.fastq.gz ./''
ossutil cp oss://sz-haploXseq/rawFQ/'2019'05/190502_A00250_0127_BHJY5VDSXX_clinical/S009_SZ'2019'0326026WHB-b_g'#'dna_wEspluS_24629_S3_L003_R2_001.fastq.gz ./''
#finished!
zcat S092_SZ'2019'0326026WHB-b_g'#'dna_wEspluS_21812_S15_L004_R1_001.fastq.gz S009_SZ'2019'0326026WHB-b_g'#'dna_wEspluS_24629_S3_L003_R1_001.fastq.gz >merge_24629_R1.fastq && gzip merge_24629_R1.fastq
#finished! 
zcat S092_SZ'2019'0326026WHB-b_g'#'dna_wEspluS_21812_S15_L004_R2_001.fastq.gz S009_SZ'2019'0326026WHB-b_g'#'dna_wEspluS_24629_S3_L003_R2_001.fastq.gz >merge_24629_R2.fastq && gzip merge_24629_R2.fastq
#doing... 

#5_x02
cd /haplox/users/zhx/104DATAall/191218YKY/needmerge/24269-24634
ossutil cp oss://sz-haploXseq/rawFQ/'2019'05/190502_A00250_0127_BHJY5VDSXX_clinical/S014_SZ'2019'0423018FPT-1_tt'#'dna_wEspluS_24634_S8_L003_R1_001.fastq.gz ./''
ossutil cp oss://sz-haploXseq/rawFQ/'2019'05/190502_A00250_0127_BHJY5VDSXX_clinical/S014_SZ'2019'0423018FPT-1_tt'#'dna_wEspluS_24634_S8_L003_R2_001.fastq.gz ./''
ossutil cp oss://sz-haploXseq/rawFQ/'2019'04/190427_A00251_0107_AHJYV2DSXX_clinical/S077_SZ'2019'0423018FPT-1_tt'#'dna_wEspluS_24269_S12_L004_R1_001.fastq.gz ./''
ossutil cp oss://sz-haploXseq/rawFQ/'2019'04/190427_A00251_0107_AHJYV2DSXX_clinical/S077_SZ'2019'0423018FPT-1_tt'#'dna_wEspluS_24269_S12_L004_R2_001.fastq.gz ./''
#finished!
zcat S077_SZ'2019'0423018FPT-1_tt'#'dna_wEspluS_24269_S12_L004_R1_001.fastq.gz S014_SZ'2019'0423018FPT-1_tt'#'dna_wEspluS_24634_S8_L003_R1_001.fastq.gz >merge_24634_R1.fastq && gzip merge_24634_R1.fastq
#doing... 
zcat S077_SZ'2019'0423018FPT-1_tt'#'dna_wEspluS_24269_S12_L004_R2_001.fastq.gz S014_SZ'2019'0423018FPT-1_tt'#'dna_wEspluS_24634_S8_L003_R2_001.fastq.gz >merge_24634_R2.fastq && gzip merge_24634_R2.fastq
#waiting... 

#6_x02 before201903 downloading...
#7_x02 after201904_R1 downloading...
#8_x02 after201904_R2 downloading...
