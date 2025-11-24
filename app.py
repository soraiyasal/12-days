# """
# 🎄 12 DAYS OF SUSTAINABILITY - Interactive Campaign App
# """

# import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta
# import gspread
# from google.oauth2.service_account import Credentials
# import json

# # Page configuration
# st.set_page_config(
#     page_title="🎄 12 Days of Sustainability",
#     page_icon="🎄",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Adaptive Theme CSS - Works with Light and Dark Mode
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
#     * {
#         font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
#     }
    
#     /* Let Streamlit handle the background */
#     .block-container {
#         padding: 0.5rem;
#         max-width: 420px;
#     }
    
#     /* Hide Streamlit elements */
#     #MainMenu, footer, header {visibility: hidden;}
    
#     /* Animations */
#     @keyframes float {
#         0%, 100% { transform: translateY(0); }
#         50% { transform: translateY(-5px); }
#     }
    
#     @keyframes glow {
#         0%, 100% { box-shadow: 0 2px 10px rgba(34, 197, 94, 0.3); }
#         50% { box-shadow: 0 2px 15px rgba(34, 197, 94, 0.5); }
#     }
    
#     /* Top Bar - Adaptive */
#     .top-bar {
#         background: var(--background-color);
#         padding: 0.4rem 0.6rem;
#         border-radius: 10px;
#         margin-bottom: 0.4rem;
#         border: 1px solid var(--secondary-background-color);
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
#     }
    
#     .user-info h3 {
#         color: var(--text-color);
#         font-size: 0.8rem;
#         margin: 0;
#         font-weight: 600;
#     }
    
#     .user-info p {
#         color: var(--text-color);
#         opacity: 0.7;
#         font-size: 0.65rem;
#         margin: 0;
#     }
    
#     .progress-badge {
#         background: linear-gradient(135deg, #dc2626, #16a34a);
#         color: white;
#         padding: 0.3rem 0.6rem;
#         border-radius: 15px;
#         font-size: 0.7rem;
#         font-weight: 700;
#         animation: glow 2s infinite;
#         position: relative;
#     }
    
#     .progress-badge::after {
#         content: " ✨";
#         filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.8));
#         animation: sparkle 2s ease-in-out infinite;
#     }
    
#     @keyframes sparkle {
#         0%, 100% { 
#             opacity: 1;
#             transform: scale(1);
#         }
#         50% { 
#             opacity: 0.6;
#             transform: scale(1.2);
#         }
#     }
    
#     /* Cards - Adaptive */
#     .card {
#         background: var(--background-color);
#         border-radius: 12px;
#         border: 1px solid var(--secondary-background-color);
#         padding: 0.6rem;
#         margin-bottom: 0.4rem;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
#     }
    
#     /* Achievement Header - SOFTER COLORS with White Text */
#     .ach-header {
#         background: linear-gradient(135deg, var(--color1), var(--color2));
#         padding: 1rem 0.6rem;
#         border-radius: 12px;
#         text-align: center;
#         margin-bottom: 0.5rem;
#     }
    
#     .day-badge {
#         background: rgba(255,255,255,0.25);
#         padding: 0.3rem 0.8rem;
#         border-radius: 15px;
#         font-size: 0.75rem;
#         font-weight: 700;
#         color: white;
#         display: inline-block;
#         margin-bottom: 0.5rem;
#         letter-spacing: 0.5px;
#         text-shadow: 0 2px 4px rgba(0,0,0,0.3);
#     }
    
#     .ach-emoji {
#         font-size: 3.5rem;
#         margin: 0.5rem 0;
#         animation: float 3s ease-in-out infinite;
#         filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
#         transform-style: preserve-3d;
#         display: block;
#         text-align: center;
#     }
    
#     .ach-emoji:hover {
#         animation: bounce 0.6s ease;
#     }
    
#     @keyframes bounce {
#         0%, 100% { transform: translateY(0) scale(1); }
#         25% { transform: translateY(-10px) scale(1.1); }
#         50% { transform: translateY(0) scale(1.05); }
#         75% { transform: translateY(-5px) scale(1.08); }
#     }
    
#     /* White text on colored backgrounds */
#     .ach-title {
#         font-size: 1.1rem;
#         font-weight: 700;
#         color: white;
#         margin: 0.3rem 0;
#         line-height: 1.2;
#         text-shadow: 0 2px 4px rgba(0,0,0,0.3);
#     }
    
#     .ach-subtitle {
#         font-size: 0.75rem;
#         color: white;
#         opacity: 0.95;
#         text-shadow: 0 1px 2px rgba(0,0,0,0.2);
#     }
    
#     /* Description - Adaptive */
#     .description {
#         font-size: 0.75rem;
#         line-height: 1.4;
#         color: var(--text-color);
#         text-align: center;
#         margin-bottom: 0.6rem;
#         font-weight: 400;
#     }
    
#     /* Stats Grid - Adaptive */
#     .stats-grid {
#         display: grid;
#         grid-template-columns: repeat(3, 1fr);
#         gap: 0.4rem;
#         margin-bottom: 0.6rem;
#     }
    
#     .stat {
#         background: var(--secondary-background-color);
#         border: 1px solid var(--secondary-background-color);
#         border-radius: 10px;
#         padding: 0.6rem 0.3rem;
#         text-align: center;
#         transition: transform 0.2s;
#     }
    
#     .stat:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 2px 8px rgba(0,0,0,0.15);
#     }
    
#     .stat-value {
#         font-size: 1.1rem;
#         font-weight: 700;
#         color: #16a34a;
#         margin-bottom: 0.2rem;
#     }
    
#     .stat-label {
#         font-size: 0.65rem;
#         color: var(--text-color);
#         opacity: 0.7;
#         line-height: 1.2;
#         font-weight: 500;
#     }
    
#     /* Quiz - Adaptive */
#     .quiz-title {
#         font-size: 0.9rem;
#         font-weight: 700;
#         color: #16a34a;
#         text-align: center;
#         margin-bottom: 0.5rem;
#     }
    
#     .quiz-q {
#         font-size: 0.8rem;
#         font-weight: 600;
#         color: var(--text-color);
#         background: var(--secondary-background-color);
#         padding: 0.7rem;
#         border-radius: 10px;
#         text-align: center;
#         margin-bottom: 0.6rem;
#         border: 1px solid var(--secondary-background-color);
#         line-height: 1.4;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.05);
#     }
    
