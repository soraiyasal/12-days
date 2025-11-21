"""
🎄 12 DAYS OF SUSTAINABILITY - Interactive Campaign App
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import gspread
from google.oauth2.service_account import Credentials
import json

# Page configuration
st.set_page_config(
    page_title="🎄 12 Days of Sustainability",
    page_icon="🎄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ultra-Compact White Theme CSS - NO SCROLL
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* White Background */
    .stApp {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
    }
    
    .main {
        background: transparent;
    }
    
    .block-container {
        padding: 0.5rem   ;
        max-width: 420px   ;
    }
    
    /* Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Animations */
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 2px 10px rgba(34, 197, 94, 0.3); }
        50% { box-shadow: 0 2px 15px rgba(34, 197, 94, 0.5); }
    }
    
    /* Top Bar - ULTRA COMPACT */
    .top-bar {
        background: white;
        padding: 0.4rem 0.6rem;
        border-radius: 10px;
        margin-bottom: 0.4rem;
        border: 1px solid #e2e8f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    .user-info h3 {
        color: #1f2937;
        font-size: 0.8rem;
        margin: 0;
        font-weight: 600;
    }
    
    .user-info p {
        color: #6b7280;
        font-size: 0.65rem;
        margin: 0;
    }
    
    .progress-badge {
        background: linear-gradient(135deg, #dc2626, #16a34a);
        color: white;
        padding: 0.3rem 0.6rem;
        border-radius: 15px;
        font-size: 0.7rem;
        font-weight: 700;
        animation: glow 2s infinite;
        position: relative;
    }
    
    .progress-badge::after {
        content: " ✨";
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
    
    /* Cards - COMPACT */
    .card {
        background: white;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        padding: 0.6rem;
        margin-bottom: 0.4rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Achievement Header - COMPACT */
    .ach-header {
        background: linear-gradient(135deg, var(--color1), var(--color2));
        padding: 1rem 0.6rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 0.5rem;
    
    }
    
    .day-badge {
        background: rgba(255,255,255,0.3);
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 700;
        color: #10b981;
        display: inline-block;
        margin-bottom: 0.5rem;
        letter-spacing: 0.5px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .ach-emoji {
        font-size: 3.5rem;
        margin: 0.5rem 0;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(0 6px 12px rgba(0,0,0,0.3)) 
                drop-shadow(0 0 25px rgba(255,255,255,0.6));
        transform-style: preserve-3d;
        display: block;
        text-align: center;
    }
    
    .ach-emoji:hover {
        animation: bounce 0.6s ease;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0) scale(1); }
        25% { transform: translateY(-10px) scale(1.1); }
        50% { transform: translateY(0) scale(1.05); }
        75% { transform: translateY(-5px) scale(1.08); }
    }
    
    .ach-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #10b981;
        margin: 0.3rem 0;
        line-height: 1.2;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .ach-subtitle {
        font-size: 0.75rem;
        color: #10b981;
        text-shadow: 0 1px 2px rgba(0,0,0,0.15);
    }
    
    /* Description - COMPACT */
    .description {
        font-size: 0.75rem;
        line-height: 1.4;
        color: #4b5563;
        text-align: center;
        margin-bottom: 0.6rem;
        font-weight: 400;
    }
    
    /* Stats Grid - ULTRA COMPACT */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.4rem;
        margin-bottom: 0.6rem;
    }
    
    .stat {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.6rem 0.3rem;
        text-align: center;
        transition: transform 0.2s;
    }
    
    .stat:hover {
        transform: translateY(-2px);
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stat-value {
        font-size: 1.1rem;
        font-weight: 700;
        color: #16a34a;
        margin-bottom: 0.2rem;
    }
    
    .stat-label {
        font-size: 0.65rem;
        color: #6b7280;
        line-height: 1.2;
        font-weight: 500;
    }
    
    /* Quiz - ULTRA COMPACT */
    .quiz-title {
        font-size: 0.9rem;
        font-weight: 700;
        color: #16a34a;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }
    
    .quiz-q {
        font-size: 0.8rem;
        font-weight: 600;
        color: #1f2937;
        background: #f8fafc;
        padding: 0.7rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 0.6rem;
        border: 1px solid #e2e8f0;
        line-height: 1.4;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    /* Radio Buttons - COMPACT 2x2 Grid */
    div[data-testid="stRadio"] > div {
        display: grid  ;
        grid-template-columns: 1fr 1fr   ;
        gap: 0.5rem   ;
    }
    
    div[data-testid="stRadio"] > div > label {
        background: white   ;
        border: 2px solid #e5e7eb   ;
        border-radius: 10px   ;
        padding: 0.75rem 0.4rem   ;
        cursor: pointer   ;
        transition: all 0.2s   ;
        font-size: 0.75rem   ;
        font-weight: 500   ;
        color: #374151   ;
        text-align: center   ;
        margin: 0   ;
        min-height: 52px   ;
        display: flex   ;
        align-items: center   ;
        justify-content: center   ;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05)   ;
        line-height: 1.3   ;
    }
    
    div[data-testid="stRadio"] > div > label:hover {
        border-color: #16a34a   ;
        background: #f0fdf4   ;
        transform: translateY(-1px)   ;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1)   ;
    }
    
    div[data-testid="stRadio"] > div > label[data-checked="true"] {
        border-color: #16a34a   ;
        background: linear-gradient(135deg, #dcfce7, #bbf7d0)   ;
        color: #166534   ;
        font-weight: 700   ;
        transform: scale(1.02)   ;
        box-shadow: 0 3px 8px rgba(22, 163, 74, 0.3)   ;
    }
    
    /* Property selection - 2x4 grid for 8 items */
    div[data-testid="stRadio"][data-baseweb="radio"] > div:has(> label:nth-child(8)) {
        grid-template-columns: 1fr 1fr   ;
    }
    
    /* Button - COMPACT */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #dc2626, #16a34a)   ;
        color: white   ;
        border: none   ;
        border-radius: 10px   ;
        padding: 0.65rem   ;
        font-size: 0.8rem   ;
        font-weight: 700   ;
        box-shadow: 0 2px 8px rgba(34, 197, 94, 0.3)   ;
        transition: all 0.3s   ;
        margin-top: 0.5rem   ;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px)   ;
        box-shadow: 0 4px 12px rgba(34, 197, 94, 0.4)   ;
    }
    
    /* Result Box - COMPACT */
    .result {
        border-radius: 10px;
        padding: 0.6rem;
        text-align: center;
        margin-top: 0.5rem;
    }
    
    .result-correct {
        background: linear-gradient(135deg, #dcfce7, #bbf7d0);
        border: 2px solid #16a34a;
    }
    
    .result-incorrect {
        background: linear-gradient(135deg, #fed7aa, #fde68a);
        border: 2px solid #fb923c;
    }
    
    .result-completed {
        background: linear-gradient(135deg, #dbeafe, #bfdbfe);
        border: 2px solid #3b82f6;
    }
    
    .result h4 {
        font-size: 0.85rem;
        color: #1f2937;
        margin-bottom: 0.3rem;
    }
    
    /* Enhanced result emojis */
    .result-correct h4::before {
        content: "🎉 ";
        font-size: 1rem;
        filter: drop-shadow(0 2px 4px rgba(34, 197, 94, 0.4));
        animation: bounce 0.6s ease;
    }
    
    .result-incorrect h4::before {
        content: "💪 ";
        font-size: 1rem;
        filter: drop-shadow(0 2px 4px rgba(251, 146, 60, 0.4));
    }
    
    .result-completed h4::before {
        content: "✅ ";
        font-size: 1rem;
        filter: drop-shadow(0 2px 4px rgba(59, 130, 246, 0.4));
    }
    
    .result p {
        font-size: 0.7rem;
        color: #4b5563;
        margin: 0.15rem 0;
        line-height: 1.3;
    }
    
    /* Prize Banner - COMPACT */
    .prize {
        background: linear-gradient(135deg, #fef3c7, #fde68a);
        border-radius: 10px;
        padding: 0.5rem 0.6rem;
        text-align: center;
        margin-bottom: 0.4rem;
        box-shadow: 0 2px 8px rgba(251, 191, 36, 0.3);
        border: 1px solid #fbbf24;
        position: relative;
    }
    
    .prize p {
        font-size: 0.7rem;
        font-weight: 700;
        color: #78350f;
        margin: 0;
        line-height: 1.2;
    }
    
    /* Enhance prize emoji */
    .prize::before {
        content: "🎁";
        position: absolute;
        left: 0.5rem;
        font-size: 1.2rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
        animation: float 3s ease-in-out infinite;
    }
    
    .prize::after {
        content: "🎁";
        position: absolute;
        right: 0.5rem;
        font-size: 1.2rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
        animation: float 3s ease-in-out infinite 1.5s;
    }
    
    /* Inputs - COMPACT */
    .stTextInput input, .stSelectbox > div > div {
        background: white   ;
        border: 2px solid #e5e7eb   ;
        border-radius: 8px   ;
        padding: 0.6rem   ;
        font-size: 0.8rem   ;
        color: #1f2937   ;
    }
    
    .stTextInput input:focus, .stSelectbox > div > div:focus-within {
        border-color: #16a34a   ;
        box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.1)   ;
    }
    
    .stTextInput label, .stSelectbox label {
        color: #374151   ;
        font-size: 0.75rem   ;
        font-weight: 600   ;
        margin-bottom: 0.2rem   ;
    }
    
    /* Selectbox - ULTRA AGGRESSIVE FIX for dropdown visibility */
    /* Force all text in selectbox to be dark */
    .stSelectbox,
    .stSelectbox *,
    .stSelectbox div,
    .stSelectbox span,
    .stSelectbox input,
    .stSelectbox [data-baseweb] *,
    .stSelectbox [data-baseweb="select"] *,
    .stSelectbox [data-baseweb="popover"] *,
    .stSelectbox [data-baseweb="menu"] *,
    .stSelectbox ul *,
    .stSelectbox li * {
        color: #1f2937   ;
    }
    
    /* Main selectbox container */
    .stSelectbox [data-baseweb="select"] {
        background: white   ;
        color: #1f2937   ;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        color: #1f2937   ;
        background: white   ;
    }
    
    .stSelectbox [data-baseweb="select"] input {
        color: #1f2937   ;
        background: white   ;
    }
    
    .stSelectbox [data-baseweb="select"] span {
        color: #1f2937   ;
    }
    
    /* Dropdown popover */
    .stSelectbox [data-baseweb="popover"] {
        background: white   ;
    }
    
    .stSelectbox [data-baseweb="popover"] > div {
        background: white   ;
    }
    
    /* Menu container */
    .stSelectbox [data-baseweb="menu"] {
        background: white   ;
    }
    
    .stSelectbox [data-baseweb="menu"] > div {
        background: white   ;
    }
    
    .stSelectbox ul[role="listbox"] {
        background: white   ;
    }
    
    /* Options - EVERY POSSIBLE SELECTOR */
    .stSelectbox [role="option"],
    .stSelectbox li[role="option"],
    .stSelectbox [data-baseweb="menu"] li,
    .stSelectbox ul li,
    .stSelectbox [data-baseweb="list-item"] {
        background: white   ;
        color: #1f2937   ;
        font-size: 0.8rem   ;
        padding: 0.6rem 0.75rem   ;
    }
    
    /* Hover state */
    .stSelectbox [role="option"]:hover,
    .stSelectbox li[role="option"]:hover,
    .stSelectbox [data-baseweb="menu"] li:hover,
    .stSelectbox ul li:hover {
        background: #f0fdf4   ;
        color: #166534   ;
    }
    
    /* Selected state */
    .stSelectbox [aria-selected="true"],
    .stSelectbox li[aria-selected="true"],
    .stSelectbox [data-baseweb="list-item"][aria-selected="true"] {
        background: #dcfce7   ;
        color: #166534   ;
        font-weight: 600   ;
    }
    
    /* Selected value display */
    .stSelectbox [data-baseweb="select"] [data-baseweb="tag"] {
        background: #dcfce7   ;
        color: #166534   ;
    }
    
    .stSelectbox [data-baseweb="tag"] span {
        color: #166534   ;
    }
    
    /* Placeholder */
    .stSelectbox [data-baseweb="select"] input::placeholder {
        color: #9ca3af   ;
    }
    
    /* Force text color on all children */
    .stSelectbox [data-baseweb="popover"] div,
    .stSelectbox [data-baseweb="popover"] span,
    .stSelectbox [data-baseweb="menu"] div,
    .stSelectbox [data-baseweb="menu"] span {
        color: #1f2937   ;
    }
    
    /* List item content */
    .stSelectbox li div,
    .stSelectbox li span {
        color: #1f2937   ;
    }
    
    /* Override any inherited colors */
    .stSelectbox [data-baseweb] {
        color: #1f2937   ;
    }
    
    /* NUCLEAR OPTION: Force selected value to be visible */
    .stSelectbox [data-baseweb="select"] [class*="singleValue"] {
        color: #1f2937   ;
    }
    
    .stSelectbox [data-baseweb="select"] [class*="value-container"] * {
        color: #1f2937   ;
    }
    
    .stSelectbox [data-baseweb="select"] [class*="ValueContainer"] * {
        color: #1f2937   ;
    }
    
    /* Force ALL elements in the select control */
    .stSelectbox [data-baseweb="select"] * {
        color: #1f2937   ;
    }
    
    /* Expander - COMPACT */
    .streamlit-expanderHeader {
        background: white   ;
        border: 1px solid #e2e8f0   ;
        border-radius: 8px   ;
        color: #1f2937   ;
        font-size: 0.75rem   ;
        padding: 0.4rem   ;
    }
    
    .streamlit-expanderContent {
        background: white   ;
        border: 1px solid #e2e8f0   ;
        border-top: none   ;
        border-radius: 0 0 8px 8px   ;
        padding: 0.5rem   ;
    }
    
    /* Welcome - COMPACT */
    .welcome {
        text-align: center;
        padding: 1.5rem 0.75rem;
    }
    
    .welcome h1 {
        font-size: 1.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #dc2626, #16a34a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.75rem 0 0.4rem 0;
    }
    
    .welcome p {
        font-size: 0.75rem;
        color: #6b7280;
        margin-bottom: 1.5rem;
    }
    
    .welcome .emoji {
        font-size: 4rem;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(0 6px 12px rgba(0,0,0,0.2)) 
                drop-shadow(0 0 30px rgba(220, 38, 38, 0.3))
                drop-shadow(0 0 30px rgba(22, 163, 74, 0.3));
        display: inline-block;
        transform-style: preserve-3d;
    }
    
    /* Tree icon in top bar */
    .tree-icon {
        font-size: 1.2rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
        animation: bounce 2s ease-in-out infinite;
    }
    
    /* Quiz title icon enhancement */
    .quiz-title::before {
        content: "✨ ";
        filter: drop-shadow(0 2px 4px rgba(22, 163, 74, 0.3));
    }
    
    /* Prize banner emojis */
    .prize::before,
    .prize::after {
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
    }
    
    /* Celebration - COMPACT */
    .celebration {
        background: linear-gradient(135deg, #dc2626, #16a34a);
        border-radius: 12px;
        padding: 0.75rem;
        text-align: center;
        margin-top: 0.5rem;
        position: relative;
        overflow: hidden;
    }
    
    .celebration::before {
        content: "🎉";
        position: absolute;
        top: 0.5rem;
        left: 0.5rem;
        font-size: 1.5rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
        animation: float 3s ease-in-out infinite;
    }
    
    .celebration::after {
        content: "🎊";
        position: absolute;
        top: 0.5rem;
        right: 0.5rem;
        font-size: 1.5rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
        animation: float 3s ease-in-out infinite 1.5s;
    }
    
    .celebration h3 {
        font-size: 1rem;
        color: white;
        margin-bottom: 0.4rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
    }
    
    .celebration p {
        font-size: 0.75rem;
        color: rgba(255,255,255,0.95);
        margin: 0.2rem 0;
    }
    
    /* Form spacing */
    .stForm {
        margin-bottom: 0   ;
    }
    
    /* Reduce all spacing */
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.5rem   ;
    }
    
    /* Info/Success/Error boxes - COMPACT */
    .stAlert {
        padding: 0.4rem   ;
        font-size: 0.7rem   ;
        border-radius: 8px   ;
        margin: 0.3rem 0   ;
    }
    
    /* Slider - COMPACT */
    .stSlider {
        padding: 0.3rem 0   ;
    }
    
    /* Checkbox */
    .stCheckbox label {
        font-size: 0.75rem   ;
        color: #374151   ;
    }
</style>
""", unsafe_allow_html=True)

