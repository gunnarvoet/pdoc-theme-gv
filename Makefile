syntax : syntax-highlighting.css

.PHONY: clean

clean :
	rm syntax-highlighting.css

gv_pygments.css : pygments-gv.py
	python -m pygments-gv.py

syntax-highlighting.css : gv_pygments.css
	cp gv_pygments.css syntax-highlighting.css
	rm gv_pygments.css

