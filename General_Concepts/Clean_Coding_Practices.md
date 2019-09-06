# Tips on writing clean code

## Make code readable
- Spacing and indentation is important
- Example is in json:
    - ```
        {
            userId: 3,
            userName: 'Bradley Stark',
            memberSince: '29-08-2013',
            fluentIn: [
                'Czech',
                'English',
                'Polish'
                ]
        }
        ```
    Rather than
    - ```{userId: 3, userName: 'Bradley Stark', memberSince: '29-08-2013', fluentIn: [ 'Czech', 'English', 'Polish']} ``` 

## Use Meaningful names for variables, functions and methods
- Make the names longer and more intuitive, rather than a,b,c.

## Let one function or method perform only one task
- Single responsibility principle, making them modular helps with unit testing

## Comment on code
- Explain why you did what you did
- Could help explain unconventional ways of tackling a problem
- Comments could help others to get the full picture and optimize at a later date
- Use only when necessary

## Be consistent
- Consistent styling and keywords: "GetSomethingHere" shouldn't be followed by "RetrieveSomething" later.

## Review code regularly
- update and refactor old code

## Write unit tests
- First Law: You may not write production code until you have written a failing unit test.
- Second Law: You may not write more of a unit test than is sufficient to fail, and not compiling is failing.
- Third Law: You may not write more production code than is sufficient to pass the currently failing test.