# Configuration
CAMPAIGN_START_DATE = datetime(2025, 12, 1)
CAMPAIGN_END_DATE = datetime(2025, 12, 12)
TEST_MODE_DEFAULT = True  # 🧪 Change to False for production!

# Properties list
PROPERTIES = [
    "Camden",
    "St Albans",
    "Westin",
    "Canopy",
    "CIE",
    "CIV",
    "EH",
    "Head Office"
]

# Achievements data
ACHIEVEMENTS = [
    {
        "day": 1,
        "title": "Green Champions Programme",
        "subtitle": "Community Growth",
        "emoji": "👥",
        "color": "#10b981",
        "description": "Our Green Champions network has grown exponentially, with passionate team members leading sustainability initiatives.",
        "stats": [
            {"label": "Properties", "value": "12"},
            {"label": "Initiatives", "value": "47"},
            {"label": "Engagement", "value": "89%"}
        ],
        "quiz": {
            "question": "How many properties are actively participating in the Green Champions Programme?",
            "options": ["8", "12", "15", "20"],
            "correct": "12"
        }
    },
    {
        "day": 2,
        "title": "Digital Transformation",
        "subtitle": "Paper Reduction Victory",
        "emoji": "📄",
        "color": "#3b82f6",
        "description": "Through digitisation initiatives, we've dramatically reduced paper consumption while improving efficiency.",
        "stats": [
            {"label": "Trees Saved", "value": "234"},
            {"label": "Digital Docs", "value": "12.5K"},
            {"label": "Cost Savings", "value": "£18K"}
        ],
        "quiz": {
            "question": "How many trees have we saved through our digitisation efforts?",
            "options": ["150", "234", "300", "400"],
            "correct": "234"
        }
    },
    {
        "day": 3,
        "title": "Industry Recognition",
        "subtitle": "ESG Canopy Finalists",
        "emoji": "🏆",
        "color": "#f59e0b",
        "description": "Recognised as ESG Canopy Finalists for our outstanding commitment to sustainability.",
        "stats": [
            {"label": "Score", "value": "94/100"},
            {"label": "Categories", "value": "5"},
            {"label": "Ranking", "value": "Top 3"}
        ],
        "quiz": {
            "question": "What was our ESG Canopy nomination score?",
            "options": ["85/100", "90/100", "94/100", "98/100"],
            "correct": "94/100"
        }
    },
    {
        "day": 4,
        "title": "Recycling Revolution",
        "subtitle": "Record Performance",
        "emoji": "♻️",
        "color": "#10b981",
        "description": "Improved from 40% to 51% year-over-year through enhanced programs and team engagement.",
        "stats": [
            {"label": "YoY Growth", "value": "+11%"},
            {"label": "Diverted", "value": "127t"},
            {"label": "Contamination", "value": "<5%"}
        ],
        "quiz": {
            "question": "What is our current recycling rate achievement?",
            "options": ["40%", "45%", "51%", "60%"],
            "correct": "51%"
        }
    },
    {
        "day": 5,
        "title": "Marketplace Success",
        "subtitle": "Circular Economy",
        "emoji": "🛍️",
        "color": "#a855f7",
        "description": "Our marketplace platform connects surplus items with those who need them.",
        "stats": [
            {"label": "Value", "value": "£45K"},
            {"label": "Donations", "value": "320"},
            {"label": "Waste Avoided", "value": "3.2t"}
        ],
        "quiz": {
            "question": "How many items have been donated to charity through the marketplace?",
            "options": ["200", "320", "450", "500"],
            "correct": "320"
        }
    },
    {
        "day": 6,
        "title": "Community Impact",
        "subtitle": "Giving Back",
        "emoji": "❤️",
        "color": "#ef4444",
        "description": "Through dedicated fundraising and volunteer efforts, we've made a real difference.",
        "stats": [
            {"label": "Hours", "value": "1,240"},
            {"label": "Team", "value": "78%"},
            {"label": "Charities", "value": "15"}
        ],
        "quiz": {
            "question": "How many volunteer hours did our team contribute this year?",
            "options": ["800", "1,000", "1,240", "1,500"],
            "correct": "1,240"
        }
    },
    {
        "day": 7,
        "title": "Charity Partnerships",
        "subtitle": "Lunch & Learn Series",
        "emoji": "🤝",
        "color": "#6366f1",
        "description": "Educational sessions connecting team members with charity partners.",
        "stats": [
            {"label": "Attendance", "value": "92%"},
            {"label": "Partners", "value": "12"},
            {"label": "Hours", "value": "360"}
        ],
        "quiz": {
            "question": "How many Lunch & Learn sessions were delivered this year?",
            "options": ["18", "24", "30", "36"],
            "correct": "24"
        }
    },
    {
        "day": 8,
        "title": "Wave Innovation",
        "subtitle": "Westin Excellence",
        "emoji": "⚡",
        "color": "#06b6d4",
        "description": "The Westin's Wave initiative demonstrates smart energy management.",
        "stats": [
            {"label": "kWh Saved", "value": "145K"},
            {"label": "Savings", "value": "£32K"},
            {"label": "Carbon", "value": "34t"}
        ],
        "quiz": {
            "question": "What percentage of energy reduction did the Westin Wave initiative achieve?",
            "options": ["15%", "18%", "22%", "25%"],
            "correct": "22%"
        }
    },
    {
        "day": 9,
        "title": "Food Waste Warriors",
        "subtitle": "Zero Waste Journey",
        "emoji": "🍽️",
        "color": "#f97316",
        "description": "Innovative tracking and prevention programs have dramatically reduced food waste.",
        "stats": [
            {"label": "Food Saved", "value": "18t"},
            {"label": "Meals", "value": "42K"},
            {"label": "Savings", "value": "£24K"}
        ],
        "quiz": {
            "question": "How many tonnes of food waste did we save this year?",
            "options": ["12", "15", "18", "22"],
            "correct": "18"
        }
    },
    {
        "day": 10,
        "title": "Energy Excellence",
        "subtitle": "Smart Management",
        "emoji": "💡",
        "color": "#eab308",
        "description": "Data-driven energy management delivering measurable results.",
        "stats": [
            {"label": "Properties", "value": "12"},
            {"label": "Savings", "value": "£156K"},
            {"label": "Carbon", "value": "287t"}
        ],
        "quiz": {
            "question": "How many properties have been optimised for energy management?",
            "options": ["8", "10", "12", "15"],
            "correct": "12"
        }
    },
    {
        "day": 11,
        "title": "Academic Partnership",
        "subtitle": "University of Surrey",
        "emoji": "🎓",
        "color": "#8b5cf6",
        "description": "Sharing real-world sustainability insights with future hospitality leaders.",
        "stats": [
            {"label": "Students", "value": "320"},
            {"label": "Cases", "value": "15"},
            {"label": "Lectures", "value": "6"}
        ],
        "quiz": {
            "question": "How many students were reached through our University of Surrey partnership?",
            "options": ["200", "250", "320", "400"],
            "correct": "320"
        }
    },
    {
        "day": 12,
        "title": "Get Involved!",
        "subtitle": "Your Sustainability Journey",
        "emoji": "✨",
        "color": "#ec4899",
        "description": "Every team member can make a difference. Join our sustainability initiatives!",
        "stats": [
            {"label": "Ways", "value": "20+"},
            {"label": "Training", "value": "Yes"},
            {"label": "Recognition", "value": "✓"}
        ],
        "quiz": {
            "question": "What's the best way to get involved in 2025 sustainability initiatives?",
            "options": [
                "Join Green Champions",
                "Attend Lunch & Learns",
                "Use the Marketplace",
                "All of the above"
            ],
            "correct": "All of the above"
        }
    }
]