#     /* Radio Buttons - VERTICAL LIST instead of grid */
#     div[data-testid="stRadio"] > div {
#         display: flex;
#         flex-direction: column;
#         gap: 0.5rem;
#     }
    
#     div[data-testid="stRadio"] > div > label {
#         background: var(--background-color);
#         border: 2px solid var(--secondary-background-color);
#         border-radius: 10px;
#         padding: 0.75rem 1rem;
#         cursor: pointer;
#         transition: all 0.2s;
#         font-size: 0.85rem;
#         font-weight: 500;
#         color: var(--text-color);
#         text-align: left;
#         margin: 0;
#         display: flex;
#         align-items: center;
#         box-shadow: 0 1px 2px rgba(0,0,0,0.05);
#         line-height: 1.4;
#     }
    
#     div[data-testid="stRadio"] > div > label:hover {
#         border-color: #16a34a;
#         background: rgba(22, 163, 74, 0.1);
#         transform: translateX(2px);
#         box-shadow: 0 2px 4px rgba(0,0,0,0.1);
#     }
    
#     div[data-testid="stRadio"] > div > label[data-checked="true"] {
#         border-color: #16a34a;
#         background: rgba(22, 163, 74, 0.15);
#         color: #16a34a;
#         font-weight: 700;
#         box-shadow: 0 3px 8px rgba(22, 163, 74, 0.3);
#     }
    
#     /* Button - Adaptive */
#     .stButton > button {
#         width: 100%;
#         background: linear-gradient(135deg, #dc2626, #16a34a);
#         color: white;
#         border: none;
#         border-radius: 10px;
#         padding: 0.65rem;
#         font-size: 0.8rem;
#         font-weight: 700;
#         box-shadow: 0 2px 8px rgba(34, 197, 94, 0.3);
#         transition: all 0.3s;
#         margin-top: 0.5rem;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 4px 12px rgba(34, 197, 94, 0.4);
#     }
    
#     /* Result Box - More prominent feedback */
#     .result {
#         border-radius: 12px;
#         padding: 1rem;
#         text-align: center;
#         margin-top: 0.75rem;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.15);
#     }
    
#     .result-correct {
#         background: rgba(22, 163, 74, 0.2);
#         border: 3px solid #16a34a;
#     }
    
#     .result-incorrect {
#         background: rgba(251, 146, 60, 0.2);
#         border: 3px solid #fb923c;
#     }
    
#     .result-completed {
#         background: rgba(59, 130, 246, 0.2);
#         border: 3px solid #3b82f6;
#     }
    
#     .result h4 {
#         font-size: 1rem;
#         color: var(--text-color);
#         margin-bottom: 0.5rem;
#         font-weight: 700;
#     }
    
#     /* Enhanced result emojis - larger and more prominent */
#     .result-correct h4::before {
#         content: "🎉 ";
#         font-size: 1.5rem;
#         filter: drop-shadow(0 2px 4px rgba(34, 197, 94, 0.4));
#         animation: bounce 0.6s ease;
#     }
    
#     .result-incorrect h4::before {
#         content: "💪 ";
#         font-size: 1.5rem;
#         filter: drop-shadow(0 2px 4px rgba(251, 146, 60, 0.4));
#     }
    
#     .result-completed h4::before {
#         content: "✅ ";
#         font-size: 1.5rem;
#         filter: drop-shadow(0 2px 4px rgba(59, 130, 246, 0.4));
#     }
    
#     .result p {
#         font-size: 0.85rem;
#         color: var(--text-color);
#         margin: 0.3rem 0;
#         line-height: 1.5;
#     }
    
#     .result p strong {
#         font-weight: 700;
#         color: var(--text-color);
#     }
    
#     /* Prize Banner - Adaptive */
#     .prize {
#         background: rgba(251, 191, 36, 0.2);
#         border-radius: 10px;
#         padding: 0.5rem 0.6rem;
#         text-align: center;
#         margin-bottom: 0.4rem;
#         box-shadow: 0 2px 8px rgba(251, 191, 36, 0.2);
#         border: 1px solid rgba(251, 191, 36, 0.4);
#         position: relative;
#     }
    
#     .prize p {
#         font-size: 0.7rem;
#         font-weight: 700;
#         color: var(--text-color);
#         margin: 0;
#         line-height: 1.2;
#     }
    
#     /* Enhance prize emoji */
#     .prize::before {
#         content: "🎁";
#         position: absolute;
#         left: 0.5rem;
#         font-size: 1.2rem;
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
#         animation: float 3s ease-in-out infinite;
#     }
    
#     .prize::after {
#         content: "🎁";
#         position: absolute;
#         right: 0.5rem;
#         font-size: 1.2rem;
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
#         animation: float 3s ease-in-out infinite 1.5s;
#     }
    
#     /* Inputs - Let Streamlit handle most styling */
#     .stTextInput label {
#         font-size: 0.75rem;
#         font-weight: 600;
#         margin-bottom: 0.2rem;
#     }
    
#     .stTextInput input {
#         font-size: 0.8rem;
#         padding: 0.6rem;
#     }
    
#     /* Selectbox - AGGRESSIVE FIX for selected value visibility */
#     .stSelectbox label {
#         font-size: 0.75rem;
#         font-weight: 600;
#         margin-bottom: 0.2rem;
#     }
    
#     .stSelectbox [data-baseweb="select"] > div {
#         font-size: 0.8rem;
#         padding: 0.6rem;
#     }
    
#     /* Force selected value to be visible - CRITICAL */
#     .stSelectbox input {
#         color: var(--text-color) !important;
#         opacity: 1 !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] input {
#         color: var(--text-color) !important;
#         opacity: 1 !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] > div > div {
#         color: var(--text-color) !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] span {
#         color: var(--text-color) !important;
#     }
    
#     /* Selected value container */
#     .stSelectbox [data-baseweb="select"] [class*="singleValue"],
#     .stSelectbox [data-baseweb="select"] [class*="SingleValue"] {
#         color: var(--text-color) !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] [class*="value"],
#     .stSelectbox [data-baseweb="select"] [class*="Value"] {
#         color: var(--text-color) !important;
#     }
    
#     /* Dropdown menu options - CRITICAL */
#     .stSelectbox [data-baseweb="popover"] {
#         z-index: 999999 !important;
#     }
    
#     .stSelectbox li[role="option"] {
#         color: var(--text-color) !important;
#         background: var(--background-color) !important;
#     }
    
#     .stSelectbox li[role="option"]:hover {
#         background: rgba(22, 163, 74, 0.1) !important;
#     }
    
