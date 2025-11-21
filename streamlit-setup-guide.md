# Streamlit Advent Calendar - Complete Setup Guide

## 📦 What You Get

A beautiful, interactive Streamlit dashboard that:
- ✅ Unlocks one achievement per day
- ✅ Tracks user progress with name entry
- ✅ Daily quiz with immediate feedback
- ✅ Logs all responses to Google Sheets
- ✅ Responsive design with festive styling
- ✅ Progress tracking sidebar
- ✅ Completion celebration with balloons!

---

## 🚀 Quick Start (5 Steps)

### Step 1: Set Up Google Sheets Integration

#### 1.1 Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "New Project"
3. Name it: "Christmas Dashboard API"
4. Click "Create"

#### 1.2 Enable Google Sheets API
1. In your project, go to "APIs & Services" → "Library"
2. Search for "Google Sheets API"
3. Click it and press "Enable"

#### 1.3 Create Service Account
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "Service Account"
3. Name: "christmas-dashboard"
4. Click "Create and Continue"
5. Skip the optional steps
6. Click "Done"

#### 1.4 Generate Key
1. Click on the service account you just created
2. Go to "Keys" tab
3. Click "Add Key" → "Create new key"
4. Choose "JSON"
5. Click "Create" - a JSON file will download
6. **Keep this file safe!**

#### 1.5 Create Google Sheet
1. Create a new Google Sheet
2. Name it: "12 Days Christmas Quiz Responses"
3. Click "Share" button
4. Paste the service account email (from JSON: `client_email`)
5. Give it "Editor" access
6. Click "Send"

### Step 2: Configure Your Streamlit App

#### 2.1 Create Project Structure
```
christmas-dashboard/
├── advent_calendar_streamlit.py
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
└── .gitignore
```

#### 2.2 Set Up Secrets
1. Create `.streamlit` folder in your project
2. Copy `secrets.toml.template` to `.streamlit/secrets.toml`
3. Open the JSON file you downloaded
4. Copy all fields into `secrets.toml`:

```toml
[gcp_service_account]
type = "service_account"
project_id = "your-project-123456"
private_key_id = "abc123..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "christmas-dashboard@your-project.iam.gserviceaccount.com"
client_id = "123456789"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/..."
```

#### 2.3 Create .gitignore
```
.streamlit/secrets.toml
*.json
__pycache__/
.env
```

### Step 3: Configure Campaign Dates

Open `advent_calendar_streamlit.py` and find these lines (around line 223):

```python
# Configuration
CAMPAIGN_START_DATE = datetime(2024, 12, 1)
CAMPAIGN_END_DATE = datetime(2024, 12, 12)
```

Change to your desired dates:
```python
CAMPAIGN_START_DATE = datetime(2024, 12, 1)  # Your start date
CAMPAIGN_END_DATE = datetime(2024, 12, 12)   # 12 days later
```

Also update the Google Sheet name (line 273):
```python
sheet_name = "12 Days Christmas Quiz Responses"  # Your sheet name
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run Locally to Test

```bash
streamlit run advent_calendar_streamlit.py
```

App should open at `http://localhost:8501`

---

## 🌐 Deploy to Streamlit Cloud (FREE)

### Option 1: Deploy from GitHub

#### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/christmas-dashboard.git
git push -u origin main
```

**Important:** Make sure `.gitignore` excludes `secrets.toml`!

#### 2. Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub repo
4. Select your repository and main file
5. Click "Deploy"

#### 3. Add Secrets
1. In Streamlit Cloud, go to app settings
2. Click "Secrets" in sidebar
3. Paste contents of your `secrets.toml` file
4. Click "Save"

Your app is now live! 🎉

---

## 📊 Google Sheets Data Structure

After first submission, your sheet will have these columns:

| Column | Description | Example |
|--------|-------------|---------|
| Timestamp | Exact submission time | 2024-12-01 10:30:45 |
| Name | User's name | Sarah Jones |
| Day | Day number (1-12) | 1 |
| Achievement | Achievement title | Green Champions Programme |
| Question | Quiz question | How many properties... |
| Selected Answer | User's choice | 12 |
| Correct Answer | Right answer | 12 |
| Is Correct | Yes/No | Yes |
| Date Submitted | Date only | 2024-12-01 |

---

## 🎨 Customization Guide

### Change Colors

Each achievement has a color property (line 229+):
```python
"color": "#10b981",  # Green
```

Available colors:
- `#10b981` - Green
- `#3b82f6` - Blue  
- `#f59e0b` - Amber/Gold
- `#ef4444` - Red
- `#a855f7` - Purple
- `#06b6d4` - Cyan
- `#f97316` - Orange

