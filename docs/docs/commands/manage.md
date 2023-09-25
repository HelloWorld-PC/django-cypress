# manage

Run administrative tasks using Django’s command-line utility `manage.py`.
For example: `python manage.py migrate` or `python manage.py flush`.

## Syntax

```javascript
cy.manage(command)
cy.manage(command, options)
```

## Usage

```javascript
cy.manage("migrate")
cy.manage("flush", ["--no-input"])
```

## Arguments
### > command ( string )

command should be one of the commands listed in this [document](https://docs.djangoproject.com/en/4.2/ref/django-admin/).

### > options ( string [ ] )

options, which is optional, should be zero or more of the options available for the given command.