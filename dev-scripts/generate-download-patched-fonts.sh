#!/bin/bash

outputFile="download.yml"
rm -f $outputFile
touch $outputFile

counter=0
variants=("regular" "italic" "bold" "bolditalic" "semibold" "semibolditalic" "light" "lightitalic" "extralight" "extralightitalic")

for variant in ${variants[@]}; do
  yq e -i ".jobs.job.steps[$counter].uses = \"actions/download-artifact@v4\"" $outputFile
  yq e -i ".jobs.job.steps[$counter].with.name = \"patched sarasa-\${{ matrix.styles }}-\${{ matrix.orthographies }}-$variant font\"" $outputFile

  ((counter++))
done

sed -i "/jobs/ d; /job/ d; /steps/ d" $outputFile
