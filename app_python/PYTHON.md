#Style

- Follow PEP 8, when sensible.

## Naming
- Variables, functions, methods, packages, modules
 `lower_case_with_underscores`
- Classes and Exceptions `CapWords`
- Protected methods and internal functions
`_single_leading_underscore(self, ...)`
- Private methods
`__double_leading_underscore(self, ...)`
- Constants
`ALL_CAPS_WITH_UNDERSCORES`

- Avoid one-letter variables

- Avoid redundant labeling

- Prefer *reverse notation*: if there are the variable with the same prefix, make it prefix, not suffix

- Avoid getter and setter methods

## Documentation

- Follow PEP 257's docstring guidelines.

- Use one-line docstrings for obvious functions.

- Multiline docstrings should include

  + Summary line
  + Use case, if appropriate
  + Args
  + Return type and semantics, unless None is returned


- Use action words ("Return") rather than descriptions ("Returns").
Document __init__ methods in the docstring for the class

- Don't stress over Line lengths. 80-100 characters is fine

- Use parentheses for line continuations

#Testing

- Use long, descriptive names. This often obviates the need for doctrings in test methods.
- Tests should be isolated. Don't interact with a real database or network. Use a separate test database that gets torn down or use mock objects.
- Prefer factories to fixtures.
- Never let incomplete tests pass, else you run the risk of forgetting about them. Instead, add a placeholder like assert False, "TODO: finish me".

# Unit test best practices
1. Tests Should Be Fast
2. Tests Should Be Simple
3. Test Shouldn’t Duplicate Implementation Logic
4. Tests Should Be Readable
5. Tests Should Be Deterministic
6. Make Sure They’re Part of the Build Process
7. Distinguish Between The Many Types of Test Doubles and Use Them Appropriately
8. Adopt a Sound Naming Convention for Your Tests
9. Don’t Couple Your Tests With Implementation Details