#     .stSelectbox li[role="option"][aria-selected="true"] {
#         background: rgba(22, 163, 74, 0.15) !important;
#         font-weight: 600 !important;
#     }
    
#     /* Expander - Minimal styling */
#     .streamlit-expanderHeader {
#         font-size: 0.75rem;
#         font-weight: 600;
#         padding: 0.5rem 0.75rem;
#         border-radius: 8px;
#     }
    
#     .streamlit-expanderContent {
#         padding: 0.75rem;
#     }
    
#     /* Welcome - Adaptive */
#     .welcome {
#         text-align: center;
#         padding: 1.5rem 0.75rem;
#     }
    
#     .welcome h1 {
#         font-size: 1.5rem;
#         font-weight: 800;
#         background: linear-gradient(135deg, #dc2626, #16a34a);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin: 0.75rem 0 0.4rem 0;
#     }
    
#     .welcome p {
#         font-size: 0.75rem;
#         color: var(--text-color);
#         opacity: 0.7;
#         margin-bottom: 1.5rem;
#     }
    
#     .welcome .emoji {
#         font-size: 4rem;
#         animation: float 3s ease-in-out infinite;
#         filter: drop-shadow(0 6px 12px rgba(0,0,0,0.2));
#         display: inline-block;
#         transform-style: preserve-3d;
#     }
    
#     /* Tree icon in top bar */
#     .tree-icon {
#         font-size: 1.2rem;
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
#         animation: bounce 2s ease-in-out infinite;
#     }
    
#     /* Quiz title icon enhancement */
#     .quiz-title::before {
#         content: "✨ ";
#         filter: drop-shadow(0 2px 4px rgba(22, 163, 74, 0.3));
#     }
    
#     /* Prize banner emojis */
#     .prize::before,
#     .prize::after {
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
#     }
    
#     /* Celebration - Adaptive */
#     .celebration {
#         background: linear-gradient(135deg, #dc2626, #16a34a);
#         border-radius: 12px;
#         padding: 0.75rem;
#         text-align: center;
#         margin-top: 0.5rem;
#         position: relative;
#         overflow: hidden;
#     }
    
#     .celebration::before {
#         content: "🎉";
#         position: absolute;
#         top: 0.5rem;
#         left: 0.5rem;
#         font-size: 1.5rem;
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
#         animation: float 3s ease-in-out infinite;
#     }
    
#     .celebration::after {
#         content: "🎊";
#         position: absolute;
#         top: 0.5rem;
#         right: 0.5rem;
#         font-size: 1.5rem;
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
#         animation: float 3s ease-in-out infinite 1.5s;
#     }
    
#     .celebration h3 {
#         font-size: 1rem;
#         color: white;
#         margin-bottom: 0.4rem;
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2));
#     }
    
#     .celebration p {
#         font-size: 0.75rem;
#         color: rgba(255,255,255,0.95);
#         margin: 0.2rem 0;
#     }
    
#     /* Form spacing */
#     .stForm {
#         margin-bottom: 0;
#     }
    
#     /* Reduce all spacing */
#     div[data-testid="stVerticalBlock"] > div {
#         gap: 0.5rem;
#     }
    
#     /* Info/Success/Error boxes */
#     .stAlert {
#         padding: 0.4rem;
#         font-size: 0.7rem;
#         border-radius: 8px;
#         margin: 0.3rem 0;
#     }
    
#     /* Slider */
#     .stSlider {
#         padding: 0.3rem 0;
#     }
    
#     .stSlider label {
#         font-size: 0.75rem;
#         font-weight: 600;
#     }
    
#     /* Checkbox */
#     .stCheckbox label {
#         font-size: 0.75rem;
#         font-weight: 500;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Configuration
# CAMPAIGN_START_DATE = datetime(2025, 12, 1)
# CAMPAIGN_END_DATE = datetime(2025, 12, 12)
# TEST_MODE_DEFAULT = True  # 🧪 Change to False for production!

# # Properties list
# PROPERTIES = [
#     "Camden",
#     "St Albans",
#     "Westin",
#     "Canopy",
#     "CIE",
#     "CIV",
#     "EH",
#     "Head Office"
# ]

