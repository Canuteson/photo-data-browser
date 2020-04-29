.PHONY: package
IMG := photo-album-cli


default: package

package:
	docker build -t ${IMG} .

test: package
	docker run -t --rm --entrypoint pytest ${IMG}
