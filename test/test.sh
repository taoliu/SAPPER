#!/bin/bash

#!/bin/bash

# integrative subcmds testing

if [ $# -lt 1 ];then
    echo "Run all tests for subcommands of SAPPER. Need 1 parameter for a tag name! A unique string combining date, time and SAPPER version is recommended. ./test.sh <TAG>"
    exit
fi

# test all sub-commands
TAG=$1

T_SE=examples/SE_demo/SEsample_peaks_sorted.bam
C_SE=examples/SE_demo/SEcontrol_peaks_sorted.bam
P_SE=examples/PE_demo/PEsample_peaks_sorted.bed

T_PE=examples/PE_demo/PEsample_peaks_sorted.bam
C_PE=examples/PE_demo/PEcontrol_peaks_sorted.bam
P_PE=examples/PE_demo/PEsample_peaks_sorted.bed

# call
echo "1. call from single dataset"

## SE
echo "1.1 Single-end library w/ control w/ auto"

sapper call -t $T_SE -c $C_SE -b $P_SE -o ${TAG}.1.1.vcf > ${TAG}.1.1.log

## SE with fermi
echo "1.2 Single-end library w/ control w/ fermi"

sapper call -F on -t $T_SE -c $C_SE -b $P_SE -o ${TAG}.1.2.vcf > ${TAG}.1.2.log

## SE w/o control
echo "1.3 Single-end library w/o control w/ auto"

sapper call -t $T_SE -b $P_SE -o ${TAG}.1.3.vcf > ${TAG}.1.3.log

## SE w/o control with fermi
echo "1.4 Single-end library w/o control w/ fermi"

sapper call -F on -t $T_SE -b $P_SE -o ${TAG}.1.4.vcf > ${TAG}.1.4.log

## PE
echo "1.5 Single-end library w/ control w/ auto"

sapper call -t $T_PE -c $C_PE -b $P_PE -o ${TAG}.1.5.vcf > ${TAG}.1.5.log

## PE with fermi
echo "1.6 Single-end library w/ control w/ fermi"

sapper call -F on -t $T_PE -c $C_PE -b $P_PE -o ${TAG}.1.6.vcf > ${TAG}.1.6.log

## PE w/o control
echo "1.7 Single-end library w/o control w/ auto"

sapper call -t $T_PE -b $P_PE -o ${TAG}.1.7.vcf > ${TAG}.1.7.log

## PE w/o control with fermi
echo "1.8 Single-end library w/o control w/ fermi"

sapper call -F on -t $T_PE -b $P_PE -o ${TAG}.1.8.vcf > ${TAG}.1.8.log

## end
echo "done"
