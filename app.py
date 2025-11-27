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
#     page_title="12 Days of Sustainability",
#     page_icon="🎄",
#     layout="centered",
#     initial_sidebar_state="collapsed"
# )

# # Engaging Mobile-Optimized Theme CSS
# st.markdown("""
# <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
#     * {
#         font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
#     }
    
#     /* Mobile-friendly base sizes */
#     html {
#         font-size: 16px;
#     }
    
#     @media (max-width: 768px) {
#         html {
#             font-size: 18px;  /* Larger base size on mobile */
#         }
#     }
    
#     /* Let Streamlit handle the background */
#     .block-container {
#         padding: 0.5rem;
#         max-width: 420px;
#     }
    
#     /* Hide Streamlit elements */
#     #MainMenu, footer, header {visibility: hidden;}
    
#     /* SNOWFLAKES ANIMATION ❄️ */
#     .snowflakes {
#         position: fixed;
#         top: -10px;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         pointer-events: none;
#         z-index: 1;
#         overflow: hidden;
#     }
    
#     .snowflake {
#         position: absolute;
#         top: -10px;
#         font-size: 1.5rem;
#         animation: fall linear infinite;
#         user-select: none;
#     }
    
#     /* Adaptive snowflake colors for light/dark mode */
#     @media (prefers-color-scheme: dark) {
#         .snowflake {
#             color: rgba(255, 255, 255, 0.7);
#             text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
#         }
#     }
    
#     @media (prefers-color-scheme: light) {
#         .snowflake {
#             color: rgba(200, 230, 255, 0.8);
#             text-shadow: 0 0 5px rgba(150, 200, 255, 0.3);
#         }
#     }
    
#     /* Default (works for both) */
#     .snowflake {
#         color: rgba(220, 240, 255, 0.75);
#         text-shadow: 0 0 8px rgba(200, 230, 255, 0.4);
#     }
    
#     @keyframes fall {
#         0% {
#             top: -10%;
#             opacity: 0;
#         }
#         10% {
#             opacity: 1;
#         }
#         90% {
#             opacity: 1;
#         }
#         100% {
#             top: 110%;
#             opacity: 0;
#         }
#     }
    
#     @keyframes sway {
#         0%, 100% { transform: translateX(0); }
#         50% { transform: translateX(30px); }
#     }
    
#     /* Create multiple snowflakes with different positions and speeds */
#     .snowflake:nth-child(1) { left: 5%; animation-duration: 12s; animation-delay: 0s; }
#     .snowflake:nth-child(2) { left: 15%; animation-duration: 15s; animation-delay: 2s; font-size: 1.2rem; }
#     .snowflake:nth-child(3) { left: 25%; animation-duration: 10s; animation-delay: 4s; font-size: 1.8rem; }
#     .snowflake:nth-child(4) { left: 35%; animation-duration: 18s; animation-delay: 1s; }
#     .snowflake:nth-child(5) { left: 45%; animation-duration: 13s; animation-delay: 3s; font-size: 1.3rem; }
#     .snowflake:nth-child(6) { left: 55%; animation-duration: 16s; animation-delay: 5s; }
#     .snowflake:nth-child(7) { left: 65%; animation-duration: 11s; animation-delay: 0s; font-size: 1.6rem; }
#     .snowflake:nth-child(8) { left: 75%; animation-duration: 14s; animation-delay: 2s; }
#     .snowflake:nth-child(9) { left: 85%; animation-duration: 17s; animation-delay: 4s; font-size: 1.4rem; }
#     .snowflake:nth-child(10) { left: 95%; animation-duration: 12s; animation-delay: 1s; }
#     .snowflake:nth-child(11) { left: 10%; animation-duration: 15s; animation-delay: 6s; font-size: 1.7rem; }
#     .snowflake:nth-child(12) { left: 20%; animation-duration: 13s; animation-delay: 3s; }
#     .snowflake:nth-child(13) { left: 30%; animation-duration: 16s; animation-delay: 5s; font-size: 1.5rem; }
#     .snowflake:nth-child(14) { left: 40%; animation-duration: 11s; animation-delay: 2s; }
#     .snowflake:nth-child(15) { left: 50%; animation-duration: 14s; animation-delay: 4s; font-size: 1.3rem; }
#     .snowflake:nth-child(16) { left: 60%; animation-duration: 17s; animation-delay: 0s; }
#     .snowflake:nth-child(17) { left: 70%; animation-duration: 12s; animation-delay: 6s; font-size: 1.8rem; }
#     .snowflake:nth-child(18) { left: 80%; animation-duration: 15s; animation-delay: 1s; }
#     .snowflake:nth-child(19) { left: 90%; animation-duration: 13s; animation-delay: 3s; font-size: 1.4rem; }
#     .snowflake:nth-child(20) { left: 8%; animation-duration: 16s; animation-delay: 5s; }
    
#     /* Add swaying motion to some snowflakes */
#     .snowflake:nth-child(odd) {
#         animation: fall linear infinite, sway 3s ease-in-out infinite;
#     }
    
#     /* Ensure content stays above snowflakes */
#     .stApp > div {
#         position: relative;
#         z-index: 10;
#     }
    
#     /* Animations */
#     @keyframes float {
#         0%, 100% { transform: translateY(0); }
#         50% { transform: translateY(-5px); }
#     }
    
#     @keyframes glow {
#         0%, 100% { box-shadow: 0 2px 10px rgba(34, 197, 94, 0.3); }
#         50% { box-shadow: 0 2px 15px rgba(34, 197, 94, 0.5); }
#     }
    
#     @keyframes pulse {
#         0%, 100% { transform: scale(1); }
#         50% { transform: scale(1.05); }
#     }
    
#     @keyframes shimmer {
#         0% { background-position: -200% center; }
#         100% { background-position: 200% center; }
#     }
    
#     /* Top Bar - More prominent */
#     .top-bar {
#         background: var(--background-color);
#         padding: 0.75rem 1rem;
#         border-radius: 12px;
#         margin-bottom: 0.75rem;
#         border: 2px solid var(--secondary-background-color);
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.15);
#     }
    
