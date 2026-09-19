import os
import xml.etree.ElementTree as ET

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Common SVG defs & styles
COMMON_DEFS = """
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c14"/>
      <stop offset="50%" stop-color="#0e1526"/>
      <stop offset="100%" stop-color="#120c24"/>
    </linearGradient>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#111827" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="cyanPurple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="100%" stop-color="#7C3AED"/>
    </linearGradient>
    <linearGradient id="purplePink" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#FF2E93"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#FBBF24"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="100%" stop-color="#38BDF8"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#10B981"/>
      <stop offset="100%" stop-color="#34D399"/>
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <pattern id="cyberGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#00E5FF" stroke-width="0.6" stroke-opacity="0.07"/>
      <circle cx="24" cy="0" r="0.8" fill="#00E5FF" fill-opacity="0.15"/>
    </pattern>
"""

COMMON_STYLE = """
    .mono { font-family: 'Fira Code', 'Courier New', monospace; }
    .sans { font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Roboto', sans-serif; }
"""

def save_and_validate(filename, content):
    filepath = os.path.join(ASSETS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    ET.fromstring(content)
    print(f"Validated and saved: {filename}")

# -------------------------------------------------------------
# 1. Section Header Generator (viewBox="0 0 950 64" width="100%" height="100%")
# -------------------------------------------------------------
def create_section_header(number_str, title_str, subtitle_str, icon_char):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 64" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .sec-num {{ font-size: 13px; font-weight: 700; fill: #00E5FF; letter-spacing: 1.5px; }}
    .sec-title {{ font-size: 18px; font-weight: 800; fill: #FFFFFF; letter-spacing: 2px; }}
    .sec-sub {{ font-size: 12px; font-weight: 500; fill: #9CA3AF; letter-spacing: 1.5px; }}
    .pulse-dot {{ fill: #00E5FF; }}
  </style>
  <!-- Background -->
  <rect width="950" height="64" rx="10" fill="url(#bgGrad)"/>
  <rect width="950" height="64" rx="10" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="62" rx="9" fill="none" stroke="#1f293d" stroke-width="1.2"/>
  <rect x="0" y="0" width="950" height="64" rx="10" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.4"/>

  <!-- Left Accent Bar -->
  <rect x="8" y="12" width="4.5" height="40" rx="2" fill="url(#cyanPurple)"/>

  <!-- Section Number & Title -->
  <g transform="translate(26, 38)">
    <text class="sans sec-title">
      <tspan class="mono sec-num">// {number_str} </tspan>
      <tspan fill="#7C3AED">[</tspan> {icon_char} {title_str} <tspan fill="#7C3AED">]</tspan>
    </text>
  </g>

  <!-- Subtitle / HUD Code -->
  <g transform="translate(926, 38)" text-anchor="end">
    <text class="mono sec-sub">{subtitle_str}</text>
  </g>

  <!-- Top Right Cyber Accents -->
  <line x1="840" y1="12" x2="935" y2="12" stroke="#00E5FF" stroke-width="1.5" stroke-opacity="0.4"/>
  <circle cx="935" cy="12" r="2" fill="#00E5FF" filter="url(#softGlow)"/>

  <!-- Bottom Glowing Accent Line -->
  <line x1="20" y1="63" x2="930" y2="63" stroke="url(#cyanPurple)" stroke-width="1" stroke-opacity="0.6"/>
</svg>"""

section_headers = [
    ("section-about.svg", "01", "ABOUT ME", "PERSONAL DOSSIER &amp; PHILOSOPHY", "👨‍💻"),
    ("section-focus.svg", "02", "CORE FOCUS", "TECHNICAL PILLARS &amp; SPECIALTIES", "🎯"),
    ("section-projects.svg", "03", "FEATURED PROJECTS", "PRODUCTION SYSTEMS &amp; HARDWARE", "🚀"),
    ("section-cyber.svg", "04", "CYBERSECURITY &amp; NETWORKING", "PACKET ANALYSIS &amp; DEFENSE OPS", "🛡️"),
    ("section-techstack.svg", "05", "TECH STACK &amp; TOOLING", "ENGINEERING ARSENAL &amp; FRAMEWORKS", "🧰"),
    ("section-experience.svg", "06", "PROFESSIONAL EXPERIENCE", "INDUSTRY IMMERSION &amp; WORKFLOW", "💼"),
    ("section-education.svg", "07", "EDUCATION MATRIX", "ACADEMIC TIMELINE &amp; FOUNDATIONS", "🎓"),
    ("section-achievements.svg", "08", "HONORS &amp; ACHIEVEMENTS", "HACKATHONS &amp; COMPETITIVE AWARDS", "🏆"),
    ("section-certifications.svg", "09", "VERIFIED CREDENTIALS", "NPTEL &amp; INDUSTRY ACCREDITATIONS", "📜"),
    ("section-analytics.svg", "10", "GITHUB ANALYTICS", "PERFORMANCE METRICS &amp; REPO STATS", "📊"),
    ("section-activity.svg", "11", "CONTRIBUTION JOURNEY", "CONTINUOUS INTEGRATION &amp; ROADMAP", "🐍"),
    ("section-connect.svg", "12", "CONNECT &amp; TRANSMIT", "INQUIRIES &amp; COLLABORATION", "🤝")
]

for filename, num, title, subtitle, icon in section_headers:
    save_and_validate(filename, create_section_header(num, title, subtitle, icon))

# -------------------------------------------------------------
# 2. Section 01: About Me Dossier Card (950 x 205)
# -------------------------------------------------------------
about_card_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 205" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .ab-name {{ font-size: 20px; font-weight: 800; fill: #FFFFFF; letter-spacing: 1px; }}
    .ab-role {{ font-size: 11px; font-weight: 700; fill: #00E5FF; letter-spacing: 1.5px; }}
    .ab-heading {{ font-size: 11.5px; font-weight: 700; letter-spacing: 1.2px; }}
    .ab-body {{ font-size: 12px; font-weight: 400; fill: #D1D5DB; }}
    .ab-badge {{ font-size: 10px; font-weight: 700; letter-spacing: 1px; }}
  </style>

  <rect width="950" height="205" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="205" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="203" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.45"/>

  <!-- Left Identity Quadrant -->
  <g transform="translate(20, 20)">
    <rect width="200" height="165" rx="10" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1.2" stroke-opacity="0.6"/>
    <circle cx="100" cy="50" r="32" fill="#00E5FF" fill-opacity="0.1" stroke="#00E5FF" stroke-width="1.2"/>
    <text x="100" y="60" font-size="34" text-anchor="middle">👨‍💻</text>
    
    <rect x="25" y="96" width="150" height="22" rx="11" fill="#00E5FF" fill-opacity="0.15" stroke="#00E5FF" stroke-width="1"/>
    <text x="100" y="111" class="mono ab-badge" fill="#00E5FF" text-anchor="middle">B.TECH IT • FINAL YEAR</text>

    <text x="100" y="136" class="mono" font-size="10.5" fill="#9CA3AF" text-anchor="middle">Kongunadu CET • India</text>
    <text x="100" y="150" class="mono" font-size="9.5" fill="#10B981" text-anchor="middle">● AVAILABLE FOR ROLES</text>
  </g>

  <!-- Right Dossier Matrix -->
  <g transform="translate(240, 24)">
    <text class="sans ab-name">KABILAN M</text>
    <text x="140" y="-3" class="mono ab-role">// SOFTWARE DEVELOPER &amp; SYSTEM BUILDER</text>
    <line x1="0" y1="12" x2="685" y2="12" stroke="url(#cyanPurple)" stroke-width="1" stroke-opacity="0.3"/>

    <!-- Dossier Row 1 -->
    <g transform="translate(0, 32)">
      <text class="mono ab-heading" fill="#00E5FF">[ ARCHITECTURE &amp; BACKEND ]</text>
      <text x="0" y="18" class="sans ab-body">Specializing in Java object-oriented design, algorithm optimization, and reliable backend services.</text>
    </g>

    <!-- Dossier Row 2 -->
    <g transform="translate(0, 78)">
      <text class="mono ab-heading" fill="#A78BFA">[ SECURITY &amp; NETWORKING ]</text>
      <text x="0" y="18" class="sans ab-body">Practical expertise in IEEE 802.11 frame dissection, Wireshark packet auditing, and ESP32 hardware defense.</text>
    </g>

    <!-- Dossier Row 3 / Core Philosophy -->
    <g transform="translate(0, 124)">
      <text class="mono ab-heading" fill="#34D399">[ CORE PHILOSOPHY ]</text>
      <text x="0" y="18" class="sans ab-body">&quot;The strongest learning happens when an abstract idea becomes a resilient working system.&quot;</text>
    </g>
  </g>
</svg>"""

save_and_validate("about-card.svg", about_card_svg)

# -------------------------------------------------------------
# 3. Section 02: Focus Areas Grid (950 x 230)
# -------------------------------------------------------------
focus_grid_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 230" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .card-title {{ font-size: 15px; font-weight: 800; fill: #FFFFFF; letter-spacing: 1px; }}
    .card-tag {{ font-size: 10px; font-weight: 700; letter-spacing: 1.2px; }}
    .card-bullet {{ font-size: 12px; font-weight: 400; fill: #9CA3AF; }}
  </style>

  <rect width="950" height="230" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="230" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="228" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.4"/>

  <!-- Card 1: Java Development -->
  <g transform="translate(18, 18)">
    <rect width="215" height="194" rx="10" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1.2" stroke-opacity="0.6"/>
    <rect x="12" y="14" width="80" height="20" rx="10" fill="#00E5FF" fill-opacity="0.15"/>
    <text x="52" y="28" class="mono card-tag" fill="#00E5FF" text-anchor="middle">CORE JAVA</text>
    <text x="12" y="60" class="sans card-title">☕ Java Architecture</text>
    <line x1="12" y1="70" x2="200" y2="70" stroke="#00E5FF" stroke-width="1" stroke-opacity="0.3"/>
    
    <text x="12" y="96" class="sans card-bullet">• OOP &amp; Clean Design</text>
    <text x="12" y="120" class="sans card-bullet">• Data Structures &amp; Alg</text>
    <text x="12" y="144" class="sans card-bullet">• High-Performance Logic</text>
    <text x="12" y="168" class="sans card-bullet">• Backend Systems Prep</text>

    <path d="M 195 180 L 205 180 L 205 170" fill="none" stroke="#00E5FF" stroke-width="1.5"/>
  </g>

  <!-- Card 2: Cybersecurity -->
  <g transform="translate(251, 18)">
    <rect width="215" height="194" rx="10" fill="url(#cardBg)" stroke="#7C3AED" stroke-width="1.2" stroke-opacity="0.6"/>
    <rect x="12" y="14" width="94" height="20" rx="10" fill="#7C3AED" fill-opacity="0.2"/>
    <text x="59" y="28" class="mono card-tag" fill="#A78BFA" text-anchor="middle">NET DEFENSE</text>
    <text x="12" y="60" class="sans card-title">🛡️ Cyber &amp; Network</text>
    <line x1="12" y1="70" x2="200" y2="70" stroke="#7C3AED" stroke-width="1" stroke-opacity="0.3"/>
    
    <text x="12" y="96" class="sans card-bullet">• Wi-Fi Packet Sniffing</text>
    <text x="12" y="120" class="sans card-bullet">• IEEE 802.11 Frame Audit</text>
    <text x="12" y="144" class="sans card-bullet">• Wireshark &amp; Kali Linux</text>
    <text x="12" y="168" class="sans card-bullet">• ESP32 Hardware Security</text>

    <path d="M 195 180 L 205 180 L 205 170" fill="none" stroke="#7C3AED" stroke-width="1.5"/>
  </g>

  <!-- Card 3: Applied AI -->
  <g transform="translate(484, 18)">
    <rect width="215" height="194" rx="10" fill="url(#cardBg)" stroke="#FF2E93" stroke-width="1.2" stroke-opacity="0.6"/>
    <rect x="12" y="14" width="96" height="20" rx="10" fill="#FF2E93" fill-opacity="0.2"/>
    <text x="60" y="28" class="mono card-tag" fill="#F472B6" text-anchor="middle">INTELLIGENCE</text>
    <text x="12" y="60" class="sans card-title">🤖 Applied AI Systems</text>
    <line x1="12" y1="70" x2="200" y2="70" stroke="#FF2E93" stroke-width="1" stroke-opacity="0.3"/>
    
    <text x="12" y="96" class="sans card-bullet">• Predictive ML Pipelines</text>
    <text x="12" y="120" class="sans card-bullet">• Wildfire Vulnerability</text>
    <text x="12" y="144" class="sans card-bullet">• Geospatial Heatmaps</text>
    <text x="12" y="168" class="sans card-bullet">• Real-Time Early Alerts</text>

    <path d="M 195 180 L 205 180 L 205 170" fill="none" stroke="#FF2E93" stroke-width="1.5"/>
  </g>

  <!-- Card 4: Career & Cloud -->
  <g transform="translate(717, 18)">
    <rect width="215" height="194" rx="10" fill="url(#cardBg)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.6"/>
    <rect x="12" y="14" width="84" height="20" rx="10" fill="#10B981" fill-opacity="0.2"/>
    <text x="54" y="28" class="mono card-tag" fill="#34D399" text-anchor="middle">EVOLUTION</text>
    <text x="12" y="60" class="sans card-title">🚀 Cloud &amp; Scale</text>
    <line x1="12" y1="70" x2="200" y2="70" stroke="#10B981" stroke-width="1" stroke-opacity="0.3"/>
    
    <text x="12" y="96" class="sans card-bullet">• RESTful Web APIs</text>
    <text x="12" y="120" class="sans card-bullet">• Database Optimization</text>
    <text x="12" y="144" class="sans card-bullet">• Distributed Computing</text>
    <text x="12" y="168" class="sans card-bullet">• Scalable Architecture</text>

    <path d="M 195 180 L 205 180 L 205 170" fill="none" stroke="#10B981" stroke-width="1.5"/>
  </g>
</svg>"""

save_and_validate("focus-grid.svg", focus_grid_svg)

# -------------------------------------------------------------
# 4. Section 03: Featured Project Cards (465 x 275 each)
# -------------------------------------------------------------
# Project 1: Forest Fire AI (Wrap lines <= 55 chars, max width ~370px)
project_forest_fire = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 465 275" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .p-title {{ font-size: 17px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.8px; }}
    .p-award {{ font-size: 11px; font-weight: 700; fill: #FBBF24; letter-spacing: 0.8px; }}
    .p-desc {{ font-size: 12px; font-weight: 400; fill: #9CA3AF; }}
    .tag-txt {{ font-size: 10.5px; font-weight: 600; fill: #00E5FF; }}
    .btn-txt {{ font-size: 11px; font-weight: 700; fill: #FFFFFF; letter-spacing: 1px; }}
  </style>

  <rect width="465" height="275" rx="14" fill="url(#bgGrad)"/>
  <rect width="465" height="275" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="463" height="273" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.4" stroke-opacity="0.6"/>

  <!-- Top Ribbon / Award Pill -->
  <g transform="translate(20, 20)">
    <rect width="210" height="26" rx="13" fill="#F59E0B" fill-opacity="0.15" stroke="#F59E0B" stroke-width="1"/>
    <circle cx="16" cy="13" r="4" fill="#FBBF24" filter="url(#softGlow)"/>
    <text x="28" y="17" class="sans p-award">🏆 1ST PLACE • AI HACKATHON</text>
  </g>

  <!-- Live Status Pill -->
  <g transform="translate(345, 20)">
    <rect width="100" height="26" rx="13" fill="#10B981" fill-opacity="0.15" stroke="#10B981" stroke-width="1"/>
    <circle cx="14" cy="13" r="3.5" fill="#10B981"/>
    <text x="26" y="17" class="mono tag-txt" fill="#34D399">VERIFIED</text>
  </g>

  <!-- Project Title -->
  <g transform="translate(20, 76)">
    <text class="sans p-title">🔥 Forest Fire AI Prediction</text>
    <text x="0" y="18" class="mono" font-size="11" fill="#7C3AED">AI ML • CLIMATE TELEMETRY • GEO-ALERT</text>
  </g>

  <!-- Divider -->
  <line x1="20" y1="106" x2="445" y2="106" stroke="url(#cyanPurple)" stroke-width="1" stroke-opacity="0.4"/>

  <!-- Description (Safely wrapped into 4 lines within 370px) -->
  <g transform="translate(20, 124)">
    <text class="sans p-desc">
      <tspan x="0" dy="0">Predictive wildfire hazard engine utilizing environmental</tspan>
      <tspan x="0" dy="16">and meteorological datasets to model disaster risk with</tspan>
      <tspan x="0" dy="16">real-time geospatial heatmaps and automated hazard</tspan>
      <tspan x="0" dy="16">early-warning notifications and alert protocols.</tspan>
    </text>
  </g>

  <!-- Tech Badges -->
  <g transform="translate(20, 194)">
    <rect x="0" y="0" width="62" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="31" y="15" class="mono tag-txt" text-anchor="middle">React</text>

    <rect x="68" y="0" width="70" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="103" y="15" class="mono tag-txt" text-anchor="middle">Node.js</text>

    <rect x="144" y="0" width="65" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="176" y="15" class="mono tag-txt" text-anchor="middle">Python</text>

    <rect x="215" y="0" width="80" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="255" y="15" class="mono tag-txt" text-anchor="middle">REST APIs</text>

    <rect x="301" y="0" width="80" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="341" y="15" class="mono tag-txt" fill="#A78BFA" text-anchor="middle">Heatmap</text>
  </g>

  <!-- Bottom CTA Button / Link Display -->
  <g transform="translate(20, 230)">
    <rect width="425" height="32" rx="8" fill="url(#cyanPurple)" fill-opacity="0.2" stroke="url(#cyanPurple)" stroke-width="1.2"/>
    <text x="212" y="21" class="mono btn-txt" text-anchor="middle" fill="#00E5FF">⚡ VIEW GITHUB REPOSITORY ➔</text>
  </g>
</svg>"""

save_and_validate("project-forest-fire.svg", project_forest_fire)

# Project 2: ESP32 Wi-Fi Security Sniffer (Wrap lines <= 55 chars, max width ~360px)
project_esp32_wifi = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 465 275" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .p-title {{ font-size: 17px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.8px; }}
    .p-award {{ font-size: 11px; font-weight: 700; fill: #38BDF8; letter-spacing: 0.8px; }}
    .p-desc {{ font-size: 12px; font-weight: 400; fill: #9CA3AF; }}
    .tag-txt {{ font-size: 10.5px; font-weight: 600; fill: #A78BFA; }}
    .btn-txt {{ font-size: 11px; font-weight: 700; fill: #FFFFFF; letter-spacing: 1px; }}
  </style>

  <rect width="465" height="275" rx="14" fill="url(#bgGrad)"/>
  <rect width="465" height="275" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="463" height="273" rx="13" fill="none" stroke="url(#purplePink)" stroke-width="1.4" stroke-opacity="0.6"/>

  <!-- Top Ribbon / Award Pill -->
  <g transform="translate(20, 20)">
    <rect width="215" height="26" rx="13" fill="#38BDF8" fill-opacity="0.15" stroke="#38BDF8" stroke-width="1"/>
    <circle cx="16" cy="13" r="4" fill="#38BDF8" filter="url(#softGlow)"/>
    <text x="28" y="17" class="sans p-award">🥈 2ND PLACE • IT PROJECT EXPO</text>
  </g>

  <!-- Prototype Pill -->
  <g transform="translate(335, 20)">
    <rect width="110" height="26" rx="13" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="1"/>
    <circle cx="14" cy="13" r="3.5" fill="#00E5FF"/>
    <text x="26" y="17" class="mono tag-txt" fill="#00E5FF">HARDWARE</text>
  </g>

  <!-- Project Title -->
  <g transform="translate(20, 76)">
    <text class="sans p-title">🛡️ ESP32 Wi-Fi Security Sniffer</text>
    <text x="0" y="18" class="mono" font-size="11" fill="#00E5FF">WIRELESS DEFENSE • IEEE 802.11 • IOT</text>
  </g>

  <!-- Divider -->
  <line x1="20" y1="106" x2="445" y2="106" stroke="url(#purplePink)" stroke-width="1" stroke-opacity="0.4"/>

  <!-- Description (Safely wrapped into 4 lines within 360px) -->
  <g transform="translate(20, 124)">
    <text class="sans p-desc">
      <tspan x="0" dy="0">Real-time wireless security monitor operating on ESP32</tspan>
      <tspan x="0" dy="16">microcontroller in promiscuous mode. Sniffs IEEE 802.11</tspan>
      <tspan x="0" dy="16">management frames to detect deauthentication attacks</tspan>
      <tspan x="0" dy="16">and beacon flooding with instant OLED visual alerts.</tspan>
    </text>
  </g>

  <!-- Tech Badges -->
  <g transform="translate(20, 194)">
    <rect x="0" y="0" width="65" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="32" y="15" class="mono tag-txt" text-anchor="middle">ESP32</text>

    <rect x="71" y="0" width="60" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="101" y="15" class="mono tag-txt" text-anchor="middle">C / C++</text>

    <rect x="137" y="0" width="70" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="172" y="15" class="mono tag-txt" text-anchor="middle">Arduino</text>

    <rect x="213" y="0" width="85" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="255" y="15" class="mono tag-txt" text-anchor="middle">802.11 L2</text>

    <rect x="304" y="0" width="75" height="22" rx="6" fill="#1F2937" stroke="#374151" stroke-width="1"/>
    <text x="341" y="15" class="mono tag-txt" fill="#00E5FF" text-anchor="middle">OLED HUD</text>
  </g>

  <!-- Bottom CTA Button / Link Display -->
  <g transform="translate(20, 230)">
    <rect width="425" height="32" rx="8" fill="url(#purplePink)" fill-opacity="0.2" stroke="url(#purplePink)" stroke-width="1.2"/>
    <text x="212" y="21" class="mono btn-txt" text-anchor="middle" fill="#A78BFA">🛠️ HARDWARE PROTOTYPE • EXPO RUNNER-UP ➔</text>
  </g>
</svg>"""

save_and_validate("project-esp32-wifi.svg", project_esp32_wifi)

# -------------------------------------------------------------
# 5. Section 04: Cybersecurity Architecture SVG (950 x 185)
# -------------------------------------------------------------
cyber_architecture = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 185" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .flow-title {{ font-size: 13px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.8px; }}
    .flow-step {{ font-size: 10px; font-weight: 700; fill: #00E5FF; letter-spacing: 1.2px; }}
    .flow-desc {{ font-size: 11px; font-weight: 400; fill: #9CA3AF; }}
    .banner-txt {{ font-size: 11px; font-weight: 600; fill: #A78BFA; letter-spacing: 1px; }}
  </style>

  <rect width="950" height="185" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="185" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="183" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.5"/>

  <!-- Step 1: Capture -->
  <g transform="translate(20, 20)">
    <rect width="200" height="110" rx="8" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1" stroke-opacity="0.5"/>
    <text x="12" y="24" class="mono flow-step">[ STEP 01 ]</text>
    <text x="12" y="44" class="sans flow-title">📡 RF Sniffing</text>
    <line x1="12" y1="52" x2="188" y2="52" stroke="#00E5FF" stroke-width="1" stroke-opacity="0.3"/>
    <text x="12" y="72" class="sans flow-desc">• Promiscuous 802.11</text>
    <text x="12" y="90" class="sans flow-desc">• ESP32 / WLAN Interface</text>
  </g>

  <!-- Arrow 1 -->
  <g transform="translate(225, 70)">
    <line x1="0" y1="0" x2="18" y2="0" stroke="#00E5FF" stroke-width="2" stroke-linecap="round"/>
    <polygon points="18,-4 26,0 18,4" fill="#00E5FF"/>
  </g>

  <!-- Step 2: Dissect -->
  <g transform="translate(255, 20)">
    <rect width="200" height="110" rx="8" fill="url(#cardBg)" stroke="#7C3AED" stroke-width="1" stroke-opacity="0.5"/>
    <text x="12" y="24" class="mono flow-step" fill="#A78BFA">[ STEP 02 ]</text>
    <text x="12" y="44" class="sans flow-title">🔬 Frame Filtering</text>
    <line x1="12" y1="52" x2="188" y2="52" stroke="#7C3AED" stroke-width="1" stroke-opacity="0.3"/>
    <text x="12" y="72" class="sans flow-desc">• 0x00C0 Deauth Catch</text>
    <text x="12" y="90" class="sans flow-desc">• Beacon Flood Detection</text>
  </g>

  <!-- Arrow 2 -->
  <g transform="translate(460, 70)">
    <line x1="0" y1="0" x2="18" y2="0" stroke="#7C3AED" stroke-width="2" stroke-linecap="round"/>
    <polygon points="18,-4 26,0 18,4" fill="#7C3AED"/>
  </g>

  <!-- Step 3: Analyze -->
  <g transform="translate(490, 20)">
    <rect width="200" height="110" rx="8" fill="url(#cardBg)" stroke="#FF2E93" stroke-width="1" stroke-opacity="0.5"/>
    <text x="12" y="24" class="mono flow-step" fill="#F472B6">[ STEP 03 ]</text>
    <text x="12" y="44" class="sans flow-title">🔍 Deep Inspection</text>
    <line x1="12" y1="52" x2="188" y2="52" stroke="#FF2E93" stroke-width="1" stroke-opacity="0.3"/>
    <text x="12" y="72" class="sans flow-desc">• Wireshark Dissector</text>
    <text x="12" y="90" class="sans flow-desc">• Kali Linux Forensics</text>
  </g>

  <!-- Arrow 3 -->
  <g transform="translate(695, 70)">
    <line x1="0" y1="0" x2="18" y2="0" stroke="#10B981" stroke-width="2" stroke-linecap="round"/>
    <polygon points="18,-4 26,0 18,4" fill="#10B981"/>
  </g>

  <!-- Step 4: Alert -->
  <g transform="translate(725, 20)">
    <rect width="205" height="110" rx="8" fill="url(#cardBg)" stroke="#10B981" stroke-width="1" stroke-opacity="0.5"/>
    <text x="12" y="24" class="mono flow-step" fill="#34D399">[ STEP 04 ]</text>
    <text x="12" y="44" class="sans flow-title">⚡ Alert &amp; Defense</text>
    <line x1="12" y1="52" x2="193" y2="52" stroke="#10B981" stroke-width="1" stroke-opacity="0.3"/>
    <text x="12" y="72" class="sans flow-desc">• Real-Time OLED Warning</text>
    <text x="12" y="90" class="sans flow-desc">• Telemetry &amp; Log Capture</text>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(20, 145)">
    <rect width="910" height="28" rx="6" fill="#111827" stroke="#1F2937" stroke-width="1"/>
    <text x="455" y="18" class="mono banner-txt" text-anchor="middle">
      🛡️ PROTOCOL: ETHICAL TESTING • AUTHORIZED SECURITY AUDITING • DEFENSIVE ENGINEERING ONLY
    </text>
  </g>
</svg>"""

save_and_validate("cyber-architecture.svg", cyber_architecture)

# -------------------------------------------------------------
# 6. Section 05: Tech Stack Command Deck (950 x 240)
# -------------------------------------------------------------
techstack_card_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 240" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .stack-col-title {{ font-size: 13.5px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.8px; }}
    .stack-pill {{ font-size: 10px; font-weight: 700; letter-spacing: 1px; }}
    .stack-item {{ font-size: 11.5px; font-weight: 500; fill: #D1D5DB; }}
    .stack-hud {{ font-size: 11px; font-weight: 600; fill: #9CA3AF; letter-spacing: 1.2px; }}
  </style>

  <rect width="950" height="240" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="240" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="238" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.45"/>

  <!-- Module 1: Languages -->
  <g transform="translate(20, 20)">
    <rect width="215" height="165" rx="10" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1.2" stroke-opacity="0.6"/>
    <rect x="12" y="12" width="90" height="20" rx="10" fill="#00E5FF" fill-opacity="0.15"/>
    <text x="57" y="26" class="mono stack-pill" fill="#00E5FF" text-anchor="middle">LANGUAGES</text>
    <text x="12" y="55" class="sans stack-col-title">⚡ Core Syntax</text>
    <line x1="12" y1="64" x2="200" y2="64" stroke="#00E5FF" stroke-width="1" stroke-opacity="0.3"/>

    <text x="12" y="88" class="sans stack-item">☕ Java (Core, OOP, Collections)</text>
    <text x="12" y="110" class="sans stack-item">🐍 Python (ML &amp; Scripting)</text>
    <text x="12" y="132" class="sans stack-item">⚙️ C / C++ (Embedded Systems)</text>
    <text x="12" y="154" class="sans stack-item">🌐 JavaScript (Modern ES6+)</text>
  </g>

  <!-- Module 2: Web & Backend -->
  <g transform="translate(252, 20)">
    <rect width="215" height="165" rx="10" fill="url(#cardBg)" stroke="#7C3AED" stroke-width="1.2" stroke-opacity="0.6"/>
    <rect x="12" y="12" width="95" height="20" rx="10" fill="#7C3AED" fill-opacity="0.2"/>
    <text x="59" y="26" class="mono stack-pill" fill="#A78BFA" text-anchor="middle">WEB &amp; BACKEND</text>
    <text x="12" y="55" class="sans stack-col-title">🌐 Services &amp; UI</text>
    <line x1="12" y1="64" x2="200" y2="64" stroke="#7C3AED" stroke-width="1" stroke-opacity="0.3"/>

    <text x="12" y="88" class="sans stack-item">⚛️ React.js &amp; Component UI</text>
    <text x="12" y="110" class="sans stack-item">🟢 Node.js &amp; Express Engine</text>
    <text x="12" y="132" class="sans stack-item">🔄 RESTful API Integration</text>
    <text x="12" y="154" class="sans stack-item">🎨 HTML5, CSS3 &amp; Flexbox</text>
  </g>

  <!-- Module 3: Data & Systems -->
  <g transform="translate(484, 20)">
    <rect width="215" height="165" rx="10" fill="url(#cardBg)" stroke="#FF2E93" stroke-width="1.2" stroke-opacity="0.6"/>
    <rect x="12" y="12" width="90" height="20" rx="10" fill="#FF2E93" fill-opacity="0.2"/>
    <text x="57" y="26" class="mono stack-pill" fill="#F472B6" text-anchor="middle">DATA &amp; INFRA</text>
    <text x="12" y="55" class="sans stack-col-title">🗄️ Persistence</text>
    <line x1="12" y1="64" x2="200" y2="64" stroke="#FF2E93" stroke-width="1" stroke-opacity="0.3"/>

    <text x="12" y="88" class="sans stack-item">🐬 MySQL Relational DBMS</text>
    <text x="12" y="110" class="sans stack-item">🍃 MongoDB Document Store</text>
    <text x="12" y="132" class="sans stack-item">🐘 Apache Hadoop HDFS</text>
    <text x="12" y="154" class="sans stack-item">📊 Apache Pig MapReduce</text>
  </g>

  <!-- Module 4: Security & DevOps -->
  <g transform="translate(716, 20)">
    <rect width="214" height="165" rx="10" fill="url(#cardBg)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.6"/>
    <rect x="12" y="12" width="105" height="20" rx="10" fill="#10B981" fill-opacity="0.15"/>
    <text x="64" y="26" class="mono stack-pill" fill="#34D399" text-anchor="middle">SECURITY &amp; TOOLS</text>
    <text x="12" y="55" class="sans stack-col-title">🛡️ Defense Ops</text>
    <line x1="12" y1="64" x2="200" y2="64" stroke="#10B981" stroke-width="1" stroke-opacity="0.3"/>

    <text x="12" y="88" class="sans stack-item">🦈 Wireshark Packet Audit</text>
    <text x="12" y="110" class="sans stack-item">🐉 Kali Linux Forensics</text>
    <text x="12" y="132" class="sans stack-item">📟 ESP32 Microcontrollers</text>
    <text x="12" y="154" class="sans stack-item">🐙 Git, GitHub &amp; Linux CLI</text>
  </g>

  <!-- Bottom Telemetry HUD -->
  <g transform="translate(20, 198)">
    <rect width="910" height="26" rx="6" fill="#111827" stroke="#1F2937" stroke-width="1"/>
    <text x="455" y="17" class="mono stack-hud" text-anchor="middle">
      ARSENAL STATUS: MODERN FULL-STACK DEVELOPMENT • EMBEDDED HARDWARE • NETWORK DISSECTION
    </text>
  </g>
</svg>"""

save_and_validate("techstack-card.svg", techstack_card_svg)

# -------------------------------------------------------------
# 7. Section 06: Professional Experience Card (950 x 175)
# -------------------------------------------------------------
# Safely formatted bullets: <= 90 characters, max rendered width ~540px, group x=175 -> ends at 715px < 930px!
experience_card = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 175" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .exp-title {{ font-size: 16px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.8px; }}
    .exp-company {{ font-size: 14px; font-weight: 700; fill: #00E5FF; }}
    .exp-date {{ font-size: 11px; font-weight: 600; fill: #A78BFA; letter-spacing: 1px; }}
    .exp-bullet {{ font-size: 12px; font-weight: 400; fill: #D1D5DB; }}
    .tag-sm {{ font-size: 10px; font-weight: 600; fill: #00E5FF; }}
  </style>

  <rect width="950" height="175" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="175" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="173" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.5"/>

  <!-- Left Icon Emblem -->
  <g transform="translate(24, 25)">
    <rect width="130" height="125" rx="10" fill="url(#cardBg)" stroke="#7C3AED" stroke-width="1.2"/>
    <text x="65" y="55" font-size="36" text-anchor="middle">💼</text>
    <rect x="15" y="80" width="100" height="22" rx="11" fill="#7C3AED" fill-opacity="0.2"/>
    <text x="65" y="95" class="mono exp-date" text-anchor="middle" fill="#A78BFA">INTERNSHIP</text>
  </g>

  <!-- Main Info -->
  <g transform="translate(175, 30)">
    <text class="sans exp-title">Full Stack Developer Intern</text>
    <text x="0" y="24" class="sans exp-company">e-soft IT Solutions</text>
    
    <!-- Date Pill -->
    <g transform="translate(620, -5)">
      <rect width="130" height="24" rx="12" fill="#00E5FF" fill-opacity="0.15" stroke="#00E5FF" stroke-width="1"/>
      <circle cx="16" cy="12" r="3.5" fill="#00E5FF"/>
      <text x="28" y="16" class="mono exp-date" fill="#00E5FF">JUNE 2025</text>
    </g>

    <!-- Divider -->
    <line x1="0" y1="36" x2="750" y2="36" stroke="#1F2937" stroke-width="1"/>

    <!-- Bullets (Safely under 92 chars each) -->
    <g transform="translate(0, 56)">
      <text class="sans exp-bullet">⚡ Engineered full-stack web applications integrating dynamic frontends with Java services.</text>
      <text x="0" y="22" class="sans exp-bullet">🗄️ Structured MySQL relational schemas, authored optimized queries, and enforced validation.</text>
      <text x="0" y="44" class="sans exp-bullet">🔍 Conducted thorough unit testing, bug isolation, and cross-browser performance tuning.</text>
    </g>

    <!-- Skills Badges -->
    <g transform="translate(0, 114)">
      <rect x="0" y="0" width="60" height="20" rx="5" fill="#1F2937" stroke="#374151" stroke-width="1"/>
      <text x="30" y="14" class="mono tag-sm" text-anchor="middle">Java</text>

      <rect x="68" y="0" width="80" height="20" rx="5" fill="#1F2937" stroke="#374151" stroke-width="1"/>
      <text x="108" y="14" class="mono tag-sm" text-anchor="middle">JavaScript</text>

      <rect x="156" y="0" width="65" height="20" rx="5" fill="#1F2937" stroke="#374151" stroke-width="1"/>
      <text x="188" y="14" class="mono tag-sm" text-anchor="middle">MySQL</text>

      <rect x="229" y="0" width="90" height="20" rx="5" fill="#1F2937" stroke="#374151" stroke-width="1"/>
      <text x="274" y="14" class="mono tag-sm" text-anchor="middle">HTML5/CSS3</text>

      <rect x="327" y="0" width="85" height="20" rx="5" fill="#1F2937" stroke="#374151" stroke-width="1"/>
      <text x="369" y="14" class="mono tag-sm" text-anchor="middle">CRUD Ops</text>

      <rect x="420" y="0" width="90" height="20" rx="5" fill="#1F2937" stroke="#374151" stroke-width="1"/>
      <text x="465" y="14" class="mono tag-sm" fill="#A78BFA" text-anchor="middle">Debugging</text>
    </g>
  </g>
</svg>"""

save_and_validate("experience-card.svg", experience_card)

# -------------------------------------------------------------
# 8. Section 07: Education Timeline SVG (950 x 215)
# -------------------------------------------------------------
# Pill 1: 160px for "CGPA 7.16 (Current)"
# Pill 2: 190px for "Score: 92% (Distinction)"
education_timeline = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 215" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .deg-title {{ font-size: 14px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.5px; }}
    .inst-title {{ font-size: 11.5px; font-weight: 500; fill: #9CA3AF; }}
    .score-badge {{ font-size: 11px; font-weight: 700; }}
    .period-txt {{ font-size: 11px; font-weight: 700; fill: #00E5FF; letter-spacing: 1px; }}
  </style>

  <rect width="950" height="215" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="215" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="213" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.4"/>

  <!-- Connecting Bus -->
  <line x1="60" y1="36" x2="890" y2="36" stroke="url(#cyanPurple)" stroke-width="2" stroke-opacity="0.5"/>

  <!-- Milestone 1 (B.Tech IT) -->
  <g transform="translate(20, 20)">
    <circle cx="20" cy="16" r="8" fill="#00E5FF" filter="url(#softGlow)"/>
    <circle cx="20" cy="16" r="4" fill="#080c14"/>
    <text x="36" y="20" class="mono period-txt">2024 — 2027</text>

    <!-- Card Box -->
    <g transform="translate(0, 36)">
      <rect width="285" height="140" rx="10" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1.2" stroke-opacity="0.6"/>
      <text x="14" y="26" class="sans deg-title">B.Tech Information Technology</text>
      <text x="14" y="46" class="sans inst-title">Kongunadu College of Eng &amp; Tech</text>
      <line x1="14" y1="56" x2="270" y2="56" stroke="#1F2937" stroke-width="1"/>

      <!-- Score Pill Expanded to 160px for clean padding -->
      <rect x="14" y="68" width="160" height="24" rx="12" fill="#00E5FF" fill-opacity="0.15" stroke="#00E5FF" stroke-width="1"/>
      <text x="94" y="84" class="mono score-badge" fill="#00E5FF" text-anchor="middle">CGPA 7.16 (Current)</text>
      
      <text x="14" y="112" class="mono" font-size="10.5" fill="#9CA3AF">Focus: Java • Networks • DBMS</text>
      <text x="14" y="126" class="mono" font-size="9.5" fill="#6B7280">*Evaluated up to 6th semester</text>
    </g>
  </g>

  <!-- Milestone 2 (Diploma Mech) -->
  <g transform="translate(332, 20)">
    <circle cx="20" cy="16" r="8" fill="#7C3AED" filter="url(#softGlow)"/>
    <circle cx="20" cy="16" r="4" fill="#080c14"/>
    <text x="36" y="20" class="mono period-txt" fill="#A78BFA">2022 — 2024</text>

    <!-- Card Box -->
    <g transform="translate(0, 36)">
      <rect width="285" height="140" rx="10" fill="url(#cardBg)" stroke="#7C3AED" stroke-width="1.2" stroke-opacity="0.6"/>
      <text x="14" y="26" class="sans deg-title">Diploma — Mechanical Eng.</text>
      <text x="14" y="46" class="sans inst-title">Kongunadu Polytechnic College</text>
      <line x1="14" y1="56" x2="270" y2="56" stroke="#1F2937" stroke-width="1"/>

      <!-- Score Pill Expanded to 190px so 24-char text never overflows -->
      <rect x="14" y="68" width="190" height="24" rx="12" fill="#7C3AED" fill-opacity="0.2" stroke="#7C3AED" stroke-width="1"/>
      <text x="109" y="84" class="mono score-badge" fill="#C4B5FD" text-anchor="middle">Score: 92% (Distinction)</text>
      
      <text x="14" y="112" class="mono" font-size="10.5" fill="#9CA3AF">Focus: Analytical Mechanics</text>
      <text x="14" y="126" class="mono" font-size="9.5" fill="#6B7280">Top Academic Standing</text>
    </g>
  </g>

  <!-- Milestone 3 (HSC) -->
  <g transform="translate(645, 20)">
    <circle cx="20" cy="16" r="8" fill="#10B981" filter="url(#softGlow)"/>
    <circle cx="20" cy="16" r="4" fill="#080c14"/>
    <text x="36" y="20" class="mono period-txt" fill="#34D399">2021 — 2022</text>

    <!-- Card Box -->
    <g transform="translate(0, 36)">
      <rect width="285" height="140" rx="10" fill="url(#cardBg)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.6"/>
      <text x="14" y="26" class="sans deg-title">Higher Secondary (HSC)</text>
      <text x="14" y="46" class="sans inst-title">Govt Higher Secondary School</text>
      <line x1="14" y1="56" x2="270" y2="56" stroke="#1F2937" stroke-width="1"/>

      <!-- Score Pill -->
      <rect x="14" y="68" width="120" height="24" rx="12" fill="#10B981" fill-opacity="0.15" stroke="#10B981" stroke-width="1"/>
      <text x="74" y="84" class="mono score-badge" fill="#34D399" text-anchor="middle">Score: 50%</text>
      
      <text x="14" y="112" class="mono" font-size="10.5" fill="#9CA3AF">State Board Examination</text>
      <text x="14" y="126" class="mono" font-size="9.5" fill="#6B7280">Foundation in Sciences</text>
    </g>
  </g>
</svg>"""

save_and_validate("education-timeline.svg", education_timeline)

# -------------------------------------------------------------
# 9. Section 08: Honors & Achievements Card (950 x 175)
# -------------------------------------------------------------
# Descriptions safely wrapped into 2 tspans of <= 48 chars each!
achievements_card = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 175" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .ach-trophy {{ font-size: 32px; }}
    .ach-place {{ font-size: 15px; font-weight: 800; letter-spacing: 1px; }}
    .ach-event {{ font-size: 14px; font-weight: 700; fill: #FFFFFF; }}
    .ach-project {{ font-size: 12.5px; font-weight: 600; }}
    .ach-desc {{ font-size: 11.5px; font-weight: 400; fill: #9CA3AF; }}
  </style>

  <rect width="950" height="175" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="175" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="173" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.4"/>

  <!-- Achievement 1: 1st Place -->
  <g transform="translate(20, 20)">
    <rect width="445" height="135" rx="10" fill="url(#cardBg)" stroke="#F59E0B" stroke-width="1.4"/>
    
    <!-- Trophy Box -->
    <g transform="translate(16, 16)">
      <rect width="56" height="56" rx="8" fill="#F59E0B" fill-opacity="0.15" stroke="#F59E0B" stroke-width="1"/>
      <text x="28" y="38" class="ach-trophy" text-anchor="middle">🥇</text>
    </g>

    <g transform="translate(86, 22)">
      <text class="sans ach-place" fill="#FBBF24">FIRST PLACE WINNER</text>
      <text x="0" y="20" class="sans ach-event">AI &amp; Data Science Hackathon</text>
      <text x="0" y="42" class="mono ach-project" fill="#00E5FF">Project: AI Forest Fire Prediction System</text>
      <text x="0" y="60" class="sans ach-desc">
        <tspan x="0" dy="0">Awarded for high-accuracy wildfire forecasting</tspan>
        <tspan x="0" dy="16">&amp; real-time geospatial heatmap alert pipeline.</tspan>
      </text>
    </g>
  </g>

  <!-- Achievement 2: 2nd Place -->
  <g transform="translate(485, 20)">
    <rect width="445" height="135" rx="10" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1.4"/>
    
    <!-- Medal Box -->
    <g transform="translate(16, 16)">
      <rect width="56" height="56" rx="8" fill="#00E5FF" fill-opacity="0.15" stroke="#00E5FF" stroke-width="1"/>
      <text x="28" y="38" class="ach-trophy" text-anchor="middle">🥈</text>
    </g>

    <g transform="translate(86, 22)">
      <text class="sans ach-place" fill="#38BDF8">SECOND PLACE RUNNER-UP</text>
      <text x="0" y="20" class="sans ach-event">State-Level IT Project Expo</text>
      <text x="0" y="42" class="mono ach-project" fill="#A78BFA">Project: ESP32 Wi-Fi Security Monitoring</text>
      <text x="0" y="60" class="sans ach-desc">
        <tspan x="0" dy="0">Commended for standalone hardware deauth attack</tspan>
        <tspan x="0" dy="16">detection and instant OLED telemetry alerts.</tspan>
      </text>
    </g>
  </g>
</svg>"""

save_and_validate("achievements-card.svg", achievements_card)

# -------------------------------------------------------------
# 10. Section 09: Certifications Grid (950 x 175)
# -------------------------------------------------------------
certifications_card = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 175" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .cert-issuer {{ font-size: 11px; font-weight: 700; letter-spacing: 1px; }}
    .cert-name {{ font-size: 14px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.5px; }}
    .cert-desc {{ font-size: 11px; font-weight: 400; fill: #9CA3AF; }}
    .cert-badge {{ font-size: 9.5px; font-weight: 700; letter-spacing: 1px; }}
  </style>

  <rect width="950" height="175" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="175" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="173" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.4"/>

  <!-- Cert 1: Infosys -->
  <g transform="translate(20, 20)">
    <rect width="288" height="135" rx="10" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1.2" stroke-opacity="0.7"/>
    
    <rect x="14" y="14" width="130" height="20" rx="10" fill="#00E5FF" fill-opacity="0.15"/>
    <text x="79" y="28" class="mono cert-badge" fill="#00E5FF" text-anchor="middle">VERIFIED CREDENTIAL</text>
    
    <text x="14" y="58" class="mono cert-issuer" fill="#00E5FF">INFOSYS SPRINGBOARD</text>
    <text x="14" y="78" class="sans cert-name">Front End Developer</text>
    <line x1="14" y1="88" x2="274" y2="88" stroke="#1F2937" stroke-width="1"/>
    <text x="14" y="108" class="sans cert-desc">Modern Web Design • UI Components</text>
    <text x="14" y="124" class="sans cert-desc">JavaScript Architecture &amp; Styling</text>
  </g>

  <!-- Cert 2: NPTEL IoT -->
  <g transform="translate(331, 20)">
    <rect width="288" height="135" rx="10" fill="url(#cardBg)" stroke="#7C3AED" stroke-width="1.2" stroke-opacity="0.7"/>
    
    <rect x="14" y="14" width="115" height="20" rx="10" fill="#7C3AED" fill-opacity="0.2"/>
    <text x="71" y="28" class="mono cert-badge" fill="#C4B5FD" text-anchor="middle">ELITE NPTEL CERT</text>
    
    <text x="14" y="58" class="mono cert-issuer" fill="#A78BFA">NPTEL • IIT KHARAGPUR</text>
    <text x="14" y="78" class="sans cert-name">Internet of Things (IoT)</text>
    <line x1="14" y1="88" x2="274" y2="88" stroke="#1F2937" stroke-width="1"/>
    <text x="14" y="108" class="sans cert-desc">Embedded Sensors • Wireless Protocols</text>
    <text x="14" y="124" class="sans cert-desc">IoT Architecture &amp; Microcontrollers</text>
  </g>

  <!-- Cert 3: NPTEL Cyber Security -->
  <g transform="translate(642, 20)">
    <rect width="288" height="135" rx="10" fill="url(#cardBg)" stroke="#10B981" stroke-width="1.2" stroke-opacity="0.7"/>
    
    <rect x="14" y="14" width="115" height="20" rx="10" fill="#10B981" fill-opacity="0.15"/>
    <text x="71" y="28" class="mono cert-badge" fill="#34D399" text-anchor="middle">ELITE NPTEL CERT</text>
    
    <text x="14" y="58" class="mono cert-issuer" fill="#34D399">NPTEL • IIT MADRAS</text>
    <text x="14" y="78" class="sans cert-name">Fundamentals of Cyber Security</text>
    <line x1="14" y1="88" x2="274" y2="88" stroke="#1F2937" stroke-width="1"/>
    <text x="14" y="108" class="sans cert-desc">Cryptographic Fundamentals • Threat Models</text>
    <text x="14" y="124" class="sans cert-desc">Network Defense &amp; Protocol Security</text>
  </g>
</svg>"""

save_and_validate("certifications-card.svg", certifications_card)

# -------------------------------------------------------------
# 11. Section 11: Learning Roadmap Pipeline (950 x 135)
# -------------------------------------------------------------
learning_roadmap = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 135" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .road-step {{ font-size: 10px; font-weight: 700; letter-spacing: 1px; }}
    .road-title {{ font-size: 13.5px; font-weight: 800; fill: #FFFFFF; letter-spacing: 0.5px; }}
    .road-sub {{ font-size: 11px; font-weight: 400; fill: #9CA3AF; }}
  </style>

  <rect width="950" height="135" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="135" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="133" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.4"/>

  <!-- Stage 1 -->
  <g transform="translate(20, 20)">
    <rect width="200" height="95" rx="8" fill="url(#cardBg)" stroke="#10B981" stroke-width="1.2"/>
    <text x="12" y="22" class="mono road-step" fill="#34D399">01 // FOUNDATION [DONE]</text>
    <text x="12" y="44" class="sans road-title">☕ Java Core &amp; OOP</text>
    <line x1="12" y1="52" x2="188" y2="52" stroke="#10B981" stroke-width="1" stroke-opacity="0.3"/>
    <text x="12" y="72" class="sans road-sub">Collections • Multithreading</text>
    <text x="12" y="86" class="sans road-sub">Object-Oriented Design</text>
  </g>

  <!-- Flow 1 -->
  <g transform="translate(225, 68)">
    <line x1="0" y1="0" x2="18" y2="0" stroke="#00E5FF" stroke-width="2"/>
    <polygon points="18,-4 26,0 18,4" fill="#00E5FF"/>
  </g>

  <!-- Stage 2 -->
  <g transform="translate(255, 20)">
    <rect width="200" height="95" rx="8" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1.2"/>
    <text x="12" y="22" class="mono road-step" fill="#00E5FF">02 // ACTIVE [IN PROGRESS]</text>
    <text x="12" y="44" class="sans road-title">🧩 DSA &amp; Algorithms</text>
    <line x1="12" y1="52" x2="188" y2="52" stroke="#00E5FF" stroke-width="1" stroke-opacity="0.3"/>
    <text x="12" y="72" class="sans road-sub">Trees • Graphs • Dynamic Prog</text>
    <text x="12" y="86" class="sans road-sub">LeetCode Problem Solving</text>
  </g>

  <!-- Flow 2 -->
  <g transform="translate(460, 68)">
    <line x1="0" y1="0" x2="18" y2="0" stroke="#7C3AED" stroke-width="2"/>
    <polygon points="18,-4 26,0 18,4" fill="#7C3AED"/>
  </g>

  <!-- Stage 3 -->
  <g transform="translate(490, 20)">
    <rect width="200" height="95" rx="8" fill="url(#cardBg)" stroke="#7C3AED" stroke-width="1.2"/>
    <text x="12" y="22" class="mono road-step" fill="#A78BFA">03 // UPCOMING [TARGET]</text>
    <text x="12" y="44" class="sans road-title">⚙️ Spring &amp; Backend</text>
    <line x1="12" y1="52" x2="188" y2="52" stroke="#7C3AED" stroke-width="1" stroke-opacity="0.3"/>
    <text x="12" y="72" class="sans road-sub">Spring Boot • Microservices</text>
    <text x="12" y="86" class="sans road-sub">RESTful Enterprise APIs</text>
  </g>

  <!-- Flow 3 -->
  <g transform="translate(695, 68)">
    <line x1="0" y1="0" x2="18" y2="0" stroke="#FF2E93" stroke-width="2"/>
    <polygon points="18,-4 26,0 18,4" fill="#FF2E93"/>
  </g>

  <!-- Stage 4 -->
  <g transform="translate(725, 20)">
    <rect width="205" height="95" rx="8" fill="url(#cardBg)" stroke="#FF2E93" stroke-width="1.2"/>
    <text x="12" y="22" class="mono road-step" fill="#F472B6">04 // ROADMAP [NEXT]</text>
    <text x="12" y="44" class="sans road-title">☁️ Cloud &amp; Distributed</text>
    <line x1="12" y1="52" x2="193" y2="52" stroke="#FF2E93" stroke-width="1" stroke-opacity="0.3"/>
    <text x="12" y="72" class="sans road-sub">Docker • CI/CD Pipelines</text>
    <text x="12" y="86" class="sans road-sub">Cloud Native Systems</text>
  </g>
</svg>"""

save_and_validate("learning-roadmap.svg", learning_roadmap)

# -------------------------------------------------------------
# 12. Section 12: Connect Terminal Card (950 x 130)
# -------------------------------------------------------------
connect_card_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 130" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
  </defs>
  <style>
    {COMMON_STYLE}
    .con-title {{ font-size: 14px; font-weight: 800; fill: #FFFFFF; letter-spacing: 1px; }}
    .con-sub {{ font-size: 11.5px; font-weight: 500; fill: #9CA3AF; }}
    .con-label {{ font-size: 10px; font-weight: 700; letter-spacing: 1px; }}
    .con-val {{ font-size: 11px; font-weight: 600; fill: #FFFFFF; }}
  </style>

  <rect width="950" height="130" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="130" rx="14" fill="url(#cyberGrid)"/>
  <rect x="1" y="1" width="948" height="128" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.45"/>

  <!-- Top HUD Header -->
  <g transform="translate(24, 26)">
    <text class="sans con-title">
      <tspan class="mono" fill="#00E5FF">&gt;&gt;&gt; SECURE TRANSMISSION CHANNELS </tspan>
      <tspan fill="#7C3AED">[</tspan> ACTIVE &amp; OPEN <tspan fill="#7C3AED">]</tspan>
    </text>
    <text x="0" y="18" class="sans con-sub">Available for software engineering roles, Java backend development, cybersecurity, and tech innovation.</text>
  </g>

  <!-- 4 Channel Nodes -->
  <g transform="translate(20, 68)">
    <!-- Node 1: LinkedIn -->
    <g transform="translate(0, 0)">
      <rect width="215" height="46" rx="8" fill="url(#cardBg)" stroke="#0A66C2" stroke-width="1.2" stroke-opacity="0.7"/>
      <circle cx="16" cy="23" r="4" fill="#0A66C2" filter="url(#softGlow)"/>
      <text x="28" y="18" class="mono con-label" fill="#38BDF8">CHANNEL 01 // LINKEDIN</text>
      <text x="28" y="34" class="sans con-val">in/kabilan-m</text>
    </g>

    <!-- Node 2: Email -->
    <g transform="translate(232, 0)">
      <rect width="215" height="46" rx="8" fill="url(#cardBg)" stroke="#EA4335" stroke-width="1.2" stroke-opacity="0.7"/>
      <circle cx="16" cy="23" r="4" fill="#EA4335" filter="url(#softGlow)"/>
      <text x="28" y="18" class="mono con-label" fill="#F87171">CHANNEL 02 // EMAIL</text>
      <text x="28" y="34" class="sans con-val">mkabilan1409@gmail.com</text>
    </g>

    <!-- Node 3: Portfolio -->
    <g transform="translate(464, 0)">
      <rect width="215" height="46" rx="8" fill="url(#cardBg)" stroke="#7C3AED" stroke-width="1.2" stroke-opacity="0.7"/>
      <circle cx="16" cy="23" r="4" fill="#7C3AED" filter="url(#softGlow)"/>
      <text x="28" y="18" class="mono con-label" fill="#C4B5FD">CHANNEL 03 // PORTFOLIO</text>
      <text x="28" y="34" class="sans con-val">kabii.me</text>
    </g>

    <!-- Node 4: GitHub -->
    <g transform="translate(695, 0)">
      <rect width="215" height="46" rx="8" fill="url(#cardBg)" stroke="#00E5FF" stroke-width="1.2" stroke-opacity="0.7"/>
      <circle cx="16" cy="23" r="4" fill="#00E5FF" filter="url(#softGlow)"/>
      <text x="28" y="18" class="mono con-label" fill="#00E5FF">CHANNEL 04 // GITHUB</text>
      <text x="28" y="34" class="sans con-val">@kabilanm1409</text>
    </g>
  </g>
</svg>"""

save_and_validate("connect-card.svg", connect_card_svg)

# -------------------------------------------------------------
# 13. Cyber Footer SVG (950 x 140)
# -------------------------------------------------------------
footer_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 140" width="100%" height="100%">
  <defs>
    {COMMON_DEFS}
    <linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="50%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#FF2E93"/>
    </linearGradient>
  </defs>
  <style>
    {COMMON_STYLE}
    .f-title {{ font-size: 13px; font-weight: 700; fill: #00E5FF; letter-spacing: 2px; }}
    .f-sub {{ font-size: 12px; font-weight: 400; fill: #9CA3AF; letter-spacing: 0.8px; }}
    .f-status {{ font-size: 10.5px; font-weight: 600; fill: #10B981; letter-spacing: 1.5px; }}
  </style>

  <rect width="950" height="140" rx="14" fill="url(#bgGrad)"/>
  <rect width="950" height="140" rx="14" fill="url(#cyberGrid)"/>
  
  <!-- Glowing Wave Top Border -->
  <path d="M 0 35 Q 237.5 10 475 35 T 950 35 L 950 0 L 0 0 Z" fill="url(#cardBg)" opacity="0.5"/>
  <path d="M 0 35 Q 237.5 10 475 35 T 950 35" fill="none" stroke="url(#waveGrad)" stroke-width="2.5" filter="url(#softGlow)"/>

  <!-- Border -->
  <rect x="1" y="1" width="948" height="138" rx="13" fill="none" stroke="url(#cyanPurple)" stroke-width="1.2" stroke-opacity="0.4"/>

  <!-- Corner Brackets -->
  <path d="M 20 120 L 20 130 L 30 130" fill="none" stroke="#00E5FF" stroke-width="2"/>
  <path d="M 930 120 L 930 130 L 920 130" fill="none" stroke="#7C3AED" stroke-width="2"/>

  <!-- Center Content -->
  <g transform="translate(475, 68)" text-anchor="middle">
    <text class="mono f-title">&lt; KABILAN M // PORTFOLIO ARCHITECTURE /&gt;</text>
    <text y="24" class="sans f-sub">Built with Cyberpunk Precision • Engineered for Performance &amp; Scalability</text>
  </g>

  <!-- Live Status Pill Bottom -->
  <g transform="translate(475, 118)">
    <rect x="-135" y="-10" width="270" height="20" rx="10" fill="#111827" stroke="#1F2937" stroke-width="1"/>
    <circle cx="-115" cy="0" r="3.5" fill="#10B981" filter="url(#softGlow)"/>
    <text x="-98" y="4" class="mono f-status">TERMINAL STATUS: ACTIVE &amp; READY</text>
  </g>
</svg>"""

save_and_validate("footer.svg", footer_svg)

print("ALL 25 ASSETS GENERATED, VERIFIED AND VALIDATED!")
