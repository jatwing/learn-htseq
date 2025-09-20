## Installation


## Official Website

https://github.com/htseq/htseq

## Example Data

https://htseq.readthedocs.io/en/latest/tutorials/exon_example.html

For the annotations, we will use Saccharomyces_cerevisiae.SGD1.01.56.gtf.gz from the example_data folder, while for the reads we will use yeast_RNASeq_excerpt.sam from the same folder.

https://github.com/htseq/htseq/tree/main/example_data

## Execution

view -bS input.sam -o output.bam

samtools sort -n name.bam -o output.bam 

htseq-count -r name -f sam output.bam name.annotation.gtf > output.count




## Drawing