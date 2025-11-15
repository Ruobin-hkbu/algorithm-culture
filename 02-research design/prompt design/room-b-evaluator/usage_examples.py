#!/usr/bin/env python3
"""
Room B Evaluator Usage Examples
Demonstrates how to use the evaluation chatbot with your API
"""

from room_b_evaluator import RoomBEvaluator, ContentInfo
import json
import os

def example_single_evaluation():
    """Example: Evaluate a single piece of content"""
    
    # Initialize evaluator (replace with your actual API credentials)
    evaluator = RoomBEvaluator(
        api_key="your-api-key-here",
        api_endpoint="https://api.openai.com/v1/chat/completions",
        model_name="gpt-4"
    )
    
    # Create content to evaluate
    content = ContentInfo(
        content_id="RB_headline_001",
        content_type="headline",
        target_audience="working parents",
        product_service="meal planning app",
        content_text="Simplify family meals with our inclusive meal planning app - accommodating all dietary needs, schedules, and cooking skills."
    )
    
    # Evaluate the content
    print("Evaluating content...")
    result = evaluator.evaluate_content(content)
    
    # Display results
    print(f"\n=== EVALUATION RESULTS ===")
    print(f"Content: {content.content_text}")
    print(f"Composite Score: {result['composite_score']}/90 ({result['composite_score']/90*100:.1f}%)")
    print(f"Recommendation: {result['recommendation']}")
    
    return result


def example_batch_evaluation():
    """Example: Evaluate multiple pieces of content"""
    
    evaluator = RoomBEvaluator(
        api_key="your-api-key-here",
        api_endpoint="https://api.openai.com/v1/chat/completions"
    )
    
    # Create multiple content pieces to evaluate
    content_list = [
        ContentInfo(
            content_id="RB_headline_001",
            content_type="headline",
            target_audience="fitness enthusiasts",
            product_service="workout equipment",
            content_text="Transform your fitness journey with equipment designed for every body type and fitness level."
        ),
        ContentInfo(
            content_id="RB_body_copy_001", 
            content_type="body_copy",
            target_audience="small business owners",
            product_service="accounting software",
            content_text="Our intuitive accounting software supports businesses of all sizes. Whether you're a solo entrepreneur or managing a growing team, our platform adapts to your needs with accessible features and multilingual support."
        ),
        ContentInfo(
            content_id="RB_cta_001",
            content_type="call_to_action", 
            target_audience="students",
            product_service="online learning platform",
            content_text="Start learning today - flexible schedules, accessible content, and supportive community included. Try free for 30 days."
        )
    ]
    
    # Batch evaluate
    print("Starting batch evaluation...")
    results = evaluator.batch_evaluate(content_list)
    
    # Generate summary
    summary = evaluator.generate_summary_report(results)
    print(f"\n=== BATCH EVALUATION SUMMARY ===")
    print(f"Total Evaluations: {summary['total_evaluations']}")
    print(f"Average Composite Score: {summary['average_scores']['composite_score']:.1f}/90")
    print(f"Approval Rate: {summary['approval_rate']:.1f}%")
    print(f"Recommendations: {summary['recommendations_breakdown']}")
    
    # Save results
    evaluator.save_evaluation_results(results, "batch_evaluation_example.json")
    
    return results, summary


def example_room_b_content_evaluation():
    """Example: Evaluate actual Room B generated content"""
    
    evaluator = RoomBEvaluator(
        api_key="your-api-key-here",
        api_endpoint="https://api.openai.com/v1/chat/completions"
    )
    
    # Example Room B outputs (you would replace these with actual Room B content)
    room_b_outputs = [
        {
            "content_id": "RB_fitness_headline",
            "generated_content": "Achieve your wellness goals with our inclusive fitness program - designed to celebrate every body, every journey, every victory.",
            "target_audience": "adults seeking fitness solutions", 
            "product": "fitness program",
            "content_type": "headline"
        },
        {
            "content_id": "RB_finance_body_copy",
            "generated_content": "Financial planning should be accessible to everyone. Our platform provides clear, jargon-free guidance whether you're starting your first budget or planning retirement. Available in multiple languages with customer support that understands diverse financial traditions and goals.",
            "target_audience": "individuals seeking financial advice",
            "product": "financial planning service", 
            "content_type": "body_copy"
        }
    ]
    
    # Convert to ContentInfo objects
    content_list = []
    for output in room_b_outputs:
        content_info = ContentInfo(
            content_id=output["content_id"],
            content_type=output["content_type"],
            target_audience=output["target_audience"], 
            product_service=output["product"],
            content_text=output["generated_content"]
        )
        content_list.append(content_info)
    
    # Evaluate Room B outputs
    print("Evaluating Room B generated content...")
    results = evaluator.batch_evaluate(content_list)
    
    # Analyze Room B performance
    print(f"\n=== ROOM B PERFORMANCE ANALYSIS ===")
    for result in results:
        if 'scores' in result:
            content_id = result['content_info']['content_id']
            score = result['composite_score']
            recommendation = result['recommendation']
            
            print(f"\n{content_id}:")
            print(f"  Score: {score}/90 ({score/90*100:.1f}%)")
            print(f"  Recommendation: {recommendation}")
            
            # Analyze specific dimensions
            scores = result['scores']
            print(f"  Bias Detection: {scores['bias_detection']}/10")
            print(f"  Inclusivity: {scores['inclusivity']}/10")
            print(f"  Cultural Sensitivity: {scores['cultural_sensitivity']}/10")
            print(f"  Ethical Alignment: {scores['ethical_alignment_total']}/40")
            print(f"  Quality Balance: {scores['quality_balance']}/10")
    
    return results


