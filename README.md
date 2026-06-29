# 💱 AI Currency Converter Agent

An AI-powered Currency Converter Agent built using **Python**, **OpenRouter LLM**, **ExchangeRate API**, and **Streamlit**. The agent understands natural language currency conversion requests, automatically invokes an external API to retrieve real-time exchange rates, and provides accurate currency conversions through an interactive chat interface.

---

# 📌 Project Overview

The AI Currency Converter Agent is an intelligent conversational assistant that performs real-time currency conversions between different international currencies. Instead of relying on hardcoded exchange rates, the agent uses the **ExchangeRate API** to retrieve the latest market exchange rates whenever a user requests a conversion.

The Large Language Model (LLM) analyzes the user's request, determines when a currency conversion is required, invokes the currency conversion tool, processes the API response, and presents the result in a clear and user-friendly format.

This project demonstrates the practical implementation of **Agentic AI**, where an AI model collaborates with external tools to solve real-world problems.

---

# 🎯 Objectives

- Build an AI-powered currency conversion assistant.
- Integrate an external REST API for live exchange rates.
- Demonstrate OpenRouter Tool Calling.
- Provide an interactive Streamlit chatbot interface.
- Store conversation history using memory.
- Allow users to perform conversions using natural language.

---

# 🚀 Features

- 🤖 AI-powered conversational chatbot
- 💱 Real-time currency conversion
- 🌍 Supports over 160 international currencies
- 📈 Live exchange rates
- ⚡ Fast API response
- 🧠 Conversation memory
- 💬 Natural language understanding
- 🔄 Automatic tool calling
- 📜 Chat history
- 🖥️ Streamlit web application
- 🎨 User-friendly interface
- 🔐 Secure API key management using `.env`

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| OpenRouter | Large Language Model API |
| ExchangeRate API | Real-Time Exchange Rates |
| Streamlit | Web User Interface |
| Requests | REST API Calls |
| JSON | Conversation Memory |
| python-dotenv | Environment Variables |

---

# 📂 Project Structure

```
Currency_Agent/
│
├── app.py
├── main.py
├── tools.py
├── prompts.py
├── memory.py
├── memory.json
├── .env
├── requirements.txt
└── README.md
```

---

# 🔑 Environment Variable

Create a `.env` file.

```
OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
```

---

# 🌐 API Used

## ExchangeRate API

Endpoint

```
https://open.er-api.com/v6/latest/USD
```

Example

```
https://open.er-api.com/v6/latest/INR
```

No API key is required for the ExchangeRate API.

---

# 🤖 Agent Workflow

```
                 User
                   │
                   ▼
          Streamlit Chat Interface
                   │
                   ▼
              User Prompt
                   │
                   ▼
            OpenRouter LLM
                   │
                   ▼
      Determines Tool Requirement
                   │
                   ▼
      Calls currency_converter()
                   │
                   ▼
          ExchangeRate API
                   │
                   ▼
      Returns Exchange Rates
                   │
                   ▼
       LLM Formats Response
                   │
                   ▼
         Streamlit Displays Result
```

---

# 🧰 Tool Used

## currency_converter()

### Purpose

Converts an amount from one currency to another using real-time exchange rates.

### Parameters

| Parameter | Type | Description |
|------------|------|-------------|
| from_currency | String | Source Currency |
| to_currency | String | Target Currency |
| amount | Float | Amount to Convert |

---

# 🌍 Supported Currencies

The agent supports almost every international currency including:

- USD
- INR
- EUR
- GBP
- AUD
- CAD
- SGD
- AED
- CHF
- CNY
- JPY
- NZD
- PKR
- LKR
- MYR
- ZAR
- SAR
- THB
- RUB
- KRW

and many more.

---

# 🖥️ Streamlit Interface

The user interface provides:

- ChatGPT-style conversation
- Sidebar information
- Currency conversion examples
- Chat history
- Loading spinner
- Clear Chat button
- Responsive layout
- Easy-to-use chat input

---

# 🧠 Memory Management

Conversation history is stored inside

```
memory.json
```

The memory module

- Stores previous conversations
- Loads existing history
- Saves new interactions
- Maintains conversational context

---

# 📊 System Architecture

```
                    User
                      │
                      ▼
            Streamlit Interface
                      │
                      ▼
                 main.py
                      │
                      ▼
              OpenRouter API
                      │
              Tool Calling
                      │
                      ▼
                 tools.py
                      │
                      ▼
             ExchangeRate API
                      │
                      ▼
              Exchange Rates
                      │
                      ▼
             OpenRouter Response
                      │
                      ▼
            Streamlit Interface
```

---

# 📁 File Description

## app.py

- Streamlit User Interface
- Chat Interface
- Displays Conversation
- Handles User Input

---

## main.py

Responsible for

- OpenRouter Communication
- Agent Loop
- Tool Calling
- Memory Loading
- Memory Saving
- Final Response Generation

---

## tools.py

Contains

```
currency_converter()
```

Responsibilities

- Calls ExchangeRate API
- Fetches Exchange Rates
- Converts Currency
- Returns Final Result

---

## prompts.py

Contains the System Prompt.

Responsibilities

- Defines AI behaviour
- Instructs model to use tools
- Controls conversation style

---

## memory.py

Responsibilities

- Load conversation
- Save conversation
- Maintain history

---

## memory.json

Stores conversation history in JSON format.

---

# 📈 Advantages

- Beginner Friendly
- Real-world Application
- Modular Code Structure
- Easy to Extend
- Uses Live Data
- Demonstrates Agentic AI
- External API Integration
- Tool Calling
- Interactive Interface
- Memory Support
- Scalable Architecture

---

# 🔮 Future Enhancements

- Historical Exchange Rates
- Exchange Rate Charts
- Currency Trend Prediction
- Voice Input
- Voice Output
- User Authentication
- Conversion History Dashboard
- Export Conversion History
- Favorite Currency Pairs
- Dark Mode
- Multi-language Support
- Offline Cached Exchange Rates
- Currency Comparison Dashboard
- Mobile Responsive Design

---

# 🎓 Learning Outcomes

This project demonstrates:

- Agentic AI
- Prompt Engineering
- Function Calling
- Tool Calling
- REST API Integration
- JSON Parsing
- Streamlit Development
- Conversation Memory
- Python Programming
- OpenRouter API Integration
- Environment Variable Management

---

# 📸 Sample Conversation

### User

```
Convert 100 USD to INR
```

### Agent

```
100 USD is approximately 8582.74 INR based on the latest exchange rate.
```

---

### User

```
Convert 500 EUR to GBP
```

### Agent

```
500 EUR is approximately 425.18 GBP.
```

---

### User

```
Convert 1000 JPY to USD
```

### Agent

```
1000 JPY is approximately 6.82 USD.
```

---

# 📄 License

This project is intended for educational and learning purposes.

---

# 👨‍💻 Author

Developed as a hands-on Agentic AI project using **Python**, **OpenRouter**, **ExchangeRate API**, and **Streamlit** to demonstrate tool calling, conversational AI, memory management, and real-time API integration.