# Google Sheets setup
def setup_google_sheets():
    try:
        credentials_dict = st.secrets["gcp_service_account"]
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]
        credentials = Credentials.from_service_account_info(credentials_dict, scopes=scope)
        client = gspread.authorize(credentials)
        return client
    except Exception as e:
        return None

def log_to_sheets(client, data):
    try:
        sheet_name = "12 Days Christmas Quiz Responses"
        spreadsheet = client.open(sheet_name)
        worksheet = spreadsheet.sheet1
        
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["name"],
            data["property"],
            data["day"],
            data["achievement"],
            data["question"],
            data["selected_answer"],
            data["correct_answer"],
            "Yes" if data["is_correct"] else "No",
            datetime.now().strftime("%Y-%m-%d")
        ]
        
        worksheet.append_row(row)
        return True
    except Exception as e:
        return False

def calculate_current_day():
    if st.session_state.test_mode:
        return st.session_state.test_day
    
    today = datetime.now()
    if today < CAMPAIGN_START_DATE:
        return 1
    if today > CAMPAIGN_END_DATE:
        return 12
    
    days_since_start = (today - CAMPAIGN_START_DATE).days
    return min(max(days_since_start + 1, 1), 12)

def init_session_state():
    if 'user_name' not in st.session_state:
        st.session_state.user_name = None
    if 'user_property' not in st.session_state:
        st.session_state.user_property = None
    if 'completed_days' not in st.session_state:
        st.session_state.completed_days = []
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False
    if 'quiz_result' not in st.session_state:
        st.session_state.quiz_result = None
    if 'test_day' not in st.session_state:
        st.session_state.test_day = 1
    if 'test_mode' not in st.session_state:
        st.session_state.test_mode = TEST_MODE_DEFAULT

