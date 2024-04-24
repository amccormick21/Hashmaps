# Makefile

# Variables
TEST_DIR := tests
MODULE_DIR := message_table

# Command to run the tests
.PHONY: test run

all: config test

config:
	@python config.py

test:
	@echo "Running tests..."
	@python -m unittest discover -s $(TEST_DIR) -p 'test_*.py' -v
	@echo "Tests complete."