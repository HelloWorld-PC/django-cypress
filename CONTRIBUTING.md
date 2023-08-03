# Contributing Guidelines

Thank you for considering contributing to this project! We appreciate your 
interest and efforts to improve the library. To ensure smooth collaboration 
and maintain consistency, please review and follow these guidelines.

## Local Installation
1. You should have [Python 3](https://www.python.org/downloads/) and [venv](https://docs.python.org/3/library/venv.html) installed.
2. Create an new venv
```
python -m venv .venv
```
3. Activate the venv
```
source .venv/bin/activate
```
4. Install the required dependencies
```
pip install -r requirements.txt
```

## Commit Messages
It's important to provide descriptive commit messages that tell a story. 
We suggest following the guidelines outlined in the 
[Git Commit Message Convention](https://cbea.ms/git-commit/) 
for writing meaningful commit messages.

As the blog post mentions:
1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how

## Development Workflow

Here's the suggested workflow for contributing:

1. Fork the repository to your own GitHub account.
2. Create a new branch from the `main` branch for your changes. Choose a descriptive name for your branch that includes the issue number.
   - Format the branch name as `XXXX-something`, where `XXXX` is the number of the corresponding issue.
   - For example, if you are addressing issue number 42 and adding a new feature, you could name your branch `42-new-feature`.
3. Make the necessary changes and commits in your branch.
4. Push the changes to your forked repository.
5. Submit a pull request from your branch to the main repository.
   - Please include a clear and concise description of the changes made in the Pull Request.
   - If the pull request addresses any existing issues, reference them using the `#issue_number` syntax in the description.
6. Your pull request will be reviewed by the maintainers, and any feedback or changes required will be communicated to you.
7. Once the pull request is approved and meets the necessary criteria, it will be merged into the main repository.

## Coding Style

To maintain a consistent coding style across the project, we use [Ruff](https://beta.ruff.rs/docs/) for code linting and [Black](https://black.readthedocs.io/en/stable/) for code 
formatting. Before submitting any code changes, please make sure your code 
adheres to these guidelines.

All code should be formatted with 
1. `ruff --fix src`
2. `black src`

## Developer Certificate of Origin (DCO)

To ensure that all contributions to this project are properly licensed and authorized,
each commit should be signed-off as a statement of origin and acceptance of the project's 
[Developer Certificate of Origin](https://developercertificate.org/). This can be done by 
adding the `-s` or `--signoff` flag when making commits (e.g., `git commit -s`).

By signing off your commits, you acknowledge that you have the right to contribute the code under the project's license.