# # Achievements data
# ACHIEVEMENTS = [
#     {
#         "day": 1,
#         "title": "Green Champions Programme",
#         "subtitle": "Community Growth",
#         "emoji": "👥",
#         "color": "#059669",
#         "description": "Our Green Champions network has grown exponentially, with passionate team members leading sustainability initiatives.",
#         "stats": [
#             {"label": "Properties", "value": "7"},
#             {"label": "Initiatives", "value": "47"},
#             {"label": "Engagement", "value": "89%"}
#         ],
#         "quiz": {
#             "question": "How many properties are actively participating in the Green Champions Programme?",
#             "options": ["8", "7", "15", "20"],
#             "correct": "7"
#         }
#     },
#     {
#         "day": 2,
#         "title": "Digital Transformation",
#         "subtitle": "Paper Reduction Victory",
#         "emoji": "📄",
#         "color": "#2563eb",
#         "description": "Through digitisation initiatives, we've dramatically reduced paper consumption while improving efficiency.",
#         "stats": [
#             {"label": "Trees Saved", "value": "234"},
#             {"label": "Digital Docs", "value": "12.5K"},
#             {"label": "Cost Savings", "value": "£18K"}
#         ],
#         "quiz": {
#             "question": "How many trees have we saved through our digitisation efforts?",
#             "options": ["150", "234", "300", "400"],
#             "correct": "234"
#         }
#     },
#     {
#         "day": 3,
#         "title": "Industry Recognition",
#         "subtitle": "ESG Canopy Finalists",
#         "emoji": "🏆",
#         "color": "#f59e0b",
#         "description": "Recognised as ESG Canopy Finalists for our outstanding commitment to sustainability.",
#         "stats": [
#             {"label": "Score", "value": "94/100"},
#             {"label": "Categories", "value": "5"},
#             {"label": "Ranking", "value": "Top 3"}
#         ],
#         "quiz": {
#             "question": "What was our ESG Canopy nomination score?",
#             "options": ["85/100", "90/100", "94/100", "98/100"],
#             "correct": "94/100"
#         }
#     },
#     {
#         "day": 4,
#         "title": "Recycling Revolution",
#         "subtitle": "Record Performance",
#         "emoji": "♻️",
#         "color": "#059669",
#         "description": "Improved from 40% to 51% year-over-year through enhanced programs and team engagement.",
#         "stats": [
#             {"label": "YoY Growth", "value": "+11%"},
#             {"label": "Recycling Rate", "value": "51%"},
#             {"label": "Waste Diverted", "value": "2.4T"}
#         ],
#         "quiz": {
#             "question": "What was our year-over-year recycling improvement?",
#             "options": ["+8%", "+11%", "+15%", "+20%"],
#             "correct": "+11%"
#         }
#     },
#     {
#         "day": 5,
#         "title": "Energy Efficiency",
#         "subtitle": "Smart Management",
#         "emoji": "⚡",
#         "color": "#eab308",
#         "description": "Strategic energy management delivering significant cost savings while reducing environmental impact.",
#         "stats": [
#             {"label": "Cost Savings", "value": "£45K"},
#             {"label": "kWh Reduced", "value": "180K"},
#             {"label": "CO₂ Saved", "value": "42T"}
#         ],
#         "quiz": {
#             "question": "How much did we save through energy efficiency?",
#             "options": ["£30K", "£45K", "£60K", "£75K"],
#             "correct": "£45K"
#         }
#     },
#     {
#         "day": 6,
#         "title": "Water Conservation",
#         "subtitle": "Resource Protection",
#         "emoji": "💧",
#         "color": "#06b6d4",
#         "description": "Smart water management systems reducing consumption across all properties.",
#         "stats": [
#             {"label": "Litres Saved", "value": "2.1M"},
#             {"label": "Properties", "value": "12"},
#             {"label": "Reduction", "value": "18%"}
#         ],
#         "quiz": {
#             "question": "How many litres of water did we save?",
#             "options": ["1.5M", "2.1M", "2.8M", "3.2M"],
#             "correct": "2.1M"
#         }
#     },
#     {
#         "day": 7,
#         "title": "Food Waste Reduction",
#         "subtitle": "Zero Waste Journey",
#         "emoji": "🍽️",
#         "color": "#84cc16",
#         "description": "Comprehensive food waste program with donations and composting initiatives.",
#         "stats": [
#             {"label": "Meals Saved", "value": "3,400"},
#             {"label": "Waste Reduced", "value": "34%"},
#             {"label": "Value", "value": "£28K"}
#         ],
#         "quiz": {
#             "question": "How many meals were saved from waste?",
#             "options": ["2,200", "3,400", "4,100", "5,000"],
#             "correct": "3,400"
#         }
#     },
#     {
#         "day": 8,
#         "title": "Sustainable Procurement",
#         "subtitle": "Responsible Sourcing",
#         "emoji": "🛒",
#         "color": "#8b5cf6",
#         "description": "Prioritising eco-friendly suppliers and sustainable product alternatives.",
#         "stats": [
#             {"label": "Eco Products", "value": "78%"},
#             {"label": "Suppliers", "value": "45"},
#             {"label": "Savings", "value": "£32K"}
#         ],
#         "quiz": {
#             "question": "What percentage of our products are eco-friendly?",
#             "options": ["65%", "72%", "78%", "85%"],
#             "correct": "78%"
#         }
#     },
#     {
#         "day": 9,
#         "title": "Team Training",
#         "subtitle": "Building Expertise",
#         "emoji": "📚",
#         "color": "#ec4899",
#         "description": "Comprehensive sustainability training empowering team members as change agents.",
#         "stats": [
#             {"label": "Hours", "value": "420"},
#             {"label": "Trained", "value": "156"},
#             {"label": "Satisfaction", "value": "96%"}
#         ],
#         "quiz": {
#             "question": "How many team members received sustainability training?",
#             "options": ["120", "156", "180", "200"],
#             "correct": "156"
#         }
#     },
#     {
#         "day": 10,
#         "title": "Carbon Footprint",
#         "subtitle": "Climate Action",
#         "emoji": "🌍",
#         "color": "#059669",
#         "description": "Measurable reduction in carbon emissions through comprehensive initiatives.",
#         "stats": [
#             {"label": "CO₂ Reduced", "value": "156T"},
#             {"label": "Reduction", "value": "22%"},
#             {"label": "Offsetting", "value": "£18K"}
#         ],
#         "quiz": {
#             "question": "How much did we reduce our carbon footprint?",
#             "options": ["15%", "22%", "28%", "35%"],
#             "correct": "22%"
#         }
#     },
#     {
#         "day": 11,
#         "title": "Community Impact",
#         "subtitle": "Local Partnerships",
#         "emoji": "🤝",
#         "color": "#f59e0b",
#         "description": "Collaborating with local organisations to amplify our positive impact.",
#         "stats": [
#             {"label": "Partnerships", "value": "18"},
#             {"label": "Volunteers", "value": "89"},
#             {"label": "Hours Given", "value": "340"}
#         ],
#         "quiz": {
#             "question": "How many community partnerships did we establish?",
#             "options": ["12", "18", "24", "30"],
#             "correct": "18"
#         }
#     },
#     {
#         "day": 12,
#         "title": "2025 Achievement",
#         "subtitle": "Year in Review",
#         "emoji": "🎊",
#         "color": "#dc2626",
#         "description": "Celebrating a transformative year of sustainability excellence and team dedication.",
#         "stats": [
#             {"label": "Total Impact", "value": "£180K"},
#             {"label": "Initiatives", "value": "47"},
#             {"label": "Team Pride", "value": "100%"}
#         ],
#         "quiz": {
#             "question": "What was our total sustainability impact value?",
#             "options": ["£140K", "£180K", "£220K", "£250K"],
#             "correct": "£180K"
#         }
#     }
# ]

# def setup_google_sheets():
#     try:
#         creds_dict = st.secrets["gcp_service_account"]
#         scopes = [
#             "https://www.googleapis.com/auth/spreadsheets",
#             "https://www.googleapis.com/auth/drive"
#         ]
#         creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
#         client = gspread.authorize(creds)
#         return client
#     except Exception as e:
#         return None

# def log_to_sheets(client, data):
#     try:
#         sheet_name = "12 Days Christmas Quiz Responses"
#         spreadsheet = client.open(sheet_name)
#         worksheet = spreadsheet.sheet1
        
#         row = [
#             datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             data["name"],
#             data["property"],
#             data["day"],
#             data["achievement"],
#             data["question"],
#             data["selected_answer"],
#             data["correct_answer"],
#             "Yes" if data["is_correct"] else "No",
#             datetime.now().strftime("%Y-%m-%d")
#         ]
        
#         worksheet.append_row(row)
#         return True
#     except Exception as e:
#         return False

