# Overview

| Developed by | Guardrails AI |
| Date of development | Feb 15, 2024 |
| Validator type | Format |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

# Description

This validator ensures that a generated output is polite.

# Installation

```bash
$ guardrails hub install hub://guardrails/politeness_check
```

# Usage Examples

## Validating string output via Python

In this example, we’ll test that a generated sentence is polite.

```python
# Import Guard and Validator
from guardrails.hub import PolitenessCheck
from guardrails import Guard

# Initialize Validator
val = PolitenessCheck()

# Setup Guard
guard = Guard.from_string(
    validators=[val, ...],
)

guard.parse("Hello there!")  # Validator passes
guard.parse("What's wrong with you?")  # Validator fails
```

## Validating JSON output via Python

In this example, we verify that a user’s comment is considered polite.

```python
# Import Guard and Validator
from pydantic import BaseModel
from guardrails.hub import LowerCase
from guardrails import Guard

val = PolitenessCheck()

# Create Pydantic BaseModel
class UserInfo(BaseModel):
		name: str
		comments: str = Field(validators=[val])

# Create a Guard to check for valid Pydantic output
guard = Guard.from_pydantic(output_class=UserInfo)

# Run LLM output generating JSON through guard
guard.parse("""
{
		"name": "John Doe",
		"comment": "You're doing great!"
}
""")
```

# API Reference

`__init__`
- `llm_callable`: Model name to make the litellm call.
- `on_fail`: The policy to enact when a validator fails.
