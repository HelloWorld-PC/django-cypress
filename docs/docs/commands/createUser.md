# createUser

Create a new user.

## Syntax

```javascript
cy.createUser(attributes);
```

## Usage

```javascript
cy.createUser({username: "django-user", password: "123456789"})
cy.createUser({email: "user@mail.com", password: "123456789"})
```


## Arguments
### > attributes ( object )
This argument supports both the default Django User Model
and the custom User Model. The attributes objects should
contain the appropriate attributes for the given User Model.