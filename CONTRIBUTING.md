# Contributing Guidelines

Thank you for considering contributing to this project! We appreciate your 
interest and efforts to improve the library. To ensure smooth collaboration 
and maintain consistency, please review and follow these guidelines.

## Local Installation
1. You should have [Python 3](https://www.python.org/downloads/) and [venv](https://docs.python.org/3/library/venv.html) installed.
2. Create a new virtual environment
```
python -m venv .venv
```
3. Activate the virtual environment
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

To maintain a consistent coding style across the project, we use [Ruff](https://beta.ruff.rs/docs/) for code linting, [Black](https://black.readthedocs.io/en/stable/) for code formatting and
[mypy](https://mypy-lang.org/) for static type checking. Before submitting any code changes,
please make sure your code adheres to these guidelines.

All code should be formatted with 
1. `ruff --fix .`
2. `black .`
3. `mypy .`

## Documentation
The documentation for this project is located in the `docs` directory and is hosted at
[django-cypress.helloworldpc.com](https://django-cypress.helloworldpc.com).
[MkDocs](https://www.mkdocs.org/) is used as the framework and
[Material](https://squidfunk.github.io/mkdocs-material/) as the theme.
To view the documentation locally and contribute to it, follow these steps:
1. Install the required documentation dependencies:
```
pip install -r requirements-docs.txt
```
2. Navigate to the `docs` directory:
```
cd docs
```
3. Start a local development server:
```
mkdocs serve --dev-addr localhost:3000
```
4. Open your web browser and visit [http://localhost:3000](http://localhost:3000) to
access the local documentation.

We encourage all contributors to keep the documentation up-to-date and comprehensive.
If you find any errors or have suggestions for improvement, please consider contributing
to the documentation alongside your code changes.

## Testing

Before submitting any code changes, it's important to ensure that your 
code passes all the relevant tests. Follow these steps to run the tests:

```
python run_tests.py
```

## Creating a new Cypress command
1. Create a new view at [`django_cypress/views.py`](./django_cypress/views.py) file. For example: `ManageView`.
```python
class ManageView(View):
    """A view for running Django management commands via HTTP POST requests."""

    def post(
        self,
        request: HttpRequest,
    ) -> JsonResponse:
        """Handle HTTP POST requests to execute Django management commands.

        Args:
        ----
        request (HttpRequest): The HTTP request object containing the command to execute.

        Returns:
        -------
        JsonResponse: A JSON response indicating the success of the command execution.
        """
        body = json.loads(request.body.decode("utf-8"))
        command = body.get("command")
        parameters = body.get("parameters")
        management.call_command(
            command,
            *parameters,
        )

        return JsonResponse({"success": True})

```
2. Add a new URL entry at [`django_cypress/urls.py`](./django_cypress/urls.py) file.
The URL should start with `__cypress__/` prefix.
```python
from .views import ManageView

urlpatterns = [
   ...
   path("__cypress__/manage/", ManageView.as_view(), name="manage-view"),
   ...
]
```
3. Create a new command at [`django_cypress/stubs/cypress/support/commands.js`](./django_cypress/stubs/cypress/support/commands.js) file that will do a request to the Django view.
```javascript
Cypress.Commands.add('manage', (command, parameters = []) => {
    return cy.csrfToken().then((token) => {
        return cy.request({
            method: 'POST',
            url: '/__cypress__/manage/',
            body: { command: command, parameters: parameters  },
            log: false,
            headers: {
                "X-CSRFToken": token["body"]["token"]
            }
        });
    });
})
```
4. Add the types of the command at the [`example/cypress/support/index.d.ts`](./example/cypress/support/index.d.ts) file.
```typescript
/// <reference types="cypress" />

declare namespace Cypress {
    interface Chainable<Subject> {
      ...
      /**
      * Run an Management command.
      *
      * @example
      * cy.manage()
      */
      manage(command: string, parameters?: string[]): Chainable<any>;
    }
}
```
5. Add a test case of the command at [`tests/tests.py`](./tests/tests.py) file.
```python
class ManageViewTestCase(TestCase):
    """Test case for the Manage view."""

    def setUp(self) -> None:
        """Set up the test case."""
        self.client = Client()

    def test_run_manage_command(self) -> None:
        """Do an HTTP GET request to the ManageView.

        First of all, create a dummy user. Then run the
        manage.py flush command through the ManageView.
        Finally, make sure that the HTTP Status Code of
        the response is 200 and the database is empty.
        """
        path = reverse("manage-view")

        User.objects.create(username="Testuser")

        request_data = {"command": "flush", "parameters": ["--no-input"]}
        content_type = "application/json"
        response = self.client.post(path, request_data, content_type)

        expected_count = 0
        actual_count = User.objects.all().count()
        self.assertEqual(expected_count, actual_count)

        expected_status_code = HTTPStatus.OK
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code)
```
6. Add documentation for your command by creating a new file `{command}.md` at [`./docs/docs/commands`](./docs/docs/commands/) directory. This file should use the following structure. View [`manage.md`](./docs/docs/commands/manage.md) example.

```markdown
# Command name

Command Description

## Syntax

Command Syntax

## Usage

Command Usage

## Arguments

### > argument 1 (Type of the Argument)

Description for the argument 1

### > argument 2 (Type of the Argument)

Description for the argument 2
```

## Developer Certificate of Origin (DCO)

To ensure that all contributions to this project are properly licensed and authorized,
each commit should be signed-off as a statement of origin and acceptance of the project's 
[Developer Certificate of Origin](https://developercertificate.org/). This can be done by 
adding the `-s` or `--signoff` flag when making commits (e.g., `git commit -s`).

By signing off your commits, you acknowledge that you have the right to contribute the code under the project's license.