


"""
🎄 12 DAYS OF SUSTAINABILITY - Interactive Campaign App
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import gspread
from google.oauth2.service_account import Credentials
import json

# ============================================
# GOOGLE SHEETS CONFIGURATION
# ============================================
def setup_google_sheets():
    """Connect to Google Sheets using Streamlit secrets"""
    try:
        # Define the scope
        scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        
        # Load credentials from Streamlit secrets
        credentials_dict = st.secrets["google_credentials"]
        
        # Create credentials object
        credentials = Credentials.from_service_account_info(
            credentials_dict,
            scopes=scope
        )
        
        # Authorize and return the client
        client = gspread.authorize(credentials)
        return client
    except Exception as e:
        st.error(f"Google Sheets connection error: {str(e)}")
        return None

def log_to_sheets(client, data):
    """Log participation data to Google Sheets"""
    try:
        # IMPORTANT: Replace with your actual Google Sheet URL or ID
        # Option 1: Use the full URL (easier)
        sheet_url = st.secrets.get("https://docs.google.com/spreadsheets/d/14gjZTmx63ffN1JZX5q8y8a9Sq6iv5ZhVnnU5fM71ujo/", "")
        
        # Option 2: Or use just the sheet ID (more flexible)
        # sheet_id = st.secrets.get("sheet_id", "")
        
        if sheet_url:
            spreadsheet = client.open_by_url(sheet_url)
        else:
            # If no URL in secrets, you'll need to add it
            st.error("Please add 'sheet_url' to your Streamlit secrets")
            return False
        
        # Get the worksheet by name (specify your tab name here)
        # Option 1: Use a specific tab name
        worksheet_name = st.secrets.get("worksheet_name", "12 Days")  # Default to "Sheet1"
        worksheet = spreadsheet.worksheet(worksheet_name)
        
        # Option 2: Or just use the first sheet
        # worksheet = spreadsheet.sheet1
        
        # Prepare row data matching your columns: Date, Name, Property
        row_data = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Date
            data['name'],                                   # Name
            data['property']                                # Property
        ]
        
        # Append the row
        worksheet.append_row(row_data)
        return True
        
    except Exception as e:
        st.error(f"Error logging to sheets: {str(e)}")
        return False

# Page configuration
st.set_page_config(
    page_title="🎄 12 Days of Sustainability",
    page_icon="🎄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Engaging Mobile-Optimized Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Mobile-friendly base sizes */
    html {
        font-size: 16px;
    }
    
    @media (max-width: 768px) {
        html {
            font-size: 18px;  /* Larger base size on mobile */
        }
    }
    
    /* Let Streamlit handle the background */
    .block-container {
        padding: 0.5rem;
        max-width: 420px;
    }
    
    /* Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* SNOWFLAKES ANIMATION ❄️ */
    .snowflakes {
        position: fixed;
        top: -10px;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
        overflow: hidden;
    }
    
    .snowflake {
        position: absolute;
        top: -10px;
        font-size: 1.5rem;
        animation: fall linear infinite;
        user-select: none;
    }
    
    /* Adaptive snowflake colors for light/dark mode */
    @media (prefers-color-scheme: dark) {
        .snowflake {
            color: rgba(255, 255, 255, 0.7);
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
        }
    }
    
    @media (prefers-color-scheme: light) {
        .snowflake {
            color: rgba(200, 230, 255, 0.8);
            text-shadow: 0 0 5px rgba(150, 200, 255, 0.3);
        }
    }
    
    /* Default (works for both) */
    .snowflake {
        color: rgba(220, 240, 255, 0.75);
        text-shadow: 0 0 8px rgba(200, 230, 255, 0.4);
    }
    
    @keyframes fall {
        0% {
            top: -10%;
            opacity: 0;
        }
        10% {
            opacity: 1;
        }
        90% {
            opacity: 1;
        }
        100% {
            top: 110%;
            opacity: 0;
        }
    }
    
    @keyframes sway {
        0%, 100% { transform: translateX(0); }
        50% { transform: translateX(30px); }
    }
    
    /* Create multiple snowflakes with different positions and speeds */
    .snowflake:nth-child(1) { left: 5%; animation-duration: 12s; animation-delay: 0s; }
    .snowflake:nth-child(2) { left: 15%; animation-duration: 15s; animation-delay: 2s; font-size: 1.2rem; }
    .snowflake:nth-child(3) { left: 25%; animation-duration: 10s; animation-delay: 4s; font-size: 1.8rem; }
    .snowflake:nth-child(4) { left: 35%; animation-duration: 18s; animation-delay: 1s; }
    .snowflake:nth-child(5) { left: 45%; animation-duration: 13s; animation-delay: 3s; font-size: 1.3rem; }
    .snowflake:nth-child(6) { left: 55%; animation-duration: 16s; animation-delay: 5s; }
    .snowflake:nth-child(7) { left: 65%; animation-duration: 11s; animation-delay: 0s; font-size: 1.6rem; }
    .snowflake:nth-child(8) { left: 75%; animation-duration: 14s; animation-delay: 2s; }
    .snowflake:nth-child(9) { left: 85%; animation-duration: 17s; animation-delay: 4s; font-size: 1.4rem; }
    .snowflake:nth-child(10) { left: 95%; animation-duration: 12s; animation-delay: 1s; }
    .snowflake:nth-child(11) { left: 10%; animation-duration: 15s; animation-delay: 6s; font-size: 1.7rem; }
    .snowflake:nth-child(12) { left: 20%; animation-duration: 13s; animation-delay: 3s; }
    .snowflake:nth-child(13) { left: 30%; animation-duration: 16s; animation-delay: 5s; font-size: 1.5rem; }
    .snowflake:nth-child(14) { left: 40%; animation-duration: 11s; animation-delay: 2s; }
    .snowflake:nth-child(15) { left: 50%; animation-duration: 14s; animation-delay: 4s; font-size: 1.3rem; }
    .snowflake:nth-child(16) { left: 60%; animation-duration: 17s; animation-delay: 0s; }
    .snowflake:nth-child(17) { left: 70%; animation-duration: 12s; animation-delay: 6s; font-size: 1.8rem; }
    .snowflake:nth-child(18) { left: 80%; animation-duration: 15s; animation-delay: 1s; }
    .snowflake:nth-child(19) { left: 90%; animation-duration: 13s; animation-delay: 3s; font-size: 1.4rem; }
    .snowflake:nth-child(20) { left: 8%; animation-duration: 16s; animation-delay: 5s; }
    
    /* Add swaying motion to some snowflakes */
    .snowflake:nth-child(odd) {
        animation: fall linear infinite, sway 3s ease-in-out infinite;
    }
    
    /* Ensure content stays above snowflakes */
    .stApp > div {
        position: relative;
        z-index: 10;
    }
    
    /* Animations */
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 2px 10px rgba(34, 197, 94, 0.3); }
        50% { box-shadow: 0 2px 15px rgba(34, 197, 94, 0.5); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes shimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }
    
    /* Top Bar - More prominent */
    .top-bar {
        background: var(--background-color);
        padding: 0.75rem 1rem;
        border-radius: 12px;
        margin-bottom: 0.75rem;
        border: 2px solid var(--secondary-background-color);
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .user-info h3 {
        color: var(--text-color);
        font-size: 1rem;
        margin: 0;
        font-weight: 700;
    }
    
    .user-info p {
        color: var(--text-color);
        opacity: 0.7;
        font-size: 0.85rem;
        margin: 0;
        font-weight: 500;
    }
    
    .progress-badge {
        background: linear-gradient(135deg, #dc2626, #16a34a);
        color: white;
        padding: 0.5rem 0.9rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 800;
        animation: glow 2s infinite;
        position: relative;
        box-shadow: 0 4px 12px rgba(22, 163, 74, 0.4);
    }
    
    .progress-badge::after {
        content: " ✨";
        font-size: 1.2rem;
        filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.8));
        animation: sparkle 2s ease-in-out infinite;
    }
    
    @keyframes sparkle {
        0%, 100% { 
            opacity: 1;
            transform: scale(1);
        }
        50% { 
            opacity: 0.6;
            transform: scale(1.2);
        }
    }
    
    /* Card Design */
    .card {
        background: var(--background-color);
        border-radius: 16px;
        padding: 1rem;
        margin-bottom: 0.75rem;
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
        border: 2px solid var(--secondary-background-color);
    }
    
    /* Achievement Header */
    .ach-header {
        background: linear-gradient(135deg, var(--color1), var(--color2));
        padding: 1.25rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 0.75rem;
        position: relative;
        overflow: hidden;
    }
    
    .ach-header::before {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 200%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shimmer 3s infinite;
    }
    
    .day-badge {
        display: inline-block;
        background: rgba(255,255,255,0.3);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .ach-emoji {
        font-size: 3.5rem;
        margin: 0.5rem 0;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
    }
    
    .ach-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: white;
        margin: 0.5rem 0 0.25rem 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .ach-subtitle {
        font-size: 0.9rem;
        color: rgba(255,255,255,0.95);
        font-weight: 500;
    }
    
    /* Description */
    .description {
        font-size: 0.95rem;
        line-height: 1.6;
        color: var(--text-color);
        margin-bottom: 0.75rem;
        padding: 0.5rem 0;
    }
    
    /* Stats Grid */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 0.5rem;
        margin-top: 0.75rem;
    }
    
    .stat {
        background: var(--secondary-background-color);
        padding: 0.75rem;
        border-radius: 10px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat:active {
        transform: scale(0.97);
    }
    
    .stat-value {
        font-size: 1.5rem;
        font-weight: 800;
        color: #16a34a;
        margin-bottom: 0.25rem;
    }
    
    .stat-label {
        font-size: 0.8rem;
        color: var(--text-color);
        opacity: 0.8;
        font-weight: 500;
    }
    
    /* Quiz Section */
    .quiz-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .quiz-title::before {
        content: "🎯";
        font-size: 1.3rem;
    }
    
    .quiz-q {
        font-size: 1rem;
        font-weight: 600;
        color: var(--text-color);
        margin-bottom: 0.75rem;
        padding: 0.75rem;
        background: var(--secondary-background-color);
        border-radius: 8px;
        border-left: 4px solid #16a34a;
    }
    
    /* Radio buttons styling */
    .stRadio > label {
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }
    
    .stRadio > div {
        gap: 0.5rem !important;
    }
    
    .stRadio > div > label {
        background: var(--secondary-background-color) !important;
        padding: 0.75rem 1rem !important;
        border-radius: 8px !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        border: 2px solid transparent !important;
    }
    
    .stRadio > div > label:hover {
        border-color: #16a34a !important;
        transform: translateX(4px);
    }
    
    .stRadio > div > label[data-checked="true"] {
        background: linear-gradient(135deg, #16a34a, #15803d) !important;
        color: white !important;
        border-color: #16a34a !important;
        font-weight: 700 !important;
    }
    
    /* Result styles */
    .result {
        padding: 1rem;
        border-radius: 10px;
        margin-top: 0.75rem;
        animation: pulse 0.5s ease;
    }
    
    .result h4 {
        margin: 0 0 0.5rem 0;
        font-size: 1.1rem;
    }
    
    .result p {
        margin: 0.25rem 0;
        font-size: 0.95rem;
    }
    
    .result-correct {
        background: linear-gradient(135deg, #dcfce7, #bbf7d0);
        border: 2px solid #16a34a;
    }
    
    .result-correct h4 {
        color: #15803d;
    }
    
    .result-incorrect {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        border: 2px solid #f59e0b;
    }
    
    .result-incorrect h4 {
        color: #d97706;
    }
    
    .result-completed {
        background: linear-gradient(135deg, #e0e7ff, #c7d2fe);
        border: 2px solid #6366f1;
    }
    
    .result-completed h4 {
        color: #4f46e5;
    }
    
    /* Prize Banner */
    .prize {
        background: linear-gradient(135deg, #fbbf24, #f59e0b);
        color: white;
        padding: 0.75rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 0.75rem;
        font-weight: 700;
        font-size: 0.95rem;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
        animation: glow 2s infinite;
    }
    
    .prize p {
        margin: 0;
    }
    
    /* Welcome Screen */
    .welcome {
        text-align: center;
        padding: 2rem 1rem;
    }
    
    .welcome .emoji {
        font-size: 5rem;
        margin-bottom: 1rem;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
    }
    
    .welcome h1 {
        font-size: 1.8rem;
        font-weight: 800;
        color: var(--text-color);
        margin-bottom: 0.5rem;
    }
    
    .welcome p {
        font-size: 1rem;
        color: var(--text-color);
        opacity: 0.8;
    }
    
    /* Celebration */
    .celebration {
        background: linear-gradient(135deg, #fbbf24, #f59e0b, #dc2626);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 1rem;
        animation: pulse 2s infinite;
        box-shadow: 0 6px 20px rgba(220, 38, 38, 0.4);
    }
    
    .celebration h3 {
        margin: 0 0 0.5rem 0;
        font-size: 1.5rem;
        font-weight: 800;
    }
    
    .celebration p {
        margin: 0.25rem 0;
        font-size: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 0.75rem 1.5rem !important;
        border-radius: 10px !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton > button:active {
        transform: scale(0.97) !important;
    }
    
    /* Form styling */
    .stTextInput > div > div > input {
        font-size: 1rem !important;
        padding: 0.75rem !important;
        border-radius: 8px !important;
    }
    
    .stSelectbox > div > div > select {
        font-size: 1rem !important;
        padding: 0.75rem !important;
        border-radius: 8px !important;
    }
    
    /* Tree icon */
    .tree-icon {
        display: inline-block;
        animation: float 2s ease-in-out infinite;
    }
</style>
""", unsafe_allow_html=True)