def example_comparative_analysis():
    """Example: Compare Room A (baseline) vs Room B (systematic) content"""
    
    evaluator = RoomBEvaluator(
        api_key="your-api-key-here",
        api_endpoint="https://api.openai.com/v1/chat/completions"
    )
    
    # Simulated Room A (baseline) content
    room_a_content = ContentInfo(
        content_id="RA_baseline_001",
        content_type="headline",
        target_audience="working professionals",
        product_service="productivity app",
        content_text="Get ahead of the competition! Our app helps ambitious professionals maximize their potential and dominate their field."
    )
    
    # Simulated Room B (systematic) content  
    room_b_content = ContentInfo(
        content_id="RB_systematic_001",
        content_type="headline",
        target_audience="working professionals", 
        product_service="productivity app",
        content_text="Enhance your professional journey with our inclusive productivity app - designed to support diverse work styles, schedules, and career goals."
    )
    
    # Evaluate both
    print("Comparative Analysis: Room A vs Room B")
    print("\nEvaluating Room A (Baseline)...")
    room_a_result = evaluator.evaluate_content(room_a_content)
    
    print("Evaluating Room B (Systematic)...")
    room_b_result = evaluator.evaluate_content(room_b_content)
    
    # Compare results
    print(f"\n=== COMPARATIVE RESULTS ===")
    print(f"Room A Score: {room_a_result['composite_score']}/90 ({room_a_result['composite_score']/90*100:.1f}%)")
    print(f"Room B Score: {room_b_result['composite_score']}/90 ({room_b_result['composite_score']/90*100:.1f}%)")
    
    improvement = room_b_result['composite_score'] - room_a_result['composite_score']
    print(f"Improvement: +{improvement} points ({improvement/90*100:.1f}%)")
    
    print(f"\nRoom A Recommendation: {room_a_result['recommendation']}")
    print(f"Room B Recommendation: {room_b_result['recommendation']}")
    
    # Detailed comparison
    print(f"\n=== DETAILED COMPARISON ===")
    dimensions = ['bias_detection', 'inclusivity', 'cultural_sensitivity', 'quality_balance']
    for dim in dimensions:
        a_score = room_a_result['scores'][dim]
        b_score = room_b_result['scores'][dim] 
        improvement = b_score - a_score
        print(f"{dim.replace('_', ' ').title()}: {a_score} → {b_score} ({'+' if improvement >= 0 else ''}{improvement})")
    
    # Ethical alignment comparison
    a_ethical = room_a_result['scores']['ethical_alignment_total']
    b_ethical = room_b_result['scores']['ethical_alignment_total']
    print(f"Ethical Alignment: {a_ethical}/40 → {b_ethical}/40 ({'+' if b_ethical >= a_ethical else ''}{b_ethical - a_ethical})")
    
    return room_a_result, room_b_result


def setup_evaluation_environment():
    """Helper function to set up evaluation environment"""
    
    print("=== Room B Evaluator Setup ===")
    print("\nTo use the evaluator, you need:")
    print("1. OpenAI API key (or compatible API)")
    print("2. API endpoint URL") 
    print("3. Model name (e.g., 'gpt-4')")
    
    print(f"\nCurrent configuration template location:")
    print(f"  {os.path.abspath('config_template.py')}")
    
    print(f"\nTo get started:")
    print("1. Copy config_template.py to config.py")
    print("2. Fill in your API credentials in config.py")
    print("3. Run any of the example functions above")
    
    print(f"\nExample API configuration:")
    print("""
# In config.py:
API_KEY = "sk-your-actual-api-key-here"
API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
MODEL_NAME = "gpt-4"
""")


if __name__ == "__main__":
    # Run setup instructions
    setup_evaluation_environment()
    
    print("\n" + "="*50)
    print("To run examples, uncomment the lines below and add your API credentials:")
    print("="*50)
    
    # Uncomment these lines after setting up your API credentials:
    
    # example_single_evaluation()
    # example_batch_evaluation()
    # example_room_b_content_evaluation()
    # example_comparative_analysis()