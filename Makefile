VERSION=0.9.8

all:
	echo "Run make dis"

clean:
	find . -type d -name '.xvpics'|xargs rm -rf

install: clean
	rm -rf mandrake_desk-$(VERSION)
	mkdir mandrake_desk-$(VERSION)
	find . ! -name mandrake_desk-$(VERSION)|cpio -pvd mandrake_desk-$(VERSION) 
	find mandrake_desk-$(VERSION) -type d -name CVS|xargs rm -rf
	tar cyf ../mandrake_desk-$(VERSION).tar.bz2 mandrake_desk-$(VERSION)
	rm -rf mandrake_desk-$(VERSION)
