# 🎄 12 Days of Sustainability Dashboard - Complete Package

A beautiful advent calendar to celebrate your organization's sustainability achievements with daily unlocking, quizzes, and Google Sheets tracking.

---

## 📦 What's Included

You have **3 complete dashboard versions** to choose from:

### 1️⃣ React - All at Once Version
**Files:**
- `12-days-christmas-with-quiz.jsx`
- `google-apps-script-setup.js` (shared)
- `setup-guide.md`

**Best For:**
- Self-paced learning
- End-of-year reviews
- Flexible engagement
- Low maintenance

**How it works:** All 12 doors visible, users complete at their own pace

---

### 2️⃣ React - Daily Advent Calendar
**Files:**
- `advent-calendar-daily.jsx`
- `google-apps-script-setup.js` (shared)
- `daily-advent-setup-guide.md`

**Best For:**
- Sustained 12-day campaigns
- Building daily habits
- Maximum engagement
- True advent experience

**How it works:** One door unlocks per day based on date

---

### 3️⃣ Streamlit - Daily Advent Calendar ⭐ RECOMMENDED
**Files:**
- `advent_calendar_streamlit.py`
- `requirements.txt`
- `secrets.toml.template`
- `.gitignore`
- `streamlit-setup-guide.md`

**Best For:**
- Python/data teams
- Easy deployment
- Google Sheets integration
- Professional dashboards

**How it works:** One door per day, runs on Streamlit Cloud (FREE)

---

## 🎯 Quick Decision Guide

**Choose React (All at Once) if:**
- ✅ You want one-time engagement
- ✅ Users need flexibility to complete anytime
- ✅ You prefer minimal maintenance
- ✅ Content should be always available

**Choose React (Daily Advent) if:**
- ✅ You want sustained engagement over 12 days
- ✅ You're comfortable with React/JavaScript
- ✅ You have existing web hosting
- ✅ You want true advent calendar magic

**Choose Streamlit if:**
- ✅ You're comfortable with Python
- ✅ You want easiest deployment (Streamlit Cloud)
- ✅ You prefer Python ecosystem
- ✅ You want built-in session management

---

## 📋 Feature Comparison

| Feature | React All-at-Once | React Daily | Streamlit Daily |
|---------|-------------------|-------------|-----------------|
| **Setup Difficulty** | Medium | Medium | Easy |
| **Deployment** | Need web host | Need web host | FREE on Streamlit Cloud |
| **Daily Unlocking** | ❌ | ✅ | ✅ |
| **Name Entry** | ✅ | ✅ | ✅ |
| **Quiz Tracking** | ✅ | ✅ | ✅ |
| **Google Sheets** | ✅ Apps Script | ✅ Apps Script | ✅ Native API |
| **Progress Tracking** | ✅ | ✅ | ✅ Sidebar |
| **Mobile Friendly** | ✅ | ✅ | ✅ |
| **Customization** | High | High | Medium-High |
| **Tech Stack** | React/JSX | React/JSX | Python |

---

## 🚀 Getting Started

### For React Versions (1 & 2):

1. **Read the appropriate guide:**
   - All at once: `setup-guide.md`
   - Daily advent: `daily-advent-setup-guide.md`

2. **Set up Google Sheets:**
   - Follow instructions in `google-apps-script-setup.js`
   - Get your Web App URL

3. **Configure the dashboard:**
   - Add Google Script URL to React file
   - Customize content/dates
   - Deploy to your web host

### For Streamlit Version (3):

1. **Read the guide:**
   - `streamlit-setup-guide.md`

2. **Set up Google Cloud:**
   - Create service account
   - Download credentials
   - Share Google Sheet

3. **Configure secrets:**
   - Copy credentials to `.streamlit/secrets.toml`
   - Update campaign dates

4. **Deploy:**
   ```bash
   pip install -r requirements.txt
   streamlit run advent_calendar_streamlit.py
   ```

5. **Or deploy to Streamlit Cloud** (FREE!)

---

## 🎨 Key Features (All Versions)

### User Experience
- 🎁 Beautiful festive design
- 📝 Name entry and tracking
- 📊 Progress visualization
- ❓ Daily quiz questions
- ✅ Immediate feedback (correct/incorrect)
- 🎉 Completion celebration

### Data Tracking
- 📈 All responses logged to Google Sheets
- 👤 User names recorded
- 📅 Timestamps for each submission
- ✅ Accuracy tracking
- 📊 Easy to analyze and report

### Content
- 12 sustainability achievements
- Custom metrics and stats
- Quiz questions with 4 options
- Colorful, emoji-rich design
- Detailed descriptions

---

## 📂 File Structure

```
12-days-sustainability/
│
├── React Versions/
│   ├── 12-days-christmas-with-quiz.jsx       # All at once
│   ├── advent-calendar-daily.jsx              # Daily unlock
│   ├── google-apps-script-setup.js            # Backend (shared)
│   ├── setup-guide.md                         # All at once guide
│   └── daily-advent-setup-guide.md            # Daily guide
│
├── Streamlit Version/
│   ├── advent_calendar_streamlit.py           # Main app
│   ├── requirements.txt                       # Dependencies
│   ├── secrets.toml.template                  # Credentials template
│   ├── .gitignore                             # Git ignore rules
│   └── streamlit-setup-guide.md               # Setup guide
│
└── Documentation/
    ├── version-comparison-guide.md            # Detailed comparison
    └── README.md                              # This file
```

---

## 🎯 Typical Use Cases

### Scenario 1: Corporate Sustainability Report
**Recommendation:** Streamlit Daily
**Why:** Professional, easy to deploy, good for distributed teams

### Scenario 2: Internal Web Portal
**Recommendation:** React Daily
**Why:** Integrates with existing React infrastructure

