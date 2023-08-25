.PHONY : pdf preview

bookname = shap

all : amazon leanpub

docx : *.qmd
	quarto render --to docx --profile beta-reader


output/leanpub/$(bookname).epub : *.qmd _quarto-leanpub.yml _quarto.yml
	mkdir -p output/leanpub
	quarto render --profile leanpub --to epub
	mv _book/*.epub output/leanpub/
	python3 ../scripts/fix-epub.py ./output/leanpub/shap.epub

output/leanpub/$(bookname).pdf: *.qmd _quarto-leanpub.yml latex _quarto.yml
	mkdir -p output/leanpub
	git rev-parse --short HEAD > latex/hash.tex
	quarto render --profile leanpub --to pdf
	mv _book/*.pdf output/leanpub/

output/leanpub/sample-$(bookname).pdf: output/leanpub/$(bookname).pdf
	pdftk output/leanpub/$(bookname).pdf cat 1-40 output output/leanpub/sample-$(bookname).pdf

leanpub: output/leanpub/$(bookname).pdf output/leanpub/$(bookname).epub output/leanpub/sample-$(bookname).pdf

output/amazon/$(bookname).epub : *.qmd _quarto-amazon.yml _quarto.yml
	mkdir -p output/amazon
	quarto render --profile amazon --to epub
	mv _book/*.epub output/amazon/
	python3 ../scripts/fix-epub.py ./output/amazon/shap.epub

output/amazon/$(bookname).pdf: *.qmd _quarto-amazon.yml latex _quarto.yml
	mkdir -p output/amazon
	git rev-parse --short HEAD > latex/hash.tex
	quarto render --profile amazon --to pdf
	mv _book/*.pdf output/amazon/


amazon: output/amazon/$(bookname).pdf output/amazon/$(bookname).epub

check-epub-leanpub:
	java -jar ../scripts/epubcheck-5.0.0/epubcheck.jar ~/repos/shap-book/manuscript/output/leanpub/shap.epub

check-epub-amazon:
	java -jar ../scripts/epubcheck-5.0.0/epubcheck.jar ~/repos/shap-book/manuscript/output/amazon/shap.epub

check-epubs: check-epub-leanpub check-epub-amazon
 
venv:
	@rm -rf venv
	@echo "Creating virtual environment"
	@python3.10 -m venv venv
	@echo "Activating virtual environment"
	@venv/bin/pip install jupyter
	@echo "Installing dependencies from requirements.txt"
	@venv/bin/pip install -r requirements.txt
	@echo "Virtual environment is ready to use!"
