#!/bin/bash
#coding:utf-8

echo "--germline dir:$1"; ##eg:/haplox/rawout/191108_A00250_0201_BHT3NYDSXX/S001_SZ20191105008WHB-2_cfdna_86gene-180518_35601
echo "--genename:$2";     ##eg:S001_SZ20191105008WHB-2_cfdna_86gene-180518_35601
echo "--dataID:$3";       ##eg:35601 
echo "--11 or 90:$4";     ##eg:11 "lung11 use 11; lung90 use 90"

mkdir $1/$3/
#创建同dataID目录

cp $1/cnv/$2_rg_cnv.genes$4.csv $1/$3/$3_cnv$4.csv
cp $1/cnv/$2_rg_cnv.genes$4_Curl_gain.csv $1/$3/$3_Curl_gain.csv
#复制cnv文件以及对应的自动上传文件

mkdir $1/$3/fusionscan$3/
cp $1/fusionscan/* $1/$3/fusionscan$3/
cp -r $1/MutScan/ $1/$3/
mv $1/$3/MutScan/ $1/$3/MutScan$3/
#复制fusionscan和MutScan文件夹

cp $1/fusion/$2_factera.fusions.txt $1/$3/factera.fusions_$3.txt
#复制fusion中的factera.fusions.txt文件

cp $1/*_indel-lung$4-GB18030-baseline.csv $1/$3/$3_indel.csv
cp $1/*_snv-lung$4-GB18030-baseline.csv $1/$3/$3_snv.csv
#复制snv/indel文件