#     .user-info h3 {
#         color: var(--text-color);
#         font-size: 1rem;
#         margin: 0;
#         font-weight: 700;
#     }
    
#     .user-info p {
#         color: var(--text-color);
#         opacity: 0.7;
#         font-size: 0.85rem;
#         margin: 0;
#         font-weight: 500;
#     }
    
#     .progress-badge {
#         background: linear-gradient(135deg, #dc2626, #16a34a);
#         color: white;
#         padding: 0.5rem 0.9rem;
#         border-radius: 20px;
#         font-size: 0.9rem;
#         font-weight: 800;
#         animation: glow 2s infinite;
#         position: relative;
#         box-shadow: 0 4px 12px rgba(22, 163, 74, 0.4);
#     }
    
#     .progress-badge::after {
#         content: " ✨";
#         font-size: 1.2rem;
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
    
#     /* Cards - More prominent with shadows */
#     .card {
#         background: var(--background-color);
#         border-radius: 16px;
#         border: 2px solid var(--secondary-background-color);
#         padding: 1rem;
#         margin-bottom: 0.75rem;
#         box-shadow: 0 6px 16px rgba(0,0,0,0.12);
#     }
    
#     /* Achievement Header - More dramatic */
#     .ach-header {
#         background: linear-gradient(135deg, var(--color1), var(--color2));
#         padding: 1.5rem 1rem;
#         border-radius: 16px;
#         text-align: center;
#         margin-bottom: 1rem;
#         box-shadow: 0 8px 20px rgba(0,0,0,0.2);
#         position: relative;
#         overflow: hidden;
#     }
    
#     .ach-header::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: -200%;
#         width: 200%;
#         height: 100%;
#         background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
#         animation: shimmer 3s infinite;
#     }
    
#     .day-badge {
#         background: rgba(255,255,255,0.3);
#         padding: 0.5rem 1rem;
#         border-radius: 20px;
#         font-size: 0.9rem;
#         font-weight: 800;
#         color: white;
#         display: inline-block;
#         margin-bottom: 0.75rem;
#         letter-spacing: 1px;
#         text-shadow: 0 2px 4px rgba(0,0,0,0.3);
#         border: 2px solid rgba(255,255,255,0.4);
#     }
    
#     .ach-emoji {
#         font-size: 5rem;
#         margin: 1rem 0;
#         animation: float 3s ease-in-out infinite;
#         filter: drop-shadow(0 8px 16px rgba(0,0,0,0.3));
#         transform-style: preserve-3d;
#         display: block;
#         text-align: center;
#     }
    
#     .ach-emoji:hover {
#         animation: bounce 0.6s ease;
#     }
    
#     @keyframes bounce {
#         0%, 100% { transform: translateY(0) scale(1); }
#         25% { transform: translateY(-15px) scale(1.1); }
#         50% { transform: translateY(0) scale(1.05); }
#         75% { transform: translateY(-8px) scale(1.08); }
#     }
    
#     .ach-title {
#         font-size: 1.4rem;
#         font-weight: 800;
#         color: white;
#         margin: 0.5rem 0;
#         line-height: 1.2;
#         text-shadow: 0 3px 6px rgba(0,0,0,0.4);
#     }
    
#     .ach-subtitle {
#         font-size: 1rem;
#         color: white;
#         opacity: 0.95;
#         text-shadow: 0 2px 4px rgba(0,0,0,0.3);
#         font-weight: 600;
#     }
    
#     /* Description - Larger and more readable */
#     .description {
#         font-size: 1rem;
#         line-height: 1.6;
#         color: var(--text-color);
#         text-align: center;
#         margin-bottom: 1rem;
#         font-weight: 500;
#     }
    
#     /* Stats Grid - PROMINENT BOXES with animations */
#     .stats-grid {
#         display: grid;
#         grid-template-columns: repeat(3, 1fr);
#         gap: 0.75rem;
#         margin-bottom: 1rem;
#     }
    
#     .stat {
#         background: linear-gradient(135deg, var(--secondary-background-color), var(--background-color));
#         border: 3px solid #16a34a;
#         border-radius: 16px;
#         padding: 1rem 0.5rem;
#         text-align: center;
#         transition: all 0.3s ease;
#         box-shadow: 0 4px 12px rgba(22, 163, 74, 0.2);
#         position: relative;
#         overflow: hidden;
#     }
    
#     .stat::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         height: 3px;
#         background: linear-gradient(90deg, #16a34a, #22c55e, #16a34a);
#         background-size: 200% 100%;
#         animation: shimmer 2s linear infinite;
#     }
    
#     .stat:hover {
#         transform: translateY(-4px) scale(1.03);
#         box-shadow: 0 8px 20px rgba(22, 163, 74, 0.4);
#         border-color: #22c55e;
#     }
    
#     .stat:active {
#         transform: translateY(-2px) scale(1.01);
#     }
    
#     .stat-value {
#         font-size: 1.8rem;
#         font-weight: 800;
#         color: #16a34a;
#         margin-bottom: 0.3rem;
#         text-shadow: 0 2px 4px rgba(22, 163, 74, 0.2);
#         animation: pulse 2s ease-in-out infinite;
#     }
    
#     .stat-label {
#         font-size: 0.85rem;
#         color: var(--text-color);
#         opacity: 0.8;
#         line-height: 1.3;
#         font-weight: 600;
#         text-transform: uppercase;
#         letter-spacing: 0.5px;
#     }
    
#     /* Quiz - Larger and more engaging */
#     .quiz-title {
#         font-size: 1.3rem;
#         font-weight: 800;
#         color: #16a34a;
#         text-align: center;
#         margin-bottom: 0.75rem;
#         text-shadow: 0 2px 4px rgba(22, 163, 74, 0.2);
#     }
    
#     .quiz-q {
#         font-size: 1.1rem;
#         font-weight: 700;
#         color: var(--text-color);
#         background: var(--secondary-background-color);
#         padding: 1.25rem;
#         border-radius: 16px;
#         text-align: center;
#         margin-bottom: 1rem;
#         border: 3px solid rgba(22, 163, 74, 0.3);
#         line-height: 1.5;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.1);
#     }
    
