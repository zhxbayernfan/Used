#!/bin/bash
#coding:utf-8

echo "--germline dir:$1"; ##eg:/haplox/rawout/191108_A00250_0201_BHT3NYDSXX/S001_SZ20191105008WHB-2_cfdna_86gene-180518_35601
echo "--genename:$2";     ##eg:S001_SZ20191105008WHB-2_cfdna_86gene-180518_35601
echo "--dataID:$3";       ##eg:35601 
echo "--11 or 90:$4";     ##eg:11 "lung11 use 11; lung90 use 90"

mkdir ${S1}/${S3}/
#创建同dataID目录

cp ${S1}/cnv/${S2}_rg_cnv.genes${S4}.csv ${S1}/${S3}/${S3}_cnv${S4}.csv
cp ${S1}/cnv/${S2}_rg_cnv.genes${S4}_Curl_gain.csv ${S1}/${S3}/${S3}_Curl_gain.csv
#复制cnv文件以及对应的自动上传文件

mkdir {$1}/${3}/fusionscan{$3}/
cp ${S1}/fusionscan/* ${S1}/${S3}/fusionscan${S3}/
cp -r ${S1}/MutScan/ ${S1}/${S3}/
mv ${S1}/${S3}/MutScan/ ${S1}/${S3}/MutScan${S3}/
#复制fusionscan和MutScan文件夹

cp ${S1}/fusion/${S2}_factera.fusions.txt ${S1}/${S3}/factera.fusions_${S3}.txt
#复制fusion中的factera.fusions.txt文件

cp ${S1}/*_indel-lung${S4}-GB18030-baseline.csv ${S1}/${S3}/${S3}_indel.csv
cp ${S1}/*_snv-lung${S4}-GB18030-baseline.csv ${S1}/${S3}/${S3}_snv.csv
#复制snv/indel文件