# def calculate_current_day():
#     if st.session_state.test_mode:
#         return st.session_state.test_day
    
#     today = datetime.now()
#     if today < CAMPAIGN_START_DATE:
#         return 1
#     if today > CAMPAIGN_END_DATE:
#         return 12
    
#     days_since_start = (today - CAMPAIGN_START_DATE).days
#     return min(max(days_since_start + 1, 1), 12)

# def init_session_state():
#     if 'user_name' not in st.session_state:
#         st.session_state.user_name = None
#     if 'user_property' not in st.session_state:
#         st.session_state.user_property = None
#     if 'completed_days' not in st.session_state:
#         st.session_state.completed_days = []
#     if 'quiz_submitted' not in st.session_state:
#         st.session_state.quiz_submitted = False
#     if 'quiz_result' not in st.session_state:
#         st.session_state.quiz_result = None
#     if 'test_day' not in st.session_state:
#         st.session_state.test_day = 1
#     if 'test_mode' not in st.session_state:
#         st.session_state.test_mode = TEST_MODE_DEFAULT

# def main():
#     init_session_state()
    
#     # Welcome Screen
#     if st.session_state.user_name is None or st.session_state.user_property is None:
#         st.markdown("""
#         <div class="welcome">
#             <div class="emoji">🎄</div>
#             <h1>12 Days of Sustainability</h1>
#             <p>Celebrating Our 2024 Achievements<br>December 1-12, 2025</p>
#         </div>
#         """, unsafe_allow_html=True)
        
#         # Test mode - collapsed by default
#         with st.expander("🧪 Testing Mode", expanded=False):
#             test_mode = st.checkbox("Enable Testing Mode", value=st.session_state.test_mode)
#             st.session_state.test_mode = test_mode
            
#             if st.session_state.test_mode:
#                 test_day = st.slider("Day", 1, 12, st.session_state.test_day)
#                 st.session_state.test_day = test_day
        
#         # Name and Property Form
#         with st.form("user_entry_form"):
#             name = st.text_input("Your Name", placeholder="Enter your full name...")
            
#             # Use SELECTBOX dropdown for property selection
#             property_select = st.selectbox(
#                 "Your Property",
#                 options=[""] + PROPERTIES,  # Add empty option as default
#                 format_func=lambda x: "Select your property..." if x == "" else x,
#                 index=0
#             )
            
#             submitted = st.form_submit_button("🎄 Start Journey", use_container_width=True, type="primary")
            
#             if submitted:
#                 if name and name.strip() and property_select and property_select != "":
#                     st.session_state.user_name = name.strip()
#                     st.session_state.user_property = property_select
#                     st.rerun()
#                 else:
#                     st.error("⚠️ Please enter your name and select your property")
        
#         return
    
#     # Main App
#     current_day = calculate_current_day()
#     current_achievement = next((a for a in ACHIEVEMENTS if a["day"] == current_day), None)
    
#     if not current_achievement:
#         st.error("Achievement not found")
#         return
    
#     # Top Bar
#     st.markdown(f"""
#     <div class="top-bar">
#         <div class="user-info">
#             <h3><span class="tree-icon">🎄</span> {st.session_state.user_name}</h3>
#             <p>{st.session_state.user_property}</p>
#         </div>
#         <div class="progress-badge">{len(st.session_state.completed_days)}/12</div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Settings - collapsed
#     with st.expander("⚙️ Settings", expanded=False):
#         test_toggle = st.checkbox("Testing Mode", value=st.session_state.test_mode)
#         if test_toggle != st.session_state.test_mode:
#             st.session_state.test_mode = test_toggle
#             st.rerun()
        
#         if st.session_state.test_mode:
#             test_day = st.slider("Day", 1, 12, st.session_state.test_day)
#             if test_day != st.session_state.test_day:
#                 st.session_state.test_day = test_day
#                 st.session_state.quiz_submitted = False
#                 st.session_state.quiz_result = None
#                 st.rerun()
    
#     # Prize Banner
#     st.markdown("""
#     <div class="prize">
#         <p>Complete all 12 days → Win £25 Amazon Gift Card!</p>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Achievement Card
#     st.markdown(f"""
#     <div class="card">
#         <div class="ach-header" style="--color1: {current_achievement['color']}; --color2: {current_achievement['color']}dd;">
#             <div class="day-badge">DAY {current_day} OF 12</div>
#             <div class="ach-emoji">{current_achievement['emoji']}</div>
#             <div class="ach-title">{current_achievement['title']}</div>
#             <div class="ach-subtitle">{current_achievement['subtitle']}</div>
#         </div>
#         <div class="description">{current_achievement['description']}</div>
#         <div class="stats-grid">
#     """, unsafe_allow_html=True)
    
#     for stat in current_achievement['stats']:
#         st.markdown(f"""
#             <div class="stat">
#                 <div class="stat-value">{stat['value']}</div>
#                 <div class="stat-label">{stat['label']}</div>
#             </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown("</div></div>", unsafe_allow_html=True)
    
#     # Quiz Section
#     is_completed = current_day in st.session_state.completed_days
    
#     st.markdown('<div class="card">', unsafe_allow_html=True)
    
#     # Show quiz result if just submitted (PRIORITY CHECK)
#     if st.session_state.quiz_submitted and st.session_state.quiz_result:
#         st.markdown(f"""
#         <div class="quiz-title">Today's Quiz Challenge</div>
#         <div class="quiz-q">{current_achievement['quiz']['question']}</div>
#         """, unsafe_allow_html=True)
        
#         result = st.session_state.quiz_result
#         if result['correct']:
#             st.markdown(f"""
#             <div class="result result-correct">
#                 <h4>✓ CORRECT! Well Done! 🎉</h4>
#                 <p>Your answer <strong>"{result['answer']}"</strong> is correct!</p>
#                 <p style="margin-top: 0.5rem; font-size: 0.9rem;">✅ Day {current_day} complete! See you tomorrow for Day {current_day + 1}!</p>
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div class="result result-incorrect">
#                 <h4>Not quite, but great effort! 💪</h4>
#                 <p>You answered: <strong>"{result['answer']}"</strong></p>
#                 <p>The correct answer is: <strong>"{current_achievement['quiz']['correct']}"</strong></p>
#                 <p style="margin-top: 0.5rem; font-size: 0.9rem;">✅ Day {current_day} complete! See you tomorrow for Day {current_day + 1}!</p>
#             </div>
#             """, unsafe_allow_html=True)
    
