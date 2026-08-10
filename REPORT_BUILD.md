# Building the archival report

The canonical editable source is `paper.md`; references are in `paper.bib`.

Build the citation-resolved Word intermediate and PDF with:

```bash
mkdir -p output/pdf
quarto pandoc paper.md --citeproc -o output/pdf/qualitative-to-quantitative-transition-guide.docx
libreoffice --headless --convert-to pdf --outdir output/pdf output/pdf/qualitative-to-quantitative-transition-guide.docx
```

The committed PDF is the archival human-readable report. The DOCX is a build intermediate and is not part of the release.

Before release, inspect PDF metadata and render every page:

```bash
pdfinfo output/pdf/qualitative-to-quantitative-transition-guide.pdf
mkdir -p tmp/pdfs
pdftoppm -png -r 150 output/pdf/qualitative-to-quantitative-transition-guide.pdf tmp/pdfs/transition-guide
```