def main():
    init_session_state()
    
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
            
            # Use radio instead of selectbox for better visibility
            st.markdown("**Your Property**")
            property_select = st.radio(
                "property_radio",
                options=PROPERTIES,
                index=None,
                label_visibility="collapsed"
            )
            
            submitted = st.form_submit_button("🎄 Start Journey", use_container_width=True, type="primary")
            
            if submitted:
                if name and name.strip() and property_select:
                    st.session_state.user_name = name.strip()
                    st.session_state.user_property = property_select
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
    
    if not is_completed:
        st.markdown(f"""
        <div class="quiz-title">Today's Quiz Challenge</div>
        <div class="quiz-q">{current_achievement['quiz']['question']}</div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.quiz_submitted:
            selected = st.radio(
                "",
                current_achievement['quiz']['options'],
                key=f"quiz_{current_day}",
                label_visibility="collapsed"
            )
            
            if st.button("🎯 Submit Answer", type="primary", use_container_width=True):
                is_correct = selected == current_achievement['quiz']['correct']
                st.session_state.quiz_result = {'answer': selected, 'correct': is_correct}
                st.session_state.quiz_submitted = True
                st.session_state.completed_days.append(current_day)
                
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
                    pass
                
                st.rerun()
        else:
            result = st.session_state.quiz_result
            if result['correct']:
                st.markdown(f"""
                <div class="result result-correct">
                    <h4>Correct! Well done!</h4>
                    <p>Answer: <strong>{result['answer']}</strong></p>
                    <p>✅ See you tomorrow for Day {current_day + 1}!</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result result-incorrect">
                    <h4>Great try!</h4>
                    <p>Your answer: <strong>{result['answer']}</strong></p>
                    <p>Correct: <strong>{current_achievement['quiz']['correct']}</strong></p>
                    <p>✅ See you tomorrow for Day {current_day + 1}!</p>
                </div>
                """, unsafe_allow_html=True)
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