### Scenario 3: One-Week Campaign
**Recommendation:** React All at Once
**Why:** Short timeframe, flexible completion

### Scenario 4: Remote Team Building
**Recommendation:** Streamlit Daily
**Why:** Daily touchpoints, easy access, no infrastructure needed

---

## 📊 Data Structure (All Versions)

Every quiz submission logs:

| Field | Example | Purpose |
|-------|---------|---------|
| Timestamp | 2024-12-01 10:30:45 | When submitted |
| Name | Sarah Jones | Who participated |
| Day | 1 | Which day (1-12) |
| Achievement | Green Champions | What achievement |
| Question | How many... | The question asked |
| Selected Answer | 12 | User's answer |
| Correct Answer | 12 | Right answer |
| Is Correct | Yes/No | Accuracy |
| Date | 2024-12-01 | Date only |

---

## 🛠️ Customization

### All Versions Support:

**Content Changes:**
- Achievement titles and descriptions
- Metrics and statistics
- Quiz questions and answers
- Emojis and colors

**Date Configuration:**
- Campaign start date
- Campaign end date
- Number of days (can extend beyond 12)

**Styling:**
- Color schemes
- Fonts and sizes
- Layout adjustments

**Functionality:**
- Add/remove achievements
- Change quiz format
- Modify tracking fields

---

## 📈 Success Metrics to Track

### Participation Metrics
- Total unique participants
- Completion rate (all 12 days)
- Daily engagement rate
- Drop-off by day

### Performance Metrics
- Average quiz accuracy
- Most/least popular days
- Peak engagement times
- Mobile vs desktop usage

### Impact Metrics
- Awareness increase
- Team engagement boost
- Sustainability knowledge growth

---

## 🎓 Support & Resources

### Documentation
- Each version has detailed setup guide
- Troubleshooting sections included
- Customization examples provided

### External Resources

**React:**
- [React Documentation](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com)

**Streamlit:**
- [Streamlit Docs](https://docs.streamlit.io)
- [Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud)

**Google Sheets:**
- [Apps Script Guide](https://developers.google.com/apps-script)
- [gspread Library](https://docs.gspread.org)

---

## ⚠️ Important Notes

### Security
- ✅ Never commit secrets/credentials to Git
- ✅ Use `.gitignore` (provided)
- ✅ Rotate API keys regularly
- ✅ Share sheets only with service accounts

### Testing
- ✅ Test with small group first
- ✅ Verify Google Sheets logging
- ✅ Check mobile responsiveness
- ✅ Test date logic thoroughly

### Launch
- ✅ Schedule communications
- ✅ Monitor first few days
- ✅ Have backup plan
- ✅ Celebrate successes!

---

## 🎉 Launch Checklist

Before going live:

- [ ] Version selected (React or Streamlit)
- [ ] Google Sheets configured
- [ ] Service account/Apps Script set up
- [ ] Campaign dates configured
- [ ] All content customized
- [ ] Quiz questions verified
- [ ] Tested on multiple devices
- [ ] Secrets properly secured
- [ ] Deployment tested
- [ ] Communications scheduled
- [ ] Analytics tracking ready
- [ ] Team briefed on campaign

---

## 💡 Pro Tips

1. **Start Small:** Test with 5-10 people before full launch

2. **Daily Reminders:** Send brief email each morning for Daily versions

3. **Celebrate Milestones:** Recognize participants at Day 6 (halfway!)

4. **Share Stats:** Post daily participation numbers to build momentum

5. **Follow Up:** Survey participants after Day 12 for feedback

6. **Repurpose Content:** Turn achievements into social media posts

7. **Archive It:** Keep as evergreen training resource

---

## 🤝 Contributing

Have improvements or found a bug?
- Submit issues or pull requests
- Share your customizations
- Help improve documentation

---

## 📄 License

These dashboards are provided as-is for internal organizational use.
Feel free to customize for your needs!

---

## 🌟 Examples & Inspiration

### Achievement Ideas
- Carbon reduction milestones
- Waste diversion successes
- Team volunteer hours
- Green initiative launches
- Sustainability certifications
- Energy savings
- Water conservation
- Local sourcing wins
- Employee engagement
- Community partnerships
- Innovation projects
- Future commitments

### Quiz Question Types
- **Multiple choice:** "How many X did we achieve?"
- **Comparative:** "Which initiative saved the most Y?"
- **True/False:** "Did we reduce waste by X%?"
- **Fill in blank:** "Our recycling rate improved by ___"

---

## 📞 Need Help?

**For Setup Issues:**
1. Check troubleshooting in respective guide
2. Verify all credentials are correct
3. Test each component individually

**For Customization:**
1. Start with small changes
2. Test after each modification
3. Keep backup of working version

**For Deployment:**
1. Follow platform-specific guides
2. Use provided templates
3. Check environment variables

---

## 🎊 Success Stories

**Template for your final report:**

```
🎄 12 Days of Sustainability - Campaign Results

📊 Participation:
• [X] team members participated ([X]%)
• [X] completed all 12 days ([X]% completion)
• [X] total quiz attempts
• [X]% average accuracy

🏆 Highlights:
• Most engaged day: Day [X] - [Achievement]
• Perfect scores: [X] participants
• Peak participation: [Day/Time]

💡 Key Learnings:
• [Insight about participation]
• [Insight about content]
• [Insight about timing]

🎯 Next Steps:
• [Action item 1]
• [Action item 2]
• [Action item 3]

Thank you to everyone who participated! 🌍
```

---

## 🚀 Ready to Launch?

Pick your version, follow the setup guide, and start celebrating your sustainability achievements!

**Questions?** Check the detailed guides for each version.

**Good luck with your campaign!** 🎄✨🌍

---

*Built with ❤️ for sustainability teams everywhere*
