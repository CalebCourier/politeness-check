from typing import Any, Dict

from guardrails.validator_base import (
    ValidationResult,
    register_validator,
)
from .generic_prompt_validator import GenericPromptValidator

@register_validator(name="guardrails/politeness_check", data_type="string")
class PolitenessCheck(GenericPromptValidator):
    """Validates that generated output is polite.

    **Key Properties**

    | Property                      | Description                       |
    | ----------------------------- | --------------------------------- |
    | Name for `format` attribute   | `guardrails/politeness_check`     |
    | Supported data types          | `string`                          |
    | Programmatic fix              | None                              |

    Args:
        llm_callable (str, optional): Model name to make the litellm call
        on_fail (Callable, optional): A function to call when validation fails.
            Defaults to None.
    """  # noqa


    def validate(self, value: Any, metadata: Dict) -> ValidationResult:
        metadata["validation_question"] = "Is the LLM Response polite?"

        return super().validate(value, metadata)
