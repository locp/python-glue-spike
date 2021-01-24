JOB_NAME='GlueSpike'
VERSION = 0.1.0

all: lint build test

build: dist/site-packages.zip
	mkdir -p dist

clean:
	docker-compose down -t 0
	rm -rf dist

cleanall: clean
	docker system prune --force --volumes

dist/site-packages.zip: site-packager/requirements.txt
	docker-compose up --build --exit-code-from site-packager site-packager
	
lint:
	yamllint -s .
	flake8
	docker run --rm -i hadolint/hadolint < site-packager/Dockerfile
	echo $(VERSION)

test:
	docker-compose up -d localstack
	pytest -k pre_integration -v
