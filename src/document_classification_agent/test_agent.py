#!/usr/bin/env python3
"""
Test script for the document classification agent.
"""

import sys
import json
from agent import (
    classify_document_type,
    extract_kyc_data,
    extract_passport_data,
    extract_w9_data,
    process_document
)
from sample_data import SAMPLE_DOCUMENTS


def test_document_classification():
    """Test document classification functionality."""
    print("Testing Document Classification:")
    print("=" * 50)
    
    for doc_type, content in SAMPLE_DOCUMENTS.items():
        print(f"\nTesting {doc_type.upper()} document:")
        result = classify_document_type(content)
        print(f"  Classified as: {result['document_type']}")
        print(f"  Confidence: {result['confidence']:.2%}")
        print(f"  Scores: {result['scores']}")


def test_data_extraction():
    """Test data extraction functionality."""
    print("\n\nTesting Data Extraction:")
    print("=" * 50)
    
    # Test KYC extraction
    print(f"\nKYC Data Extraction:")
    kyc_result = extract_kyc_data(SAMPLE_DOCUMENTS['kyc'])
    print(f"  Customer Name: {kyc_result['extracted_fields']['customer_name']}")
    print(f"  Customer ID: {kyc_result['extracted_fields']['customer_id']}")
    print(f"  Email: {kyc_result['extracted_fields']['email']}")
    
    # Test Passport extraction
    print(f"\nPassport Data Extraction:")
    passport_result = extract_passport_data(SAMPLE_DOCUMENTS['passport'])
    print(f"  Passport Number: {passport_result['extracted_fields']['passport_number']}")
    print(f"  Surname: {passport_result['extracted_fields']['surname']}")
    print(f"  Nationality: {passport_result['extracted_fields']['nationality']}")
    
    # Test W9 extraction
    print(f"\nW9 Data Extraction:")
    w9_result = extract_w9_data(SAMPLE_DOCUMENTS['w9'])
    print(f"  Name: {w9_result['extracted_fields']['name']}")
    print(f"  Business Name: {w9_result['extracted_fields']['business_name']}")
    print(f"  TIN: {w9_result['extracted_fields']['taxpayer_id_number']}")


def test_complete_processing():
    """Test complete document processing pipeline."""
    print("\n\nTesting Complete Document Processing:")
    print("=" * 50)
    
    for doc_type, content in SAMPLE_DOCUMENTS.items():
        print(f"\nProcessing {doc_type.upper()} document:")
        result = process_document(content)
        
        print(f"  Classification: {result['classification']['document_type']}")
        print(f"  Classification Confidence: {result['classification']['confidence']:.2%}")
        print(f"  Extraction Type: {result['extraction']['document_type']}")
        print(f"  Processing Status: {result['processing_status']}")
        
        # Show some key extracted fields
        if result['extraction']['extracted_fields']:
            print(f"  Sample Extracted Fields:")
            fields = result['extraction']['extracted_fields']
            count = 0
            for key, value in fields.items():
                if value and count < 3:  # Show first 3 non-empty fields
                    print(f"    {key}: {value}")
                    count += 1


def main():
    """Run all tests."""
    print("Document Classification Agent Test Suite")
    print("=" * 60)
    
    try:
        test_document_classification()
        test_data_extraction()
        test_complete_processing()
        
        print("\n\n" + "=" * 60)
        print("All tests completed successfully!")
        
    except Exception as e:
        print(f"Test failed with error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()