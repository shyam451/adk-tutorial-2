# Document Classification Agent

A specialized ADK agent for document classification and data extraction from KYC (Know Your Customer), passport, and W9 tax forms.

## Features

- **Document Classification**: Automatically classifies documents into KYC, passport, W9, or unknown categories
- **Data Extraction**: Extracts structured data from each document type
- **Confidence Scoring**: Provides confidence scores for classifications
- **Robust Processing**: Handles various document formats and edge cases

## Supported Document Types

### 1. KYC Documents
Extracts:
- Customer name and ID
- Date of birth
- Contact information (address, phone, email)
- ID document details
- Verification date and risk level

### 2. Passport Documents
Extracts:
- Passport number and personal details
- Nationality and birth information
- Issue and expiry dates
- Issuing authority

### 3. W9 Tax Forms
Extracts:
- Name and business information
- Tax classification
- Address details
- Taxpayer identification number
- Backup withholding status

## Usage

### Basic Classification
```python
from agent import classify_document_type

result = classify_document_type(document_content)
print(f"Document type: {result['document_type']}")
print(f"Confidence: {result['confidence']:.2%}")
```

### Data Extraction
```python
from agent import extract_kyc_data, extract_passport_data, extract_w9_data

# For KYC documents
kyc_data = extract_kyc_data(document_content)
print(kyc_data['extracted_fields'])

# For passport documents
passport_data = extract_passport_data(document_content)
print(passport_data['extracted_fields'])

# For W9 documents
w9_data = extract_w9_data(document_content)
print(w9_data['extracted_fields'])
```

### Complete Processing Pipeline
```python
from agent import process_document

result = process_document(document_content)
print(f"Classification: {result['classification']}")
print(f"Extraction: {result['extraction']}")
```

### Using the ADK Agent
```python
from agent import document_classification_agent

# The agent can be integrated into larger ADK applications
# and used with other agents or tools
```

## Testing

Run the test suite to verify functionality:
```bash
python3 test_agent.py
```

## File Structure

```
document_classification_agent/
├── __init__.py              # Package initialization
├── agent.py                 # Main agent implementation
├── sample_data.py           # Sample documents for testing
├── test_agent.py           # Test suite
└── README.md               # This file
```

## Implementation Details

### Classification Algorithm
- Uses keyword-based scoring for each document type
- Returns the document type with the highest score
- Provides confidence based on score ratios
- Handles unknown documents gracefully

### Data Extraction
- Pattern matching for common field formats
- Robust error handling for malformed data
- Structured output with confidence indicators
- Extensible for additional document types

### Error Handling
- Validates input format and structure
- Handles missing colons and malformed lines
- Provides fallback values for missing fields
- Returns structured error information

## Security Considerations

This agent is designed for defensive security use cases:
- Document verification and compliance checking
- Identity verification processes
- Tax form processing for legitimate business purposes
- KYC compliance for financial institutions

## Extensibility

The agent can be extended to support additional document types by:
1. Adding new keyword sets for classification
2. Implementing new extraction functions
3. Updating the process_document pipeline
4. Adding corresponding test cases

## Dependencies

- google-adk: Google Agent Development Kit
- Python 3.7+: Standard library only (no external dependencies for core functionality)