### Update Achievement Content

Edit the `ACHIEVEMENTS` array (starting line 229):
```python
{
    "day": 1,
    "title": "Your Title",
    "subtitle": "Your Subtitle",
    "emoji": "🎯",  # Any emoji
    "color": "#10b981",
    "metric": "150+",
    "metric_label": "Your Metric",
    "description": "Your description...",
    "stats": [
        {"label": "Stat 1", "value": "123"},
        {"label": "Stat 2", "value": "456"},
        {"label": "Stat 3", "value": "789"}
    ],
    "quiz": {
        "question": "Your question?",
        "options": ["A", "B", "C", "D"],
        "correct": "B"
    }
}
```

### Add More Days

To extend beyond 12 days:
1. Add more entries to `ACHIEVEMENTS` array
2. Update completion logic (change `12` to your number)
3. Adjust `CAMPAIGN_END_DATE` accordingly

---

## 🔧 Troubleshooting

### Issue: "Error connecting to Google Sheets"

**Solutions:**
1. Check service account email is in `secrets.toml`
2. Verify sheet is shared with service account
3. Confirm sheet name matches exactly
4. Check all fields in secrets.toml are properly formatted

**Test connection:**
```python
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

credentials_dict = st.secrets["gcp_service_account"]
scope = ["https://spreadsheets.google.com/feeds", 
         "https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_info(credentials_dict, scopes=scope)
client = gspread.authorize(credentials)

# Try to open sheet
sheet = client.open("12 Days Christmas Quiz Responses")
print("✅ Connection successful!")
```

### Issue: Wrong day showing

**Check:**
1. System clock is correct
2. Dates in code are correct format: `datetime(2024, 12, 1)`
3. Timezone considerations (uses local time)

**For testing, temporarily set:**
```python
CAMPAIGN_START_DATE = datetime(2024, 1, 1)  # Past date
CAMPAIGN_END_DATE = datetime(2025, 12, 31)  # Future date
```

### Issue: Session state lost on refresh

This is normal Streamlit behavior. Users need to:
- Keep browser tab open
- Or re-enter name (progress is tracked in sheets)

**To persist across sessions, add:**
```python
import pickle
# Save state to file
# Load on startup
```

### Issue: Slow loading

**Optimize:**
1. Cache Google Sheets connection:
```python
@st.cache_resource
def get_sheets_client():
    # connection code
    return client
```

2. Reduce API calls - only log on submit

---

## 📱 Mobile Optimization

The app is mobile-responsive, but for best experience:

1. Use columns for mobile layout
2. Reduce font sizes on small screens
3. Stack elements vertically

Add to CSS:
```python
@media (max-width: 768px) {
    .big-title {
        font-size: 2rem !important;
    }
}
```

---

## 🎯 Launch Checklist

Before going live:

- [ ] Google Sheets integration working
- [ ] Service account has access to sheet
- [ ] Campaign dates configured correctly
- [ ] All quiz questions/answers verified
- [ ] Tested on mobile device
- [ ] Secrets NOT committed to Git
- [ ] Achievement content finalized
- [ ] Color scheme approved
- [ ] Test user journey completed
- [ ] Google Sheet headers created
- [ ] Deployment tested on Streamlit Cloud

---

## 📧 Communications Template

