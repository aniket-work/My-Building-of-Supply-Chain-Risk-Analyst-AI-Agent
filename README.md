# Supply Chain Risk Analyst AI - Streamlit App

A professional AI-powered supply chain risk assessment platform built with Streamlit, featuring an Anthropic-inspired design and advanced thinking process visualization.

## 🚀 Features

- **Professional Anthropic-themed UI** with modern design elements
- **Thinking Process Visualization** showing vertical AI reasoning steps (similar to Google Gemini)
- **Interactive Chat Interface** for natural language queries
- **Real-time Analytics Dashboard** with risk metrics and visualizations
- **Sample Query Suggestions** for quick testing
- **Responsive Design** with sidebar configuration options
- **Advanced Risk Assessment** with multiple data sources

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- Tavily API key (for web search capabilities)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd My-Building-of-Supply-Chain-Risk-Analyst-AI-Agent
   ```

2. **Create and configure the .env file**
   ```bash
   # Create .env file with your API keys
   OPENAI_API_KEY=your_openai_api_key_here
   TAVILY_API_KEY=your_tavily_api_key_here
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**
   
   **Option 1: Using PowerShell (Windows)**
   ```powershell
   .\launch.ps1
   ```
   
   **Option 2: Using Python**
   ```bash
   python launch.py
   ```
   
   **Option 3: Direct Streamlit**
   ```bash
   streamlit run app.py
   ```

5. **Access the application**
   Open your browser and navigate to: `http://localhost:8501`

## 🎯 How to Use

### Main Interface
1. **Chat Interface**: Type your supply chain risk questions in the chat input
2. **Thinking Process**: Toggle "Show Thinking Process" to see AI reasoning steps
3. **Sample Queries**: Use pre-defined questions from the sidebar
4. **Analytics Dashboard**: View risk metrics and visualizations in real-time

### Sample Queries
- "What are the current supply chain risks for semiconductor manufacturing in Taiwan?"
- "How might port congestion in Long Beach affect automotive supply chains?"
- "What are the geopolitical risks affecting rare earth mineral supply chains?"
- "Analyze the impact of recent weather events on agricultural supply chains"

### Features Overview

#### 🧠 Thinking Process Visualization
The app displays the AI's reasoning process in vertical steps:
1. **Query Analysis** - Understanding the user's question
2. **Tool Selection** - Choosing appropriate analysis tools
3. **Information Gathering** - Searching for relevant data
4. **Risk Analysis** - Processing and analyzing information
5. **Synthesis** - Combining insights for final assessment

#### 📊 Analytics Dashboard
- **Risk Level**: Current assessment status
- **Sources**: Number of analyzed data sources
- **Regions**: Geographic areas affected
- **Confidence**: Analysis accuracy percentage

#### 🎨 Professional Design
- Anthropic-inspired color scheme
- Modern gradient backgrounds
- Smooth animations and transitions
- Responsive layout for all screen sizes

## 🔧 Configuration

### Theme Customization
Edit `app_config.py` to customize:
- Color scheme and branding
- Sample queries
- Risk categories
- Default metrics
- API settings

### Thinking Steps
Configure thinking process display in `app_config.py`:
```python
THINKING_STEPS_CONFIG = {
    "enable_by_default": True,
    "animation_speed": "0.6s",
    "step_delay": 0.5,
    "max_steps": 10
}
```

## 📁 Project Structure

```
My-Building-of-Supply-Chain-Risk-Analyst-AI-Agent/
├── app.py                 # Main Streamlit application
├── agent.py              # AI agent logic
├── config.py             # Configuration loader
├── app_config.py         # App-specific configuration
├── tools.py              # Analysis tools
├── prompts.py            # AI prompts
├── launch.py             # Python launcher script
├── launch.ps1            # PowerShell launcher script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── README.md            # Documentation
└── main.py              # Original CLI version
```

## 🚨 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your `.env` file exists and contains valid API keys
   - Check that API keys have proper permissions

2. **Package Installation Issues**
   - Make sure Python 3.8+ is installed
   - Try updating pip: `python -m pip install --upgrade pip`
   - Use virtual environment if needed

3. **Streamlit Not Starting**
   - Check if port 8501 is available
   - Try using a different port: `streamlit run app.py --server.port=8502`

4. **Thinking Steps Not Displaying**
   - Toggle the "Show Thinking Process" option in the sidebar
   - Check browser console for any JavaScript errors

### Performance Tips

- Use thinking mode sparingly for faster responses
- Clear chat history periodically to improve performance
- Ensure stable internet connection for API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Check the troubleshooting section
- Review the configuration options
- Open an issue in the repository

---

**Built with ❤️ using Streamlit, OpenAI, and modern web technologies**