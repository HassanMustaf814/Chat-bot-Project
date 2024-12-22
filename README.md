# Chat-bot-Project
Title
AI-Powered Chatbot for PDF and Word Document Querying
________________________________________
1. Introduction
With the growing use of unstructured data, it has become critical to create tools that can help users make sense of it. This project addresses this need by enabling users to interact with document content using natural language queries.
________________________________________
2. System Design
2.1 Architecture
•	Frontend: A Streamlit-based interface to upload files and input queries.
•	Backend: Handles file processing, text chunking, and query answering.
•	AI Integration: Google Generative AI manages conversational responses.
2.2 Workflow
1.	User uploads PDF/Word documents.
2.	Files are processed, and their content is split into chunks.
3.	The FAISS vector store indexes these chunks.
4.	User queries are matched against the indexed content.
5.	The AI model generates accurate and context-aware answers.
________________________________________
3. Implementation
The implementation is divided into three main modules:
1.	File Processing: Extracts text and prepares it for querying.
2.	Vector Store: Indexes and retrieves document chunks.
3.	Question-Answering Chain: Uses Google Generative AI to handle queries.
________________________________________
4. Results
The chatbot was tested with multiple document types and achieved high accuracy in responses. Users found the interface intuitive and the responses contextually relevant.
________________________________________
5. Conclusion
This project demonstrates the feasibility of combining AI and document processing to deliver an innovative and practical solution for document querying.

