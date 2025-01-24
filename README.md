# 🌍 AI-Powered Travel Itinerary Generator

## Project Overview

This project is a sophisticated AI-powered travel planning application that generates personalized travel itineraries using OpenAI's GPT model. The application provides a flexible and interactive way to create tailored travel experiences based on user preferences.

### 🎯 Assignment Objective

The goal was to build a multi-step prompt system that generates highly personalized travel itineraries by:
- Understanding user context
- Refining user inputs
- Creating coherent, day-by-day travel plans

## 🚀 Features

### CLI Application
- Interactive command-line interface
- Support for multiple destinations
- Customizable trip parameters:
  - Destination selection
  - Trip duration
  - Budget constraints
  - Personal interests

### Streamlit Web Application
- User-friendly web interface
- Real-time itinerary generation
- Comprehensive input options
- Immediate feedback and itinerary display

## 🔧 Technologies Used

- Python
- OpenAI GPT-4o API
- Streamlit (Web Interface)
- Argparse (CLI Argument Handling)

## 📦 Prerequisites

- Python 3.8+
- OpenAI API Key
- Required Python packages:
  - `openai`
  - `streamlit` (for web app)

## 🔐 Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/frzn23/travelChatbot.git
cd travelChatbot
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Configure OpenAI API Key
- Open `env.py`
- Replace `API_KEY = ""` with your actual OpenAI API key

## 💻 Running the Applications

### CLI Application
```bash
python main.py
```
Follow the interactive prompts to generate your travel itinerary.

### Streamlit Web Application
```bash
streamlit run app_st.py
```
Open the provided local URL in your web browser.

## 🤖 Prompt Engineering Approach

The project implements a multi-step prompt system:

1. **User Context Understanding**
   - Gather initial travel preferences
   - Capture key details like destination, budget, duration

2. **Input Refinement**
   - Use AI to ask clarifying questions
   - Extract more nuanced user preferences
   - Validate and enhance initial inputs

3. **Personalized Itinerary Generation**
   - Leverage GPT-4o to create unique, tailored travel plans
   - Consider budget, interests, and trip purpose

## 🌟 Evaluation Criteria Highlights

- **Prompt Design**: Clear, structured prompts guiding model responses
- **Prompt Chaining**: Strategic use of multiple prompts
- **Personalization**: Unique, preference-aligned itineraries
- **Documentation**: Comprehensive explanation of approach

## 🔍 Prompt Examples

### System Prompt
```
You are a professional travel agent creating a personalized travel itinerary for a client.
```

### User Prompt Structure
```
Destination: [User's Destination]
Budget: [Budget Level]
Trip Duration: [Number of Days]
Purpose: [Trip Purpose]
Preferences: [Specific Interests]
```

## 📝 Notes

- Requires an active OpenAI API key
- Responses are generated in real-time
- Itinerary uniqueness depends on AI model output

## 📄 License

MIT License

## 👥 Acknowledgements

- OpenAI for GPT-4o
- Streamlit for web application framework

## 🐛 Reporting Issues

Please report any issues or suggestions in the GitHub repository's issue tracker.
