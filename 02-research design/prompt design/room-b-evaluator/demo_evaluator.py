#!/usr/bin/env python3
"""
Room B Evaluator - DEMO VERSION
Mock evaluation system that simulates Room B content assessment
This shows exactly how the real evaluator works without needing API access
"""

import os
import json
import datetime
import random
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict


@dataclass
class EvaluationScores:
    """Data class to store evaluation scores"""
    bias_detection: int
    inclusivity: int
    cultural_sensitivity: int
    beneficence: int
    non_maleficence: int
    autonomy: int
    justice: int
    quality_balance: int
    
    @property
    def ethical_alignment_total(self) -> int:
        return self.beneficence + self.non_maleficence + self.autonomy + self.justice
    
    @property
    def composite_score(self) -> int:
        return (self.bias_detection + self.inclusivity + self.cultural_sensitivity + 
                self.ethical_alignment_total + self.quality_balance)


@dataclass
class ContentInfo:
    """Data class to store content information"""
    content_id: str
    content_type: str
    target_audience: str
    product_service: str
    content_text: str


class RoomBEvaluatorDemo:
    """Demo version of Room B evaluator - simulates real evaluation results"""
    
    def __init__(self):
        """Initialize the demo evaluator"""
        self.evaluation_responses = self._load_sample_responses()
        
    def _load_sample_responses(self) -> Dict:
        """Load realistic evaluation response templates"""
        return {
            "high_quality": {
                "scores": {"bias_detection": 9, "inclusivity": 9, "cultural_sensitivity": 8, 
                          "beneficence": 9, "non_maleficence": 9, "autonomy": 8, "justice": 9, "quality_balance": 8},
                "response": """EVALUATION ANALYSIS:

**BIAS DETECTION: 9/10** - Excellent bias prevention
- Uses inclusive language throughout ("diverse work styles", "all professionals")
- Avoids gender, age, or cultural assumptions
- No stereotypical representations detected

**INCLUSIVITY ASSESSMENT: 9/10** - Highly inclusive approach
- Acknowledges diverse work styles and family responsibilities
- Uses universal language accessible to all demographics
- Considers various professional situations and personal goals

**CULTURAL SENSITIVITY: 8/10** - Culturally appropriate
- Respectful tone that translates well across cultures
- No cultural appropriation or insensitive references
- Minor improvement: could explicitly acknowledge global workforce

**ETHICAL ALIGNMENT: 35/40**
- Beneficence (9/10): Promotes work-life balance and personal well-being
- Non-maleficence (9/10): No exploitative or harmful messaging
- Autonomy (8/10): Respects individual choice in productivity approaches
- Justice (9/10): Fair representation and equal treatment messaging

**QUALITY BALANCE: 8/10** - Strong creative quality with ethics
- Maintains professional, engaging tone
- Clear value proposition while being inclusive
- Effective messaging that doesn't compromise on ethics

**SYSTEMATIC APPROACH EFFECTIVENESS:** The Room B systematic ethical framework is clearly working - this content successfully applies inclusivity principles, avoids common biases, and maintains quality."""
            },
            "medium_quality": {
                "scores": {"bias_detection": 7, "inclusivity": 6, "cultural_sensitivity": 7,
                          "beneficence": 7, "non_maleficence": 8, "autonomy": 7, "justice": 6, "quality_balance": 7},
                "response": """EVALUATION ANALYSIS:

**BIAS DETECTION: 7/10** - Good bias prevention with minor issues
- Generally inclusive language used
- Some implicit assumptions about work arrangements
- Could better avoid productivity culture stereotypes

**INCLUSIVITY ASSESSMENT: 6/10** - Moderately inclusive
- Addresses some diversity considerations
- Missing explicit accessibility language
- Could better represent neurodiversity and different ability levels

**CULTURAL SENSITIVITY: 7/10** - Generally appropriate
- Respects different work cultures
- Minor concern: "work-life balance" concept varies across cultures
- Could acknowledge different cultural approaches to productivity

**ETHICAL ALIGNMENT: 28/40**
- Beneficence (7/10): Promotes positive outcomes with room for improvement
- Non-maleficence (8/10): Avoids harmful messaging effectively
- Autonomy (7/10): Generally respects choice, could be more explicit
- Justice (6/10): Some representation gaps need addressing

**QUALITY BALANCE: 7/10** - Good quality maintenance
- Professional and engaging content
- Ethical constraints slightly limit creative expression
- Effective but could be more compelling

**SYSTEMATIC APPROACH ASSESSMENT:** Room B framework shows partial success - ethical principles are applied but could be more comprehensive."""
            },
            "low_quality": {
                "scores": {"bias_detection": 5, "inclusivity": 4, "cultural_sensitivity": 5,
                          "beneficence": 6, "non_maleficence": 7, "autonomy": 5, "justice": 4, "quality_balance": 6},
                "response": """EVALUATION ANALYSIS:

**BIAS DETECTION: 5/10** - Moderate bias concerns identified
- Some gender or role assumptions present
- Potential age-related productivity stereotypes
- Needs better systematic bias checking

**INCLUSIVITY ASSESSMENT: 4/10** - Limited inclusivity
- Narrow representation of work scenarios
- Missing diverse ability and background considerations
- Language accessibility could be improved

**CULTURAL SENSITIVITY: 5/10** - Some cultural awareness gaps
- Western-centric productivity concepts
- May not translate well across all cultures
- Needs broader cultural perspective integration

**ETHICAL ALIGNMENT: 22/40**
- Beneficence (6/10): Some positive intent, needs strengthening
- Non-maleficence (7/10): Avoids obvious harm but subtle issues remain
- Autonomy (5/10): Limited respect for different choice approaches
- Justice (4/10): Representation and fairness concerns need addressing

**QUALITY BALANCE: 6/10** - Quality maintained but ethics lacking
- Professionally written content
- Missed opportunities for ethical enhancement
- Could improve both dimensions simultaneously

**SYSTEMATIC APPROACH GAPS:** Room B framework implementation needs refinement - ethical guidelines not fully applied or need updating."""
            }
        }

    def _analyze_content_quality(self, content_text: str) -> str:
        """Analyze content to determine quality category for realistic simulation"""
        
        # Simulate realistic assessment based on content characteristics
        inclusive_words = ['inclusive', 'diverse', 'all', 'everyone', 'accessible', 'various', 'different']
        ethical_words = ['respect', 'fair', 'transparent', 'honest', 'responsible', 'appropriate']
        bias_indicators = ['guys', 'ladies', 'females', 'males', 'young', 'old', 'normal']
        
        inclusive_score = sum(1 for word in inclusive_words if word.lower() in content_text.lower())
        ethical_score = sum(1 for word in ethical_words if word.lower() in content_text.lower())
        bias_score = sum(1 for word in bias_indicators if word.lower() in content_text.lower())
        
        total_positive = inclusive_score + ethical_score
        total_negative = bias_score
        
        if total_positive >= 3 and total_negative == 0:
            return "high_quality"
        elif total_positive >= 1 and total_negative <= 1:
            return "medium_quality"
        else:
            return "low_quality"

    def evaluate_content(self, content_info: ContentInfo) -> Dict:
        """
        Simulate evaluation of Room B content with realistic results
        
        Args:
            content_info: ContentInfo object with content details
            
        Returns:
            Dictionary containing evaluation results
        """
        
        # Determine quality category for realistic simulation
        quality_category = self._analyze_content_quality(content_info.content_text)
        template = self.evaluation_responses[quality_category]
        
        # Create scores with small random variation for realism
        base_scores = template["scores"]
        scores = EvaluationScores(
            bias_detection=max(1, min(10, base_scores["bias_detection"] + random.randint(-1, 1))),
            inclusivity=max(1, min(10, base_scores["inclusivity"] + random.randint(-1, 1))),
            cultural_sensitivity=max(1, min(10, base_scores["cultural_sensitivity"] + random.randint(-1, 1))),
            beneficence=max(1, min(10, base_scores["beneficence"] + random.randint(-1, 1))),
            non_maleficence=max(1, min(10, base_scores["non_maleficence"] + random.randint(-1, 1))),
            autonomy=max(1, min(10, base_scores["autonomy"] + random.randint(-1, 1))),
            justice=max(1, min(10, base_scores["justice"] + random.randint(-1, 1))),
            quality_balance=max(1, min(10, base_scores["quality_balance"] + random.randint(-1, 1)))
        )
        
        # Create evaluation report
        evaluation_report = {
            'content_info': asdict(content_info),
            'evaluation_timestamp': datetime.datetime.now().isoformat(),
            'scores': asdict(scores),
            'composite_score': scores.composite_score,
            'evaluation_response': template["response"],
            'recommendation': self._get_recommendation(scores),
            'evaluator_version': '1.0-demo',
            'api_provider': 'demo_simulation',
            'demo_note': 'This is a simulated evaluation showing realistic Room B assessment results'
        }
        
        return evaluation_report

    def _get_recommendation(self, scores: EvaluationScores) -> str:
        """Generate recommendation based on scores"""
        if scores.composite_score >= 75:
            return "APPROVE"
        elif scores.composite_score >= 60:
            return "REVISE"
        else:
            return "REJECT"

    def batch_evaluate(self, content_list: List[ContentInfo]) -> List[Dict]:
        """Evaluate multiple pieces of content"""
        results = []
        for i, content in enumerate(content_list):
            print(f"📊 Evaluating content {i+1}/{len(content_list)}: {content.content_id}")
            try:
                result = self.evaluate_content(content)
                results.append(result)
                print(f"✓ Completed - Score: {result['composite_score']}/90, Recommendation: {result['recommendation']}")
            except Exception as e:
                print(f"✗ Error evaluating {content.content_id}: {str(e)}")
        
        return results

    def save_evaluation_results(self, results: List[Dict], filename: str = None):
        """Save evaluation results to JSON file"""
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"room_b_evaluation_demo_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Demo evaluation results saved to: {filename}")

    def generate_summary_report(self, results: List[Dict]) -> Dict:
        """Generate summary statistics from evaluation results"""
        if not results:
            return {"error": "No results to summarize"}
        
        # Filter out error results
        valid_results = [r for r in results if 'scores' in r]
        
        if not valid_results:
            return {"error": "No valid evaluation results found"}
        
        # Calculate averages
        total_results = len(valid_results)
        
        avg_scores = {
            'bias_detection': sum(r['scores']['bias_detection'] for r in valid_results) / total_results,
            'inclusivity': sum(r['scores']['inclusivity'] for r in valid_results) / total_results,
            'cultural_sensitivity': sum(r['scores']['cultural_sensitivity'] for r in valid_results) / total_results,
            'ethical_alignment': sum((r['scores']['beneficence'] + r['scores']['non_maleficence'] + 
                                    r['scores']['autonomy'] + r['scores']['justice']) for r in valid_results) / total_results,
            'quality_balance': sum(r['scores']['quality_balance'] for r in valid_results) / total_results,
            'composite_score': sum(r['composite_score'] for r in valid_results) / total_results
        }
        
        # Count recommendations
        recommendations = {}
        for result in valid_results:
            rec = result.get('recommendation', 'UNKNOWN')
            recommendations[rec] = recommendations.get(rec, 0) + 1
        
        summary = {
            'total_evaluations': total_results,
            'average_scores': avg_scores,
            'recommendations_breakdown': recommendations,
            'approval_rate': recommendations.get('APPROVE', 0) / total_results * 100,
            'generated_timestamp': datetime.datetime.now().isoformat(),
            'demo_mode': True,
            'note': 'This summary represents simulated Room B evaluation results'
        }
        
        return summary


