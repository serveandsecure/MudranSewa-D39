#!/usr/bin/env python3
"""
Generate high-fidelity, publication-grade PNG diagrams and wireframe mockups
matching the exact visual styling and 16:9 widescreen aspect ratio (1376x768 px)
of the reference PDFs (NESFIC-D-50) for Mudran-Sewa (NESFIC-D-39).
"""

import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

ASSETS_DIR = os.path.abspath("docs/assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Color Palette matching Government of Assam Directorate Branding
GOV_GREEN = "#004d40"       # Deep Emerald Green
GOV_GREEN_DARK = "#00332c"
GOV_GREEN_LIGHT = "#065f46"
GOV_GREEN_SUBTLE = "#ecfdf5"
GOV_GOLD = "#d97706"        # Assam Gold
GOV_GOLD_SHINE = "#f59e0b"
BG_DARK = "#0a1e17"         # Dark Green Slate
CARD_DARK = "#112a22"       # Slate
TEXT_WHITE = "#f8fafc"
TEXT_MUTED = "#94a3b8"
CRIMSON = "#dc2626"
BLUE_ACCENT = "#0284c7"

def draw_browser_chrome(ax, title, url="https://mudran.sascol.com"):
    # Window chrome bar
    rect_bar = patches.Rectangle((0, 0.93), 1, 0.07, transform=ax.transAxes, facecolor="#00332c", edgecolor=None, zorder=10)
    ax.add_patch(rect_bar)
    # 3 dots
    ax.add_patch(patches.Circle((0.02, 0.965), 0.007, transform=ax.transAxes, facecolor="#ef4444", zorder=11))
    ax.add_patch(patches.Circle((0.035, 0.965), 0.007, transform=ax.transAxes, facecolor="#f59e0b", zorder=11))
    ax.add_patch(patches.Circle((0.05, 0.965), 0.007, transform=ax.transAxes, facecolor="#10b981", zorder=11))
    # URL Pill
    url_box = patches.FancyBboxPatch((0.08, 0.942), 0.48, 0.045, transform=ax.transAxes,
                                    boxstyle="round,pad=0.005,rounding_size=0.015",
                                    facecolor="#00241e", edgecolor="#065f46", linewidth=1, zorder=11)
    ax.add_patch(url_box)
    ax.text(0.09, 0.965, f"SECURE GOVT SSL | {url}", transform=ax.transAxes, color="#a7f3d0", fontsize=8.5, va="center", zorder=12, family="sans-serif")
    # Title
    ax.text(0.98, 0.965, title, transform=ax.transAxes, color="#ffffff", fontsize=10, weight="bold", ha="right", va="center", zorder=12, family="sans-serif")

# 1. PARADIGM SHIFT: GOVERNMENT PRESS INVENTORY & MOVEMENT MANAGEMENT
def gen_paradigm_shift():
    fig, ax = plt.subplots(figsize=(13.76, 7.68), dpi=100)
    ax.set_facecolor("#ffffff")
    fig.patch.set_facecolor("#ffffff")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Header Box
    ax.text(0.5, 0.94, "PARADIGM SHIFT: GOVERNMENT STATIONERY & PRESS INVENTORY", fontsize=15, weight="heavy", color="#004d40", ha="center")
    ax.text(0.5, 0.90, "Directorate of Printing & Stationery, Assam (Bamunimaidam) • Problem NESFIC-D-39", fontsize=10.5, color="#475569", ha="center")

    # Left Container: Current Reactive Paradigm
    box_l = patches.FancyBboxPatch((0.03, 0.10), 0.44, 0.76, transform=ax.transAxes,
                                  boxstyle="round,pad=0.01,rounding_size=0.02",
                                  facecolor="#fef2f2", edgecolor="#fca5a5", linewidth=1.5)
    ax.add_patch(box_l)
    ax.text(0.25, 0.82, "CURRENT MANUAL PARADIGM", fontsize=12, weight="bold", color="#991b1b", ha="center")

    steps_l = [
        ("1. Paper Ledger Inward at Sheds", "Unrecorded mill reels; lack of GSM & lot serialization; manual hand receipts."),
        ("2. Press Floor Trimming Blind Spot", "Loose job slips; paper trimming scrap exceeds 5% without real-time accountability."),
        ("3. Delayed Requisition Approvals", "Physical indent letters take 3-4 weeks to clear quotas; artificial shortages in districts."),
        ("4. Untracked Highway Dispatches", "Vulnerable physical gatepasses; zero transit visibility; 60-day reconciliation delays.")
    ]
    y = 0.72
    for title, desc in steps_l:
        card = patches.FancyBboxPatch((0.05, y - 0.10), 0.40, 0.10, transform=ax.transAxes,
                                      boxstyle="round,pad=0.005,rounding_size=0.01",
                                      facecolor="#ffffff", edgecolor="#f87171", linewidth=1)
        ax.add_patch(card)
        ax.text(0.07, y - 0.03, title, fontsize=10, weight="bold", color="#7f1d1d")
        ax.text(0.07, y - 0.07, desc, fontsize=8.5, color="#475569")
        y -= 0.14

    # Central Arrow
    ax.annotate("", xy=(0.52, 0.48), xytext=(0.48, 0.48),
                arrowprops=dict(arrowstyle="->", color=GOV_GOLD, lw=4))
    ax.text(0.50, 0.52, "MUDRAN-SEWA\nTRANSFORMATION", fontsize=8.5, weight="bold", color=GOV_GOLD, ha="center")

    # Right Container: Mudran-Sewa Proactive Assurance
    box_r = patches.FancyBboxPatch((0.53, 0.10), 0.44, 0.76, transform=ax.transAxes,
                                  boxstyle="round,pad=0.01,rounding_size=0.02",
                                  facecolor="#ecfdf5", edgecolor="#6ee7b7", linewidth=1.5)
    ax.add_patch(box_r)
    ax.text(0.75, 0.82, "MUDRAN-SEWA PROACTIVE ASSURANCE", fontsize=12, weight="bold", color="#065f46", ha="center")

    steps_r = [
        ("1. Serialized Mill Lot Registry", "Real-time GRN recording; automatic safety buffer threshold alerts (<800 reams)."),
        ("2. Machine Telemetry & Wastage Guard", "Harris Web & Heidelberg speed tracking; live scrap calculation with >3% alerts."),
        ("3. Instant 24-Hour e-Indent Sanctions", "Digital quota verification; 35 Assam districts connected with digital sanction orders."),
        ("4. Tamper-Proof QR E-Gatepass & GPS", "Verified highway route pings (NH-27/715); OTP delivery handshake at treasuries.")
    ]
    y = 0.72
    for title, desc in steps_r:
        card = patches.FancyBboxPatch((0.55, y - 0.10), 0.40, 0.10, transform=ax.transAxes,
                                      boxstyle="round,pad=0.005,rounding_size=0.01",
                                      facecolor="#ffffff", edgecolor="#34d399", linewidth=1)
        ax.add_patch(card)
        ax.text(0.57, y - 0.03, title, fontsize=10, weight="bold", color="#064e3b")
        ax.text(0.57, y - 0.07, desc, fontsize=8.5, color="#1e293b")
        y -= 0.14

    # KPI Banner bottom
    ax.text(0.5, 0.04, "Pre-Emptive Defect Discovery: 100%  •  Indent Turnaround: 24 Hours  •  Reconciliation Accuracy: 100%",
            fontsize=9.5, weight="bold", color="#004d40", ha="center")

    out_path = os.path.join(ASSETS_DIR, "d39_fig_paradigm_shift.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=100)
    plt.close()
    print("Generated:", out_path)

# 2. ENTERPRISE CLOUD-NATIVE SYSTEM ARCHITECTURE
def gen_architecture():
    fig, ax = plt.subplots(figsize=(13.76, 7.68), dpi=100)
    ax.set_facecolor(BG_DARK)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Enterprise System Architecture: Mudran-Sewa", "https://mudran.sascol.com/architecture")

    # Header
    ax.text(0.04, 0.88, "ENTERPRISE CLOUD-NATIVE SYSTEM ARCHITECTURE: MUDRAN-SEWA", color=TEXT_WHITE, fontsize=14, weight="heavy")
    ax.text(0.04, 0.85, "High-Availability, Zero-Trust Edge Deployment for Directorate of Printing & Stationery, Assam (NESFIC-D-39)", color=GOV_GOLD_SHINE, fontsize=10)

    # 5 Tier Layers
    tiers = [
        ("TIER 1: EDGE INGRESS & ZERO-TRUST SECURITY",
         "• Cloudflare Global Edge Network (300+ PoPs)\n• HSTS, Strict CORS & X-Frame-Options: SAMEORIGIN\n• Multi-Tenant RBAC (Super Admin, Storekeeper, Press Master, DC Indenter)\n• Offline Progressive Web App (PWA) Caching",
         "#004d40", "#10b981", 0.70),
        ("TIER 2: PRESS PRODUCTION & INVENTORY MICROSERVICES",
         "• Master Paper Reel/Ream Registry (<50ms V8 Runtime)\n• Trimming Loss % Telemetry (<2.5% Benchmark)\n• e-Indent Sanction Order Generator\n• The Assam Gazette (Asom Rajpatra) High-Security Vault",
         "#0c4a6e", "#38bdf8", 0.53),
        ("TIER 3: DISTRIBUTED EVENT LOG & STATE SYNCHRONIZATION",
         "• Chained SHA-256 State Transition Hashing\n• Automated Safety Buffer Threshold Alerter\n• Inward GRN Mill Inspection Sentry\n• Ephemeral Delivery OTP Dispatcher",
         "#4c1d95", "#c084fc", 0.36),
        ("TIER 4: GEOSPATIAL RADAR & RECONCILIATION ENGINE",
         "• PostGIS GeoJSON Corridors (NH-27, NH-715, NH-37)\n• Tamper-Evident QR E-Gatepass Token Signer\n• Bamunimaidam GPS Central Anchor (26.1834°N, 91.7766°E)\n• Automated CAG Form GFR-19 Audit Exporter",
         "#78350f", "#f59e0b", 0.19),
    ]

    for title, desc, bg, border, y in tiers:
        box = patches.FancyBboxPatch((0.04, y), 0.92, 0.14, transform=ax.transAxes,
                                     boxstyle="round,pad=0.008,rounding_size=0.015",
                                     facecolor=CARD_DARK, edgecolor=border, linewidth=1.5)
        ax.add_patch(box)
        # Header strip inside box
        hdr = patches.FancyBboxPatch((0.04, y + 0.105), 0.92, 0.035, transform=ax.transAxes,
                                    boxstyle="round,pad=0.004,rounding_size=0.01",
                                    facecolor=bg, edgecolor=None)
        ax.add_patch(hdr)
        ax.text(0.06, y + 0.12, title, transform=ax.transAxes, color="#ffffff", fontsize=9.5, weight="bold", va="center")
        ax.text(0.06, y + 0.05, desc, transform=ax.transAxes, color="#cbd5e1", fontsize=8.5, va="center", linespacing=1.4)

    # Bottom Footer SLA
    ax.text(0.5, 0.07, "Throughput: >250 Trans/sec  •  Latency: <50ms Global Edge  •  Availability: 99.95% SLA  •  Compliance: GFR-19 & IT Act 2000",
            color="#a7f3d0", fontsize=9.5, weight="bold", ha="center")

    out_path = os.path.join(ASSETS_DIR, "d39_fig_architecture.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=100)
    plt.close()
    print("Generated:", out_path)

# 3. END-TO-END PRESS INVENTORY & DISPATCH VERIFICATION ENGINE
def gen_lifecycle_engine():
    fig, ax = plt.subplots(figsize=(13.76, 7.68), dpi=100)
    ax.set_facecolor("#ffffff")
    fig.patch.set_facecolor("#ffffff")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.94, "END-TO-END PRESS INVENTORY & DISPATCH VERIFICATION ENGINE", fontsize=15, weight="heavy", color="#004d40", ha="center")
    ax.text(0.5, 0.90, "Automated Cross-Verification from Mill Inward to District Treasury Delivery • Assam NESFIC-D-39", fontsize=10, color="#475569", ha="center")

    stages = [
        ("1. CENTRAL PAPER STORE\n(Bamunimaidam)", 
         "• 2,850 Reams Maplitho 70 GSM\n• 1,420 Reams Sunlit Bond 80 GSM\n• 48 Web Rotary Reels (60 GSM)\n• Mill Lot & GRN Registration", 
         "#ecfdf5", "#059669", 0.04),
        ("2. PRESS FLOOR ALLOCATION\n& TRIMMING WATCH", 
         "• Harris Web Offset Press #1\n• Heidelberg Sheet-fed Line #2\n• Scrap Trimming Loss: 1.8%\n• Automated Alert if Wastage >3%", 
         "#f0fdf4", "#16a34a", 0.28),
        ("3. THE ASSAM GAZETTE &\nSECURITY PRINTING", 
         "• Extraordinary Issue #488\n• 5,000 Verified Copies Run\n• SHA-256 Publication Seal\n• Assembly Budget Books Safe", 
         "#fefce8", "#ca8a04", 0.52),
        ("4. QR E-GATEPASS &\nHIGHWAY TRANSIT", 
         "• E-Gatepass #DPS/GP/2026/088\n• Dedicated Carrier AS-01-GC-4182\n• GPS Highway Telemetry (NH-715)\n• OTP Handshake at District Depot", 
         "#eff6ff", "#0284c7", 0.76)
    ]

    for title, desc, bg, border, x in stages:
        box = patches.FancyBboxPatch((x, 0.22), 0.20, 0.60, transform=ax.transAxes,
                                     boxstyle="round,pad=0.01,rounding_size=0.02",
                                     facecolor=bg, edgecolor=border, linewidth=2)
        ax.add_patch(box)
        hdr = patches.FancyBboxPatch((x, 0.70), 0.20, 0.12, transform=ax.transAxes,
                                    boxstyle="round,pad=0.005,rounding_size=0.01",
                                    facecolor=border, edgecolor=None)
        ax.add_patch(hdr)
        ax.text(x + 0.10, 0.76, title, transform=ax.transAxes, color="#ffffff", fontsize=9, weight="bold", ha="center", va="center")
        ax.text(x + 0.015, 0.46, desc, transform=ax.transAxes, color="#1e293b", fontsize=8.5, va="center", linespacing=1.5)

    # Interconnecting Arrows
    for x in [0.24, 0.48, 0.72]:
        ax.annotate("", xy=(x + 0.035, 0.52), xytext=(x + 0.005, 0.52),
                    arrowprops=dict(arrowstyle="->", color=GOV_GOLD, lw=3))

    # Bottom Metrics Strip
    ax.text(0.5, 0.10, "KPI STATS ➔  35 Districts Supported  •  Safety Buffer Watch (<800 Reams)  •  Zero Transit Blindspots  •  CAG GFR-19 Audit Ready",
            fontsize=9.5, weight="bold", color="#004d40", ha="center")

    out_path = os.path.join(ASSETS_DIR, "d39_fig_lifecycle_engine.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=100)
    plt.close()
    print("Generated:", out_path)

# 4. WIREFRAME 1: CENTRAL PAPER STORE & REEL/REAM INVENTORY REGISTER
def gen_wireframe1_store():
    fig, ax = plt.subplots(figsize=(13.76, 7.68), dpi=100)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Central Paper Store & Consumables Register", "https://mudran.sascol.com/inventory/stock-register")

    # Header Bar
    ax.text(0.04, 0.88, "Directorate of Printing & Stationery • Central Paper & Consumables Warehouse", color="#004d40", fontsize=14, weight="heavy")
    ax.text(0.04, 0.85, "Bamunimaidam, Guwahati • Real-Time Flat Sheet & Rotary Reel Stock with Mill Lot Verification", color="#64748b", fontsize=9.5)

    # 4 Metric Cards
    metrics = [
        ("TOTAL PAPER IN STOCK", "5,388 Reams", "Valued at ₹42.79 Lakhs", "#004d40", 0.04),
        ("ACTIVE ROTARY REELS", "48 Rolls", "Web Newsprint 84cm", "#0284c7", 0.28),
        ("ACTIVE PRESS RUNS", "3 Machine Lines", "Harris Web & Heidelberg", "#d97706", 0.52),
        ("BUFFER WATCH ALERTS", "0 Critical Items", "All Stock Above Safety Margin", "#16a34a", 0.76)
    ]
    for lbl, val, sub, col, x in metrics:
        card = patches.FancyBboxPatch((x, 0.69), 0.20, 0.13, transform=ax.transAxes,
                                      boxstyle="round,pad=0.01,rounding_size=0.015",
                                      facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.5)
        ax.add_patch(card)
        ax.text(x + 0.015, 0.79, lbl, transform=ax.transAxes, color="#64748b", fontsize=8, weight="bold")
        ax.text(x + 0.015, 0.74, val, transform=ax.transAxes, color=col, fontsize=14, weight="heavy")
        ax.text(x + 0.015, 0.705, sub, transform=ax.transAxes, color="#94a3b8", fontsize=7.5)

    # Main Table Simulation
    table_box = patches.FancyBboxPatch((0.04, 0.08), 0.92, 0.57, transform=ax.transAxes,
                                       boxstyle="round,pad=0.01,rounding_size=0.015",
                                       facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.5)
    ax.add_patch(table_box)
    ax.text(0.06, 0.61, "Central Paper Warehouse Stock Register (Sheds A, B, C)", fontsize=11, weight="bold", color="#0f172a")

    # Table Headers
    ax.text(0.06, 0.55, "ITEM ID / DESCRIPTION", fontsize=8.5, weight="bold", color="#64748b")
    ax.text(0.36, 0.55, "GSM & SIZE", fontsize=8.5, weight="bold", color="#64748b")
    ax.text(0.52, 0.55, "CURRENT STOCK", fontsize=8.5, weight="bold", color="#64748b")
    ax.text(0.68, 0.55, "BUFFER LIMIT", fontsize=8.5, weight="bold", color="#64748b")
    ax.text(0.82, 0.55, "STATUS", fontsize=8.5, weight="bold", color="#64748b")

    items = [
        ("PAP-MAP-70-001  White Maplitho Paper 70 GSM", "70 GSM (23x36 in)", "2,850 Reams", "800 Reams", "IN STOCK", "#16a34a"),
        ("PAP-BND-80-002  Executive Sunlit Bond Paper (Watermarked)", "80 GSM (A4 Size)", "1,420 Reams", "500 Reams", "IN STOCK", "#16a34a"),
        ("PAP-LDG-90-003  Azurelaid Ledger Paper (Land Jamabandi)", "90 GSM (17x27 in)", "680 Reams", "400 Reams", "NORMAL", "#0284c7"),
        ("PAP-ART-300-004 Gloss Art Board (Gazette & Budget Covers)", "300 GSM (22x28 in)", "390 Reams", "250 Reams", "NORMAL", "#0284c7"),
        ("PAP-REL-60-005  High-Speed Web Offset Reel (Gazette Newsprint)", "60 GSM (Width 84cm)", "48 Rolls", "20 Rolls", "RESERVE OK", "#16a34a"),
    ]
    y_row = 0.49
    for name, gsm, stock, buff, stat, col in items:
        row_bg = patches.Rectangle((0.06, y_row - 0.03), 0.88, 0.045, transform=ax.transAxes, facecolor="#f8fafc", edgecolor="#e2e8f0")
        ax.add_patch(row_bg)
        ax.text(0.07, y_row - 0.015, name, fontsize=8, weight="bold", color="#1e293b")
        ax.text(0.36, y_row - 0.015, gsm, fontsize=8, color="#475569")
        ax.text(0.52, y_row - 0.015, stock, fontsize=8, weight="bold", color="#004d40")
        ax.text(0.68, y_row - 0.015, buff, fontsize=8, color="#64748b")
        badge = patches.FancyBboxPatch((0.82, y_row - 0.025), 0.10, 0.03, transform=ax.transAxes,
                                       boxstyle="round,pad=0.002,rounding_size=0.01", facecolor="#ecfdf5", edgecolor=col)
        ax.add_patch(badge)
        ax.text(0.87, y_row - 0.015, stat, fontsize=7.5, weight="bold", color=col, ha="center")
        y_row -= 0.075

    out_path = os.path.join(ASSETS_DIR, "d39_wireframe1_store.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=100)
    plt.close()
    print("Generated:", out_path)

# 5. WIREFRAME 2: PRESS PRODUCTION FLOOR & THE ASSAM GAZETTE VAULT
def gen_wireframe2_press():
    fig, ax = plt.subplots(figsize=(13.76, 7.68), dpi=100)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Press Production Floor & Gazette Vault", "https://mudran.sascol.com/press/job-tickets")

    ax.text(0.04, 0.88, "Press Production Floor & The Assam Gazette (Asom Rajpatra) Vault", color="#004d40", fontsize=14, weight="heavy")
    ax.text(0.04, 0.85, "Real-Time Machine Impression Runs, Trimming Wastage % Telemetry & Cryptographic Gazette Stamping", color="#64748b", fontsize=9.5)

    # Left: Active Job Tickets (Width 0.54)
    left_card = patches.FancyBboxPatch((0.04, 0.08), 0.54, 0.74, transform=ax.transAxes,
                                      boxstyle="round,pad=0.01,rounding_size=0.015",
                                      facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1.5)
    ax.add_patch(left_card)
    ax.text(0.06, 0.78, "Active Press Production Job Tickets", fontsize=11, weight="bold", color="#0f172a")

    jobs = [
        ("JOB-2026-GAZ-119: The Assam Gazette Extraordinary #488",
         "Harris Web Offset Press #1  •  Target: 5,000 Copies\nPaper Used: Rotary Reel 60 GSM (25 Reams Eq.)\nStage: PRESS PRINTING  •  Trimming Wastage: 1.8% (OK)", "#059669"),
        ("JOB-2026-BDG-003: Assembly State Budget Estimates 2027",
         "Heidelberg Speedmaster Sheet-fed  •  Target: 1,200 Bound Volumes\nPaper Used: Maplitho 70 GSM (120 Reams)\nStage: PRE-PRESS PLATEMAKING  •  CONFIDENTIAL RUN", "#d97706"),
        ("JOB-2026-REV-077: Standard Jamabandi Register (Form 14)",
         "Automatic Section Stitching Line #3  •  Target: 3,000 Registers\nPaper Used: Azurelaid Ledger 90 GSM (150 Reams)\nStage: BINDING & FINISHING  •  Trimming Wastage: 2.6%", "#0284c7")
    ]
    y_job = 0.71
    for title, desc, col in jobs:
        jbox = patches.FancyBboxPatch((0.06, y_job - 0.16), 0.50, 0.16, transform=ax.transAxes,
                                     boxstyle="round,pad=0.005,rounding_size=0.01",
                                     facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=1)
        ax.add_patch(jbox)
        ax.text(0.08, y_job - 0.03, title, fontsize=9.5, weight="bold", color="#004d40")
        ax.text(0.08, y_job - 0.09, desc, fontsize=8, color="#334155", linespacing=1.4)
        y_job -= 0.21

    # Right: The Assam Gazette Vault (Width 0.36)
    right_card = patches.FancyBboxPatch((0.61, 0.08), 0.35, 0.74, transform=ax.transAxes,
                                       boxstyle="round,pad=0.01,rounding_size=0.015",
                                       facecolor="#fefce8", edgecolor="#fde047", linewidth=1.5)
    ax.add_patch(right_card)
    ax.text(0.63, 0.78, "The Assam Gazette (Asom Rajpatra) Vault", fontsize=11, weight="bold", color="#854d0e")
    ax.text(0.63, 0.74, "Serialized Tamper-Evident SHA-256 Gazette Ledger", fontsize=8, color="#a16207")

    gazettes = [
        ("Vol. 152, Extraordinary No. 488", "Publication Date: 2026-11-20\nDept: Personnel-A, Dispur\nSHA-256: e3b0c44298fc1c14... (Verified)"),
        ("Vol. 152, Ordinary Part IX No. 46", "Publication Date: 2026-11-18\nDept: Revenue & Disaster Mgmt\nSHA-256: c5d804828f7d95a8... (Verified)"),
        ("Vol. 152, Extraordinary No. 487", "Publication Date: 2026-11-15\nDept: Finance (Taxation), Dispur\nSHA-256: 7f83b1657ff1fc53... (Verified)"),
    ]
    y_gaz = 0.67
    for g_title, g_desc in gazettes:
        gbox = patches.FancyBboxPatch((0.63, y_gaz - 0.14), 0.31, 0.14, transform=ax.transAxes,
                                      boxstyle="round,pad=0.005,rounding_size=0.01",
                                      facecolor="#ffffff", edgecolor="#facc15", linewidth=1)
        ax.add_patch(gbox)
        ax.text(0.65, y_gaz - 0.03, g_title, fontsize=8.5, weight="bold", color="#713f12")
        ax.text(0.65, y_gaz - 0.08, g_desc, fontsize=7.5, color="#475569", linespacing=1.3)
        y_gaz -= 0.18

    out_path = os.path.join(ASSETS_DIR, "d39_wireframe2_press.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=100)
    plt.close()
    print("Generated:", out_path)

# 6. WIREFRAME 3: INTER-DISTRICT FLEET TRANSIT RADAR & GPS CORRIDOR TRACKER
def gen_wireframe3_transit():
    fig, ax = plt.subplots(figsize=(13.76, 7.68), dpi=100)
    ax.set_facecolor(BG_DARK)
    fig.patch.set_facecolor(BG_DARK)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Inter-District Fleet GPS Radar & Transit Tracker", "https://mudran.sascol.com/dispatch/transit-tracker")

    ax.text(0.04, 0.88, "INTER-DISTRICT FLEET GPS RADAR & TRANSIT CORRIDOR TRACKER", color=TEXT_WHITE, fontsize=14, weight="heavy")
    ax.text(0.04, 0.85, "Real-Time Consignment Movement from Bamunimaidam Central Press to 35 Assam District Treasuries", color=GOV_GOLD_SHINE, fontsize=10)

    # Radar Map Area
    map_box = patches.FancyBboxPatch((0.04, 0.18), 0.60, 0.64, transform=ax.transAxes,
                                     boxstyle="round,pad=0.01,rounding_size=0.015",
                                     facecolor="#06241b", edgecolor="#10b981", linewidth=1.5)
    ax.add_patch(map_box)
    ax.text(0.06, 0.78, "LIVE HIGHWAY GPS RADAR: ASSAM TRANSIT CORRIDORS", color="#a7f3d0", fontsize=11, weight="bold")

    # Stylized River & Highway
    ax.plot([0.08, 0.25, 0.45, 0.60], [0.55, 0.50, 0.42, 0.35], color="#0284c7", lw=5, alpha=0.5, transform=ax.transAxes)
    ax.text(0.35, 0.46, "Brahmaputra River Corridor", color="#38bdf8", fontsize=8, transform=ax.transAxes)

    # Highway line
    ax.plot([0.15, 0.30, 0.46, 0.58], [0.45, 0.40, 0.32, 0.28], color=GOV_GOLD_SHINE, lw=2.5, ls="--", transform=ax.transAxes)

    # Waypoint Nodes
    nodes = [
        (0.15, 0.45, "Bamunimaidam Press\n(Guwahati)", "#f59e0b"),
        (0.30, 0.40, "Nagaon Depot\n(Toll Plaza)", "#10b981"),
        (0.46, 0.32, "Kaziranga Kohora\n(Transit Sentry)", "#f59e0b"),
        (0.58, 0.28, "Jorhat DC Depot\n(Destination)", "#10b981")
    ]
    for x, y, name, col in nodes:
        ax.plot(x, y, "o", color=col, markersize=10, transform=ax.transAxes)
        ax.text(x, y + 0.04, name, color="#ffffff", fontsize=8, weight="bold", ha="center", transform=ax.transAxes)

    # Moving Vehicle
    ax.plot(0.42, 0.35, "s", color="#ef4444", markersize=12, transform=ax.transAxes)
    ax.text(0.42, 0.39, "TRUCK: AS-03-BC-7819\n(In Transit - 62 km/h)", color="#fef08a", fontsize=8, weight="bold", ha="center", transform=ax.transAxes)

    # Right: Telemetry Panel
    telem_box = patches.FancyBboxPatch((0.66, 0.18), 0.30, 0.64, transform=ax.transAxes,
                                       boxstyle="round,pad=0.01,rounding_size=0.015",
                                       facecolor=CARD_DARK, edgecolor=GOV_GOLD, linewidth=1.5)
    ax.add_patch(telem_box)
    ax.text(0.68, 0.78, "Vehicle Telemetry & Consignment", color=GOV_GOLD_SHINE, fontsize=11, weight="bold")

    telem_items = [
        "Gatepass: DPS/GP/2026/JHT/092",
        "Carrier: Assam State Transport Corp",
        "Driver: Moheshwar Deka (+91-94350*)",
        "Vehicle Reg: AS-03-BC-7819",
        "Destination: Jorhat DC Depot",
        "Gross Weight: 1,840 Kg (140 Bundles)",
        "Cargo: 80 Reams Azurelaid Ledger\n+ 120 Periodic Patta Registers",
        "ETA: Today, 18:00 IST",
        "Handshake OTP: #882190 (Generated)",
        "QR Status: VALID / UNTAMPERED"
    ]
    y_t = 0.72
    for item in telem_items:
        ax.text(0.68, y_t, item, color="#e2e8f0", fontsize=8, linespacing=1.3)
        y_t -= 0.055

    out_path = os.path.join(ASSETS_DIR, "d39_wireframe3_transit.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=100)
    plt.close()
    print("Generated:", out_path)

# 7. WIREFRAME 4: OFFICIAL TAMPER-EVIDENT QR E-GATEPASS & OTP VERIFICATION
def gen_wireframe4_gatepass():
    fig, ax = plt.subplots(figsize=(13.76, 7.68), dpi=100)
    ax.set_facecolor("#f8fafc")
    fig.patch.set_facecolor("#f8fafc")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Official E-Gatepass QR Verification Pass", "https://mudran.sascol.com/dispatch/gatepass")

    ax.text(0.04, 0.88, "Official Tamper-Evident QR E-Gatepass & Handshake Verification", color="#004d40", fontsize=14, weight="heavy")
    ax.text(0.04, 0.85, "Statutory Security Gatepass for Inter-District Government Stationery Transit • Government of Assam", color="#64748b", fontsize=9.5)

    # Certificate Container
    pass_box = patches.FancyBboxPatch((0.15, 0.08), 0.70, 0.74, transform=ax.transAxes,
                                      boxstyle="round,pad=0.015,rounding_size=0.02",
                                      facecolor="#ffffff", edgecolor="#004d40", linewidth=2.5)
    ax.add_patch(pass_box)

    # Pass Header
    ax.text(0.50, 0.76, "GOVERNMENT OF ASSAM • DIRECTORATE OF PRINTING & STATIONERY", fontsize=11, weight="bold", color="#004d40", ha="center")
    ax.text(0.50, 0.725, "BAMUNIMAIDAM, GUWAHATI - 781021 • OFFICIAL CONSIGNMENT E-GATEPASS", fontsize=9, color="#64748b", ha="center")

    ax.plot([0.20, 0.80], [0.705, 0.705], color="#d97706", lw=1.5, transform=ax.transAxes)

    # Pass Details (2 Columns)
    col1 = [
        ("Gatepass Number:", "DPS/GP/2026/KAM/088"),
        ("Requisition Indent No:", "IND/KAM-METRO/STN/2026/892"),
        ("Origin Press Store:", "Central Store Shed A, Bamunimaidam"),
        ("Destination Facility:", "District Treasury & Stationery Store, Panbazar"),
        ("Destination District:", "Kamrup Metropolitan, Assam")
    ]
    col2 = [
        ("Vehicle Registration:", "AS-01-GC-4182 (Dedicated E-Truck)"),
        ("Driver In-Charge:", "Prabin Chandra Bora (+91-98640*)"),
        ("Consignment Gross:", "890.0 Kg (65 Bundles)"),
        ("Contents Description:", "150 Reams Sunlit Bond + 500 Challan Books"),
        ("Departure Timestamp:", "2026-11-20T10:00:00+05:30")
    ]
    y_p = 0.65
    for lbl, val in col1:
        ax.text(0.20, y_p, lbl, fontsize=8.5, color="#64748b", weight="bold")
        ax.text(0.20, y_p - 0.03, val, fontsize=9, color="#0f172a", weight="bold")
        y_p -= 0.075

    y_p = 0.65
    for lbl, val in col2:
        ax.text(0.52, y_p, lbl, fontsize=8.5, color="#64748b", weight="bold")
        ax.text(0.52, y_p - 0.03, val, fontsize=9, color="#0f172a", weight="bold")
        y_p -= 0.075

    # Bottom Seal & QR Verification Box
    ax.plot([0.20, 0.80], [0.26, 0.26], color="#cbd5e1", lw=1, transform=ax.transAxes)

    ax.text(0.20, 0.22, "CRYPTOGRAPHIC QR TOKEN: DPS-GP-KAM-98012-VERIFIED-AUTH", fontsize=8.5, family="monospace", color="#004d40", weight="bold")
    ax.text(0.20, 0.18, "Digital Signature: SHA-256 Chained Integrity • Verified by State Dispatcher", fontsize=8, color="#64748b")
    ax.text(0.20, 0.14, "Delivery Acknowledged by: S. N. Goswami (Treasury Store Officer, Kamrup)", fontsize=8, color="#16a34a", weight="bold")

    # Simulated QR Stamp
    stamp_box = patches.FancyBboxPatch((0.70, 0.13), 0.08, 0.10, transform=ax.transAxes,
                                       boxstyle="round,pad=0.005,rounding_size=0.01",
                                       facecolor="#ecfdf5", edgecolor="#059669", linewidth=1.5)
    ax.add_patch(stamp_box)
    ax.text(0.74, 0.18, "QR CODE\nVERIFIED", fontsize=7.5, weight="bold", color="#059669", ha="center", va="center")

    out_path = os.path.join(ASSETS_DIR, "d39_wireframe4_gatepass.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=100)
    plt.close()
    print("Generated:", out_path)

# 8. 5-VECTOR TRIMMING LOSS & BUFFER RISK TRIAGE FRAMEWORK
def gen_wastage_framework():
    fig, ax = plt.subplots(figsize=(13.76, 7.68), dpi=100)
    ax.set_facecolor("#ffffff")
    fig.patch.set_facecolor("#ffffff")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.94, "5-VECTOR PRESS PRODUCTION & INVENTORY DEFECT CATALOG", fontsize=15, weight="heavy", color="#004d40", ha="center")
    ax.text(0.5, 0.90, "Statutory Discrepancy Dimensions, Wastage Formulations & Penalty Rules • Assam NESFIC-D-39", fontsize=10, color="#475569", ha="center")

    vectors = [
        ("VECTOR 1: EXCESS TRIMMING LOSS", "Trimming scrap >3.0% of allocated paper ream weight.", "Wastage % = ((Allocated - Finished) / Allocated) * 100", "PENALTY: 35 pts\nREMEDY: Press machine alignment & blade recalibration.", "#ef4444", 0.04),
        ("VECTOR 2: BUFFER STOCK BREACH", "Ream stock drops below minimum safety threshold.", "Condition: CurrentStock <= SafetyThreshold (e.g. <800 reams)", "PENALTY: 25 pts\nREMEDY: Automated emergency indent & mill PO trigger.", "#f59e0b", 0.23),
        ("VECTOR 3: QUOTA EXCEEDANCE INDENT", "Department indent exceeds approved finance annual quota.", "Condition: RequestedQty > (AnnualQuota - IssuedSoFar)", "PENALTY: 20 pts\nREMEDY: Finance Department special sanction review.", "#3b82f6", 0.42),
        ("VECTOR 4: TRANSIT DELAY DRIFT", "Consignment highway transit exceeds SLA ETA by >4 hrs.", "Condition: (CurrentTime - DepartureTime) > StandardSLA", "PENALTY: 25 pts\nREMEDY: Automated police checkpoint ping & driver alert.", "#8b5cf6", 0.61),
        ("VECTOR 5: RECONCILIATION DISCREPANCY", "Delivered ream count differs from dispatched manifest.", "Condition: DeliveredCount != DispatchedManifestCount", "PENALTY: 40 pts\nREMEDY: Mandatory joint inquiry under GFR Rule 211.", "#dc2626", 0.80),
    ]

    for title, desc, formula, rem, col, x in vectors:
        vbox = patches.FancyBboxPatch((x, 0.15), 0.17, 0.70, transform=ax.transAxes,
                                      boxstyle="round,pad=0.008,rounding_size=0.015",
                                      facecolor="#f8fafc", edgecolor=col, linewidth=2)
        ax.add_patch(vbox)
        hdr = patches.FancyBboxPatch((x, 0.76), 0.17, 0.08, transform=ax.transAxes,
                                    boxstyle="round,pad=0.004,rounding_size=0.01",
                                    facecolor=col, edgecolor=None)
        ax.add_patch(hdr)
        ax.text(x + 0.085, 0.80, title, color="#ffffff", fontsize=7.5, weight="bold", ha="center", va="center")
        ax.text(x + 0.01, 0.68, desc, color="#1e293b", fontsize=7.5, linespacing=1.3)
        
        # Formula box
        fbox = patches.Rectangle((x + 0.008, 0.45), 0.154, 0.18, transform=ax.transAxes, facecolor="#ffffff", edgecolor="#cbd5e1")
        ax.add_patch(fbox)
        ax.text(x + 0.015, 0.54, formula, color="#475569", fontsize=6.8, linespacing=1.3)
        
        ax.text(x + 0.01, 0.30, rem, color="#7f1d1d" if "40" in rem or "35" in rem else "#1e293b", fontsize=7.2, linespacing=1.3)

    ax.text(0.5, 0.06, "Automated Continuous Monitoring  •  Zero Manual Manipulation  •  Full GFR-19 & CAG Compliance",
            fontsize=9.5, weight="bold", color="#004d40", ha="center")

    out_path = os.path.join(ASSETS_DIR, "d39_fig_wastage_framework.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=100)
    plt.close()
    print("Generated:", out_path)

if __name__ == "__main__":
    gen_paradigm_shift()
    gen_architecture()
    gen_lifecycle_engine()
    gen_wireframe1_store()
    gen_wireframe2_press()
    gen_wireframe3_transit()
    gen_wireframe4_gatepass()
    gen_wastage_framework()
