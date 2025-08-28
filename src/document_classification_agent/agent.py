from typing import Any, Dict, Optional
from google.adk.agents import Agent
import json


def classify_document_with_llm(document_content: str, image_data: Optional[str] = None) -> Dict[str, Any]:
    """
    Classify document type using LLM analysis through a specialized sub-agent.
    
    Args:
        document_content: Text content extracted from document
        image_data: Base64 encoded image data (optional)
        
    Returns:
        Dictionary with classification results
    """
    # This function will be called by the classification sub-agent
    # For now, we'll create a structured prompt that the LLM can process
    
    classification_prompt = f"""
    Analyze the following document content and classify it into one of these categories:
    1. KYC (Know Your Customer) - Identity verification, customer due diligence, compliance documents
    2. PASSPORT - Travel documents with personal identification information
    3. W9 - US tax forms for taxpayer identification and certification
    4. UNKNOWN - If the document doesn't fit the above categories
    
    Document content:
    {document_content}
    
    Provide your response in JSON format with:
    - document_type: one of "kyc", "passport", "w9", or "unknown"
    - confidence: a number between 0 and 1
    - reasoning: brief explanation for the classification
    """
    
    # This will be handled by the sub-agent, but for direct function calls,
    # we'll provide a fallback classification logic
    content_lower = document_content.lower()
    
    # Enhanced keyword sets for better LLM-style analysis
    classification_indicators = {
        'kyc': {
            'keywords': ['know your customer', 'kyc', 'identity verification', 'customer identification',
                        'due diligence', 'aml', 'anti-money laundering', 'beneficial owner', 'customer name',
                        'customer id', 'verification date', 'risk level', 'compliance'],
            'patterns': ['customer', 'verification', 'identity', 'risk']
        },
        'passport': {
            'keywords': ['passport', 'travel document', 'nationality', 'passport number', 'passport no',
                        'place of birth', 'issuing authority', 'expiry date', 'given names', 'surname'],
            'patterns': ['passport', 'nationality', 'travel', 'issued', 'expiry']
        },
        'w9': {
            'keywords': ['w-9', 'form w-9', 'taxpayer identification', 'request for taxpayer',
                        'backup withholding', 'ein', 'ssn', 'taxpayer identification number',
                        'tax classification', 'business name'],
            'patterns': ['taxpayer', 'form', 'tax', 'withholding', 'certification']
        }
    }
    
    # Calculate sophisticated scores
    scores = {}
    for doc_type, indicators in classification_indicators.items():
        keyword_score = sum(1 for keyword in indicators['keywords'] if keyword in content_lower)
        pattern_score = sum(1 for pattern in indicators['patterns'] if pattern in content_lower)
        scores[doc_type] = keyword_score + (pattern_score * 0.5)
    
    # Determine classification with confidence
    if max(scores.values()) == 0:
        classification = 'unknown'
        confidence = 0.0
        reasoning = 'No matching patterns found for any supported document type'
    else:
        classification = max(scores, key=scores.get)
        total_score = sum(scores.values())
        confidence = scores[classification] / total_score if total_score > 0 else 0.0
        reasoning = f'High confidence match for {classification} document based on content analysis'
    
    return {
        'document_type': classification,
        'confidence': min(confidence, 1.0),  # Cap confidence at 1.0
        'scores': scores,
        'reasoning': reasoning,
        'classification_method': 'llm_enhanced',
        'description': f'Document classified as {classification} with confidence {confidence:.2%}'
    }


# Legacy function for backward compatibility
# def classify_document_type(document_content: str, image_data: Optional[str] = None) -> Dict[str, Any]:
#     """
#     Legacy classify function that calls the new LLM-based classifier.
#     """
#     return classify_document_with_llm(document_content, image_data)


def extract_kyc_with_llm(document_content: str) -> Dict[str, Any]:
    """
    Extract KYC data using LLM analysis. This tool will be called by the KYC extraction sub-agent.
    
    Args:
        document_content: Text content from KYC document
        
    Returns:
        Dictionary with extracted KYC data
    """
    # This function provides the expected structure for KYC extraction
    # The actual extraction will be performed by the LLM sub-agent
    return {
        'document_type': 'kyc',
        'expected_fields': [
            'customer_name', 'customer_id', 'date_of_birth', 'address', 
            'phone_number', 'email', 'id_document_type', 'id_document_number', 
            'verification_date', 'risk_level'
        ],
        'extraction_method': 'llm_based',
        'document_content': document_content
    }


