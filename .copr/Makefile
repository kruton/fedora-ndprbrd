srpm:
	dnf -y install wget rpkg git
	git clone https://github.com/google/ndprbrd.git
	wget https://raw.githubusercontent.com/meitar/git-archive-all.sh/master/git-archive-all.sh
	( pushd ndprbrd && git submodule init && git submodule update && bash ../git-archive-all.sh --prefix ndprbrd-master/ --format tar.gz ../master.tar.gz )
	rpkg prep
	$(eval COMMIT := $(shell cd ndprbrd-master; git rev-parse --short HEAD))
	$(eval GITDATE := $(shell cd ndprbrd-master; git rev-list --max-count=1 --date=format:%Y%m%d --pretty=format:%cd $(COMMIT) | tail -1))
	perl -pi -e 's/workingcopy/$(GITDATE)git$(COMMIT)/g' ndprbrd.spec
	rpkg srpm
	mv *.src.rpm "$(outdir)"
