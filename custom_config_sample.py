"""
Sample configuration file showing how to customize the Streamlit app
Copy this to create your own customizations
"""

# Custom color scheme - Anthropic Claude theme
CUSTOM_THEME = {
    "primary_color": "#FF6B35",      # Claude orange
    "secondary_color": "#4A90E2",    # Blue accent
    "accent_color": "#F7931E",       # Orange accent
    "success_color": "#5CB85C",      # Green
    "warning_color": "#F0AD4E",      # Yellow
    "danger_color": "#D9534F",       # Red
    "info_color": "#5BC0DE",         # Light blue
    "background_color": "#FAFAFA",   # Light gray
    "text_color": "#333333",         # Dark gray
    "muted_color": "#999999"         # Medium gray
}

# Custom sample queries for your specific use case
CUSTOM_QUERIES = [
    "Analyze semiconductor supply chain vulnerabilities in Asia-Pacific region",
    "What are the climate change impacts on global agricultural supply chains?",
    "Assess cybersecurity risks in pharmaceutical manufacturing networks",
    "How do US-China trade policies affect tech hardware supply chains?",
    "Evaluate port congestion effects on European automotive industry",
    "What are the labor shortage impacts on logistics and warehousing?",
    "Analyze rare earth mineral supply chain dependencies and risks",
    "How might geopolitical tensions affect energy supply chains?"
]

# Custom risk categories for your industry
CUSTOM_RISK_CATEGORIES = [
    "Supply Disruption",
    "Demand Volatility", 
    "Regulatory Changes",
    "Technology Obsolescence",
    "Currency Fluctuation",
    "Quality & Compliance",
    "Environmental Impact",
    "Social Responsibility"
]

# Custom thinking steps for specialized analysis
CUSTOM_THINKING_STEPS = [
    {
        "title": "Market Context Analysis",
        "description": "Analyzing current market conditions and economic indicators"
    },
    {
        "title": "Supplier Risk Assessment", 
        "description": "Evaluating supplier reliability and geographic distribution"
    },
    {
        "title": "Demand Pattern Analysis",
        "description": "Examining historical demand patterns and future projections"
    },
    {
        "title": "Risk Correlation Mapping",
        "description": "Identifying interconnected risks across the supply network"
    },
    {
        "title": "Mitigation Strategy Development",
        "description": "Formulating actionable risk mitigation recommendations"
    }
]

# Custom metrics for your dashboard
CUSTOM_METRICS = {
    "supply_reliability": {
        "label": "Supply Reliability",
        "value": "94%",
        "color": "success"
    },
    "lead_time_variance": {
        "label": "Lead Time Variance", 
        "value": "+15%",
        "color": "warning"
    },
    "inventory_turnover": {
        "label": "Inventory Turnover",
        "value": "8.2x",
        "color": "info"
    },
    "cost_volatility": {
        "label": "Cost Volatility",
        "value": "±12%",
        "color": "danger"
    }
}

# Instructions for implementation:
# 1. Copy the configurations you want to customize
# 2. Add them to app_config.py
# 3. Update the app.py imports if needed
# 4. Restart the Streamlit app to see changes
