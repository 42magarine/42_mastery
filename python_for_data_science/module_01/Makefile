all: up shell

up:
	docker compose up --build --detach

start stop:
	docker compose $@

ls:
	docker compose ps --all
	docker compose images

shell:
	docker compose exec python sh

logs:
	docker compose logs

clean:
	docker compose down

fclean: clean
	docker system prune --all --force --volumes

.PHONY: all up start stop ls shell logs clean fclean
