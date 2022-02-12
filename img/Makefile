all:	EquPrincipale.svg      EquPrincipale.dvi \
			EquPrincipaleMat3d.svg EquPrincipaleMat3d.dvi \
			EquDevelopB.svg        EquDevelopB.dvi \
			EquCreateMat1.svg      EquCreateMat1.dvi \
			EquCreateMat2.svg      EquCreateMat2.dvi \
			EquCreateMat3.svg      EquCreateMat3.dvi \
			EquDefinitive.svg      EquDefinitive.dvi \
			EquMatrices.svg        EquMatrices.dvi \
			FigEtape1.svg          FigEtape1.dvi \
			FigEtape2.svg          FigEtape2.dvi \
			FigEtape3.svg          FigEtape3.dvi

%.svg: %.dvi
	dvisvgm -n $<

%.dvi: %.tex
	latex $< 