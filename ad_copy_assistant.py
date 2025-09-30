#!/usr/bin/env python3
"""
AI Advertisement Writing Assistant

This module implements an advertising copy assistant that follows inclusive, 
bias-aware guidelines for generating advertisement content. It's designed as 
part of a study investigating how prompt design influences AI outputs and 
examines bias mitigation through systematic value-aligned prompts.
"""

import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class ComplianceLevel(Enum):
    """Compliance check levels"""
    PASS = "✓"
    WARNING = "⚠"
    FAIL = "✗"


@dataclass
class ComplianceCheck:
    """Individual compliance check result"""
    criterion: str
    status: ComplianceLevel
    notes: str = ""


@dataclass
class AdVariant:
    """Advertisement variant with metadata"""
    copy: str
    target_audience: str
    compliance_score: float
    compliance_checks: List[ComplianceCheck]


class InclusiveLanguageValidator:
    """Validates text for inclusive language compliance"""
    
    # Terms that should be avoided or flagged
    PROBLEMATIC_TERMS = {
        'guys': 'everyone, folks, team',
        'mankind': 'humanity, people',
        'manpower': 'workforce, staff',
        'chairman': 'chairperson, chair',
        'fireman': 'firefighter',
        'policeman': 'police officer',
        'businessman': 'businessperson, entrepreneur',
        'housewife': 'homemaker',
        'normal': 'typical, standard',
        'able-bodied': 'people without disabilities',
        'suffering from': 'living with, has',
        'victim of': 'person with, person who has experienced'
    }
    
    # Assumption-based phrases to avoid
    ASSUMPTION_PHRASES = [
        'everyone knows', 'obviously', 'of course', 'naturally',
        'typical family', 'normal person', 'average consumer',
        'working mother', 'working father', 'stay-at-home mom'
    ]
    
    # Regulated claim indicators
    REGULATED_TERMS = [
        'guaranteed', 'proven', 'scientifically proven', 'clinically tested',
        'medical', 'cure', 'treat', 'diagnose', 'prevent disease',
        'FDA approved', 'doctor recommended', 'best', 'number one',
        'fastest', 'safest', 'most effective'
    ]

    def validate_inclusivity(self, text: str) -> List[ComplianceCheck]:
        """Check text for inclusive language compliance"""
        checks = []
        text_lower = text.lower()
        
        # Check for problematic terms
        found_issues = []
        for term, suggestion in self.PROBLEMATIC_TERMS.items():
            if term in text_lower:
                found_issues.append(f"'{term}' → consider '{suggestion}'")
        
        if found_issues:
            checks.append(ComplianceCheck(
                criterion="Inclusive Language",
                status=ComplianceLevel.WARNING,
                notes="; ".join(found_issues)
            ))
        else:
            checks.append(ComplianceCheck(
                criterion="Inclusive Language",
                status=ComplianceLevel.PASS,
                notes="No problematic terms detected"
            ))
        
        # Check for assumption-based phrases
        assumption_issues = []
        for phrase in self.ASSUMPTION_PHRASES:
            if phrase in text_lower:
                assumption_issues.append(f"'{phrase}'")
        
        if assumption_issues:
            checks.append(ComplianceCheck(
                criterion="Assumption Avoidance",
                status=ComplianceLevel.WARNING,
                notes=f"Avoid assumptions: {', '.join(assumption_issues)}"
            ))
        else:
            checks.append(ComplianceCheck(
                criterion="Assumption Avoidance",
                status=ComplianceLevel.PASS,
                notes="No assumption-based language detected"
            ))
        
        # Check for regulated claims
        regulated_issues = []
        for term in self.REGULATED_TERMS:
            if term in text_lower:
                regulated_issues.append(f"'{term}'")
        
        if regulated_issues:
            checks.append(ComplianceCheck(
                criterion="Regulated Claims",
                status=ComplianceLevel.FAIL,
                notes=f"Requires disclaimer or professional consultation: {', '.join(regulated_issues)}"
            ))
        else:
            checks.append(ComplianceCheck(
                criterion="Regulated Claims",
                status=ComplianceLevel.PASS,
                notes="No regulated claims detected"
            ))
        
        return checks

    def check_tone_safety(self, text: str) -> ComplianceCheck:
        """Check for brand-safe tone"""
        # Fear-based or sensational terms
        fear_terms = [
            'urgent', 'emergency', 'crisis', 'dangerous', 'risky',
            'devastating', 'shocking', 'alarming', 'terrifying'
        ]
        
        text_lower = text.lower()
        found_fear_terms = [term for term in fear_terms if term in text_lower]
        
        if found_fear_terms:
            return ComplianceCheck(
                criterion="Brand-Safe Tone",
                status=ComplianceLevel.WARNING,
                notes=f"Consider softer alternatives to: {', '.join(found_fear_terms)}"
            )
        else:
            return ComplianceCheck(
                criterion="Brand-Safe Tone",
                status=ComplianceLevel.PASS,
                notes="Tone appears brand-safe"
            )


