.PHONY: install server swagger

ifneq (,$(wildcard ./.env))
  include .env
  export
endif

install:
	@./resources/install.sh

server:
	@./resources/server.sh

swagger:
	@./manage.py generate_swagger -f yaml -o ./resources/swagger/api.yaml

test:
	@./manage.py test -v=3 --tag=unit

populate-puffs:
	@./manage.py populate-puffs
