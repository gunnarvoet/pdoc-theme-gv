pdoc-theme-gv
=============

Theme for [pdoc](https://pdoc.dev/) API Documentation. An example may be found at https://gunnarvoet.github.io/gvpy.

Install theme into project folder as submodule:
```sh
git submodule add https://github.com/gunnarvoet/pdoc-theme-gv .pdoc-theme-gv
```

Build pdoc documentation:
```sh
PDOC_ALLOW_EXEC=1 pdoc -d numpy -o docs -t .pdoc-theme-gv --math ./<project>
```
or build live with:
```sh
PDOC_ALLOW_EXEC=1 pdoc -d numpy -t .pdoc-theme-gv --math <project>
```


syntax highlighting
-------------------
The syntax highlighting .css-file is defined in `pygments-gv.py`.
- `make syntax` generates `syntax-highlighting.css` from `pygments-gv.py`.
- Standard pygments line number setting are overwritten by settings in `theme.css`.