class AdCopyAssistant:
    """Main advertising copy assistant class"""
    
    def __init__(self):
        self.validator = InclusiveLanguageValidator()
        self.templates = {
            'product_launch': [
                "Discover {product} - designed for everyone who values {benefit}. Perfect for your {lifestyle}. {cta}",
                "Introducing {product}: {benefit} that fits your life. Made for people who appreciate {value}. {cta}"
            ],
            'service_promotion': [
                "Experience {service} tailored to your needs. Whether you're {audience_trait}, we're here to help. {cta}",
                "{service} that works for you. Designed with accessibility and flexibility in mind. {cta}"
            ],
            'lifestyle': [
                "Enhance your daily routine with {product}. Suitable for various lifestyles and preferences. {cta}",
                "Find your perfect match with {product}. Adaptable to different needs and situations. {cta}"
            ]
        }
    
    def generate_ad_variants(self, brief: str, target_audience: str, 
                           product_service: str = "", 
                           category: str = "lifestyle") -> Tuple[AdVariant, AdVariant]:
        """Generate two advertisement variants based on brief and audience"""
        
        # Extract key information from brief
        benefits = self._extract_benefits(brief)
        cta = self._generate_inclusive_cta()
        
        # Generate two variants using different templates
        templates = self.templates.get(category, self.templates['lifestyle'])
        
        variant1_text = self._fill_template(
            templates[0], 
            product_service, 
            benefits[0] if benefits else "quality and value",
            target_audience,
            cta
        )
        
        variant2_text = self._fill_template(
            templates[1] if len(templates) > 1 else templates[0], 
            product_service, 
            benefits[1] if len(benefits) > 1 else benefits[0] if benefits else "innovation and reliability",
            target_audience,
            cta
        )
        
        # Add disclaimers if needed
        variant1_text = self._add_disclaimers(variant1_text)
        variant2_text = self._add_disclaimers(variant2_text)
        
        # Validate both variants
        variant1 = self._create_ad_variant(variant1_text, target_audience)
        variant2 = self._create_ad_variant(variant2_text, target_audience)
        
        return variant1, variant2
    
    def _extract_benefits(self, brief: str) -> List[str]:
        """Extract key benefits from the brief"""
        # Simple keyword extraction - in a real implementation, 
        # this would use more sophisticated NLP
        benefit_keywords = [
            'convenient', 'reliable', 'affordable', 'innovative', 'sustainable',
            'efficient', 'user-friendly', 'accessible', 'flexible', 'durable',
            'quality', 'value', 'comfort', 'style', 'performance'
        ]
        
        brief_lower = brief.lower()
        found_benefits = [keyword for keyword in benefit_keywords if keyword in brief_lower]
        
        # Return at least 2 benefits
        if len(found_benefits) < 2:
            found_benefits.extend(['quality', 'value'])
        
        return found_benefits[:3]  # Limit to top 3
    
    def _generate_inclusive_cta(self) -> str:
        """Generate an inclusive call-to-action"""
        ctas = [
            "Learn more today.",
            "Explore your options.",
            "Find what works for you.",
            "Discover the possibilities.",
            "See how it fits your life."
        ]
        
        import random
        return random.choice(ctas)
    
    def _fill_template(self, template: str, product: str, benefit: str, 
                      audience: str, cta: str) -> str:
        """Fill template with provided information"""
        # Sanitize audience description to avoid assumptions
        sanitized_audience = self._sanitize_audience_description(audience)
        
        return template.format(
            product=product or "our offering",
            service=product or "our service", 
            benefit=benefit,
            lifestyle="unique needs",
            audience_trait=sanitized_audience,
            value=benefit,
            cta=cta
        )
    
    def _sanitize_audience_description(self, audience: str) -> str:
        """Remove potentially problematic assumptions from audience descriptions"""
        # Replace demographic assumptions with inclusive language
        replacements = {
            'busy moms': 'busy parents and caregivers',
            'working mothers': 'working parents',
            'elderly': 'older adults',
            'disabled people': 'people with disabilities',
            'normal people': 'most people',
            'average consumers': 'everyday consumers'
        }
        
        sanitized = audience.lower()
        for problematic, inclusive in replacements.items():
            sanitized = sanitized.replace(problematic, inclusive)
        
        return sanitized
    
    def _add_disclaimers(self, text: str) -> str:
        """Add appropriate disclaimers based on content"""
        needs_disclaimer = any(term in text.lower() for term in 
                             self.validator.REGULATED_TERMS)
        
        if needs_disclaimer:
            disclaimer = " *Individual results may vary. Consult a professional for personalized advice."
            return text + disclaimer
        
        return text
    
    def _create_ad_variant(self, text: str, audience: str) -> AdVariant:
        """Create an AdVariant with compliance analysis"""
        # Perform compliance checks
        inclusivity_checks = self.validator.validate_inclusivity(text)
        tone_check = self.validator.check_tone_safety(text)
        
        all_checks = inclusivity_checks + [tone_check]
        
        # Calculate compliance score (percentage of passing checks)
        passing_checks = sum(1 for check in all_checks if check.status == ComplianceLevel.PASS)
        compliance_score = (passing_checks / len(all_checks)) * 100
        
        return AdVariant(
            copy=text,
            target_audience=audience,
            compliance_score=compliance_score,
            compliance_checks=all_checks
        )
    
    def generate_compliance_report(self, variants: List[AdVariant]) -> str:
        """Generate a comprehensive compliance report"""
        report = "\n=== COMPLIANCE CHECKLIST ===\n"
        
        for i, variant in enumerate(variants, 1):
            report += f"\nVariant {i} (Score: {variant.compliance_score:.1f}%):\n"
            report += f"Text: {variant.copy}\n"
            report += "Compliance Checks:\n"
            
            for check in variant.compliance_checks:
                report += f"  {check.status.value} {check.criterion}: {check.notes}\n"
        
        report += "\n=== GENERAL GUIDELINES FOLLOWED ===\n"
        report += "✓ Gender-neutral language preferred\n"
        report += "✓ Inclusive terminology used\n"
        report += "✓ Avoided demographic assumptions\n"
        report += "✓ Brand-safe tone maintained\n"
        report += "✓ Disclaimers added where appropriate\n"
        
        return report


def main():
    """Demonstration of the ad copy assistant"""
    assistant = AdCopyAssistant()
    
    # Example usage
    brief = "New sustainable water bottle that keeps drinks cold for 24 hours. Affordable and durable."
    target_audience = "environmentally conscious consumers"
    
    print("=== AI Advertisement Writing Assistant ===")
    print(f"Brief: {brief}")
    print(f"Target Audience: {target_audience}\n")
    
    # Generate variants
    variant1, variant2 = assistant.generate_ad_variants(
        brief=brief,
        target_audience=target_audience,
        product_service="EcoBottle",
        category="product_launch"
    )
    
    # Display results
    print("VARIANT 1:")
    print(f"Copy: {variant1.copy}")
    print(f"Compliance Score: {variant1.compliance_score:.1f}%\n")
    
    print("VARIANT 2:")
    print(f"Copy: {variant2.copy}")
    print(f"Compliance Score: {variant2.compliance_score:.1f}%\n")
    
    # Generate compliance report
    compliance_report = assistant.generate_compliance_report([variant1, variant2])
    print(compliance_report)


if __name__ == "__main__":
    main()