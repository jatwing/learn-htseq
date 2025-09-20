## Installation


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

