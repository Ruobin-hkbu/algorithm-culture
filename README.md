# Algorithm Culture: AI Advertisement Writing Assistant

This study investigates how prompt design influences the outputs of a generative AI advertisement writing assistant and examines whether human adjustments to a systematic value-aligned prompt can mitigate bias.

## Overview

The AI Advertisement Writing Assistant demonstrates bias-aware advertising copy generation that follows inclusive language principles and compliance guidelines. This implementation serves as a research tool for examining how systematic prompt design and validation can help mitigate bias in AI-generated content.

## Features

- **Dual Variant Generation**: Produces 2 short advertisement variants per request
- **Inclusive Language**: Uses gender-neutral, inclusive terminology
- **Bias Mitigation**: Avoids assumptions based on demographics, abilities, or socioeconomic status
- **Compliance Checking**: Validates content against regulatory and brand-safety guidelines
- **Disclaimer Management**: Automatically adds appropriate disclaimers for regulated claims
- **Scoring System**: Provides compliance scores and detailed feedback

## Key Principles

1. **Inclusive Language**: Avoids gendered terms, uses people-first language
2. **Assumption Avoidance**: Doesn't make generalizations about target audiences
3. **Regulatory Compliance**: Flags health claims, financial promises, and other regulated content
4. **Brand Safety**: Maintains professional tone, avoids fear-based marketing
5. **Accessibility**: Considers diverse abilities and circumstances

## Usage

### Basic Usage

```python
from ad_copy_assistant import AdCopyAssistant

assistant = AdCopyAssistant()
variant1, variant2 = assistant.generate_ad_variants(
    brief="Sustainable water bottle with 24-hour cold retention",
    target_audience="environmentally conscious consumers",
    product_service="EcoBottle",
    category="product_launch"
)

print(f"Variant 1: {variant1.copy}")
print(f"Compliance Score: {variant1.compliance_score}%")
```

### Running Examples

```bash
# Run the main demonstration
python ad_copy_assistant.py

# See various scenarios and use cases
python examples.py

# Test compliance validation
python test_compliance.py
```

## Implementation Details

### Compliance Validation

The system checks for:
- **Inclusive Language**: Problematic gendered or exclusionary terms
- **Assumption Avoidance**: Language that makes demographic generalizations
- **Regulated Claims**: Medical, financial, or other claims requiring disclaimers
- **Brand-Safe Tone**: Avoids fear tactics and sensationalism

### Scoring System

- **Pass (✓)**: 100% compliance
- **Warning (⚠)**: 75% compliance (minor issues)
- **Fail (✗)**: 0% compliance (major issues requiring attention)

## Research Applications

This implementation can be used to study:
- Impact of systematic prompt design on AI outputs
- Effectiveness of bias mitigation techniques
- Trade-offs between creativity and compliance in AI-generated content
- Human-AI collaboration in content creation

## Files

- `ad_copy_assistant.py`: Main implementation with assistant and validation classes
- `examples.py`: Demonstration of various use cases and scenarios
- `test_compliance.py`: Comprehensive testing of validation system
- `README.md`: This documentation

## Contributing

This is a research project examining bias in AI-generated advertising content. Contributions should maintain focus on inclusive language, bias mitigation, and compliance validation.