# Properties list
PROPERTIES = [
    "Camden", "St Albans", "Westin", "Canopy", "CIE", "CIV", "EH", "Head Office"
]

# Session state initialization
if 'user_name' not in st.session_state:
    st.session_state.user_name = None
if 'user_property' not in st.session_state:
    st.session_state.user_property = None
if 'completed_days' not in st.session_state:
    st.session_state.completed_days = []
if 'test_mode' not in st.session_state:
    st.session_state.test_mode = False
if 'test_day' not in st.session_state:
    st.session_state.test_day = 1
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False
if 'quiz_result' not in st.session_state:
    st.session_state.quiz_result = None

# [Rest of your ACHIEVEMENTS data structure goes here - keeping it as is]
ACHIEVEMENTS = [
    {
        "day": 1,
        "title": "Green Champions Programme",
        "subtitle": "Community Growth",
        "emoji": "👥",
        "color": "#059669",
        "description": "Our Green Champions network has grown exponentially, with passionate team members leading sustainability initiatives.",
        "stats": [
            {"label": "Properties", "value": "7"},
            {"label": "Initiatives", "value": "209"},
            {"label": "Number of Green Champions", "value": "9"}
        ],
        "quiz": {
            "question": "How many properties are actively participating in the Green Champions Programme?",
            "options": ["8", "7", "15", "20"],
            "correct": "7"
        }
    },
    {
        "day": 2,
        "title": "Digital Transformation",
        "subtitle": "Paper Reduction Victory",
        "emoji": "📄",
        "color": "#2563eb",
        "description": "Through digitisation initiatives, we've dramatically reduced paper consumption while improving efficiency. In the last 4 months:",
        "stats": [
            {"label": "Trees Saved", "value": "1"},
            {"label": "Paper Saved", "value": "11k"},
            {"label": "Cost Savings", "value": "£110"}
        ],
        "quiz": {
            "question": "How much paper have we saved in the last 4 months?",
            "options": ["11k", "6k", "3.5k", "2k"],
            "correct": "11k"
        }
    },
    {
        "day": 3,
        "title": "Removing Single Use Plastics",
        "subtitle": "Bulk Toiletries",
        "emoji": "🧼",
        "color": "#f59e0b",
        "description": "Using bulk toiletries in guest bedrooms",
        "stats": [
            {"label": "Number of Properties Using Bulk Amentities (Voco Included)", "value": "100%"},
            {"label": "Single Use Plastic Bottles Saved In One Month", "value": "70,000"},
            {"label": "of Bottles Replaced", "value": "94%"},


        ],
        "quiz": {
            "question": "How many single use plastic bottles have we saved in one month?",
            "options": ["70,000", "95,000", "60,000", "30,000"],
            "correct": "70,000"
        }
    },
    {
        "day": 4,
        "title": "Recycling Revolution",
        "subtitle": "Record Performance",
        "emoji": "♻️",
        "color": "#059669",
        "description": "Improved from 37% to 48% YoY through enhanced programs and team engagement.",
        "stats": [
            {"label": "YoY Growth", "value": "+11%"},
            {"label": "Oct Recycling Rate", "value": "51%"},
            {"label": "Tonnes Recycled in 2025", "value": "227"}
        ],
        "quiz": {
            "question": "What was our year-over-year recycling improvement?",
            "options": ["+8%", "+11%", "+15%", "+20%"],
            "correct": "+11%"
        }
    },
    {
        "day": 5,
        "title": "Energy Efficiency",
        "subtitle": "Smart Management",
        "emoji": "⚡",
        "color": "#eab308",
        "description": "Strategic energy management delivering significant cost savings while reducing environmental impact. See data compared to last year.",
        "stats": [
            {"label": "Cost Savings", "value": "£137K"},
            {"label": "kWh Reduced", "value": " 1,068,745.90"},
            {"label": "Property that Reduced the Most", "value": "CIE"}
        ],
        "quiz": {
            "question": "Which property saved the most energy?",
            "options": ["CIE", "EH", "Westin", "St Albans"],
            "correct": "CIE"
        }
    },
    {
        "day": 6,
        "title": "Water Conservation",
        "subtitle": "Resource Protection",
        "emoji": "💧",
        "color": "#06b6d4",
        "description": "Smart water management systems reducing consumption across all properties.",
        "stats": [
            {"label": "Litres Saved", "value": "1.241M"},
            {"label": "Saved the Equivalent of an Olympic Sized Pool", "value": "1/2"},
            {"label": "Reduction", "value": "2%"}
        ],
        "quiz": {
            "question": "How many litres of water did we save?",
            "options": ["1.5M", "1.24M", "2.8M", "3.2M"],
            "correct": "1.24M"
        }
    },
    {
        "day": 7,
        "title": "Food Waste Reduction",
        "subtitle": "Zero Waste Journey",
        "emoji": "🍽️",
        "color": "#84cc16",
        "description": "Comprehensive food waste program with donations and composting initiatives.",
        "stats": [
            {"label": "Meals Saved", "value": "3,502"},
            {"label": "Waste Reduced", "value": "14%"},
            {"label": "Value", "value": "£7,004"}
        ],
        "quiz": {
            "question": "How many meals were saved from waste?",
            "options": ["2,205", "3,502", "4,104", "5,320"],
            "correct": "3,502"
        }
    },
    {
        "day": 8,
        "title": "Upcycling",
        "subtitle": "Reusing Materials",
        "emoji": "🛍️",
        "color": "#8b5cf6",
        "description": "Upcycling materials and finding them a new home",
        "stats": [
            {"label": "Number of items available on our marketplace", "value": "85"},
            {"label": "Number of items we've given away", "value": "50"},
            {"label": "Cost of Items available on Our Marketplace (All Donated to a Charity!)", "value": "£1-£5"},

                            ],
        "quiz": {
            "question": "Which types of items do we have on our marketplace?",
            "options": ["Books", "Lamps", "Kindles", "All of the above"],
            "correct": "All of the above"
        }
    },
    {
        "day": 9,
        "title": "Becoming More Sustainable",
        "subtitle": "Building Awareness",
        "emoji": "📚",
        "color": "#ec4899",
        "description": "Comprehensive sustainability training empowering team members as change agents.",
        # "stats": [
        #     {"label": "Hours", "value": "420"},
        #     {"label": "Trained", "value": "156"},
        #     {"label": "Satisfaction", "value": "96%"}
        # ],
        "quiz": {
            "question": "What everyday mindful behaviours have our team members adopted as a result of our sustainability efforts?",
            "options": ["Being more intentional about reducing and managing waste", "Sorting waste correctly and more consistently", "Encouraging others by sharing sustainability tips and knowledge", "All of the above"],
            "correct": "All of the above"
        }
    },
    {
        "day": 10,
        "title": "Carbon Footprint",
        "subtitle": "Climate Action",
        "emoji": "🌍",
        "color": "#059669",
        "description": "Measurable reduction in carbon emissions through comprehensive initiatives.",
        "stats": [
            {"label": "CO₂ Reduced", "value": "142.26T"},
            {"label": "Reduction", "value": "6%"}        ],
        "quiz": {
            "question": "How much did we reduce our carbon footprint?",
            "options": ["0%", "2%", "12%", "6%"],
            "correct": "6%"
        }
    },
    {
        "day": 11,
        "title": "Community Impact",
        "subtitle": "Local Partnerships",
        "emoji": "🤝",
        "color": "#f59e0b",
        "description": "Collaborating with local organisations to amplify our positive impact.",
        "stats": [
            {"label": "Partnerships", "value": "30"},
            {"label": "Money Raised", "value": "£75k"},
            {"label": "Hours Given", "value": "94"}
        ],
        "quiz": {
            "question": "How many community partnerships did we establish?",
            "options": ["12", "18", "24", "30"],
            "correct": "30"
        }
    },
    {
        "day": 12,
        "title": "2025 Achievement",
        "subtitle": "Year in Review",
        "emoji": "🎊",
        "color": "#dc2626",
        "description": "Celebrating a transformative year of sustainability excellence and team dedication.",
        "stats": [
            {"label": "Total Impact", "value": "£75k"},
            {"label": "Initiatives", "value": "251"},
            {"label": "Team Pride", "value": "100%"}
        ],
        "quiz": {
            "question": "How much money did we raise for charity in 2025?",
            "options": ["£75K", "£18K", "£42K", "£53K"],
            "correct": "£75K"
        }
    }
]


