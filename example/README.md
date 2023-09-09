# Example Django Project

## Installation

Please, ensure that you have both [Python](https://www.python.org/) and 
[Node.js](https://nodejs.org/en) installed on your system.


To install the necessary dependencies, run the following commands:
```
npm install
pip install django django_cypress
```

Next, start the Django project's server with this command:
```
python manage.py runserver
```

Now, open Cypress using the command:
```
npx cypress open
```

In the Cypress window that appears, select "E2E Testing," followed by
"Start E2E Testing in Chrome." This action will display a list of all 
the specs in your application. Click on `example.cy.js` to execute it.
