from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Load environment variables
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASS = os.getenv("PASS")
TO_EMAIL = os.getenv("TO_EMAIL")

# Setup Chrome - HEADLESS MODE (invisible browser)
chrome_op = webdriver.ChromeOptions()
chrome_op.add_argument("--headless")  # This makes Chrome invisible!
chrome_op.add_argument("--no-sandbox")
chrome_op.add_argument("--disable-dev-shm-usage")
chrome_op.add_argument("--disable-gpu")
chrome_op.add_argument("--window-size=1920,1080")
chrome_op.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

print("🤖 Starting headless browser (invisible)...")
driver = webdriver.Chrome(options=chrome_op)

try:
    print("🌐 Navigating to anime site...")
    # Open anime site
    driver.get("https://hianime.my/")
    print("✅ Page loaded successfully")

    wa = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div[2]')
    print("📊 Anime content found and extracted")

    # Extract text
    data = wa.text.split("\n")
    A = data[3::2]

    # Pair episodes + titles
    pairs = []
    for i in range(0, len(A), 2):
        episode = A[i] if i < len(A) else "N/A"
        title = A[i + 1] if i + 1 < len(A) else "N/A"
        pairs.append([episode, title])

    # Make DataFrame
    df = pd.DataFrame(pairs, columns=["Episode", "Title"])
    print(f"📺 Found {len(df)} anime episodes")

    # Convert DataFrame to HTML table (clean, no index)
    table_html = df.to_html(index=False, border=0, classes="anime-table", escape=False)

    # Get current date for personalization
    current_date = datetime.now().strftime("%B %d, %Y")

    # Enhanced HTML email template
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Anime Updates</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
            }}

            .email-container {{
                max-width: 600px;
                margin: 20px auto;
                background: white;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            }}

            .header {{
                background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
                color: white;
                padding: 30px;
                text-align: center;
                position: relative;
            }}

            .header::before {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="80" cy="40" r="3" fill="rgba(255,255,255,0.1)"/><circle cx="40" cy="80" r="2" fill="rgba(255,255,255,0.1)"/></svg>');
            }}

            .header h1 {{
                margin: 0;
                font-size: 2.2em;
                font-weight: 700;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
                position: relative;
                z-index: 1;
            }}

            .header .emoji {{
                font-size: 1.5em;
                margin-right: 10px;
                animation: bounce 2s infinite;
            }}

            @keyframes bounce {{
                0%, 20%, 50%, 80%, 100% {{
                    transform: translateY(0);
                }}
                40% {{
                    transform: translateY(-10px);
                }}
                60% {{
                    transform: translateY(-5px);
                }}
            }}

            .date-badge {{
                background: rgba(255, 255, 255, 0.2);
                padding: 8px 16px;
                border-radius: 20px;
                display: inline-block;
                margin-top: 10px;
                font-size: 0.9em;
                font-weight: 500;
                backdrop-filter: blur(10px);
            }}

            .content {{
                padding: 30px;
            }}

            .intro {{
                text-align: center;
                margin-bottom: 30px;
                color: #666;
                font-size: 1.1em;
            }}

            .anime-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                background: white;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            }}

            .anime-table th {{
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                padding: 15px;
                text-align: left;
                font-weight: 600;
                font-size: 1.1em;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }}

            .anime-table td {{
                padding: 15px;
                border-bottom: 1px solid #f0f0f0;
                transition: background-color 0.3s ease;
            }}

            .anime-table tr:hover td {{
                background-color: #f8f9ff;
            }}

            .anime-table tr:last-child td {{
                border-bottom: none;
            }}

            .anime-table td:first-child {{
                font-weight: 600;
                color: #667eea;
                white-space: nowrap;
            }}

            .footer {{
                background: #f8f9fa;
                padding: 25px;
                text-align: center;
                border-top: 1px solid #eee;
            }}

            .footer p {{
                margin: 0;
                color: #666;
                font-size: 1.1em;
            }}

            .footer .emoji {{
                font-size: 1.3em;
                margin: 0 5px;
            }}

            .stats {{
                background: linear-gradient(135deg, #ffecd2, #fcb69f);
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
                text-align: center;
            }}

            .stats strong {{
                color: #d63031;
                font-size: 1.2em;
            }}

            .headless-badge {{
                background: linear-gradient(135deg, #2ecc71, #27ae60);
                color: white;
                padding: 10px 15px;
                border-radius: 20px;
                display: inline-block;
                margin: 10px 0;
                font-size: 0.9em;
                font-weight: 600;
            }}

            /* Mobile responsiveness */
            @media (max-width: 600px) {{
                .email-container {{
                    margin: 10px;
                    border-radius: 10px;
                }}

                .header {{
                    padding: 20px;
                }}

                .header h1 {{
                    font-size: 1.8em;
                }}

                .content {{
                    padding: 20px;
                }}

                .anime-table th,
                .anime-table td {{
                    padding: 10px;
                    font-size: 0.9em;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <h1><span class="emoji">📺</span>Today's Anime Updates</h1>
                <div class="date-badge">{current_date}</div>
                <div class="headless-badge">🤖 Scraped Silently</div>
            </div>

            <div class="content">
                <div class="intro">
                    <p>Here are the latest anime episodes available for streaming!</p>
                    <p><em>🤖 Collected silently in the background - no browser window opened!</em></p>
                </div>

                <div class="stats">
                    <strong>{len(df)}</strong> new episodes ready to watch!
                </div>

                {table_html}
            </div>

            <div class="footer">
                <p>Happy watching! <span class="emoji">🍿</span><span class="emoji">✨</span></p>
                <p style="font-size: 0.9em; color: #999; margin-top: 10px;">
                    Delivered with ❤️ by your Headless Anime Tracker
                </p>
                <p style="font-size: 0.8em; color: #bbb; margin-top: 5px;">
                    ⚡ Powered by invisible Chrome browser
                </p>
            </div>
        </div>
    </body>
    </html>
    """

    print("📧 Preparing email...")
    # Create email (HTML)
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🤖 Headless Anime Updates - {current_date} ({len(df)} Episodes)"
    msg["From"] = MY_EMAIL
    msg["To"] = TO_EMAIL

    # Add some email headers for better deliverability
    msg["X-Priority"] = "3"
    msg["X-Mailer"] = "Headless Anime Updates Bot"

    msg.attach(MIMEText(html_content, "html", "utf-8"))

    # Send email
    print("📤 Sending email...")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASS)
        connection.send_message(msg)
    print(f"✅ Email sent successfully with {len(df)} anime episodes!")
    print("🤖 No browser window was opened during this process!")

except Exception as e:
    print(f"❌ Error occurred: {e}")
    import traceback

    traceback.print_exc()

finally:
    print("🔒 Closing headless browser...")
    driver.quit()
    print("✅ Script completed!")