def calculate_current_day():
    """Calculate which day of the campaign we're on (Dec 1-12, 2025)"""
    if st.session_state.test_mode:
        return st.session_state.test_day
    
    # Campaign runs December 1-12, 2025
    start_date = datetime(2025, 12, 1)
    end_date = datetime(2025, 12, 12, 23, 59, 59)
    now = datetime.now()
    
    if now < start_date:
        return 1  # Before campaign starts, show Day 1
    elif now > end_date:
        return 12  # After campaign ends, show Day 12
    else:
        # During campaign, calculate current day
        delta = now - start_date
        return min(delta.days + 1, 12)

def main():
    # Snowflakes animation
    st.markdown("""
    <div class="snowflakes">
        <div class="snowflake">❄</div>
        <div class="snowflake">❅</div>
        <div class="snowflake">❆</div>
        <div class="snowflake">❄</div>
        <div class="snowflake">❅</div>
        <div class="snowflake">❆</div>
        <div class="snowflake">❄</div>
        <div class="snowflake">❅</div>
        <div class="snowflake">❆</div>
        <div class="snowflake">❄</div>
        <div class="snowflake">❅</div>
        <div class="snowflake">❆</div>
        <div class="snowflake">❄</div>
        <div class="snowflake">❅</div>
        <div class="snowflake">❆</div>
        <div class="snowflake">❄</div>
        <div class="snowflake">❅</div>
        <div class="snowflake">❆</div>
        <div class="snowflake">❄</div>
        <div class="snowflake">❅</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Welcome Screen
    if st.session_state.user_name is None or st.session_state.user_property is None:
        st.markdown("""
        <div class="welcome">
            <div class="emoji">🎄</div>
            <h1>12 Days of Sustainability</h1>
            <p>Celebrating Our 2024 Achievements<br>December 1-12, 2025</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Test mode - collapsed by default
        with st.expander("🧪 Testing Mode", expanded=False):
            test_mode = st.checkbox("Enable Testing Mode", value=st.session_state.test_mode)
            st.session_state.test_mode = test_mode
            
            if st.session_state.test_mode:
                test_day = st.slider("Day", 1, 12, st.session_state.test_day)
                st.session_state.test_day = test_day
        
        # Name and Property Form
        with st.form("user_entry_form"):
            name = st.text_input("Your Name", placeholder="Enter your full name...")
            
            # Use SELECTBOX dropdown for property selection
            property_select = st.selectbox(
                "Your Property",
                options=[""] + PROPERTIES,  # Add empty option as default
                format_func=lambda x: "Select your property..." if x == "" else x,
                index=0
            )
            
            submitted = st.form_submit_button("🎄 Start Journey", use_container_width=True, type="primary")
            
            if submitted:
                if name and name.strip() and property_select and property_select != "":
                    st.session_state.user_name = name.strip()
                    st.session_state.user_property = property_select
                    
                    # Log to Google Sheets
                    try:
                        client = setup_google_sheets()
                        if client:
                            data = {
                                "name": st.session_state.user_name,
                                "property": st.session_state.user_property
                            }
                            log_to_sheets(client, data)
                    except Exception as e:
                        # Don't block the app if logging fails
                        st.warning(f"Could not log participation: {str(e)}")
                    
                    st.rerun()
                else:
                    st.error("⚠️ Please enter your name and select your property")
        
        return
    
    # Main App
    current_day = calculate_current_day()
    current_achievement = next((a for a in ACHIEVEMENTS if a["day"] == current_day), None)
    
    if not current_achievement:
        st.error("Achievement not found")
        return
    
    # Top Bar
    st.markdown(f"""
    <div class="top-bar">
        <div class="user-info">
            <h3><span class="tree-icon">🎄</span> {st.session_state.user_name}</h3>
            <p>{st.session_state.user_property}</p>
        </div>
        <div class="progress-badge">{len(st.session_state.completed_days)}/12</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Settings - collapsed
    with st.expander("⚙️ Settings", expanded=False):
        test_toggle = st.checkbox("Testing Mode", value=st.session_state.test_mode)
        if test_toggle != st.session_state.test_mode:
            st.session_state.test_mode = test_toggle
            st.rerun()
        
        if st.session_state.test_mode:
            test_day = st.slider("Day", 1, 12, st.session_state.test_day)
            if test_day != st.session_state.test_day:
                st.session_state.test_day = test_day
                st.session_state.quiz_submitted = False
                st.session_state.quiz_result = None
                st.rerun()
    
    # Prize Banner
    st.markdown("""
    <div class="prize">
        <p>Complete all 12 days → Win £25 Amazon Gift Card!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Achievement Card
    st.markdown(f"""
    <div class="card">
        <div class="ach-header" style="--color1: {current_achievement['color']}; --color2: {current_achievement['color']}dd;">
            <div class="day-badge">DAY {current_day} OF 12</div>
            <div class="ach-emoji">{current_achievement['emoji']}</div>
            <div class="ach-title">{current_achievement['title']}</div>
            <div class="ach-subtitle">{current_achievement['subtitle']}</div>
        </div>
        <div class="description">{current_achievement['description']}</div>
        <div class="stats-grid">
    """, unsafe_allow_html=True)
    
    for stat in current_achievement['stats']:
        st.markdown(f"""
            <div class="stat">
                <div class="stat-value">{stat['value']}</div>
                <div class="stat-label">{stat['label']}</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    # Quiz Section
    is_completed = current_day in st.session_state.completed_days
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Show quiz result if just submitted (PRIORITY CHECK)
    if st.session_state.quiz_submitted and st.session_state.quiz_result:
        st.markdown(f"""
        <div class="quiz-title">Today's Quiz Challenge</div>
        <div class="quiz-q">{current_achievement['quiz']['question']}</div>
        """, unsafe_allow_html=True)
        
        result = st.session_state.quiz_result
        if result['correct']:
            st.markdown(f"""
            <div class="result result-correct">
                <h4>✓ CORRECT! Well Done! 🎉</h4>
                <p>Your answer <strong>"{result['answer']}"</strong> is correct!</p>
                <p style="margin-top: 0.5rem; font-size: 0.9rem;">✅ Day {current_day} complete! See you tomorrow for Day {current_day + 1}!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result result-incorrect">
                <h4>Not quite, but great effort! 💪</h4>
                <p>You answered: <strong>"{result['answer']}"</strong></p>
                <p>The correct answer is: <strong>"{current_achievement['quiz']['correct']}"</strong></p>
                <p style="margin-top: 0.5rem; font-size: 0.9rem;">✅ Day {current_day} complete! See you tomorrow for Day {current_day + 1}!</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Show quiz if not completed and not just submitted
    elif not is_completed:
        st.markdown(f"""
        <div class="quiz-title">Today's Quiz Challenge</div>
        <div class="quiz-q">{current_achievement['quiz']['question']}</div>
        """, unsafe_allow_html=True)
        
        selected = st.radio(
            "",
            current_achievement['quiz']['options'],
            index=None,  # No pre-selection - user must choose!
            key=f"quiz_{current_day}",
            label_visibility="collapsed"
        )
        
        if st.button("🎯 Submit Answer", type="primary", use_container_width=True):
            if selected is None:
                st.error("⚠️ Please select an answer before submitting!")
            else:
                is_correct = selected == current_achievement['quiz']['correct']
                st.session_state.quiz_result = {'answer': selected, 'correct': is_correct}
                st.session_state.quiz_submitted = True
                st.session_state.completed_days.append(current_day)
                
                # Log to Google Sheets
                try:
                    client = setup_google_sheets()
                    if client:
                        data = {
                            "name": st.session_state.user_name,
                            "property": st.session_state.user_property,
                            "day": current_day,
                            "achievement": current_achievement['title'],
                            "question": current_achievement['quiz']['question'],
                            "selected_answer": selected,
                            "correct_answer": current_achievement['quiz']['correct'],
                            "is_correct": is_correct
                        }
                        log_to_sheets(client, data)
                except:
                    pass  # Don't block user experience if logging fails
                
                st.rerun()
    
    # Show "already completed" message
    else:
        st.markdown(f"""
        <div class="result result-completed">
            <h4>Day {current_day} Complete!</h4>
            <p>You've finished today's quiz.</p>
            <p>Come back tomorrow for Day {current_day + 1}!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Celebration
    if len(st.session_state.completed_days) == 12:
        st.balloons()
        st.markdown(f"""
        <div class="celebration">
            <h3>Congratulations {st.session_state.user_name}!</h3>
            <p>You completed all 12 Days of Sustainability!</p>
            <p style="margin-top: 0.5rem; font-weight: 700;">
                🎁 You've earned your £25 Amazon Gift Card! 🎁
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()