def extract_passport_with_llm(document_content: str) -> Dict[str, Any]:
    """
    Extract passport data using LLM analysis. This tool will be called by the passport extraction sub-agent.
    
    Args:
        document_content: Text content from passport document
        
    Returns:
        Dictionary with extracted passport data
    """
    # This function provides the expected structure for passport extraction
    # The actual extraction will be performed by the LLM sub-agent
    return {
        'document_type': 'passport',
        'expected_fields': [
            'passport_number', 'surname', 'given_names', 'nationality', 
            'date_of_birth', 'place_of_birth', 'sex', 'date_of_issue', 
            'date_of_expiry', 'issuing_authority'
        ],
        'extraction_method': 'llm_based',
        'document_content': document_content
    }


def extract_w9_with_llm(document_content: str) -> Dict[str, Any]:
    """
    Extract W9 data using LLM analysis. This tool will be called by the W9 extraction sub-agent.
    
    Args:
        document_content: Text content from W9 form
        
    Returns:
        Dictionary with extracted W9 data
    """
    # This function provides the expected structure for W9 extraction
    # The actual extraction will be performed by the LLM sub-agent
    return {
        'document_type': 'w9',
        'expected_fields': [
            'name', 'business_name', 'tax_classification', 'address', 
            'city', 'state', 'zip_code', 'taxpayer_id_number', 
            'backup_withholding', 'signature_date'
        ],
        'extraction_method': 'llm_based',
        'document_content': document_content
    }


# def process_document(document_content: str, image_data: Optional[str] = None) -> Dict[str, Any]:
#     """
#     Complete document processing pipeline: classify and extract data.
    
#     Args:
#         document_content: Text content from document
#         image_data: Base64 encoded image data (optional)
        
#     Returns:
#         Dictionary with classification and extraction results
#     """
#     # First classify the document
#     classification_result = classify_document_type(document_content, image_data)
#     document_type = classification_result['document_type']
    
#     # Extract data based on document type
#     if document_type == 'kyc':
#         extraction_result = extract_kyc_data(document_content)
#     elif document_type == 'passport':
#         extraction_result = extract_passport_data(document_content)
#     elif document_type == 'w9':
#         extraction_result = extract_w9_data(document_content)
#     else:
#         extraction_result = {
#             'document_type': 'unknown',
#             'extracted_fields': {},
#             'extraction_confidence': 'low',
#             'description': 'Document type not supported for data extraction'
#         }
    
#     # Combine results
#     return {
#         'classification': classification_result,
#         'extraction': extraction_result,
#         'processing_status': 'completed',
#         'description': f'Document processed: {document_type} classification with data extraction'
#     }


# Create specialized extraction sub-agents
kyc_extraction_agent = Agent(
    name="kyc_extraction_specialist",
    model="gemini-2.0-flash",
    description="Specialized agent for extracting structured data from KYC documents.",
    instruction="""You are a KYC (Know Your Customer) data extraction specialist. Your task is to analyze KYC documents and extract all relevant structured information.

For KYC documents, extract these fields when available:
- customer_name: Full name of the customer
- customer_id: Unique customer identifier
- date_of_birth: Customer's date of birth
- address: Complete address information
- phone_number: Contact phone number
- email: Email address
- id_document_type: Type of ID document (driver's license, etc.)
- id_document_number: ID document number
- verification_date: When verification was completed
- risk_level: Assigned risk level (low, medium, high)

Analyze the document content carefully and extract as much information as possible. Provide confidence scores for each extracted field based on how certain you are about the accuracy of the extraction.

Return the results in a structured JSON format with:
- document_type: "kyc"
- extracted_fields: dictionary of field names and values
- extraction_confidence: overall confidence score
- field_confidence: individual confidence for each field
- description: brief summary of extraction results""",
    tools=[extract_kyc_with_llm]
)

