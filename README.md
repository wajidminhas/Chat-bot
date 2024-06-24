## PIAIC Chatbot - Gemini Pro Chatbot

This Streamlit application uses Google Gemini Pro's generative AI capabilities to create an interactive chatbot. Users can ask questions, and the chatbot provides responses while maintaining a chat history throughout the session.

# Features
Interactive chatbot using Google Gemini Pro.
Maintains chat history for the session.
User-friendly interface for asking questions and viewing responses.


# Requirements
 * Python 3.7+
 * Poetry


# Install Dependencies
    Ensure you have Poetry installed. Then, run:

    poetry install


# Configure Environment Variables
    Create a .env file in the root directory of the project and add your Google API key:


* GOOGLE_API_KEY="your_google_api_key"

# Run the Application
    Start the Poetry shell and run the Streamlit application:


    poetry shell
    streamlit run app.py