#     /* Radio Buttons - VERTICAL LIST with larger touch targets */
#     div[data-testid="stRadio"] > div {
#         display: flex;
#         flex-direction: column;
#         gap: 0.75rem;
#     }
    
#     div[data-testid="stRadio"] > div > label {
#         background: var(--background-color);
#         border: 3px solid var(--secondary-background-color);
#         border-radius: 16px;
#         padding: 1.25rem 1.5rem;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         font-size: 1.1rem;
#         font-weight: 600;
#         color: var(--text-color);
#         text-align: left;
#         margin: 0;
#         display: flex;
#         align-items: center;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.08);
#         line-height: 1.4;
#         min-height: 60px;
#     }
    
#     div[data-testid="stRadio"] > div > label:hover {
#         border-color: #16a34a;
#         background: rgba(22, 163, 74, 0.08);
#         transform: translateX(4px) scale(1.02);
#         box-shadow: 0 6px 16px rgba(22, 163, 74, 0.2);
#     }
    
#     div[data-testid="stRadio"] > div > label[data-checked="true"] {
#         border-color: #16a34a;
#         background: rgba(22, 163, 74, 0.15);
#         color: #16a34a;
#         font-weight: 800;
#         box-shadow: 0 8px 20px rgba(22, 163, 74, 0.3);
#         transform: scale(1.03);
#     }
    
#     div[data-testid="stRadio"] > div > label[data-checked="true"]::before {
#         content: "✓ ";
#         font-size: 1.5rem;
#         margin-right: 0.5rem;
#     }
    
#     /* Button - Larger and more exciting */
#     .stButton > button {
#         width: 100%;
#         background: linear-gradient(135deg, #dc2626, #16a34a);
#         color: white;
#         border: none;
#         border-radius: 16px;
#         padding: 1.25rem;
#         font-size: 1.2rem;
#         font-weight: 800;
#         box-shadow: 0 8px 20px rgba(34, 197, 94, 0.4);
#         transition: all 0.3s ease;
#         margin-top: 1rem;
#         letter-spacing: 0.5px;
#         text-transform: uppercase;
#     }
    
#     .stButton > button:hover {
#         transform: translateY(-4px);
#         box-shadow: 0 12px 28px rgba(34, 197, 94, 0.5);
#     }
    
#     .stButton > button:active {
#         transform: translateY(-2px);
#         box-shadow: 0 6px 16px rgba(34, 197, 94, 0.4);
#     }
    
#     /* Result Box - SUPER PROMINENT with confetti effect */
#     .result {
#         border-radius: 16px;
#         padding: 1.5rem;
#         text-align: center;
#         margin-top: 1rem;
#         box-shadow: 0 8px 24px rgba(0,0,0,0.2);
#         position: relative;
#         overflow: hidden;
#     }
    
#     .result::before {
#         content: '';
#         position: absolute;
#         top: 0;
#         left: -200%;
#         width: 200%;
#         height: 100%;
#         background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
#         animation: shimmer 2s infinite;
#     }
    
#     .result-correct {
#         background: linear-gradient(135deg, rgba(22, 163, 74, 0.25), rgba(34, 197, 94, 0.25));
#         border: 4px solid #16a34a;
#         animation: pulse 1s ease-in-out 3;
#     }
    
#     .result-incorrect {
#         background: linear-gradient(135deg, rgba(251, 146, 60, 0.25), rgba(249, 115, 22, 0.25));
#         border: 4px solid #fb923c;
#     }
    
#     .result-completed {
#         background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(37, 99, 235, 0.25));
#         border: 4px solid #3b82f6;
#     }
    
#     .result h4 {
#         font-size: 1.5rem;
#         color: var(--text-color);
#         margin-bottom: 0.75rem;
#         font-weight: 900;
#         text-transform: uppercase;
#         letter-spacing: 1px;
#     }
    
#     /* Enhanced result emojis - HUGE */
#     .result-correct h4::before {
#         content: "🎉 ";
#         font-size: 2.5rem;
#         filter: drop-shadow(0 4px 8px rgba(34, 197, 94, 0.5));
#         animation: bounce 0.8s ease 3;
#         display: inline-block;
#     }
    
#     .result-incorrect h4::before {
#         content: "💪 ";
#         font-size: 2.5rem;
#         filter: drop-shadow(0 4px 8px rgba(251, 146, 60, 0.5));
#         display: inline-block;
#     }
    
#     .result-completed h4::before {
#         content: "✅ ";
#         font-size: 2.5rem;
#         filter: drop-shadow(0 4px 8px rgba(59, 130, 246, 0.5));
#         display: inline-block;
#     }
    
#     .result p {
#         font-size: 1.1rem;
#         color: var(--text-color);
#         margin: 0.5rem 0;
#         line-height: 1.6;
#         font-weight: 600;
#     }
    
#     .result p strong {
#         font-weight: 900;
#         color: var(--text-color);
#         font-size: 1.2rem;
#     }
    
#     /* Prize Banner - EXCITING with animation */
#     .prize {
#         background: linear-gradient(135deg, rgba(251, 191, 36, 0.3), rgba(245, 158, 11, 0.3));
#         border-radius: 16px;
#         padding: 1rem 1.25rem;
#         text-align: center;
#         margin-bottom: 0.75rem;
#         box-shadow: 0 6px 16px rgba(251, 191, 36, 0.3);
#         border: 3px solid rgba(251, 191, 36, 0.6);
#         position: relative;
#         animation: glow 3s ease-in-out infinite;
#     }
    
#     .prize p {
#         font-size: 1rem;
#         font-weight: 800;
#         color: var(--text-color);
#         margin: 0;
#         line-height: 1.4;
#         text-transform: uppercase;
#         letter-spacing: 0.5px;
#     }
    
#     /* Enhance prize emoji - BIGGER */
#     .prize::before {
#         content: "🎁";
#         position: absolute;
#         left: 1rem;
#         font-size: 2rem;
#         filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
#         animation: float 3s ease-in-out infinite;
#     }
    
#     .prize::after {
#         content: "🎁";
#         position: absolute;
#         right: 1rem;
#         font-size: 2rem;
#         filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
#         animation: float 3s ease-in-out infinite 1.5s;
#     }
    
