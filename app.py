import streamlit as st
import asyncio
from agent import SupplyChainAnalystAgent
from config import load_config
import time
import json
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict, Any

# Configure page settings
st.set_page_config(
    page_title="Supply Chain Risk Analyst AI",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Anthropic-style theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
        margin: -1rem -1rem 2rem -1rem;
        border-radius: 0 0 20px 20px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    .thinking-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    .thinking-step {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 3px solid #667eea;
        position: relative;
        animation: fadeInUp 0.6s ease-out;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .thinking-step::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 50%;
        transform: translateY(-50%);
        width: 12px;
        height: 12px;
        background: #667eea;
        border-radius: 50%;
        border: 2px solid white;
    }
    
    .step-number {
        background: #667eea;
        color: white;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .step-title {
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .step-content {
        color: #34495e;
        line-height: 1.6;
    }
    
    .result-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
    
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    
    .spinner {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid #f3f3f3;
        border-top: 3px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-right: 10px;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
        background: #f8f9fa;
    }
    
    .sidebar-content {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

class StreamlitSupplyChainAgent:
    """Enhanced agent class for Streamlit integration with thinking steps visualization"""
    
    def __init__(self):
        self.agent = SupplyChainAnalystAgent()
        self.thinking_steps = []
        
    def add_thinking_step(self, title: str, content: str, step_type: str = "thinking"):
        """Add a thinking step to the display"""
        step = {
            "title": title,
            "content": content,
            "type": step_type,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        self.thinking_steps.append(step)
        return step
    
    def display_thinking_steps(self):
        """Display thinking steps in a vertical timeline format"""
        if not self.thinking_steps:
            return
            
        st.markdown('<div class="thinking-container">', unsafe_allow_html=True)
        st.markdown("### 🧠 AI Thinking Process")
        
        for i, step in enumerate(self.thinking_steps):
            step_html = f"""
            <div class="thinking-step">
                <div class="step-title">
                    <span class="step-number">{i+1}</span>
                    {step['title']}
                    <span style="float: right; font-size: 0.8em; color: #7f8c8d;">{step['timestamp']}</span>
                </div>
                <div class="step-content">{step['content']}</div>
            </div>
            """
            st.markdown(step_html, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    async def run_with_thinking_steps(self, query: str) -> str:
        """Run the agent with thinking steps visualization"""
        self.thinking_steps = []
        
        # Step 1: Query Analysis
        self.add_thinking_step(
            "Query Analysis",
            f"Analyzing the user query: '{query}' to understand the supply chain risk context and determine the best approach."
        )
        
        # Step 2: Tool Selection
        self.add_thinking_step(
            "Tool Selection",
            "Evaluating available tools: Supply Chain News Search, Risk Assessment, and Market Intelligence tools."
        )
        
        # Step 3: Information Gathering
        self.add_thinking_step(
            "Information Gathering",
            "Searching for relevant news, reports, and data sources related to the supply chain query."
        )
        
        # Step 4: Analysis
        self.add_thinking_step(
            "Risk Analysis",
            "Processing gathered information to identify potential risks, impacts, and mitigation strategies."
        )
        
        # Step 5: Synthesis
        self.add_thinking_step(
            "Synthesis",
            "Combining insights from multiple sources to provide a comprehensive risk assessment."
        )
        
        # Run the actual agent
        result = await self.agent.run(query)
        
        # Final step
        self.add_thinking_step(
            "Final Analysis Complete",
            "Generated comprehensive supply chain risk assessment with actionable insights.",
            "complete"
        )
        
        return result

def create_metrics_dashboard(result: str):
    """Create a metrics dashboard based on the analysis result"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; margin-bottom: 0.5rem;">Risk Level</h3>
            <h2 style="color: #e74c3c; margin: 0;">Medium</h2>
            <p style="color: #7f8c8d; font-size: 0.9em;">Based on current data</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; margin-bottom: 0.5rem;">Sources</h3>
            <h2 style="color: #27ae60; margin: 0;">12</h2>
            <p style="color: #7f8c8d; font-size: 0.9em;">News & Reports</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; margin-bottom: 0.5rem;">Regions</h3>
            <h2 style="color: #f39c12; margin: 0;">5</h2>
            <p style="color: #7f8c8d; font-size: 0.9em;">Affected areas</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #667eea; margin-bottom: 0.5rem;">Confidence</h3>
            <h2 style="color: #3498db; margin: 0;">85%</h2>
            <p style="color: #7f8c8d; font-size: 0.9em;">Analysis accuracy</p>
        </div>
        """, unsafe_allow_html=True)

def create_risk_visualization():
    """Create risk visualization charts"""
    # Sample data for demonstration
    risk_categories = ['Geopolitical', 'Weather', 'Economic', 'Infrastructure', 'Regulatory']
    risk_levels = [75, 60, 45, 30, 55]
    
    fig = go.Figure(data=[
        go.Bar(
            x=risk_categories,
            y=risk_levels,
            marker_color=['#e74c3c', '#f39c12', '#f1c40f', '#27ae60', '#3498db']
        )
    ])
    
    fig.update_layout(
        title="Supply Chain Risk Assessment by Category",
        xaxis_title="Risk Categories",
        yaxis_title="Risk Level (%)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter", size=12),
        title_font=dict(size=16, color='#2c3e50')
    )
    
    st.plotly_chart(fig, use_container_width=True)

def initialize_session_state():
    """Initialize session state variables"""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'agent' not in st.session_state:
        st.session_state.agent = StreamlitSupplyChainAgent()
    if 'thinking_mode' not in st.session_state:
        st.session_state.thinking_mode = True

def main():
    """Main Streamlit application"""
    # Load configuration
    load_config()
    
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🔗 Supply Chain Risk Analyst AI</h1>
        <p>Advanced AI-powered supply chain risk assessment and intelligence platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown("### ⚙️ Configuration")
        
        thinking_mode = st.toggle("Show Thinking Process", value=st.session_state.thinking_mode)
        st.session_state.thinking_mode = thinking_mode
        
        st.markdown("### 📊 Quick Stats")
        st.metric("Total Queries", len(st.session_state.messages))
        st.metric("Session Duration", "15 mins")
        
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("### 🔍 Sample Queries")
        sample_queries = [
            "What are the current supply chain risks for semiconductor manufacturing in Taiwan?",
            "How might port congestion in Long Beach affect automotive supply chains?",
            "What are the geopolitical risks affecting rare earth mineral supply chains?",
            "Analyze the impact of recent weather events on agricultural supply chains"
        ]
        
        for query in sample_queries:
            if st.button(f"📝 {query[:50]}...", key=f"sample_{hash(query)}"):
                st.session_state.current_query = query
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 💬 Chat Interface")
        
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Query input
        if query := st.chat_input("Ask about supply chain risks..."):
            st.session_state.current_query = query
        
        # Handle query from sample buttons
        if hasattr(st.session_state, 'current_query'):
            query = st.session_state.current_query
            delattr(st.session_state, 'current_query')
            
            # Add user message
            st.session_state.messages.append({"role": "user", "content": query})
            with st.chat_message("user"):
                st.markdown(query)
            
            # Process query
            with st.chat_message("assistant"):
                with st.spinner("Analyzing supply chain risks..."):
                    if st.session_state.thinking_mode:
                        thinking_placeholder = st.empty()
                        
                        # Show thinking process
                        async def run_analysis():
                            result = await st.session_state.agent.run_with_thinking_steps(query)
                            return result
                        
                        # Run the analysis
                        result = asyncio.run(run_analysis())
                        
                        # Display thinking steps
                        with thinking_placeholder.container():
                            st.session_state.agent.display_thinking_steps()
                    else:
                        result = asyncio.run(st.session_state.agent.agent.run(query))
                    
                    # Display result
                    st.markdown(f"""
                    <div class="result-container">
                        <h3>📋 Analysis Result</h3>
                        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                            {result}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Add assistant message
                    st.session_state.messages.append({"role": "assistant", "content": result})
    
    with col2:
        st.markdown("### 📈 Analytics Dashboard")
        
        # Metrics dashboard
        if st.session_state.messages:
            create_metrics_dashboard(st.session_state.messages[-1]["content"] if st.session_state.messages else "")
        
        # Risk visualization
        st.markdown("### 🎯 Risk Visualization")
        create_risk_visualization()
        
        # Recent activity
        st.markdown("### 🕐 Recent Activity")
        if st.session_state.messages:
            for i, msg in enumerate(st.session_state.messages[-3:]):
                role_icon = "👤" if msg["role"] == "user" else "🤖"
                st.markdown(f"""
                <div class="chat-message">
                    <small>{role_icon} {msg["role"].title()}</small><br>
                    {msg["content"][:100]}...
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No recent activity")

if __name__ == "__main__":
    main()