### Pre-Launch Email
```
Subject: 🎄 Get Ready: 12 Days of Sustainability Starts [DATE]!

Hi Team,

Starting [DATE], we're launching our 12 Days of Sustainability advent calendar!

📅 How It Works:
• One new achievement unlocks each day
• Complete a quick quiz (2 minutes)
• Track your progress
• Celebrate our 2024 wins together

🎁 Day 1 unlocks on [DATE] at midnight

Bookmark this link now: [YOUR-APP-URL]

See you on Day 1!
[Your Name]
```

### Daily Reminder
```
Subject: 🌟 Day [X] is Live: [Achievement Title]

Good morning!

Day [X] of our 12 Days of Sustainability is now available!

Today: [Achievement Title]
[Brief description in one line]

⏱️ Takes 2 minutes:
✅ Read about our impact
✅ Answer today's quiz
✅ Keep your streak alive

Visit: [YOUR-APP-URL]

Current participants: [X] 
Keep up the momentum! 🚀
```

---

## 📊 Analytics & Reporting

### View Data in Google Sheets

**Simple Formulas:**

**Count total participants:**
```
=COUNTA(UNIQUE(B2:B1000))
```

**Today's participation:**
```
=COUNTIF(I2:I1000,TODAY())
```

**Accuracy rate:**
```
=COUNTIF(H2:H1000,"Yes")/COUNTA(H2:H1000)*100
```

**Day completion rates:**
```
=COUNTIF(C2:C1000,1)  // Count Day 1 completions
```

### Create Dashboard in Google Sheets

1. Create new sheet "Dashboard"
2. Add formulas for key metrics
3. Create charts:
   - Daily participation (line chart)
   - Completion by day (bar chart)
   - Accuracy by question (column chart)

---

## 🎓 Advanced Features

### Add Email Notifications

Install: `pip install sendgrid`

```python
import sendgrid
from sendgrid.helpers.mail import Mail

def send_notification(user_email, day):
    message = Mail(
        from_email='noreply@yourcompany.com',
        to_emails=user_email,
        subject=f'Congrats on completing Day {day}!',
        html_content=f'<strong>Well done!</strong>'
    )
    sg = sendgrid.SendGridAPIClient(st.secrets["sendgrid_api_key"])
    response = sg.send(message)
```

### Add Leaderboard

```python
# At end of app
st.markdown("### 🏆 Leaderboard")
# Query Google Sheets for top participants
# Display in table
```

### Export Certificate

```python
from PIL import Image, ImageDraw, ImageFont

if len(st.session_state.completed_days) == 12:
    if st.button("Download Certificate"):
        # Generate certificate image
        # Offer download
```

---

## 🔐 Security Best Practices

1. **Never commit secrets.toml to Git**
2. **Rotate service account keys** every 90 days
3. **Use least privilege** - only enable Google Sheets API
4. **Monitor sheet access** - check for unauthorized edits
5. **Set up alerts** - for unusual activity

---

## 🆘 Support Resources

**Streamlit Docs:**
- [Documentation](https://docs.streamlit.io)
- [Community Forum](https://discuss.streamlit.io)

**Google Sheets API:**
- [gspread Documentation](https://docs.gspread.org)
- [Google Sheets API](https://developers.google.com/sheets/api)

**Deployment:**
- [Streamlit Cloud Guide](https://docs.streamlit.io/streamlit-community-cloud)

---

## ✨ Success Story Template

After your campaign:

```
📊 12 Days of Sustainability - Final Results

Participation:
• Total participants: [X]
• Completion rate: [X]%
• Total quiz attempts: [X]
• Average accuracy: [X]%

Top Performers:
1. [Name] - Perfect score!
2. [Name] - 11/12 days
3. [Name] - 11/12 days

Most Popular Achievement:
🏆 Day [X]: [Title] - [X]% engagement

Insights:
• Peak engagement on Day [X]
• Most challenging quiz: Day [X]
• [X]% improvement in sustainability awareness

Thank you for participating! 🌍
```

---

## 🎉 You're Ready!

Your Streamlit advent calendar is set up and ready to engage your team!

**Next Steps:**
1. Complete testing
2. Schedule launch communications
3. Monitor first few days closely
4. Celebrate success! 🎊

**Questions?** Check troubleshooting section or Streamlit docs.

**Good luck with your campaign!** 🎄🌍
