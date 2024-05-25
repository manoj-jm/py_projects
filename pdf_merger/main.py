from pdfmerge import pdfmerge
#python -m pip install pdfmerge
#Command-line Example
#$ pdfmerge -o out.pdf file1.pdf file2.pdf[3,3] file2.pdf[1V,2..-1] "other*.pdf[<]" "/path/pdf[1..4>,5]"
#pdfmerge(["pdf-1.pdf", "pdf-2.pdf[2>]"], "output.pdf"))

pdfmerge(['DBMS_Notes (2).pdf',"Operating System Notes.pdf"],"output.pdf")