# Autocomplete API Testing Report

## Overview
This document presents a detailed analysis of the autocomplete API available at `http://35.200.185.69:8000/v1/autocomplete`. The testing process follows a structured black-box testing methodology to evaluate the API's behavior under different conditions. The key areas examined include input handling, response behavior, security considerations, and recommendations for improvement.

---

## Approach Used to Solve the Problem

### Input-Based Testing
A variety of queries were tested to assess how the API processes different types of inputs:

- **Case Variations**: Uppercase vs. lowercase inputs (e.g., "A" vs. "a").
- **Different Query Lengths**: Single-letter, two-letter, and three-letter inputs.
- **Edge Cases**: Empty query, spaces, special characters, and non-English characters.
- **Fuzzy Matching**: Typo variations of words.

This approach helped identify patterns and inconsistencies in the API's response mechanism.

### Behavioral Analysis
Key aspects of the API's search behavior were examined, including:

- **Prefix-based Matching**: Checking if the API retrieves results based on input prefixes.
- **Case Sensitivity**: Determining whether uppercase and lowercase queries produce different results.
- **Fuzzy Matching**: Assessing whether minor typos return similar results.

Findings suggest that the API enforces a strict prefix-based search and is case-sensitive, leading to unexpected query failures.

### Rate Limiting Test
Multiple requests were sent in quick succession to identify if the API implements rate limiting. While no explicit rate-limiting restrictions were observed, inconsistent responses (`{ "count": 0, "results": [] }`) suggest possible hidden throttling mechanisms.

### Security & Special Character Handling
Special characters, numbers, and potential security vulnerabilities were tested, including:

- **SQL Injection Attempts**: `' OR 1=1 --`
- **Cross-Site Scripting (XSS) Attempts**: `<script>alert('xss')</script>`
- **Random Symbols and Unicode Characters**: `# $ % &`, Hindi ("हेलो"), Chinese ("你好"), Arabic ("مرحبا")

All such inputs were ignored, indicating strong security measures. However, querying a space (`" "`) unexpectedly returned results, suggesting a potential whitespace handling issue.

### Output Evaluation & Limitations
- **Result Consistency**: Identical queries returned the same results, indicating static responses.
- **Maximum Result Limitation**: The API restricts results to a maximum of 10 per query.

---

## Key Findings from API Testing

### Case Sensitivity
- **Uppercase queries** (e.g., "A", "AB", "Aaa") return no results.
- **Lowercase queries** (e.g., "a", "aa", "ab") return valid results.
- **Recommendation**: Enable case-insensitive search to improve usability.

### Minimum Input Length for Results
- Single-letter queries (e.g., "A", "B") return no results.
- Two-letter queries (e.g., "aa", "ab") return valid results.
- Three-letter queries (e.g., "aaa", "Aaa") return no results.
- **Conclusion**: The API enforces a strict two-letter prefix requirement.

### Empty Query Behavior
- An empty query (`""`) returns a default set of 10 results.
- **Recommendation**: Define whether this behavior is intentional.

### Prefix-Based Retrieval
The API retrieves results based on prefixes:
- "aab" returns 2 results.
- "aac" returns 0 results.
- "aad" returns 1 result.
- **Conclusion**: Some prefixes do not exist in the dataset.

### Result Limitation
- The API limits results to **10 per query**, even if more matches exist.

### Result Consistency
- Identical queries produce identical results, suggesting static responses.

### Rate Limiting
- **15 consecutive requests** returned `{ "count": 0, "results": [] }`, suggesting possible hidden rate limiting.

### Special Character Handling
- Queries with **numbers, symbols, and non-English characters** returned zero results.
- **XSS and SQL Injection attempts were ignored**, indicating good security measures.
- Querying a **space (' ')** returned results unexpectedly.
- **Recommendation**: Fix whitespace handling and refine special character processing.

### Fuzzy Matching
- Variants of "garment" (e.g., "grame", "grm", "garmnt", "grmnt") returned no results.
- **Conclusion**: The API lacks typo tolerance.
- **Recommendation**: Implement fuzzy matching for a better user experience.

### Endpoint Availability
- Only the /v1/autocomplete, /v2/autocomplete, /v3/autocomplete endpoint returned valid results.
---
