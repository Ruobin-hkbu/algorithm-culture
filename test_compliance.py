#!/usr/bin/env python3
"""
Test compliance validation with problematic content

This script tests the validation system with intentionally problematic
content to ensure the compliance checking is working properly.
"""

from ad_copy_assistant import InclusiveLanguageValidator, ComplianceLevel


def test_validator():
    """Test the validator with known problematic content"""
    validator = InclusiveLanguageValidator()
    
    test_cases = [
        {
            "name": "Problematic Gender Terms",
            "text": "Hey guys! This product is perfect for the modern businessman and his housewife.",
            "expected_issues": ["Inclusive Language"]
        },
        {
            "name": "Assumption-Based Language", 
            "text": "Obviously, everyone knows this is the best choice for normal people.",
            "expected_issues": ["Assumption Avoidance"]
        },
        {
            "name": "Regulated Claims",
            "text": "This supplement is medically proven to cure all diseases and is FDA approved.",
            "expected_issues": ["Regulated Claims"]
        },
        {
            "name": "Fear-Based Marketing",
            "text": "Don't let this dangerous crisis devastate your family! Urgent action required!",
            "expected_issues": ["Brand-Safe Tone"]
        },
        {
            "name": "Multiple Issues",
            "text": "Guys, obviously this scientifically proven solution will cure your problems! Don't let this crisis affect normal families!",
            "expected_issues": ["Inclusive Language", "Assumption Avoidance", "Regulated Claims", "Brand-Safe Tone"]
        },
        {
            "name": "Clean Content",
            "text": "Discover our new product designed for everyone who values quality and convenience.",
            "expected_issues": []
        }
    ]
    
    print("COMPLIANCE VALIDATION TESTS")
    print("="*50)
    
    for test_case in test_cases:
        print(f"\nTest: {test_case['name']}")
        print(f"Text: {test_case['text']}")
        
        # Run validation
        inclusivity_checks = validator.validate_inclusivity(test_case['text'])
        tone_check = validator.check_tone_safety(test_case['text'])
        all_checks = inclusivity_checks + [tone_check]
        
        # Find failed/warning checks
        issues_found = []
        for check in all_checks:
            if check.status != ComplianceLevel.PASS:
                issues_found.append(check.criterion)
                print(f"  {check.status.value} {check.criterion}: {check.notes}")
        
        # Verify expected issues were caught
        expected = set(test_case['expected_issues'])
        found = set(issues_found)
        
        if expected == found:
            print(f"  ✓ PASS: Correctly identified issues")
        else:
            print(f"  ✗ FAIL: Expected {expected}, found {found}")
        
        # Calculate score
        passing_checks = sum(1 for check in all_checks if check.status == ComplianceLevel.PASS)
        score = (passing_checks / len(all_checks)) * 100
        print(f"  Compliance Score: {score:.1f}%")


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    from ad_copy_assistant import AdCopyAssistant
    
    assistant = AdCopyAssistant()
    
    print(f"\n{'='*50}")
    print("EDGE CASE TESTS")
    print("="*50)
    
    # Test with minimal input
    print("\nTest: Minimal Input")
    try:
        variant1, variant2 = assistant.generate_ad_variants("product", "people")
        print(f"✓ Handled minimal input successfully")
        print(f"  Variant 1 score: {variant1.compliance_score:.1f}%")
        print(f"  Variant 2 score: {variant2.compliance_score:.1f}%")
    except Exception as e:
        print(f"✗ Failed with minimal input: {e}")
    
    # Test with problematic audience description
    print("\nTest: Problematic Audience Description")
    try:
        variant1, variant2 = assistant.generate_ad_variants(
            "Great product for busy moms and working mothers",
            "busy moms and elderly people"
        )
        print(f"✓ Handled problematic audience description")
        print(f"  Variant 1: {variant1.copy}")
        print(f"  Variant 1 score: {variant1.compliance_score:.1f}%")
    except Exception as e:
        print(f"✗ Failed with problematic audience: {e}")
    
    # Test with health claims in brief
    print("\nTest: Health Claims in Brief")
    try:
        variant1, variant2 = assistant.generate_ad_variants(
            "Guaranteed to cure all diseases and proven by doctors to be the best treatment",
            "people with health concerns"
        )
        print(f"✓ Processed health claims")
        print(f"  Variant 1: {variant1.copy}")
        print(f"  Disclaimer added: {'*' in variant1.copy}")
        print(f"  Variant 1 score: {variant1.compliance_score:.1f}%")
    except Exception as e:
        print(f"✗ Failed with health claims: {e}")


if __name__ == "__main__":
    test_validator()
    test_edge_cases()
    print(f"\n{'='*50}")
    print("Testing complete. The validation system is working to identify")
    print("and flag problematic content while maintaining usability.")