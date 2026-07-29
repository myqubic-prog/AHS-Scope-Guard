import streamlit as st

# 1. Page Configuration & Professional Corporate Aesthetic Setup
st.set_page_config(
    page_title="AHS Scope Guard - Consultant Revenue Protection",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom theme overrides for maximum text visibility in both light and dark modes
st.markdown("""
<style>
    .stApp {
        background-color: var(--background-color, #F8FAFC);
        color: var(--text-color, #0F172A);
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #475569;
        margin-bottom: 2rem;
    }
    .solution-box {
        background-color: #E6F4EA;
        border-left: 5px solid #10B981;
        padding: 20px;
        border-radius: 8px;
        margin-top: 25px;
        color: #064E3B;
    }
    .caution-box {
        background-color: #FEF2F2;
        border-left: 5px solid #EF4444;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
        color: #7F1D1D;
        font-size: 0.9rem;
    }
    .summary-card {
        background-color: var(--secondary-background-color, #FFFFFF);
        border: 1px solid var(--border-color, #E2E8F0);
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Main Application Branded Header
st.markdown('<div class="main-title">⚖️ AHS Scope Guard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Autonomous Consultant Boundary Management, Scope Protection & Professional Revenue Defense Engine</div>', unsafe_allow_html=True)

# Two-Column Balanced Dashboard Layout
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📝 Scope Ingestion Portal")
    st.write("Input the client's current communication parameters:")
    
    # Core User Controls
    consultant_name = st.text_input("Your Name / Agency Name", value="AHS Consultancy")
    client_name = st.text_input("Client Representative Name", placeholder="e.g., John Doe")
    
    project_type = st.selectbox(
        "Original Project Framework Scope",
        ["Web Design & Development", 
         "Social Media & Content Strategy", 
         "Business Management & Advisory Consulting", 
         "SEO, Marketing & Lead Generation"]
    )
    
    out_of_scope_type = st.selectbox(
        "Categorize the Client's Extra Request",
        ["Additional Feature / Extra Webpage Creation", 
         "Extra Round of Revisions / Major Structural Redesign", 
         "Rushed Urgent Deadline / Weekend Work Request", 
         "Extra Management Meetings / Ongoing Unbilled Support"]
    )
    
    estimated_extra_hours = st.slider("Estimated Extra Hours Required to Complete", min_value=1, max_value=40, value=5)
    hourly_premium_rate = st.slider("Your Out-of-Scope Hourly Rate ($ USD)", min_value=25, max_value=250, value=100)
    
    client_message = st.text_area(
        "Paste the Client's Email or Message Text Here:", 
        placeholder="e.g., 'Hey, can you also quickly add a secure checkout page and look over this 30-page deck by tomorrow morning?'"
    )

    generate_btn = st.button("Generate Professional Revenue Defense Pitch →", type="primary")

with col2:
    st.subheader("📊 Scope Creep Risk Matrix")
    
    if generate_btn:
        st.success("📈 Boundary Defense Analysis Successfully Compiled!")
        
        # Calculate dynamic risk matrix variables
        financial_leakage = estimated_extra_hours * hourly_premium_rate
        timeline_impact_risk = min(estimated_extra_hours * 2.5, 100.0)
        boundary_vulnerability = 30 if estimated_extra_hours <= 5 else (65 if estimated_extra_hours <= 15 else 95)

        # High-Impact Performance Metrics View
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Protected Revenue Leak", value=f"${financial_leakage} USD")
        m2.metric(label="Timeline Delay Risk", value=f"{int(timeline_impact_risk)}%")
        m3.metric(label="Scope Vulnerability Rating", value=f"{boundary_vulnerability}%")
        
        st.write("---")
        
        # Universal Deterministic Email Pitch Variations (No AI Dependency)
        if "Additional Feature" in out_of_scope_type:
            pitch_heading = "📦 Feature Creep Defense Strategy"
            pitch_action = "isolated addendum parameter sequence"
            email_body = (
                f"I hope you are having a productive week.\n\n"
                f"Regarding your recent request to integrate additional components into our active {project_type} track, "
                f"I took a look at our signed agreement. Building this specific module falls directly outside our original boundaries.\n\n"
                f"I would be absolutely thrilled to build this out to perfection for you. To keep our core timeline perfectly on schedule, "
                f"we can execute this asset under a brief scope addendum. Based on our framework parameters, this will require an estimated "
                f"[{estimated_extra_hours} hours] of dedicated architecture execution, covered under an additional flat fee of [${financial_leakage} USD] "
                f"billed at our standard out-of-scope rate of [${hourly_premium_rate}/hr].\n\n"
                f"Please let me know if this looks good to go, and I will queue up the work addendum document for your signature today!"
            )
            
        elif "Extra Round of Revisions" in out_of_scope_type:
            pitch_heading = "🔄 Revision Multiplier Protection Strategy"
            pitch_action = "extended modification boundary script"
            email_body = (
                f"Thank you for passing along your comprehensive modification notes.\n\n"
                f"Reviewing the items, this feedback introduces major structural revisions that expand beyond the milestone iterations "
                f"guaranteed within our original contract parameters for our {project_type} sprint.\n\n"
                f"To ensure we maintain your core launch target date without sacrificing quality, we can immediately process these extended "
                f"modifications as a separate revision allocation chunk. This modification block will encompass approximately "
                f"[{estimated_extra_hours} hours] of refactoring, mapped at an additional total allocation of [${financial_leakage} USD].\n\n"
                f"Would you prefer to proceed with the core project framework launch as originally structured first, or should I pause our pipeline "
                f"and loop in this new revision block under a standard scope adjustment voucher?"
            )
            
        elif "Rushed Urgent Deadline" in out_of_scope_type:
            pitch_heading = "⚡ Rush Fee / Emergency Overtime Strategy"
            pitch_action = "priority acceleration overhead structure"
            email_body = (
                f"I completely understand the critical nature of this upcoming deadline and your need to accelerate our normal timeline.\n\n"
                f"To pull forward our delivery calendar or incorporate weekend engineering coverage for this {project_type} request, "
                f"our firm activates a standard Priority Acceleration overhead structure. This ensures your project gets assigned maximum dedicated bandwidth.\n\n"
                f"Expediting this deployment will require an additional priority fee of [${financial_leakage} USD], which accounts for the accelerated "
                f"[{estimated_extra_hours} hours] of expedited overtime hours required to safely cross the finish line by your requested date.\n\n"
                f"Please let me know if you would like me to issue the expedited rush-fee invoice so we can clear the calendar and dedicate our full focus to this delivery tonight!"
            )
            
        else:
            pitch_heading = "👥 Maintenance & Scope Support Strategy"
            pitch_action = "dedicated monthly advisory hours framework"
            email_body = (
                f"It is always a pleasure collaborating with your team on these operational touchpoints.\n\n"
                f"As our ongoing advisory discussions continue to expand into broader functional domains outside our core {project_type} agreement, "
                f"I want to make sure we set up a sustainable framework to support your scaling needs without bottlenecking your daily operations.\n\n"
                f"To properly track and dedicate ongoing administrative focus blocks, we can seamlessly migrate these items into a dedicated monthly "
                f"support allocation. Incorporating this monthly buffer will provide your team with an additional block of [{estimated_extra_hours} hours] of "
                f"priority support per cycle, priced at a highly competitive flat subscription of [${financial_leakage} USD] per month.\n\n"
                f"Let me know if this structured support framework sounds like the right move, and I will gladly wire over the setup details!"
            )

        st.markdown(f"### {pitch_heading}")
        st.info(f"🎯 **Strategic Objective:** Protect your billable hours by transforming a free request into a paid {pitch_action}.")
        
        # Display the custom generated email template
        st.markdown('<div class="summary-card">', unsafe_allow_html=True)
        st.markdown(f"**✉️ Pre-Written Professional Email Response (Copy & Send):**")
        
        full_email_text = f"Subject: Scope Refinement Strategy - {project_type}\n\nDear {client_name if client_name else 'Client'},\n\n{email_body}\n\nBest regards,\n\n{consultant_name}"
        st.code(full_email_text, language="text")
        st.markdown('</div>', unsafe_allow_html=True)

        # 3. Interactive Lead Capture and Consultation Request
