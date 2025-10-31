#!/usr/bin/env python3
"""
Google AI Test Script for Room B Evaluator
Tests the evaluation system with Google AI Gemini API
"""

import sys
import os
from room_b_evaluator_google import RoomBEvaluatorGoogle, ContentInfo

# Import configuration
try:
    from config import API_KEY, MODEL_NAME
    API_PROVIDER = getattr(__import__('config'), 'API_PROVIDER', 'google')
except ImportError:
    print("Error: config.py not found. Please ensure config.py exists with your API credentials.")
    sys.exit(1)

def test_google_evaluator():
    """Test the evaluator with Google AI"""
    
    print("🤖 Room B Evaluator Test - Google AI")
    print("=" * 50)
    
    # Initialize evaluator with your Google AI API key
    print("Initializing Google AI evaluator...")
    evaluator = RoomBEvaluatorGoogle(
        api_key=API_KEY,
        model_name=MODEL_NAME
    )
    print("✅ Google AI Evaluator initialized successfully")
    
    # Test content that represents good Room B systematic approach
    test_content = ContentInfo(
        content_id="RB_google_test_001",
        content_type="headline",
        target_audience="working professionals",
        product_service="productivity software",
        content_text="Enhance your work-life balance with our inclusive productivity platform - designed to support diverse work styles, family responsibilities, and personal goals for all professionals."
    )
    
    print(f"\n📝 Testing with content:")
    print(f"   \"{test_content.content_text}\"")
    
    try:
        print("\n🔄 Running evaluation with Google AI...")
        result = evaluator.evaluate_content(test_content)
        
        print("\n✅ Evaluation completed successfully!")
        print("\n" + "=" * 50)
        print("📊 EVALUATION RESULTS")
        print("=" * 50)
        
        # Display main results
        print(f"Content ID: {result['content_info']['content_id']}")
        print(f"Content Type: {result['content_info']['content_type']}")
        print(f"Target Audience: {result['content_info']['target_audience']}")
        print(f"API Provider: {result['api_provider']}")
        
        print(f"\n🎯 COMPOSITE SCORE: {result['composite_score']}/90 ({result['composite_score']/90*100:.1f}%)")
        print(f"📋 RECOMMENDATION: {result['recommendation']}")
        
        # Display detailed scores
        print(f"\n📈 DETAILED SCORES:")
        scores = result['scores']
        print(f"   Bias Detection: {scores['bias_detection']}/10")
        print(f"   Inclusivity: {scores['inclusivity']}/10") 
        print(f"   Cultural Sensitivity: {scores['cultural_sensitivity']}/10")
        print(f"   Quality Balance: {scores['quality_balance']}/10")
        
        print(f"\n🎭 ETHICAL ALIGNMENT: {scores['ethical_alignment_total']}/40")
        print(f"   Beneficence: {scores['beneficence']}/10")
        print(f"   Non-maleficence: {scores['non_maleficence']}/10")
        print(f"   Autonomy: {scores['autonomy']}/10")
        print(f"   Justice: {scores['justice']}/10")
        
        # Save test results
        evaluator.save_evaluation_results([result], "test_evaluation_google.json")
        print(f"\n💾 Results saved to: test_evaluation_google.json")
        
        # Show part of the evaluation response
        print(f"\n📄 EVALUATION RESPONSE PREVIEW:")
        response_preview = result['evaluation_response'][:300] + "..." if len(result['evaluation_response']) > 300 else result['evaluation_response']
        print(f"   {response_preview}")
        
        # Interpretation
        print(f"\n🎉 INTERPRETATION:")
        if result['composite_score'] >= 75:
            print("   ✅ EXCELLENT: Room B systematic approach working well!")
        elif result['composite_score'] >= 60:
            print("   ⚠️  GOOD: Room B approach mostly effective, minor improvements needed")
        else:
            print("   ❌ NEEDS WORK: Room B systematic approach needs refinement")
            
        return result
        
    except Exception as e:
        print(f"\n❌ Error during evaluation: {str(e)}")
        print("\nPossible issues:")
        print("1. Check your Google AI API key is valid and active")
        print("2. Verify internet connection")
        print("3. Ensure you have quota remaining on your Google AI account")
        print("4. Check if the model name is correct (gemini-1.5-pro or gemini-1.5-flash)")
        return None

def test_batch_evaluation_google():
    """Test batch evaluation with Google AI"""
    
    print(f"\n" + "=" * 50)
    print("🔄 Testing Google AI Batch Evaluation")
    print("=" * 50)
    
    evaluator = RoomBEvaluatorGoogle(API_KEY, MODEL_NAME)
    
    # Multiple test contents representing different Room B outputs
    batch_contents = [
        ContentInfo(
            content_id="RB_google_fitness_001",
            content_type="headline", 
            target_audience="fitness enthusiasts",
            product_service="workout program",
            content_text="Transform your wellness journey with our adaptive fitness program - celebrating every body type, fitness level, and personal goal."
        ),
        ContentInfo(
            content_id="RB_google_finance_001",
            content_type="body_copy",
            target_audience="young adults",
            product_service="budgeting app", 
            content_text="Managing money shouldn't be stressful or confusing. Our budgeting app provides clear, accessible guidance in multiple languages, with features designed for diverse income levels, family situations, and financial goals."
        )
    ]
    
    try:
        print(f"Evaluating {len(batch_contents)} content pieces with Google AI...")
        results = evaluator.batch_evaluate(batch_contents)
        
        print("✅ Batch evaluation completed!")
        
        # Generate summary
        summary = evaluator.generate_summary_report(results)
        
        print(f"\n📊 BATCH SUMMARY:")
        print(f"   Total Evaluations: {summary['total_evaluations']}")
        print(f"   Average Score: {summary['average_scores']['composite_score']:.1f}/90")
        print(f"   Approval Rate: {summary['approval_rate']:.1f}%")
        print(f"   Recommendations: {summary['recommendations_breakdown']}")
        print(f"   API Provider: {summary['api_provider']}")
        
        # Save batch results
        evaluator.save_evaluation_results(results, "batch_test_google.json")
        print(f"\n💾 Batch results saved to: batch_test_google.json")
        
        return results, summary
        
    except Exception as e:
        print(f"❌ Batch evaluation error: {str(e)}")
        return None, None

def main():
    """Main test function for Google AI"""
    print("🚀 Starting Room B Evaluator Tests - Google AI")
    print(f"API Key: {API_KEY[:8]}..." + "*" * 20)  # Show first 8 chars only
    print(f"Model: {MODEL_NAME}")
    print(f"Provider: Google AI")
    
    # Test single evaluation
    single_result = test_google_evaluator()
    
    if single_result:
        # If single test worked, try batch evaluation (with just 2 items to be respectful to API)
        batch_results, summary = test_batch_evaluation_google()
        
        if batch_results:
            print(f"\n🎉 ALL GOOGLE AI TESTS PASSED!")
            print("Your Room B Evaluator is ready to use with Google AI for research!")
            
            print(f"\n📋 NEXT STEPS:")
            print("1. Use the evaluator to assess actual Room B content")
            print("2. Compare results with Room A baseline content")
            print("3. Export data for statistical analysis")
            print("4. See usage_examples.py for more advanced usage")
            print("5. Note: Add delays between API calls to respect rate limits")
        else:
            print(f"\n⚠️  Single evaluation worked, but batch evaluation failed")
            print("Check the error messages above")
    else:
        print(f"\n❌ Evaluation test failed")
        print("Please check your Google AI API configuration and try again")

if __name__ == "__main__":
    main()