#     /* Inputs - Larger for mobile */
#     .stTextInput label {
#         font-size: 1rem;
#         font-weight: 700;
#         margin-bottom: 0.5rem;
#     }
    
#     .stTextInput input {
#         font-size: 1.1rem;
#         padding: 1rem;
#         border-radius: 12px;
#         border: 2px solid var(--secondary-background-color);
#     }
    
#     .stTextInput input:focus {
#         border-color: #16a34a;
#         box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.2);
#     }
    
#     /* Selectbox - ULTRA AGGRESSIVE FIX for dark mode visibility */
#     .stSelectbox label {
#         font-size: 1rem;
#         font-weight: 700;
#         margin-bottom: 0.5rem;
#         color: var(--text-color) !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] > div {
#         font-size: 1.1rem;
#         padding: 1rem;
#         border-radius: 12px;
#         background-color: var(--secondary-background-color) !important;
#     }
    
#     /* NUCLEAR OPTION - Force ALL text in selectbox to be visible */
#     .stSelectbox * {
#         color: var(--text-color) !important;
#     }
    
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
    
#     /* Selected value container - ALL VARIATIONS */
#     .stSelectbox [data-baseweb="select"] [class*="singleValue"],
#     .stSelectbox [data-baseweb="select"] [class*="SingleValue"],
#     .stSelectbox [data-baseweb="select"] [class*="single-value"],
#     .stSelectbox [data-baseweb="select"] [class*="placeholder"] {
#         color: var(--text-color) !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] [class*="value"],
#     .stSelectbox [data-baseweb="select"] [class*="Value"] {
#         color: var(--text-color) !important;
#     }
    
#     /* Control container */
#     .stSelectbox [data-baseweb="select"] [class*="control"] {
#         background-color: var(--secondary-background-color) !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] [class*="control"] * {
#         color: var(--text-color) !important;
#     }
    
#     /* Value container - the actual displayed value */
#     .stSelectbox [data-baseweb="select"] [class*="valueContainer"],
#     .stSelectbox [data-baseweb="select"] [class*="value-container"] {
#         color: var(--text-color) !important;
#     }
    
#     .stSelectbox [data-baseweb="select"] [class*="valueContainer"] *,
#     .stSelectbox [data-baseweb="select"] [class*="value-container"] * {
#         color: var(--text-color) !important;
#     }
    
#     /* Dropdown menu options - CRITICAL + larger */
#     .stSelectbox [data-baseweb="popover"] {
#         z-index: 999999 !important;
#     }
    
#     .stSelectbox li[role="option"] {
#         color: var(--text-color) !important;
#         background: var(--background-color) !important;
#         font-size: 1.1rem !important;
#         padding: 1rem !important;
#     }
    
#     .stSelectbox li[role="option"]:hover {
#         background: rgba(22, 163, 74, 0.1) !important;
#     }
    
#     .stSelectbox li[role="option"][aria-selected="true"] {
#         background: rgba(22, 163, 74, 0.15) !important;
#         font-weight: 700 !important;
#     }
    
#     /* Additional selectbox select element styling */
#     .stSelectbox > div > div > select {
#         font-size: 1rem !important;
#         padding: 0.75rem !important;
#         border-radius: 8px !important;
#         color: var(--text-color) !important;
#     }
    
#     .stSelectbox > div > div > select option {
#         color: var(--text-color) !important;
#         background: var(--background-color) !important;
#     }
    
#     /* Expander - Larger */
#     .streamlit-expanderHeader {
#         font-size: 1rem;
#         font-weight: 700;
#         padding: 0.75rem 1rem;
#         border-radius: 12px;
#     }
    
#     .streamlit-expanderContent {
#         padding: 1rem;
#     }
    
#     /* Welcome - Larger and more exciting */
#     .welcome {
#         text-align: center;
#         padding: 2rem 1rem;
#     }
    
#     .welcome h1 {
#         font-size: 2rem;
#         font-weight: 900;
#         background: linear-gradient(135deg, #dc2626, #16a34a);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         background-clip: text;
#         margin: 1rem 0 0.75rem 0;
#         letter-spacing: -0.5px;
#     }
    
#     .welcome p {
#         font-size: 1rem;
#         color: var(--text-color);
#         opacity: 0.8;
#         margin-bottom: 2rem;
#         font-weight: 500;
#         line-height: 1.5;
#     }
    
#     .welcome .emoji {
#         font-size: 6rem;
#         animation: float 3s ease-in-out infinite;
#         filter: drop-shadow(0 8px 16px rgba(0,0,0,0.3));
#         display: inline-block;
#         transform-style: preserve-3d;
#     }
    
#     .welcome .emoji:hover {
#         animation: bounce 0.8s ease;
#     }
    
#     /* Tree icon in top bar - larger */
#     .tree-icon {
#         font-size: 1.5rem;
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
#         animation: bounce 2s ease-in-out infinite;
#     }
    
#     /* Quiz title icon enhancement */
#     .quiz-title::before {
#         content: "✨ ";
#         font-size: 1.5rem;
#         filter: drop-shadow(0 2px 4px rgba(22, 163, 74, 0.3));
#     }
    
#     /* Prize banner emojis */
#     .prize::before,
#     .prize::after {
#         filter: drop-shadow(0 4px 8px rgba(0,0,0,0.2));
#     }
    
#     /* Celebration - Larger and more exciting */
#     .celebration {
#         background: linear-gradient(135deg, #dc2626, #16a34a);
#         border-radius: 16px;
#         padding: 1.5rem;
#         text-align: center;
#         margin-top: 1rem;
#         position: relative;
#         overflow: hidden;
#         box-shadow: 0 8px 24px rgba(0,0,0,0.3);
#     }
    
#     .celebration::before {
#         content: "🎉";
#         position: absolute;
#         top: 1rem;
#         left: 1rem;
#         font-size: 2.5rem;
#         filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
#         animation: float 3s ease-in-out infinite;
#     }
    
#     .celebration::after {
#         content: "🎊";
#         position: absolute;
#         top: 1rem;
#         right: 1rem;
#         font-size: 2.5rem;
#         filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
#         animation: float 3s ease-in-out infinite 1.5s;
#     }
    
