## Installation

on the Terminal, interact with machine give orders to it

1. on the terminal install brew, on website https://brew.sh/

home brew is a software manager for MacOS

2. use brew to install vscode

on the terminal

brew install --cask visual-studio-code

VScode has File Explorer and Terminal

3. install anaconda

brew install --cask anaconda

4. bind anaconda and zsh (Terminal)

change .zshrc file, add this line

export PATH="/usr/local/anaconda3/bin:$PATH"

on the Terminal path

source .zshrc

conda init zsh



## add channels

conda config --add channels conda-forge
conda config --add channels bioconda

## Install Pacakages

conda install subread
conda install python=3.12
conda install htseq
conda install samtools


our key goal is to create an environment for the user to use the softwares (including htseq and samtools) managed by Conda
Also they could see the files in the File Explorer and they can edit the files and run the command via Terminal.


## Official Website

https://github.com/htseq/htseq

## Example Data

https://htseq.readthedocs.io/en/latest/tutorials/exon_example.html

For the annotations, we will use Saccharomyces_cerevisiae.SGD1.01.56.gtf.gz from the example_data folder, while for the reads we will use yeast_RNASeq_excerpt.sam from the same folder.

https://github.com/htseq/htseq/tree/main/example_data

## Execution

using dummy data


samtools sort manual

http://www.htslib.org/doc/samtools-sort.html

```bash
samtools sort -n bamfile_no_qualities.bam bamfile_no_qualities_sorted_by_name
```


## prepare for step 4, gene expression quantification

```bash

## version Version: 1.21
## Usage: samtools sort [options...] [in.bam]
samtools sort -n bamfile_no_qualities.bam -o bamfile_no_qualities_sorted_by_name.bam
```

htseq-count manual


https://htseq.readthedocs.io/en/release_0.11.1/count.html


```bash

# usage: htseq-count [-h] [--version] [-f {sam,bam,auto}] [-r {pos,name}] [--max-reads-in-buffer MAX_BUFFER_SIZE] [-s {yes,no,reverse}] [-a MINAQUAL] [-t FEATURE_TYPE]
 #                  [-i IDATTR] [--additional-attr ADDITIONAL_ATTRIBUTES] [--add-chromosome-info] [-m {union,intersection-strict,intersection-nonempty}]
  #                 [--nonunique {none,all,fraction,random}] [--secondary-alignments {score,ignore}] [--supplementary-alignments {score,ignore}] [-o SAMOUTS]
   #                [-p {SAM,BAM,sam,bam}] [-d OUTPUT_DELIMITER] [-c OUTPUT_FILENAME] [--counts-output-sparse] [--append-output] [-n NPROCESSES]
    #               [--feature-query FEATURE_QUERY] [-q] [--with-header]
   #                samfilenames [samfilenames ...] featuresfilename

htseq-count -r name bamfile_no_qualities_sorted_by_name.bam bamfile_no_qualities.gtf > results.count
```


count is only for one group, in reality, needs several groups

sorting by names and counting for multiple times.

## From the raw count file into normalized count matrix

DESeqDataSetFromHTSeqCount

check this blog:

https://www.jieandze1314.com/post/cnposts/108/

https://bioconductor.org/packages/release/data/experiment/html/pasilla.html



# R language hello world

print("Hello, World!")

## step 4.5 raw count matrix into normalized count matrix

python ./raw-into-normalize-count.py 


## Drawing