#     # Show quiz if not completed and not just submitted
#     elif not is_completed:
#         st.markdown(f"""
#         <div class="quiz-title">Today's Quiz Challenge</div>
#         <div class="quiz-q">{current_achievement['quiz']['question']}</div>
#         """, unsafe_allow_html=True)
        
#         selected = st.radio(
#             "",
#             current_achievement['quiz']['options'],
#             key=f"quiz_{current_day}",
#             label_visibility="collapsed"
#         )
        
#         if st.button("🎯 Submit Answer", type="primary", use_container_width=True):
#             is_correct = selected == current_achievement['quiz']['correct']
#             st.session_state.quiz_result = {'answer': selected, 'correct': is_correct}
#             st.session_state.quiz_submitted = True
#             st.session_state.completed_days.append(current_day)
            
#             try:
#                 client = setup_google_sheets()
#                 if client:
#                     data = {
#                         "name": st.session_state.user_name,
#                         "property": st.session_state.user_property,
#                         "day": current_day,
#                         "achievement": current_achievement['title'],
#                         "question": current_achievement['quiz']['question'],
#                         "selected_answer": selected,
#                         "correct_answer": current_achievement['quiz']['correct'],
#                         "is_correct": is_correct
#                     }
#                     log_to_sheets(client, data)
#             except:
#                 pass
            
#             st.rerun()
    
#     # Show "already completed" message
#     else:
#         st.markdown(f"""
#         <div class="result result-completed">
#             <h4>Day {current_day} Complete!</h4>
#             <p>You've finished today's quiz.</p>
#             <p>Come back tomorrow for Day {current_day + 1}!</p>
#         </div>
#         """, unsafe_allow_html=True)
    
#     st.markdown('</div>', unsafe_allow_html=True)
    