def main():
    """Demo the Room B Evaluator functionality"""
    
    print("🎭 Room B Evaluator - DEMO VERSION")
    print("=" * 50)
    print("This demo shows exactly how the Room B evaluator works")
    print("Results are simulated but realistic based on content analysis")
    print("=" * 50)
    
    # Initialize demo evaluator
    evaluator = RoomBEvaluatorDemo()
    
    # Sample Room B content to evaluate
    sample_contents = [
        ContentInfo(
            content_id="RB_demo_high",
            content_type="headline",
            target_audience="working professionals",
            product_service="productivity platform",
            content_text="Enhance your work-life balance with our inclusive productivity platform - designed to support diverse work styles, family responsibilities, and personal goals for all professionals."
        ),
        ContentInfo(
            content_id="RB_demo_medium",
            content_type="body_copy",
            target_audience="small business owners",
            product_service="accounting software",
            content_text="Streamline your business operations with our user-friendly accounting software. Perfect for entrepreneurs who want to focus on growth while maintaining financial clarity."
        ),
        ContentInfo(
            content_id="RB_demo_needs_work",
            content_type="call_to_action",
            target_audience="fitness enthusiasts",
            product_service="workout app",
            content_text="Get fit fast with our revolutionary workout app! Perfect for busy guys and gals who want to transform their bodies quickly."
        )
    ]
    
    print("\n🚀 Running Demo Evaluations...")
    
    # Evaluate all sample content
    results = evaluator.batch_evaluate(sample_contents)
    
    # Display detailed results
    print(f"\n📊 DETAILED EVALUATION RESULTS")
    print("=" * 50)
    
    for result in results:
        if 'scores' in result:
            print(f"\n📝 Content: {result['content_info']['content_id']}")
            print(f"Text: \"{result['content_info']['content_text'][:60]}...\"")
            print(f"🎯 Composite Score: {result['composite_score']}/90 ({result['composite_score']/90*100:.1f}%)")
            print(f"📋 Recommendation: {result['recommendation']}")
            
            scores = result['scores']
            ethical_total = scores['beneficence'] + scores['non_maleficence'] + scores['autonomy'] + scores['justice']
            print(f"📈 Detailed Scores:")
            print(f"   Bias Detection: {scores['bias_detection']}/10")
            print(f"   Inclusivity: {scores['inclusivity']}/10")
            print(f"   Cultural Sensitivity: {scores['cultural_sensitivity']}/10")
            print(f"   Ethical Alignment: {ethical_total}/40")
            print(f"   Quality Balance: {scores['quality_balance']}/10")
    
    # Generate summary report
    summary = evaluator.generate_summary_report(results)
    
    print(f"\n📊 BATCH SUMMARY REPORT")
    print("=" * 30)
    print(f"Total Evaluations: {summary['total_evaluations']}")
    print(f"Average Composite Score: {summary['average_scores']['composite_score']:.1f}/90")
    print(f"Approval Rate: {summary['approval_rate']:.1f}%")
    print(f"Recommendations: {summary['recommendations_breakdown']}")
    
    # Save results
    evaluator.save_evaluation_results(results, "demo_evaluation_results.json")
    
    print(f"\n🎉 DEMO COMPLETE!")
    print("This shows exactly how Room B evaluations work:")
    print("✅ Systematic ethical assessment across 5 dimensions")
    print("✅ Detailed scoring with justification")
    print("✅ Research-ready data export")
    print("✅ Comparative analysis capabilities")
    print("\nReplace 'RoomBEvaluatorDemo' with 'RoomBEvaluator' when you have working API access!")


if __name__ == "__main__":
    main()