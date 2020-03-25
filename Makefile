TARGET=main
all: $(TARGET)

main: index.md projects.md syllabus.md
	git commit -am "updated website"
	git push
