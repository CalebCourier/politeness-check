import os

import pytest
from guardrails import Guard
from validator import PolitenessCheck

guard = Guard.from_string(
    validators=[PolitenessCheck(llm_callable="gpt-3.5-turbo", on_fail="exception")]
)


@pytest.mark.skipif(
    os.environ.get("OPENAI_API_KEY") in [None, "mocked"],
    reason="openai api key not set",
)
def test_pass():
    test_output = "Hello there!"
    result = guard.parse(test_output, metadata={"pass_on_invalid": True})

    assert result.validation_passed is True
    assert result.validated_output == test_output


@pytest.mark.skipif(
    os.environ.get("OPENAI_API_KEY") in [None, "mocked"],
    reason="openai api key not set",
)
def test_fail():
    with pytest.raises(Exception) as excinfo:
        test_output = "What's wrong with you?"
        guard.parse(test_output)

    assert str(excinfo.value) in (
        "Validation failed for field with errors: The LLM says 'No'. The validation failed.",
        "The LLM returned an invalid answer. Failing the validation...",
    )
