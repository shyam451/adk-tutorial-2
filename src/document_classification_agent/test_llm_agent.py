#!/usr/bin/env python3
"""
Test script for the LLM-based document classification agent.
"""

import sys
from agent import (
    classify_document_with_llm,
    extract_kyc_with_llm,
    extract_passport_with_llm,
    extract_w9_with_llm,
    classification_specialist_agent,
    kyc_extraction_agent,
    passport_extraction_agent,
    w9_extraction_agent,
    root_agent
)
from sample_data import SAMPLE_DOCUMENTS


def test_llm_classification():
    """Test LLM-based document classification functionality."""
    print("Testing LLM-Based Document Classification:")
    print("=" * 50)
    
    for doc_type, content in SAMPLE_DOCUMENTS.items():
        print(f"\nTesting {doc_type.upper()} document:")
        result = classify_document_with_llm(content)
        print(f"  Classified as: {result['document_type']}")
        print(f"  Confidence: {result['confidence']:.2%}")
        print(f"  Method: {result.get('classification_method', 'enhanced')}")
        print(f"  Reasoning: {result.get('reasoning', 'N/A')}")


def test_llm_extraction_tools():
    """Test LLM-based extraction tool functions."""
    print("\n\nTesting LLM-Based Extraction Tools:")
    print("=" * 50)
    
    # Test KYC extraction tool
    print(f"\nKYC Extraction Tool:")
    kyc_result = extract_kyc_with_llm(SAMPLE_DOCUMENTS['kyc'])
    print(f"  Document Type: {kyc_result['document_type']}")
    print(f"  Method: {kyc_result['extraction_method']}")
    print(f"  Expected Fields: {', '.join(kyc_result['expected_fields'][:5])}...")
    
    # Test Passport extraction tool
    print(f"\nPassport Extraction Tool:")
    passport_result = extract_passport_with_llm(SAMPLE_DOCUMENTS['passport'])
    print(f"  Document Type: {passport_result['document_type']}")
    print(f"  Method: {passport_result['extraction_method']}")
    print(f"  Expected Fields: {', '.join(passport_result['expected_fields'][:5])}...")
    
    # Test W9 extraction tool
    print(f"\nW9 Extraction Tool:")
    w9_result = extract_w9_with_llm(SAMPLE_DOCUMENTS['w9'])
    print(f"  Document Type: {w9_result['document_type']}")
    print(f"  Method: {w9_result['extraction_method']}")
    print(f"  Expected Fields: {', '.join(w9_result['expected_fields'][:5])}...")


def test_agent_architecture():
    """Test the new agent architecture."""
    print("\n\nTesting Agent Architecture:")
    print("=" * 50)
    
    print(f"\nMain Agent: {root_agent.name}")
    print(f"  Sub-agents: {len(root_agent.sub_agents)} specialists")
    for sub_agent in root_agent.sub_agents:
        print(f"    - {sub_agent.name}")
        print(f"      Tools: {len(sub_agent.tools)}")
    
    print(f"\nClassification Agent: {classification_specialist_agent.name}")
    print(f"  Tools: {[tool.__name__ for tool in classification_specialist_agent.tools]}")
    
    print(f"\nKYC Extraction Agent: {kyc_extraction_agent.name}")
    print(f"  Tools: {[tool.__name__ for tool in kyc_extraction_agent.tools]}")
    
    print(f"\nPassport Extraction Agent: {passport_extraction_agent.name}")
    print(f"  Tools: {[tool.__name__ for tool in passport_extraction_agent.tools]}")
    
    print(f"\nW9 Extraction Agent: {w9_extraction_agent.name}")
    print(f"  Tools: {[tool.__name__ for tool in w9_extraction_agent.tools]}")


def main():
    """Run all tests."""
    print("LLM-Based Document Classification Agent Test Suite")
    print("=" * 60)
    
    try:
        test_llm_classification()
        test_llm_extraction_tools()
        test_agent_architecture()
        
        print("\n\n" + "=" * 60)
        print("All tests completed successfully!")
        print("\nKey improvements with LLM-based approach:")
        print("- Intelligent classification with reasoning")
        print("- Specialized extraction sub-agents")
        print("- Flexible document processing pipeline")
        print("- Better confidence scoring and field-level extraction")
        
    except Exception as e:
        print(f"Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()