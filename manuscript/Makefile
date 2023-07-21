.PHONY : pdf preview

bookname = shap

all : amazon leanpub

docx : *.qmd
	quarto render --to docx --profile beta-reader


output/leanpub/$(bookname).epub : *.qmd _quarto-leanpub.yml _quarto.yml
	mkdir -p output/leanpub
	quarto render --profile leanpub --to epub
	mv _book/*.epub output/leanpub/

output/leanpub/$(bookname).pdf: *.qmd _quarto-leanpub.yml latex _quarto.yml
	mkdir -p output/leanpub
	git rev-parse --short HEAD > latex/hash.tex
	quarto render --profile leanpub --to pdf
	mv _book/*.pdf output/leanpub/

output/leanpub/sample-$(bookname).pdf: output/leanpub/$(bookname).pdf
	pdftk output/leanpub/$(bookname).pdf cat 1-32 output output/leanpub/sample-$(bookname).pdf

leanpub: output/leanpub/$(bookname).pdf output/leanpub/$(bookname).epub output/leanpub/sample-$(bookname).pdf

output/amazon/$(bookname).epub : *.qmd _quarto-amazon.yml _quarto.yml
	mkdir -p output/amazon
	quarto render --profile amazon --to epub
	mv _book/*.epub output/amazon/

output/amazon/$(bookname).pdf: *.qmd _quarto-amazon.yml latex _quarto.yml
	mkdir -p output/amazon
	git rev-parse --short HEAD > latex/hash.tex
	quarto render --profile amazon --to pdf
	mv _book/*.pdf output/amazon/


amazon: output/amazon/$(bookname).pdf output/amazon/$(bookname).epub

  
