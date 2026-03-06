.PHONY: run test cov

run:
	uvicorn retailops.api.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest

cov:
	python -c "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec('pytest_cov') else 1)" \
		&& pytest --cov=src/retailops --cov-report=term-missing \
		|| pytest
