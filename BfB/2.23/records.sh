#!/usr/bin/env bash

set -e # stop if there's error

for file in sample*.bam # files with wildcard -> no need for wildcard afterwards
    do
    samtools index $file
        if [ ! -s "$file" ] # if there's nt:
            then
            echo "The file is empty" # empty
        else
            alignments=$(samtools view -c $file) # counting
            echo $file >> result.txt
            echo $alignments >> result.txt
            # appending results in a text file
        fi
    done

# check do & done / then, fi!!