# Python Virtual Environment Makefile
YELLOW=\033[33m
RESET=\033[0m

.PHONY: all new start freeze clean

all: new upgrade install start

new:
	@if [ ! -d .venv ]; then \
		echo "$(YELLOW)Creating Python virtual environment...$(RESET)"; \
		python3 -m venv .venv; \
	fi

upgrade:
	@if [ -d .venv ]; then \
		echo "$(YELLOW)Upgrading standard packages...$(RESET)"; \
		.venv/bin/pip install --upgrade pip setuptools wheel; \
	fi

install:
	@if [ -d .venv ] && [ -f requirements.txt ]; then \
		echo "$(YELLOW)Installing packages from requirements.txt...$(RESET)"; \
		.venv/bin/pip install -r requirements.txt; \
	fi

start:
	@if [ -d .venv ]; then \
		echo "$(YELLOW)Starting Python virtual environment...$(RESET)"; \
		bash -c "source .venv/bin/activate && exec bash"; \
	fi

freeze:
	@if [ -d .venv ]; then \
		echo "$(YELLOW)Saving requirements.txt...$(RESET)"; \
		.venv/bin/pip freeze > requirements.txt; \
	fi

clean:
	@if [ -d .venv ]; then \
		echo "$(YELLOW)Deleting virtual environment...$(RESET)"; \
		rm -rf .venv; \
	fi
