
name := cardinalityEstimation

all: $(name).pdf

$(name).pdf:$(name).tex
	pdflatex -halt-on-error ${name};
	bibtex ${name}; 
	pdflatex ${name} ;
	bibtex ${name};
	pdflatex ${name};
