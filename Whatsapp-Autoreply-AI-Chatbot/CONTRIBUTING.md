# Contributing

This is a personal learning project, but feedback and suggestions are welcome.

## How to Contribute

1. Fork the repository.
2. Create a branch:
   - For a bug fix: `git checkout -b fix/your-fix-name`
   - For a feature: `git checkout -b feature/your-feature-name`
3. Make your changes.
4. Test that the bot still works as expected.
5. Commit with a clear message:
   - `Fix: description of what was broken`
   - `Add: description of new feature`
   - `Refactor: description of what changed and why`
6. Push: `git push origin your-branch-name`
7. Open a Pull Request with a short description of what changed and why.

## Code Style

- Follow [PEP-8](https://peps.python.org/pep-0008/).
- Use type hints on all function signatures.
- Add a docstring to every new function.
- Keep functions short and focused on one responsibility.
- Use `logger` for output inside functions — avoid bare `print()` calls in production code.

## Important Rules

- Do not commit `.env` files or API keys under any circumstances.
- Do not commit personal chat data or screenshots with real names.
- Update `CHANGELOG.md` if your change is notable.
- Keep pull requests focused — one fix or feature per PR.
