"""
Sample document data for testing the document classification agent.
"""

# Sample KYC document content
SAMPLE_KYC_DOCUMENT = """
Know Your Customer (KYC) Verification Document

Customer Name: John Smith
Customer ID: KYC-2024-001
Date of Birth: January 15, 1985
Address: 123 Main Street, Suite 400, New York, NY 10001
Phone: (555) 123-4567
Email: john.smith@email.com
ID Document Type: Driver's License
Document Number: DL123456789
Verification Date: March 15, 2024
Risk Level: Low

Customer Due Diligence completed as per AML requirements.
Identity verification passed.
Beneficial owner information on file.
"""

# Sample passport document content
SAMPLE_PASSPORT_DOCUMENT = """
PASSPORT

Passport No: P123456789
Surname: JOHNSON
Given Names: MARY ELIZABETH
Nationality: UNITED STATES OF AMERICA
Date of Birth: 12 JUN 1990
Place of Birth: CHICAGO, IL, USA
Sex: F
Date of Issue: 15 JAN 2020
Date of Expiry: 14 JAN 2030
Issuing Authority: U.S. Department of State

This passport is valid for travel to all countries unless otherwise endorsed.
"""

# Sample W9 form content
SAMPLE_W9_DOCUMENT = """
Form W-9 (Rev. October 2018)
Request for Taxpayer Identification Number and Certification

Name: Robert Wilson
Business Name: Wilson Consulting LLC
Tax Classification: Limited Liability Company
Address: 456 Business Ave
City: Los Angeles
State: CA
Zip Code: 90210
Taxpayer Identification Number: 12-3456789
Backup Withholding: Not subject to backup withholding
Signature Date: March 20, 2024

I certify that the TIN entered above is correct and that I am not subject to backup withholding.
"""

# Sample unknown document content
SAMPLE_UNKNOWN_DOCUMENT = """
Invoice #INV-2024-001

Bill To:
ABC Corporation
789 Corporate Blvd
Miami, FL 33101

Service Description: Consulting Services
Amount: $5,000.00
Due Date: April 15, 2024

Thank you for your business!
"""

# Dictionary of all sample documents
SAMPLE_DOCUMENTS = {
    'kyc': SAMPLE_KYC_DOCUMENT,
    'passport': SAMPLE_PASSPORT_DOCUMENT,
    'w9': SAMPLE_W9_DOCUMENT,
    'unknown': SAMPLE_UNKNOWN_DOCUMENT
}