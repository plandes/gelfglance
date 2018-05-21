## makefile automates the build and deployment for python projects

PROJ_TYPE=	python

PYTHON_BIN_ARGS=	server --gelfserver graylog.ds.lp --glancesport 61207 -c 2 -t 5

# make build dependencies
_ :=	$(shell [ ! -d .git ] && git init ; [ ! -d zenbuild ] && \
	  git submodule add https://github.com/plandes/zenbuild && make gitinit )

include ./zenbuild/main.mk