#     .celebration h3 {
#         font-size: 1.5rem;
#         color: white;
#         margin-bottom: 0.75rem;
#         filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
#         font-weight: 900;
#     }
    
#     .celebration p {
#         font-size: 1rem;
#         color: rgba(255,255,255,0.95);
#         margin: 0.5rem 0;
#         font-weight: 600;
#     }
    
#     /* Form spacing */
#     .stForm {
#         margin-bottom: 0;
#     }
    
#     /* Reduce all spacing */
#     div[data-testid="stVerticalBlock"] > div {
#         gap: 0.75rem;
#     }
    
#     /* Info/Success/Error boxes - larger */
#     .stAlert {
#         padding: 0.75rem;
#         font-size: 1rem;
#         border-radius: 12px;
#         margin: 0.5rem 0;
#     }
    
#     /* Slider - larger */
#     .stSlider {
#         padding: 0.5rem 0;
#     }
    
#     .stSlider label {
#         font-size: 1rem;
#         font-weight: 700;
#     }
    
#     /* Checkbox - larger */
#     .stCheckbox label {
#         font-size: 1rem;
#         font-weight: 600;
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
#     "Central Office"
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
#             {"label": "Initiatives", "value": "209"},
#             {"label": "Number of Green Champions", "value": "9"}
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
#         "description": "Through digitisation initiatives, we've dramatically reduced paper consumption while improving efficiency. In the last 4 months:",
#         "stats": [
#             {"label": "Trees Saved", "value": "1"},
#             {"label": "Paper Saved", "value": "11k"},
#             {"label": "Cost Savings", "value": "£110"}
#         ],
#         "quiz": {
#             "question": "How much paper have we saved in the last 4 months?",
#             "options": ["11k", "6k", "3.5k", "2k"],
#             "correct": "11k"
#         }
#     },
#     {
#         "day": 3,
#         "title": "Removing Single Use Plastics",
#         "subtitle": "Bulk Toiletries",
#         "emoji": "🧼",
#         "color": "#f59e0b",
#         "description": "Using bulk toiletries in guest bedrooms",
#         "stats": [
#             {"label": "Number of Properties Using Bulk Amentities (Voco Included)", "value": "100%"},
#             {"label": "Single Use Plastic Bottles Saved In One Month", "value": "70,000"},
#             {"label": "of Bottles Replaced", "value": "94%"},


#         ],
#         "quiz": {
#             "question": "How many single use plastic bottles have we saved in one month?",
#             "options": ["70,000", "95,000", "60,000", "30,000"],
#             "correct": "70,000"
#         }
#     },
#     {
#         "day": 4,
#         "title": "Recycling Revolution",
#         "subtitle": "Record Performance",
#         "emoji": "♻️",
#         "color": "#059669",
#         "description": "Improved from 37% to 48% year on year (YoY) through enhanced programs and team engagement.",
#         "stats": [
#             {"label": "Year on Year (YoY) Growth", "value": "+11%"},
#             {"label": "Oct Recycling Rate", "value": "51%"},
#             {"label": "Tonnes Recycled in 2025", "value": "227"}
#         ],
#         "quiz": {
#             "question": "What was our year on year recycling improvement?",
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
#         "description": "Strategic energy management delivering significant cost savings while reducing environmental impact. See data compared to last year.",
#         "stats": [
#             {"label": "Cost Savings", "value": "£137K"},
#             {"label": "kWh Reduced", "value": " 1,068,745.90"},
#             {"label": "Property that Reduced the Most Compared to Their Previous Year Performance", "value": "CIE"}
#         ],
#         "quiz": {
#             "question": "Which property saved the most energy compared to their prior year performance?",
#             "options": ["CIE", "EH", "Westin", "St Albans"],
#             "correct": "CIE"
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
#             {"label": "Litres Saved", "value": "1.24M"},
#             {"label": "", "Properties Have Low Flow Rate Showers and Taps": "6/7"},
#             {"label": "Reduction", "value": "2%"}
#         ],
#         "quiz": {
#             "question": "How many litres of water did we save?",
#             "options": ["1.5M", "1.24M", "2.8M", "3.2M"],
#             "correct": "1.24M"
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
#             {"label": "Waste Reduced", "value": "14%"},
#             {"label": "Equivalent of Meals Saved From Reduction", "value": "3,502"},
#             {"label": "Equivalent of Cost Savings From Reduction", "value": "£7,004"}
#         ],
#         "quiz": {
#             "question": "How many meals were saved from waste?",
#             "options": ["2,205", "3,502", "4,104", "5,320"],
#             "correct": "3,502"
#         }
#     },
#     {
#         "day": 8,
#         "title": "Upcycling",
#         "subtitle": "Reusing Materials",
#         "emoji": "🛍️",
#         "color": "#8b5cf6",
#         "description": "Upcycling materials and finding them a new home. We've made 92 items available since Jan 2025 via the 4C marketplace.",
#         "stats": [
#             {"label": "Number of items we've given away since January", "value": "42"},
#             {"label": "Number of items currently available on the 4C marketplace", "value": "50"},
#             {"label": "Cost of Items available on Our Marketplace (All Donated to a Charity!)", "value": "£1-£5"},

