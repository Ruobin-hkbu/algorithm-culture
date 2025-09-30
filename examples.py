#!/usr/bin/env python3
"""
Examples and test cases for the AI Advertisement Writing Assistant

This script demonstrates various scenarios and shows how the assistant
handles different types of content, including potentially problematic cases.
"""

from ad_copy_assistant import AdCopyAssistant


def run_example(title: str, brief: str, audience: str, product: str = "", category: str = "lifestyle"):
    """Run a single example and display results"""
    print(f"\n{'='*60}")
    print(f"EXAMPLE: {title}")
    print(f"{'='*60}")
    print(f"Brief: {brief}")
    print(f"Target Audience: {audience}")
    print(f"Product/Service: {product}")
    print(f"Category: {category}")
    print()
    
    assistant = AdCopyAssistant()
    variant1, variant2 = assistant.generate_ad_variants(
        brief=brief,
        target_audience=audience,
        product_service=product,
        category=category
    )
    
    print("VARIANT 1:")
    print(f"Copy: {variant1.copy}")
    print(f"Compliance Score: {variant1.compliance_score:.1f}%")
    
    print("\nVARIANT 2:")
    print(f"Copy: {variant2.copy}")
    print(f"Compliance Score: {variant2.compliance_score:.1f}%")
    
    # Show detailed compliance for variants with issues
    if variant1.compliance_score < 100 or variant2.compliance_score < 100:
        print("\nCOMPLIANCE DETAILS:")
        for i, variant in enumerate([variant1, variant2], 1):
            print(f"\nVariant {i} Issues:")
            for check in variant.compliance_checks:
                if check.status.value != "✓":
                    print(f"  {check.status.value} {check.criterion}: {check.notes}")


def main():
    """Run various examples to demonstrate the assistant capabilities"""
    
    print("AI Advertisement Writing Assistant - Example Scenarios")
    print("This demonstrates bias mitigation and inclusive language practices")
    
    # Example 1: Standard product launch
    run_example(
        title="Sustainable Product Launch",
        brief="New eco-friendly water bottle with innovative insulation technology. Keeps drinks cold for 24 hours. Made from recycled materials.",
        audience="environmentally conscious consumers",
        product="EcoBottle Pro",
        category="product_launch"
    )
    
    # Example 2: Service promotion with potential for assumptions
    run_example(
        title="Fitness Service Promotion", 
        brief="Online fitness platform with adaptive workouts for all fitness levels. Includes modifications for different abilities.",
        audience="people interested in fitness",
        product="FitForAll Platform",
        category="service_promotion"
    )
    
    # Example 3: Healthcare-related content (should trigger disclaimers)
    run_example(
        title="Wellness Product with Health Claims",
        brief="Natural supplement that supports immune system. Scientifically proven ingredients for better health.",
        audience="health-conscious individuals",
        product="ImmuneBoost",
        category="lifestyle"
    )
    
    # Example 4: Technology product for seniors (test age-related language)
    run_example(
        title="Technology for Older Adults",
        brief="Simple smartphone designed for ease of use. Large buttons, clear display, emergency features.",
        audience="older adults who want to stay connected",
        product="SimplePhone",
        category="product_launch"
    )
    
    # Example 5: Financial services (regulated industry)
    run_example(
        title="Financial Investment Service",
        brief="Investment platform that guarantees returns. Best investment strategy for building wealth.",
        audience="people planning for retirement",
        product="WealthBuilder",
        category="service_promotion"
    )
    
    # Example 6: Beauty product (potential for appearance assumptions)
    run_example(
        title="Inclusive Beauty Product",
        brief="Skincare line for all skin types and tones. Natural ingredients that work for everyone.",
        audience="people who care about skincare", 
        product="UniversalGlow",
        category="lifestyle"
    )
    
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print("This assistant demonstrates key principles for bias-aware advertising:")
    print("• Uses inclusive, gender-neutral language")
    print("• Avoids demographic assumptions and stereotypes") 
    print("• Provides disclaimers for regulated claims")
    print("• Maintains brand-safe tone without fear tactics")
    print("• Offers compliance checking and scoring")
    print("\nThese examples show how systematic prompt design can help")
    print("mitigate bias in AI-generated advertising content.")


if __name__ == "__main__":
    main()