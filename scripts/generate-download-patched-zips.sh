#!/bin/bash

outputFile="zips.yml"
rm -f $outputFile
touch $outputFile

counter=0
styles=("fixed" "fixed-slab" "mono" "mono-slab" "term" "term-slab" "gothic" "ui")
orthographies=("cl" "hc" "j" "k" "sc" "tc")

for style in ${styles[@]}; do
  for orthography in ${orthographies[@]}; do
    yq e -i ".jobs.job.steps[$counter].uses = \"actions/download-artifact@v4\"" $outputFile
    yq e -i ".jobs.job.steps[$counter].with.name = \"sarasa-$style-$orthography-nerd-font.zip\"" $outputFile

    ((counter++))
  done
done

sed -i "/jobs/ d; /job/ d; /steps/ d" $outputFile
