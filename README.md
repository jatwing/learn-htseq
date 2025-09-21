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

htseq-count manual


https://htseq.readthedocs.io/en/release_0.11.1/count.html


```bash
htseq-count -r name bamfile_no_qualities_sorted_by_name.bam bamfile_no_qualities.gtf > results.count
```


## From the raw count file into normalized count matrix

DESeqDataSetFromHTSeqCount

check this blog:

https://www.jieandze1314.com/post/cnposts/108/

https://bioconductor.org/packages/release/data/experiment/html/pasilla.html



# R language hello world

print("Hello, World!")

## Drawing