#     # Celebration
#     if len(st.session_state.completed_days) == 12:
#         st.balloons()
#         st.markdown(f"""
#         <div class="celebration">
#             <h3>Congratulations {st.session_state.user_name}!</h3>
#             <p>You completed all 12 Days of Sustainability!</p>
#             <p style="margin-top: 0.5rem; font-weight: 700;">
#                 🎁 You've earned your £25 Amazon Gift Card! 🎁
#             </p>
#         </div>
#         """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()


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
    
    /* Cards - More prominent with shadows */
    .card {
        background: var(--background-color);
        border-radius: 16px;
        border: 2px solid var(--secondary-background-color);
        padding: 1rem;
        margin-bottom: 0.75rem;
        box-shadow: 0 6px 16px rgba(0,0,0,0.12);
    }
    
    /* Achievement Header - More dramatic */
    .ach-header {
        background: linear-gradient(135deg, var(--color1), var(--color2));
        padding: 1.5rem 1rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 1rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .ach-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -200%;
        width: 200%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        animation: shimmer 3s infinite;
    }
    
    .day-badge {
        background: rgba(255,255,255,0.3);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 800;
        color: white;
        display: inline-block;
        margin-bottom: 0.75rem;
        letter-spacing: 1px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        border: 2px solid rgba(255,255,255,0.4);
    }
    
    .ach-emoji {
        font-size: 5rem;
        margin: 1rem 0;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(0 8px 16px rgba(0,0,0,0.3));
        transform-style: preserve-3d;
        display: block;
        text-align: center;
    }
    
    .ach-emoji:hover {
        animation: bounce 0.6s ease;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0) scale(1); }
        25% { transform: translateY(-15px) scale(1.1); }
        50% { transform: translateY(0) scale(1.05); }
        75% { transform: translateY(-8px) scale(1.08); }
    }
    
    .ach-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: white;
        margin: 0.5rem 0;
        line-height: 1.2;
        text-shadow: 0 3px 6px rgba(0,0,0,0.4);
    }
    
    .ach-subtitle {
        font-size: 1rem;
        color: white;
        opacity: 0.95;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        font-weight: 600;
    }
    
    /* Description - Larger and more readable */
    .description {
        font-size: 1rem;
        line-height: 1.6;
        color: var(--text-color);
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    
    /* Stats Grid - PROMINENT BOXES with animations */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.75rem;
        margin-bottom: 1rem;
    }
    
    .stat {
        background: linear-gradient(135deg, var(--secondary-background-color), var(--background-color));
        border: 3px solid #16a34a;
        border-radius: 16px;
        padding: 1rem 0.5rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(22, 163, 74, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .stat::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #16a34a, #22c55e, #16a34a);
        background-size: 200% 100%;
        animation: shimmer 2s linear infinite;
    }
    
    .stat:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0 8px 20px rgba(22, 163, 74, 0.4);
        border-color: #22c55e;
    }
    
    .stat:active {
        transform: translateY(-2px) scale(1.01);
    }
    
    .stat-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #16a34a;
        margin-bottom: 0.3rem;
        text-shadow: 0 2px 4px rgba(22, 163, 74, 0.2);
        animation: pulse 2s ease-in-out infinite;
    }
    
    .stat-label {
        font-size: 0.85rem;
        color: var(--text-color);
        opacity: 0.8;
        line-height: 1.3;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Quiz - Larger and more engaging */
    .quiz-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: #16a34a;
        text-align: center;
        margin-bottom: 0.75rem;
        text-shadow: 0 2px 4px rgba(22, 163, 74, 0.2);
    }
    
    .quiz-q {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text-color);
        background: var(--secondary-background-color);
        padding: 1.25rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 1rem;
        border: 3px solid rgba(22, 163, 74, 0.3);
        line-height: 1.5;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Radio Buttons - VERTICAL LIST with larger touch targets */
    div[data-testid="stRadio"] > div {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }
    
    div[data-testid="stRadio"] > div > label {
        background: var(--background-color);
        border: 3px solid var(--secondary-background-color);
        border-radius: 16px;
        padding: 1.25rem 1.5rem;
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text-color);
        text-align: left;
        margin: 0;
        display: flex;
        align-items: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        line-height: 1.4;
        min-height: 60px;
    }
    
    div[data-testid="stRadio"] > div > label:hover {
        border-color: #16a34a;
        background: rgba(22, 163, 74, 0.08);
        transform: translateX(4px) scale(1.02);
        box-shadow: 0 6px 16px rgba(22, 163, 74, 0.2);
    }
    
    div[data-testid="stRadio"] > div > label[data-checked="true"] {
        border-color: #16a34a;
        background: rgba(22, 163, 74, 0.15);
        color: #16a34a;
        font-weight: 800;
        box-shadow: 0 8px 20px rgba(22, 163, 74, 0.3);
        transform: scale(1.03);
    }
    
    div[data-testid="stRadio"] > div > label[data-checked="true"]::before {
        content: "✓ ";
        font-size: 1.5rem;
        margin-right: 0.5rem;
    }
    
    /* Button - Larger and more exciting */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #dc2626, #16a34a);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 1.25rem;
        font-size: 1.2rem;
        font-weight: 800;
        box-shadow: 0 8px 20px rgba(34, 197, 94, 0.4);
        transition: all 0.3s ease;
        margin-top: 1rem;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 28px rgba(34, 197, 94, 0.5);
    }
    
    .stButton > button:active {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(34, 197, 94, 0.4);
    }
    
    /* Result Box - SUPER PROMINENT with confetti effect */
    .result {
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        margin-top: 1rem;
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .result::before {
        content: '';
        position: absolute;
        top: 0;
        left: -200%;
        width: 200%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        animation: shimmer 2s infinite;
    }
    
    .result-correct {
        background: linear-gradient(135deg, rgba(22, 163, 74, 0.25), rgba(34, 197, 94, 0.25));
        border: 4px solid #16a34a;
        animation: pulse 1s ease-in-out 3;
    }
    
    .result-incorrect {
        background: linear-gradient(135deg, rgba(251, 146, 60, 0.25), rgba(249, 115, 22, 0.25));
        border: 4px solid #fb923c;
    }
    
    .result-completed {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(37, 99, 235, 0.25));
        border: 4px solid #3b82f6;
    }
    
    .result h4 {
        font-size: 1.5rem;
        color: var(--text-color);
        margin-bottom: 0.75rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Enhanced result emojis - HUGE */
    .result-correct h4::before {
        content: "🎉 ";
        font-size: 2.5rem;
        filter: drop-shadow(0 4px 8px rgba(34, 197, 94, 0.5));
        animation: bounce 0.8s ease 3;
        display: inline-block;
    }
    
    .result-incorrect h4::before {
        content: "💪 ";
        font-size: 2.5rem;
        filter: drop-shadow(0 4px 8px rgba(251, 146, 60, 0.5));
        display: inline-block;
    }
    
    .result-completed h4::before {
        content: "✅ ";
        font-size: 2.5rem;
        filter: drop-shadow(0 4px 8px rgba(59, 130, 246, 0.5));
        display: inline-block;
    }
    
    .result p {
        font-size: 1.1rem;
        color: var(--text-color);
        margin: 0.5rem 0;
        line-height: 1.6;
        font-weight: 600;
    }
    
    .result p strong {
        font-weight: 900;
        color: var(--text-color);
        font-size: 1.2rem;
    }
    
    /* Prize Banner - EXCITING with animation */
    .prize {
        background: linear-gradient(135deg, rgba(251, 191, 36, 0.3), rgba(245, 158, 11, 0.3));
        border-radius: 16px;
        padding: 1rem 1.25rem;
        text-align: center;
        margin-bottom: 0.75rem;
        box-shadow: 0 6px 16px rgba(251, 191, 36, 0.3);
        border: 3px solid rgba(251, 191, 36, 0.6);
        position: relative;
        animation: glow 3s ease-in-out infinite;
    }
    
    .prize p {
        font-size: 1rem;
        font-weight: 800;
        color: var(--text-color);
        margin: 0;
        line-height: 1.4;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Enhance prize emoji - BIGGER */
    .prize::before {
        content: "🎁";
        position: absolute;
        left: 1rem;
        font-size: 2rem;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
        animation: float 3s ease-in-out infinite;
    }
    
    .prize::after {
        content: "🎁";
        position: absolute;
        right: 1rem;
        font-size: 2rem;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
        animation: float 3s ease-in-out infinite 1.5s;
    }
    
    /* Inputs - Larger for mobile */
    .stTextInput label {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stTextInput input {
        font-size: 1.1rem;
        padding: 1rem;
        border-radius: 12px;
        border: 2px solid var(--secondary-background-color);
    }
    
    .stTextInput input:focus {
        border-color: #16a34a;
        box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.2);
    }
    
    /* Selectbox - AGGRESSIVE FIX for selected value visibility + larger */
    .stSelectbox label {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        font-size: 1.1rem;
        padding: 1rem;
        border-radius: 12px;
    }
    
    /* Force selected value to be visible - CRITICAL */
    .stSelectbox input {
        color: var(--text-color) !important;
        opacity: 1 !important;
    }
    
    .stSelectbox [data-baseweb="select"] input {
        color: var(--text-color) !important;
        opacity: 1 !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div > div {
        color: var(--text-color) !important;
    }
    
    .stSelectbox [data-baseweb="select"] span {
        color: var(--text-color) !important;
    }
    
    /* Selected value container */
    .stSelectbox [data-baseweb="select"] [class*="singleValue"],
    .stSelectbox [data-baseweb="select"] [class*="SingleValue"] {
        color: var(--text-color) !important;
    }
    
    .stSelectbox [data-baseweb="select"] [class*="value"],
    .stSelectbox [data-baseweb="select"] [class*="Value"] {
        color: var(--text-color) !important;
    }
    
    /* Dropdown menu options - CRITICAL + larger */
    .stSelectbox [data-baseweb="popover"] {
        z-index: 999999 !important;
    }
    
    .stSelectbox li[role="option"] {
        color: var(--text-color) !important;
        background: var(--background-color) !important;
        font-size: 1.1rem !important;
        padding: 1rem !important;
    }
    
    .stSelectbox li[role="option"]:hover {
        background: rgba(22, 163, 74, 0.1) !important;
    }
    
    .stSelectbox li[role="option"][aria-selected="true"] {
        background: rgba(22, 163, 74, 0.15) !important;
        font-weight: 700 !important;
    }
    
    /* Expander - Larger */
    .streamlit-expanderHeader {
        font-size: 1rem;
        font-weight: 700;
        padding: 0.75rem 1rem;
        border-radius: 12px;
    }
    
    .streamlit-expanderContent {
        padding: 1rem;
    }
    
    /* Welcome - Larger and more exciting */
    .welcome {
        text-align: center;
        padding: 2rem 1rem;
    }
    
    .welcome h1 {
        font-size: 2rem;
        font-weight: 900;
        background: linear-gradient(135deg, #dc2626, #16a34a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 1rem 0 0.75rem 0;
        letter-spacing: -0.5px;
    }
    
    .welcome p {
        font-size: 1rem;
        color: var(--text-color);
        opacity: 0.8;
        margin-bottom: 2rem;
        font-weight: 500;
        line-height: 1.5;
    }
    
    .welcome .emoji {
        font-size: 6rem;
        animation: float 3s ease-in-out infinite;
        filter: drop-shadow(0 8px 16px rgba(0,0,0,0.3));
        display: inline-block;
        transform-style: preserve-3d;
    }
    
    .welcome .emoji:hover {
        animation: bounce 0.8s ease;
    }
    
    /* Tree icon in top bar - larger */
    .tree-icon {
        font-size: 1.5rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
        animation: bounce 2s ease-in-out infinite;
    }
    
    /* Quiz title icon enhancement */
    .quiz-title::before {
        content: "✨ ";
        font-size: 1.5rem;
        filter: drop-shadow(0 2px 4px rgba(22, 163, 74, 0.3));
    }
    
    /* Prize banner emojis */
    .prize::before,
    .prize::after {
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
    }
    
    /* Celebration - Larger and more exciting */
    .celebration {
        background: linear-gradient(135deg, #dc2626, #16a34a);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        margin-top: 1rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    
    .celebration::before {
        content: "🎉";
        position: absolute;
        top: 1rem;
        left: 1rem;
        font-size: 2.5rem;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
        animation: float 3s ease-in-out infinite;
    }
    
    .celebration::after {
        content: "🎊";
        position: absolute;
        top: 1rem;
        right: 1rem;
        font-size: 2.5rem;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
        animation: float 3s ease-in-out infinite 1.5s;
    }
    
    .celebration h3 {
        font-size: 1.5rem;
        color: white;
        margin-bottom: 0.75rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
        font-weight: 900;
    }
    
    .celebration p {
        font-size: 1rem;
        color: rgba(255,255,255,0.95);
        margin: 0.5rem 0;
        font-weight: 600;
    }
    
    /* Form spacing */
    .stForm {
        margin-bottom: 0;
    }
    
    /* Reduce all spacing */
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.75rem;
    }
    
    /* Info/Success/Error boxes - larger */
    .stAlert {
        padding: 0.75rem;
        font-size: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
    }
    
    /* Slider - larger */
    .stSlider {
        padding: 0.5rem 0;
    }
    
    .stSlider label {
        font-size: 1rem;
        font-weight: 700;
    }
    
    /* Checkbox - larger */
    .stCheckbox label {
        font-size: 1rem;
        font-weight: 600;
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
        "color": "#059669",
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
        "color": "#2563eb",
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
        "color": "#059669",
        "description": "Improved from 40% to 51% year-over-year through enhanced programs and team engagement.",
        "stats": [
            {"label": "YoY Growth", "value": "+11%"},
            {"label": "Recycling Rate", "value": "51%"},
            {"label": "Waste Diverted", "value": "2.4T"}
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
        "description": "Strategic energy management delivering significant cost savings while reducing environmental impact.",
        "stats": [
            {"label": "Cost Savings", "value": "£45K"},
            {"label": "kWh Reduced", "value": "180K"},
            {"label": "CO₂ Saved", "value": "42T"}
        ],
        "quiz": {
            "question": "How much did we save through energy efficiency?",
            "options": ["£30K", "£45K", "£60K", "£75K"],
            "correct": "£45K"
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
            {"label": "Litres Saved", "value": "2.1M"},
            {"label": "Properties", "value": "12"},
            {"label": "Reduction", "value": "18%"}
        ],
        "quiz": {
            "question": "How many litres of water did we save?",
            "options": ["1.5M", "2.1M", "2.8M", "3.2M"],
            "correct": "2.1M"
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
            {"label": "Meals Saved", "value": "3,400"},
            {"label": "Waste Reduced", "value": "34%"},
            {"label": "Value", "value": "£28K"}
        ],
        "quiz": {
            "question": "How many meals were saved from waste?",
            "options": ["2,200", "3,400", "4,100", "5,000"],
            "correct": "3,400"
        }
    },
    {
        "day": 8,
        "title": "Sustainable Procurement",
        "subtitle": "Responsible Sourcing",
        "emoji": "🛒",
        "color": "#8b5cf6",
        "description": "Prioritising eco-friendly suppliers and sustainable product alternatives.",
        "stats": [
            {"label": "Eco Products", "value": "78%"},
            {"label": "Suppliers", "value": "45"},
            {"label": "Savings", "value": "£32K"}
        ],
        "quiz": {
            "question": "What percentage of our products are eco-friendly?",
            "options": ["65%", "72%", "78%", "85%"],
            "correct": "78%"
        }
    },
    {
        "day": 9,
        "title": "Team Training",
        "subtitle": "Building Expertise",
        "emoji": "📚",
        "color": "#ec4899",
        "description": "Comprehensive sustainability training empowering team members as change agents.",
        "stats": [
            {"label": "Hours", "value": "420"},
            {"label": "Trained", "value": "156"},
            {"label": "Satisfaction", "value": "96%"}
        ],
        "quiz": {
            "question": "How many team members received sustainability training?",
            "options": ["120", "156", "180", "200"],
            "correct": "156"
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
            {"label": "CO₂ Reduced", "value": "156T"},
            {"label": "Reduction", "value": "22%"},
            {"label": "Offsetting", "value": "£18K"}
        ],
        "quiz": {
            "question": "How much did we reduce our carbon footprint?",
            "options": ["15%", "22%", "28%", "35%"],
            "correct": "22%"
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
            {"label": "Partnerships", "value": "18"},
            {"label": "Volunteers", "value": "89"},
            {"label": "Hours Given", "value": "340"}
        ],
        "quiz": {
            "question": "How many community partnerships did we establish?",
            "options": ["12", "18", "24", "30"],
            "correct": "18"
        }
    },
    {
        "day": 12,
        "title": "2024 Achievement",
        "subtitle": "Year in Review",
        "emoji": "🎊",
        "color": "#dc2626",
        "description": "Celebrating a transformative year of sustainability excellence and team dedication.",
        "stats": [
            {"label": "Total Impact", "value": "£180K"},
            {"label": "Initiatives", "value": "47"},
            {"label": "Team Pride", "value": "100%"}
        ],
        "quiz": {
            "question": "What was our total sustainability impact value?",
            "options": ["£140K", "£180K", "£220K", "£250K"],
            "correct": "£180K"
        }
    }
]

def setup_google_sheets():
    try:
        creds_dict = st.secrets["gcp_service_account"]
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
        client = gspread.authorize(creds)
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