#                             ],
#         "quiz": {
#             "question": "Which types of items do we have on our marketplace?",
#             "options": ["Books", "Lamps", "Kindles", "All of the above"],
#             "correct": "All of the above"
#         }
#     },
#     {
#         "day": 9,
#         "title": "Becoming More Sustainable",
#         "subtitle": "Building Awareness",
#         "emoji": "📚",
#         "color": "#ec4899",
#         "description": "Comprehensive sustainability training empowering team members as change agents.",
#         "stats": [
#             {"label": "No of Hotels Have Introduced No Bin Day in Staff Canteens", "value": "3"},
#             {"label": "No of Official Flow Sustainability Courses", "value": "3"}
#         ],
#         "quiz": {
#             "question": "What everyday mindful behaviours have our team members adopted as a result of our sustainability efforts?",
#             "options": ["Being more intentional about reducing and managing waste", "Sorting waste correctly and more consistently", "Encouraging others by sharing sustainability tips and knowledge", "All of the above"],
#             "correct": "All of the above"
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
#             {"label": "CO₂ Reduced", "value": "142.26T"},
#             {"label": "Reduction", "value": "6%"},
#                     {"label": "Priority Sustainable Development Goals We Support", "value": "8"}        ],
#         "quiz": {
#             "question": "How much did we reduce our carbon footprint?",
#             "options": ["0%", "2%", "12%", "6%"],
#             "correct": "6%"
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
#             {"label": "Partnerships", "value": "30"},
#             {"label": "Donated", "value": "£75k"},
#             {"label": "Volunteered", "value": "94"}
#         ],
#         "quiz": {
#             "question": "How many community partnerships did we establish?",
#             "options": ["12", "18", "24", "30"],
#             "correct": "30"
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
#             {"label": "Donated", "value": "£75k"},
#             {"label": "Initiatives", "value": "251"},
#             {"label": "Team Pride", "value": "100%"}
#         ],
#         "quiz": {
#             "question": "How much money did we contribute to charitable causes?",
#             "options": ["£75K", "£18K", "£42K", "£53K"],
#             "correct": "£75K"
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

# def log_user_registration(client, name, property_name):
#     """Log user registration to the '12 Days' sheet with Date, name, property"""
#     try:
#         # Open the spreadsheet by ID from the URL
#         spreadsheet_id = "14gjZTmx63ffN1JZX5q8y8a9Sq6iv5ZhVnnU5fM71ujo"
#         spreadsheet = client.open_by_key(spreadsheet_id)
        
#         # Get the "12 Days" worksheet
#         worksheet = spreadsheet.worksheet("12 Days")
        
#         # Prepare the row: Date, name, property
#         row = [
#             datetime.now().strftime("%Y-%m-%d"),  # Date in YYYY-MM-DD format
#             name,
#             property_name
#         ]
        
#         # Append the row to the sheet
#         worksheet.append_row(row)
#         return True
#     except Exception as e:
#         st.error(f"Error logging to Google Sheets: {str(e)}")
#         return False

# def log_to_sheets(client, data):
#     """Log quiz responses to the 'Quiz Responses' tab"""
#     try:
#         # Open the spreadsheet by ID
#         spreadsheet_id = "14gjZTmx63ffN1JZX5q8y8a9Sq6iv5ZhVnnU5fM71ujo"
#         spreadsheet = client.open_by_key(spreadsheet_id)
        
#         # Try to get or create the "Quiz Responses" worksheet
#         try:
#             worksheet = spreadsheet.worksheet("Quiz Responses")
#         except:
#             # If worksheet doesn't exist, create it with headers
#             worksheet = spreadsheet.add_worksheet(title="Quiz Responses", rows="1000", cols="10")
#             headers = [
#                 "Timestamp",
#                 "Date", 
#                 "Name",
#                 "Property",
#                 "Day",
#                 "Achievement",
#                 "Question",
#                 "Their Answer",
#                 "Correct Answer",
#                 "Result"
#             ]
#             worksheet.append_row(headers)
        
#         # Prepare the row with quiz response data
#         row = [
#             datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp
#             datetime.now().strftime("%Y-%m-%d"),            # Date
#             data["name"],
#             data["property"],
#             data["day"],
#             data["achievement"],
#             data["question"],
#             data["selected_answer"],
#             data["correct_answer"],
#             "Correct" if data["is_correct"] else "Incorrect"
#         ]
        
#         worksheet.append_row(row)
#         return True
#     except Exception as e:
#         # Log error but don't crash the app
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
    
#     # Add falling snowflakes background ❄️
#     st.markdown("""
#     <div class="snowflakes" aria-hidden="true">
#         <div class="snowflake">❄</div>
#         <div class="snowflake">❅</div>
#         <div class="snowflake">❆</div>
#         <div class="snowflake">❄</div>
#         <div class="snowflake">❅</div>
#         <div class="snowflake">❆</div>
#         <div class="snowflake">❄</div>
#         <div class="snowflake">❅</div>
#         <div class="snowflake">❆</div>
#         <div class="snowflake">❄</div>
#         <div class="snowflake">❅</div>
#         <div class="snowflake">❆</div>
#         <div class="snowflake">❄</div>
#         <div class="snowflake">❅</div>
#         <div class="snowflake">❆</div>
#         <div class="snowflake">❄</div>
#         <div class="snowflake">❅</div>
#         <div class="snowflake">❆</div>
#         <div class="snowflake">❄</div>
#         <div class="snowflake">❅</div>
#     </div>
#     """, unsafe_allow_html=True)
    
#     # Welcome Screen
#     if st.session_state.user_name is None or st.session_state.user_property is None:
#         st.markdown("""
#         <div class="welcome">
#             <div class="emoji">🎄</div>
#             <h1>12 Days of Sustainability</h1>
#             <p>Celebrating Our 2025 Achievements<br>December 1-12, 2025</p>
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
                    
#                     # Log user registration to Google Sheets
#                     try:
#                         client = setup_google_sheets()
#                         if client:
#                             log_user_registration(client, name.strip(), property_select)
#                     except Exception as e:
#                         pass  # Continue even if logging fails
                    
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
#             index=None,  # No pre-selection - user must choose!
#             key=f"quiz_{current_day}",
#             label_visibility="collapsed"
#         )
        
#         if st.button("🎯 Submit Answer", type="primary", use_container_width=True):
#             if selected is None:
#                 st.error("⚠️ Please select an answer before submitting!")
#             else:
#                 is_correct = selected == current_achievement['quiz']['correct']
#                 st.session_state.quiz_result = {'answer': selected, 'correct': is_correct}
#                 st.session_state.quiz_submitted = True
#                 st.session_state.completed_days.append(current_day)
                
#                 # Log quiz response to Google Sheets
#                 try:
#                     client = setup_google_sheets()
#                     if client:
#                         data = {
#                             "name": st.session_state.user_name,
#                             "property": st.session_state.user_property,
#                             "day": current_day,
#                             "achievement": current_achievement['title'],
#                             "question": current_achievement['quiz']['question'],
#                             "selected_answer": selected,
#                             "correct_answer": current_achievement['quiz']['correct'],
#                             "is_correct": is_correct
#                         }
#                         log_to_sheets(client, data)
#                 except:
#                     pass  # Continue even if logging fails
                
