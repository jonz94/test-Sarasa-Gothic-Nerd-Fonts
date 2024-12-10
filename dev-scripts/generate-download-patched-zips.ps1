$outputFile = "zips.yml"
New-Item $outputFile -ErrorAction SilentlyContinue | Out-Null
Clear-Content $outputFile

$counter = 0
$styles = "fixed", "fixed-slab", "mono", "mono-slab", "term", "term-slab", "gothic", "ui"
$orthographies = "cl", "hc", "j", "k", "sc", "tc"

foreach($style in $styles) {
  foreach($orthography in $orthographies) {
    $uses = '.jobs.job.steps[' + $counter + '].uses = \"actions/download-artifact@v4\"'
    $name = '.jobs.job.steps[' + $counter + '].with.name = \"sarasa-' + $style + '-' + $orthography + '-nerd-font.zip\"'

    yq e -i $uses $outputFile
    yq e -i $name $outputFile

    $counter++
  }
}

busybox sed -i "/jobs/ d; /job/ d; /steps/ d" $outputFile
