"""
Configuration file for the Supply Chain Risk Analyst AI Streamlit app
"""

# Theme configuration
THEME_CONFIG = {
    "primary_color": "#667eea",
    "secondary_color": "#764ba2",
    "accent_color": "#f39c12",
    "success_color": "#27ae60",
    "warning_color": "#f1c40f",
    "danger_color": "#e74c3c",
    "info_color": "#3498db",
    "background_color": "#f8f9fa",
    "text_color": "#2c3e50",
    "muted_color": "#7f8c8d"
}

# App configuration
APP_CONFIG = {
    "title": "Supply Chain Risk Analyst AI",
    "subtitle": "Advanced AI-powered supply chain risk assessment and intelligence platform",
    "icon": "🔗",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Thinking steps configuration
THINKING_STEPS_CONFIG = {
    "enable_by_default": True,
    "animation_speed": "0.6s",
    "step_delay": 0.5,  # seconds between steps
    "max_steps": 10
}

# Sample queries for the sidebar
SAMPLE_QUERIES = [
    "What are the current supply chain risks for semiconductor manufacturing in Taiwan?",
    "How might port congestion in Long Beach affect automotive supply chains?",
    "What are the geopolitical risks affecting rare earth mineral supply chains?",
    "Analyze the impact of recent weather events on agricultural supply chains",
    "What are the cybersecurity risks in pharmaceutical supply chains?",
    "How do trade tensions between US and China affect tech supply chains?",
    "Assess the resilience of food supply chains during natural disasters",
    "What are the regulatory risks in European automotive supply chains?"
]

# Risk categories for visualization
RISK_CATEGORIES = [
    "Geopolitical",
    "Weather & Natural Disasters",
    "Economic & Financial",
    "Infrastructure",
    "Regulatory & Legal",
    "Cybersecurity",
    "Labor & Social",
    "Environmental"
]

# Default metrics for dashboard
DEFAULT_METRICS = {
    "risk_level": "Medium",
    "sources_analyzed": 12,
    "regions_affected": 5,
    "confidence_score": 85
}

# API Configuration
API_CONFIG = {
    "openai_model": "gpt-4o",
    "max_tokens": 4000,
    "temperature": 0.7,
    "timeout": 30
}

# Streamlit specific configuration
STREAMLIT_CONFIG = {
    "page_title": APP_CONFIG["title"],
    "page_icon": APP_CONFIG["icon"],
    "layout": APP_CONFIG["layout"],
    "initial_sidebar_state": APP_CONFIG["initial_sidebar_state"]
}
