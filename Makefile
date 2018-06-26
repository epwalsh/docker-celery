python-version := `grep "python:" Dockerfile | sed -r 's/.*([0-9]\.[0-9]).*/\1/g'`
image-tag      := python$(python-version)-alpine

.PHONY : docker-build
docker-build :
	docker build -t epwalsh/docker-celery:$(image-tag) .

.PHONY : push
push :
	docker push epwalsh/docker-celery:$(image-tag)
