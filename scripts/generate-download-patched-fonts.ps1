$outputFile = "download.yml"
New-Item $outputFile -ErrorAction SilentlyContinue | Out-Null
Clear-Content $outputFile

$counter = 0
$variants = "regular", "italic", "bold", "bolditalic", "semibold", "semibolditalic", "light", "lightitalic", "extralight", "extralightitalic"

foreach($variant in $variants) {
  $uses = '.jobs.job.steps[' + $counter + '].uses = \"actions/download-artifact@v4\"'
  $name = '.jobs.job.steps[' + $counter + '].with.name = \"patched sarasa-${{ matrix.styles }}-${{ matrix.orthographies }}-' + $variant + ' font\"'

  yq e -i $uses $outputFile
  yq e -i $name $outputFile

  $counter++
}

busybox sed -i "/jobs/ d; /job/ d; /steps/ d" $outputFile
