COMPILADOR=pdflatex -synctex=1 -interaction=nonstopmode
#GRAFICOS=disenio.pdf seqnormal.pdf seqnueva.pdf
AUXILIARES=informe.aux informe.log informe.toc informe.out informe.synctex.gz qa.log
PDF=informe.pdf

all: informe.pdf

#informe.pdf: informe.tex $(GRAFICOS)
informe.pdf: informe.tex 
	$(COMPILADOR) informe.tex && $(COMPILADOR) informe.tex

clean:
	rm -f $(AUXILIARES) 

cleanall:
	rm -f $(AUXILIARES) $(PDF)