#                 st.rerun()
    
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
    page_title="12 Days of Sustainability Hotel Competition",
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
    
    /* Selectbox - ULTRA AGGRESSIVE FIX for dark mode visibility */
    .stSelectbox label {
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: var(--text-color) !important;
    }
    
    .stSelectbox [data-baseweb="select"] > div {
        font-size: 1.1rem;
        padding: 1rem;
        border-radius: 12px;
        background-color: var(--secondary-background-color) !important;
    }
    
    /* NUCLEAR OPTION - Force ALL text in selectbox to be visible */
    .stSelectbox * {
        color: var(--text-color) !important;
    }
    
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
    
    /* Selected value container - ALL VARIATIONS */
    .stSelectbox [data-baseweb="select"] [class*="singleValue"],
    .stSelectbox [data-baseweb="select"] [class*="SingleValue"],
    .stSelectbox [data-baseweb="select"] [class*="single-value"],
    .stSelectbox [data-baseweb="select"] [class*="placeholder"] {
        color: var(--text-color) !important;
    }
    
    .stSelectbox [data-baseweb="select"] [class*="value"],
    .stSelectbox [data-baseweb="select"] [class*="Value"] {
        color: var(--text-color) !important;
    }
    
    /* Control container */
    .stSelectbox [data-baseweb="select"] [class*="control"] {
        background-color: var(--secondary-background-color) !important;
    }
    
    .stSelectbox [data-baseweb="select"] [class*="control"] * {
        color: var(--text-color) !important;
    }
    
    /* Value container - the actual displayed value */
    .stSelectbox [data-baseweb="select"] [class*="valueContainer"],
    .stSelectbox [data-baseweb="select"] [class*="value-container"] {
        color: var(--text-color) !important;
    }
    
    .stSelectbox [data-baseweb="select"] [class*="valueContainer"] *,
    .stSelectbox [data-baseweb="select"] [class*="value-container"] * {
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
    
    /* Additional selectbox select element styling */
    .stSelectbox > div > div > select {
        font-size: 1rem !important;
        padding: 0.75rem !important;
        border-radius: 8px !important;
        color: var(--text-color) !important;
    }
    
    .stSelectbox > div > div > select option {
        color: var(--text-color) !important;
        background: var(--background-color) !important;
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
TEST_MODE_DEFAULT = False  # Production mode - app will go live on Dec 1, 2025

# Properties list
PROPERTIES = [
    "Camden",
    "St Albans",
    "Westin",
    "Canopy",
    "CIE",
    "CIV",
    "EH",
    "Central Office"
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
        "description": "Improved from 37% to 48% year on year (YoY) through enhanced programs and team engagement.",
        "stats": [
            {"label": "Year on Year (YoY) Growth", "value": "+11%"},
            {"label": "Oct Recycling Rate", "value": "51%"},
            {"label": "Tonnes Recycled in 2025", "value": "227"}
        ],
        "quiz": {
            "question": "What was our year on year recycling improvement?",
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
            {"label": "Property that Reduced the Most Compared to Their Previous Year Performance", "value": "CIE"}
        ],
        "quiz": {
            "question": "Which property saved the most energy compared to their prior year performance?",
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
            {"label": "Litres Saved", "value": "1.24M"},
            {"label": "", "Properties Have Low Flow Rate Showers and Taps": "6/7"},
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
            {"label": "Waste Reduced", "value": "14%"},
            {"label": "Equivalent of Meals Saved From Reduction", "value": "3,502"},
            {"label": "Equivalent of Cost Savings From Reduction", "value": "£7,004"}
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
        "description": "Upcycling materials and finding them a new home. We've made 92 items available since Jan 2025 via the 4C marketplace.",
        "stats": [
            {"label": "Number of items we've given away since January", "value": "42"},
            {"label": "Number of items currently available on the 4C marketplace", "value": "50"},
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
        "stats": [
            {"label": "No of Hotels Have Introduced No Bin Day in Staff Canteens", "value": "3"},
            {"label": "No of Official Flow Sustainability Courses", "value": "3"}
        ],
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
            {"label": "Reduction", "value": "6%"},
                    {"label": "Priority Sustainable Development Goals We Support", "value": "8"}        ],
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
            {"label": "Donated", "value": "£75k"},
            {"label": "Volunteered", "value": "94"}
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
            {"label": "Donated", "value": "£75k"},
            {"label": "Initiatives", "value": "251"},
            {"label": "Team Pride", "value": "100%"}
        ],
        "quiz": {
            "question": "How much money did we contribute to charitable causes?",
            "options": ["£75K", "£18K", "£42K", "£53K"],
            "correct": "£75K"
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

def log_user_registration(client, name, property_name):
    """Log user registration to the '12 Days' sheet with Date, name, property"""
    try:
        # Open the spreadsheet by ID from the URL
        spreadsheet_id = "14gjZTmx63ffN1JZX5q8y8a9Sq6iv5ZhVnnU5fM71ujo"
        spreadsheet = client.open_by_key(spreadsheet_id)
        
        # Get the "12 Days" worksheet
        worksheet = spreadsheet.worksheet("12 Days")
        
        # Prepare the row: Date, name, property
        row = [
            datetime.now().strftime("%Y-%m-%d"),  # Date in YYYY-MM-DD format
            name,
            property_name
        ]
        
        # Append the row to the sheet
        worksheet.append_row(row)
        return True
    except Exception as e:
        st.error(f"Error logging to Google Sheets: {str(e)}")
        return False

def log_to_sheets(client, data):
    """Log quiz responses to the 'Quiz Responses' tab"""
    try:
        # Open the spreadsheet by ID
        spreadsheet_id = "14gjZTmx63ffN1JZX5q8y8a9Sq6iv5ZhVnnU5fM71ujo"
        spreadsheet = client.open_by_key(spreadsheet_id)
        
        # Try to get or create the "Quiz Responses" worksheet
        try:
            worksheet = spreadsheet.worksheet("Quiz Responses")
        except:
            # If worksheet doesn't exist, create it with headers
            worksheet = spreadsheet.add_worksheet(title="Quiz Responses", rows="1000", cols="10")
            headers = [
                "Timestamp",
                "Date", 
                "Name",
                "Property",
                "Day",
                "Achievement",
                "Question",
                "Their Answer",
                "Correct Answer",
                "Result"
            ]
            worksheet.append_row(headers)
        
        # Prepare the row with quiz response data
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp
            datetime.now().strftime("%Y-%m-%d"),            # Date
            data["name"],
            data["property"],
            data["day"],
            data["achievement"],
            data["question"],
            data["selected_answer"],
            data["correct_answer"],
            "Correct" if data["is_correct"] else "Incorrect"
        ]
        
        worksheet.append_row(row)
        return True
    except Exception as e:
        # Log error but don't crash the app
        return False

def calculate_current_day():
    if st.session_state.test_mode:
        return st.session_state.test_day
    
    today = datetime.now()
    if today < CAMPAIGN_START_DATE:
        return None  # Campaign hasn't started yet
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
    
    # Add falling snowflakes background ❄️
    st.markdown("""
    <div class="snowflakes" aria-hidden="true">
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
            <h1>12 Days of Sustainability Hotel Competition</h1>
            <p>Celebrating Our 2025 Achievements<br>December 1-12, 2025</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Check if campaign has started
        today = datetime.now()
        if today < CAMPAIGN_START_DATE:
            # Show coming soon message - no form access
            st.markdown("""
            <div class="card" style="text-align: center; padding: 2rem; margin-top: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎄</div>
                <h2 style="color: var(--text-color); margin-bottom: 1rem;">Coming Soon!</h2>
                <p style="color: var(--text-color); font-size: 1.1rem; margin-bottom: 0.5rem;">
                    The 12 Days of Sustainability campaign starts on:
                </p>
                <p style="color: #22c55e; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">
                    December 1, 2025
                </p>
                <p style="color: var(--text-color); opacity: 0.8; margin-bottom: 0.5rem;">
                    Check back on December 1st to begin your sustainability journey!
                </p>
                <p style="color: var(--text-color); opacity: 0.6; font-size: 0.9rem;">
                    🎁 Complete all 12 days to win a £25 Amazon Gift Card!
                </p>
            </div>
            """, unsafe_allow_html=True)
            return
        
        # Name and Property Form (only shown on/after Dec 1)
        with st.form("user_entry_form"):
            name = st.text_input("Your Name", placeholder="Enter your full name...")
            
            # Use TEXT INPUT for property - simple and always works
            property_input = st.text_input(
                "Your Property", 
                placeholder="Enter your property (e.g., Camden, St Albans, Westin...)"
            )
            
            submitted = st.form_submit_button("🎄 Start Journey", use_container_width=True, type="primary")
            
            if submitted:
                if name and name.strip() and property_input and property_input.strip():
                    st.session_state.user_name = name.strip()
                    st.session_state.user_property = property_input.strip()
                    
                    # Log user registration to Google Sheets
                    try:
                        client = setup_google_sheets()
                        if client:
                            log_user_registration(client, name.strip(), property_input.strip())
                    except Exception as e:
                        pass  # Continue even if logging fails
                    
                    st.rerun()
                else:
                    st.error("⚠️ Please enter your name and property")
        
        return
    
    # Main App
    current_day = calculate_current_day()
    
    # This should not happen since we check before login, but just in case
    if current_day is None:
        st.error("Campaign hasn't started yet. Please check back on December 1, 2025.")
        return
    
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
            # Different message for Day 12
            if current_day == 12:
                completion_msg = "🎉 You've completed all 12 Days of Sustainability!"
            else:
                completion_msg = f"See you tomorrow for Day {current_day + 1}!"
            
            st.markdown(f"""
            <div class="result result-correct">
                <h4>✓ CORRECT! Well Done! 🎉</h4>
                <p>Your answer <strong>"{result['answer']}"</strong> is correct!</p>
                <p style="margin-top: 0.5rem; font-size: 0.9rem;">✅ Day {current_day} complete! {completion_msg}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Different message for Day 12
            if current_day == 12:
                completion_msg = "🎉 You've completed all 12 Days of Sustainability!"
            else:
                completion_msg = f"See you tomorrow for Day {current_day + 1}!"
            
            st.markdown(f"""
            <div class="result result-incorrect">
                <h4>Not quite, but great effort! 💪</h4>
                <p>You answered: <strong>"{result['answer']}"</strong></p>
                <p>The correct answer is: <strong>"{current_achievement['quiz']['correct']}"</strong></p>
                <p style="margin-top: 0.5rem; font-size: 0.9rem;">✅ Day {current_day} complete! {completion_msg}</p>
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
                
                # Log quiz response to Google Sheets
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
                    pass  # Continue even if logging fails
                
                st.rerun()
    
    # Show "already completed" message
    else:
        # Don't say "come back tomorrow" on Day 12
        if current_day < 12:
            st.markdown(f"""
            <div class="result result-completed">
                <h4>Day {current_day} Complete!</h4>
                <p>You've finished today's quiz.</p>
                <p>Come back tomorrow for Day {current_day + 1}!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result result-completed">
                <h4>Day {current_day} Complete!</h4>
                <p>You've finished today's quiz.</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Celebration
    if len(st.session_state.completed_days) == 12:
        st.balloons()
        st.markdown(f"""
        <div class="celebration">
            <h3>🎉 Congratulations {st.session_state.user_name}! 🎉</h3>
            <p style="font-size: 1.1rem; font-weight: 600;">You completed all 12 Days of Sustainability!</p>
            <p style="margin-top: 1rem; font-size: 1rem;">
                🎁 You've earned your £25 Amazon Gift Card! 🎁
            </p>
            <p style="margin-top: 1rem; font-size: 0.95rem; padding: 1rem; background: rgba(34, 197, 94, 0.1); border-radius: 8px; border-left: 4px solid #22c55e;">
                <strong>🏆 Special Prize Draw:</strong><br>
                We will be awarding an additional prize to the team member who completed all 12 days and achieved the highest score!
            </p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()