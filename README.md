# 🤖 Headless Anime Scraper

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Selenium](https://img.shields.io/badge/selenium-4.0+-orange.svg)
![Pandas](https://img.shields.io/badge/pandas-latest-red.svg)

A Python-powered web scraper that silently monitors anime websites and delivers beautifully formatted email updates with the latest episodes - all running invisibly in the background!

## ✨ Features

- **🕵️ Headless Scraping**: Runs Chrome browser invisibly in the background
- **📧 Email Notifications**: Beautiful HTML emails with anime episode updates
- **🎨 Styled Reports**: Professional-looking email templates with responsive design
- **⚡ Silent Operation**: No browser windows pop up - completely invisible
- **📊 Data Processing**: Extracts and organizes episode data into clean tables
- **🔐 Secure**: Uses environment variables for sensitive credentials

## 🛠️ Requirements

### Dependencies
```bash
pip install selenium pandas python-dotenv
```

### System Requirements
- Python 3.7+
- Chrome browser installed
- ChromeDriver (automatically managed by Selenium 4+)

## 📋 Setup

### 1. Clone and Install
```bash
git clone <your-repo>
cd anime-scraper
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file in the project root:

```env
# Gmail credentials for sending emails
MY_EMAIL=your-email@gmail.com
PASS=your-app-password
TO_EMAIL=recipient@gmail.com
```

### 3. Gmail App Password Setup
1. Enable 2-Factor Authentication on your Google account
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Generate an app password for "Mail"
4. Use this 16-character password in your `.env` file

## 🚀 Usage

### Basic Run
```bash
python anime_scraper.py
```

### Expected Output
```
🤖 Starting headless browser (invisible)...
🌐 Navigating to anime site...
✅ Page loaded successfully
📊 Anime content found and extracted
📺 Found 12 anime episodes
📧 Preparing email...
📤 Sending email...
✅ Email sent successfully with 12 anime episodes!
🤖 No browser window was opened during this process!
🔒 Closing headless browser...
✅ Script completed!
```

## 📁 Project Structure

```
anime-scraper/
├── anime_scraper.py      # Main scraping script
├── .env                  # Environment variables (create this)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎯 How It Works

1. **Headless Browser Launch**: Chrome starts invisibly with optimized flags
2. **Website Navigation**: Selenium navigates to the anime streaming site
3. **Content Extraction**: XPath selectors grab episode data
4. **Data Processing**: Raw text gets parsed into episode/title pairs
5. **DataFrame Creation**: Pandas organizes data into a clean table
6. **Email Generation**: HTML template creates a beautiful email
7. **Email Delivery**: SMTP sends the formatted report
8. **Cleanup**: Browser closes silently

## 🔧 Customization

### Change Target Website
```python
driver.get("https://your-anime-site.com/")
```

### Modify Data Extraction
```python
# Update XPath selector for different site structure
wa = driver.find_element(By.XPATH, value='//your-xpath-here')
```

### Customize Email Template
The HTML email template includes:
- Gradient backgrounds
- Responsive design
- Hover effects
- Mobile optimization
- Custom styling

### Adjust Chrome Options
```python
chrome_op.add_argument("--your-custom-flag")
```

## 📅 Automation Options

### Cron Job (Linux/Mac)
```bash
# Run every day at 9 AM
0 9 * * * /usr/bin/python3 /path/to/anime_scraper.py
```

### Task Scheduler (Windows)
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily, weekly, etc.)
4. Set action to run your Python script

### GitHub Actions
```yaml
name: Daily Anime Updates
on:
  schedule:
    - cron: '0 9 * * *'  # 9 AM daily
jobs:
  scrape:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run scraper
        run: python anime_scraper.py
```

## 🚨 Troubleshooting

### Common Issues

**Chrome not found**
```bash
# Ubuntu/Debian
sudo apt-get install google-chrome-stable

# Mac
brew install --cask google-chrome
```

**Email authentication failed**
- Ensure 2FA is enabled on Gmail
- Use App Password, not regular password
- Check `.env` file formatting

**Selenium errors**
```bash
pip install --upgrade selenium
```

**XPath not found**
- Website structure may have changed
- Update XPath selector
- Check if site requires different user agent

## ⚡ Performance Tips

- **Headless Mode**: Already enabled for faster execution
- **Disable Images**: Add `--disable-images` to Chrome options
- **Disable Extensions**: Add `--disable-extensions`
- **Memory Optimization**: `--disable-dev-shm-usage` already included

## 🔒 Security Notes

- Never commit `.env` files to version control
- Use app passwords, not main account passwords
- Consider using service accounts for production
- Respect website terms of service and rate limits

## 📈 Potential Enhancements

- [ ] Multiple anime sites support
- [ ] Database storage for historical tracking
- [ ] Discord/Slack notifications
- [ ] Web dashboard for results
- [ ] Anime recommendation engine
- [ ] Mobile app notifications
- [ ] Docker containerization

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational purposes. Always respect website terms of service, robots.txt files, and implement appropriate rate limiting. The authors are not responsible for any misuse of this software.

## 🙋‍♂️ Support

Having issues? Check these resources:

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [Gmail SMTP Setup](https://support.google.com/accounts/answer/185833)

---

**Made with ❤️ and invisible browsers** 🤖✨"# AniAuto" 
