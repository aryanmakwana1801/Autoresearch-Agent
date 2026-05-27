import streamlit as st
import requests
import time
import threading

# Page Configurations
st.set_page_config(
    page_title="AutoResearch Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium Styling & Theme Injection
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Glow Background Accent */
    .stApp {
        background: radial-gradient(circle at 80% 10%, rgba(168, 85, 247, 0.08) 0%, rgba(10, 12, 18, 1) 80%);
    }

    /* Glowing Multi-Color Gradient Title */
    .glowing-title {
        background: linear-gradient(135deg, #A855F7 0%, #EC4899 50%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin-bottom: 5px;
        margin-top: 10px;
    }
    
    .subtitle-text {
        font-size: 1.15rem;
        color: #94A3B8;
        font-weight: 300;
        margin-top: 0px;
        margin-bottom: 2rem;
    }

    /* Premium Glassmorphic Cards */
    .glass-card {
        background: rgba(30, 41, 59, 0.35);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 2.2rem;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
        margin-bottom: 1.5rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .glass-card:hover {
        border-color: rgba(168, 85, 247, 0.3);
        box-shadow: 0 20px 40px rgba(168, 85, 247, 0.06);
        transform: translateY(-2px);
    }

    /* Customized Sidebar Elements */
    .sidebar-header {
        font-size: 1.6rem;
        font-weight: 800;
        background: linear-gradient(135deg, #A855F7 0%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        text-align: center;
    }

    .sidebar-section {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 14px;
        padding: 1.2rem;
        margin-bottom: 1.2rem;
        border: 1px solid rgba(255, 255, 255, 0.04);
    }

    /* Stage Active Animation Card */
    .stage-card {
        background: rgba(168, 85, 247, 0.06);
        border: 1px solid rgba(168, 85, 247, 0.2);
        border-radius: 14px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 0 20px rgba(168, 85, 247, 0.1);
        animation: pulseGlow 2.5s infinite ease-in-out;
    }
    
    @keyframes pulseGlow {
        0%, 100% { transform: scale(1); opacity: 0.95; box-shadow: 0 0 20px rgba(168, 85, 247, 0.1); }
        50% { transform: scale(1.01); opacity: 1; box-shadow: 0 0 30px rgba(168, 85, 247, 0.25); border-color: rgba(236, 72, 153, 0.4); }
    }

    /* Custom Metric Styling */
    .custom-metric {
        background: rgba(15, 23, 42, 0.45);
        border-bottom: 4px solid #A855F7;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .custom-metric.pink { border-bottom-color: #EC4899; }
    .custom-metric.blue { border-bottom-color: #3B82F6; }

    .custom-metric-title {
        font-size: 0.82rem;
        color: #94A3B8;
        text-transform: uppercase;
        font-weight: 600;
        letter-spacing: 0.8px;
        margin-bottom: 0.4rem;
    }
    
    .custom-metric-value {
        font-size: 1.7rem;
        font-weight: 800;
        color: #F1F5F9;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Design
with st.sidebar:
    st.markdown('<div class="sidebar-header">🧠 AutoResearch</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown("### ⚡ Engine Infrastructure")
    st.markdown("""
    - **LangGraph** — Stateful Agent workflows
    - **LangChain** — Tool bindings & interfaces
    - **Groq Llama-3.3** — High-speed reasoning
    - **Tavily Search** — Professional Web Index
    - **FastAPI** — Concurrent Backend Service
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sidebar-section">', unsafe_allow_html=True)
    st.markdown("### 🚀 Agent Pipeline Stages")
    st.markdown("""
    1. 📋 **Planner** — Decoupled task creation
    2. 🔍 **Researcher** — Live query searches
    3. 📄 **Summarizer** — Card content synthesis
    4. ✍️ **Writer** — Report drafting (MD)
    5. 🛡️ **Supervisor** — Quality assurance reviews
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("Engineered by Aryan Makwana")

# App Header
st.markdown('<h1 class="glowing-title">🤖 AutoResearch Agent</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">An advanced, stateful multi-agent AI system that investigates deep topics and delivers verified, high-quality markdown reports.</p>', unsafe_allow_html=True)

# Main Query input wrapped in a beautiful Card
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("### 🔎 Define Your Inquiry")
query = st.text_input(
    "Enter your research query:", 
    placeholder="e.g. Compare the architecture of DeepSeek-V3 vs Llama-3.3-70B, highlighting their training efficiencies.",
    label_visibility="collapsed"
)

# Custom spacing columns for search button
_, btn_col, _ = st.columns([4, 2, 4])
with btn_col:
    search_btn = st.button("🚀 Begin Research Analysis", type="primary", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

if search_btn and query:
    # Setup interactive stage display
    progress = st.progress(0)
    status_box = st.empty()
    
    stages = [
        (12, "📋 Planner Agent: Decomposing inquiry into targeted tasks..."),
        (35, "🔍 Researcher Agent: Querying Tavily web index for active sources..."),
        (58, "📄 Summarizer Agent: Synthesizing key details and filtering noise..."),
        (80, "✍️ Writer Agent: Structuring findings into a professional Markdown report..."),
        (92, "🛡️ Supervisor Agent: Running quality audit and reviewing factuality..."),
    ]
    
    try:
        import threading
        result_container = {}
        error_container = {}

        def call_api():
            try:
                response = requests.post(
                    "http://localhost:8000/research",
                    json={"query": query},
                    timeout=180
                )
                result_container["data"] = response.json()
            except Exception as e:
                error_container["error"] = str(e)

        # Fire concurrent API call thread
        thread = threading.Thread(target=call_api)
        thread.start()

        # Update visual stage indicators dynamically
        stage_idx = 0
        while thread.is_alive():
            if stage_idx < len(stages):
                progress.progress(stages[stage_idx][0])
                status_box.markdown(
                    f'<div class="stage-card"><h4>{stages[stage_idx][1]}</h4><small style="color:#94A3B8">This may take up to 2 minutes. The backend is running multiple parallel verification loops.</small></div>', 
                    unsafe_allow_html=True
                )
                stage_idx += 1
            time.sleep(8)

        thread.join()

        progress.progress(100)
        status_box.empty()
        progress.empty()

        if "error" in error_container:
            st.markdown('<div class="glass-card" style="border-color:#EF4444">', unsafe_allow_html=True)
            st.error(f"❌ Connection or Execution Failure: {error_container['error']}")
            st.warning("Ensure the FastAPI backend is running via: python backend/main.py")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            data = result_container["data"]
            st.balloons()
            
            st.markdown("### 📊 Research Insights Panel")
            
            # Tabbed interface for Report vs Details
            report_tab, details_tab = st.tabs(["📝 Complete Research Report", "⚙️ Pipeline Diagnostic Details"])
            
            with report_tab:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown(data["report"])
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Premium styled download button
                st.download_button(
                    label="📥 Save Research Report (.md)",
                    data=data["report"],
                    file_name=f"research_report_{query[:15].strip().lower().replace(' ', '_')}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
                
            with details_tab:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                st.markdown("#### Engine Execution Metrics")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown('<div class="custom-metric blue"><div class="custom-metric-title">Pipeline Status</div><div class="custom-metric-value">COMPLETED</div></div>', unsafe_allow_html=True)
                with col2:
                    st.markdown(f'<div class="custom-metric"><div class="custom-metric-title">Supervisor Reviews</div><div class="custom-metric-value">{data["iterations"]}</div></div>', unsafe_allow_html=True)
                with col3:
                    st.markdown(f'<div class="custom-metric pink"><div class="custom-metric-title">Character Count</div><div class="custom-metric-value">{len(data["report"]):,}</div></div>', unsafe_allow_html=True)
                
                st.markdown("---")
                st.markdown(f"**Original Query Submitted:** *{data['query']}*")
                st.markdown('</div>', unsafe_allow_html=True)
                
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

elif search_btn and not query:
    st.warning("Please specify a research topic to start!")

st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#64748B; font-size:0.85rem;">AutoResearch Agent • Powered by LangGraph & Groq • Managed by Aryan Makwana</p>', 
    unsafe_allow_html=True
)