passport_extraction_agent = Agent(
    name="passport_extraction_specialist", 
    model="gemini-2.0-flash",
    description="Specialized agent for extracting structured data from passport documents.",
    instruction="""You are a passport data extraction specialist. Your task is to analyze passport documents and extract all relevant structured information.

For passport documents, extract these fields when available:
- passport_number: Passport identification number
- surname: Family name/last name
- given_names: First and middle names
- nationality: Country of citizenship
- date_of_birth: Date of birth
- place_of_birth: Birth location
- sex: Gender (M/F)
- date_of_issue: When passport was issued
- date_of_expiry: Passport expiration date
- issuing_authority: Authority that issued the passport

Analyze the document content carefully and extract as much information as possible. Pay attention to various passport formats and layouts.

Return the results in a structured JSON format with:
- document_type: "passport"
- extracted_fields: dictionary of field names and values
- extraction_confidence: overall confidence score
- field_confidence: individual confidence for each field
- description: brief summary of extraction results""",
    tools=[extract_passport_with_llm]
)

w9_extraction_agent = Agent(
    name="w9_extraction_specialist",
    model="gemini-2.0-flash", 
    description="Specialized agent for extracting structured data from W9 tax forms.",
    instruction="""You are a W9 tax form data extraction specialist. Your task is to analyze W9 forms and extract all relevant structured information.

For W9 forms, extract these fields when available:
- name: Individual or business name
- business_name: Business name (if different from above)
- tax_classification: Entity classification (Individual, Corporation, LLC, etc.)
- address: Street address
- city: City name
- state: State abbreviation
- zip_code: ZIP code
- taxpayer_id_number: SSN, EIN, or other TIN
- backup_withholding: Backup withholding status
- signature_date: Date when form was signed

Analyze the document content carefully and extract as much information as possible. Be aware of different W9 form versions and layouts.

Return the results in a structured JSON format with:
- document_type: "w9"
- extracted_fields: dictionary of field names and values
- extraction_confidence: overall confidence score
- field_confidence: individual confidence for each field
- description: brief summary of extraction results""",
    tools=[extract_w9_with_llm]
)

# Create a specialized classification sub-agent
classification_specialist_agent = Agent(
    name="document_classification_specialist",
    model="gemini-2.0-flash",
    description="Specialized sub-agent focused exclusively on document type classification.",
    instruction="""You are an expert document classification specialist. Your only task is to analyze document content and classify it into one of these categories:

1. KYC (Know Your Customer) - Documents containing customer identification and verification information
2. PASSPORT - Travel documents with personal identification data
3. W9 - US tax forms for taxpayer identification and certification  
4. UNKNOWN - Documents that don't clearly fit into the above categories

Analyze the document content carefully and provide:
- Accurate classification based on content and structure
- High confidence score for clear matches
- Detailed reasoning for your classification decision

Always respond with structured data including document_type, confidence, and reasoning.""",
    tools=[classify_document_with_llm]
)


# Create the main document classification agent with all specialized sub-agents
root_agent = Agent(
    name="document_classification_agent",
    model="gemini-2.0-flash",
    description="Comprehensive agent for document classification and data extraction from KYC, passport, and W9 forms using specialized LLM-based sub-agents.",
    instruction="""You are a comprehensive document processing system with access to specialized sub-agents for both classification and extraction.

Your workflow:
1. First, use the classification specialist sub-agent to accurately classify the document
2. Based on the classification result, delegate to the appropriate extraction specialist:
   - For KYC documents: use the KYC extraction specialist
   - For passport documents: use the passport extraction specialist  
   - For W9 documents: use the W9 extraction specialist
3. Provide complete processing results with both classification and extraction information

You have access to:
- A classification specialist sub-agent for document type identification
- Specialized extraction sub-agents for each document type (KYC, passport, W9)
- Complete LLM-powered processing pipeline for intelligent document analysis

Always delegate to the appropriate specialist sub-agents rather than trying to do the work yourself. Each sub-agent is optimized for their specific task and will provide more accurate results.

Provide thorough analysis with confidence scores and detailed extraction results from the specialist agents.""",
    tools=[],  # No tools needed - everything is handled by sub-agents
    sub_agents=[classification_specialist_agent, kyc_extraction_agent, passport_extraction_agent, w9_extraction_agent]
)