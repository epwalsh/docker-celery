.PHONY : docker-build
docker-build :
	docker build -t epwalsh/celery-test .

.PHONY : docker-run
docker-run :
	docker run --env-file=./access.txt --rm epwalsh/celery-test
