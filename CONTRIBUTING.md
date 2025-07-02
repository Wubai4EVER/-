# Contributing Guide

1. **Fork** the repository and create a feature branch.  
2. **Add or update tests** under the `tests/` directory.  
3. **Ensure code quality**:  
   ```bash
   poetry run black .
   poetry run isort .
   poetry run flake8 .
