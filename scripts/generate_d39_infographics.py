#!/usr/bin/env python3
"""
Generate High-Impact 16:9 Widescreen Technological Framework Infographics
for Mudran-Sewa (NESFIC-D-39) matching the exact architectural infographic style
of the Data Centers project (/Users/kalyan/Downloads/2026/Sep2026/Data Centers and Way Head).

Features:
- Exact 16:9 widescreen aspect ratio (2752 x 1548 px at 200 DPI)
- Clean white background with architectural light-gray blueprint gridlines
- Prominent dark navy headers with professional subtitles and status badges
- Modular color-coded diagnostic panels (Royal Blue, Cyan, Emerald Green, Amber, Purple)
- Crisp technical schematics, mathematical formulas, checklist badges, and flow arrows
- Perfect text wrapping (using textwrap) ensuring zero text collisions
"""

import os
import textwrap
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import numpy as np

ASSETS_DIR = os.path.abspath("docs/assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# High-Impact Corporate Technical Palette (Data Centers & Assam Govt Press)
C_BG = "#ffffff"
C_GRID = "#f1f5f9"
C_GRID_MAJOR = "#e2e8f0"
C_NAVY_DARK = "#0a192f"
C_NAVY_TITLE = "#0f172a"
C_SUBTITLE = "#334155"
C_MUTED = "#64748b"

# Accent Tiers / Pillars
C_PILLAR_BLUE = "#1d4ed8"      # Royal Blue
C_PILLAR_CYAN = "#0284c7"      # Electric Cyan
C_PILLAR_EMERALD = "#059669"   # Assam Emerald Green
C_PILLAR_AMBER = "#d97706"     # Gold / Amber
C_PILLAR_PURPLE = "#7c3aed"    # Saffron / Purple
C_PILLAR_CRIMSON = "#dc2626"   # Alert Crimson

def draw_blueprint_grid(ax):
    """Draws subtle architectural blueprint gridlines."""
    for x in np.linspace(0, 1, 41):
        ax.axvline(x, color=C_GRID, linewidth=0.5, zorder=0)
    for y in np.linspace(0, 1, 23):
        ax.axhline(y, color=C_GRID, linewidth=0.5, zorder=0)
    for x in np.linspace(0, 1, 9):
        ax.axvline(x, color=C_GRID_MAJOR, linewidth=0.8, linestyle="--", alpha=0.6, zorder=0)
    for y in np.linspace(0, 1, 5):
        ax.axhline(y, color=C_GRID_MAJOR, linewidth=0.8, linestyle="--", alpha=0.6, zorder=0)

def draw_header(ax, title, subtitle, badge_text=None, badge_color=C_PILLAR_EMERALD):
    """Draws bold top header banner with optional status badge."""
    ax.text(0.035, 0.950, title, fontsize=16.5, weight="bold", color=C_NAVY_TITLE, ha="left", va="center", family="sans-serif")
    ax.text(0.035, 0.908, subtitle, fontsize=9.8, weight="bold", color=C_SUBTITLE, ha="left", va="center", family="sans-serif")
    
    if badge_text:
        badge = FancyBboxPatch((0.835, 0.915), 0.130, 0.045, transform=ax.transAxes,
                               boxstyle="round,pad=0.005,rounding_size=0.010",
                               facecolor="#ffffff", edgecolor=badge_color, linewidth=1.5, zorder=10)
        ax.add_patch(badge)
        ax.text(0.900, 0.937, badge_text, fontsize=8.5, weight="bold", color=badge_color, ha="center", va="center", zorder=11)

def draw_browser_chrome(ax, title, url="https://mudran.sascol.com"):
    """Draws clean browser window bar for wireframes."""
    bar = Rectangle((0.02, 0.93), 0.96, 0.055, transform=ax.transAxes, facecolor="#0f172a", edgecolor=None, zorder=10)
    ax.add_patch(bar)
    # 3 dots
    ax.add_patch(Circle((0.04, 0.957), 0.006, transform=ax.transAxes, facecolor="#ef4444", zorder=11))
    ax.add_patch(Circle((0.055, 0.957), 0.006, transform=ax.transAxes, facecolor="#f59e0b", zorder=11))
    ax.add_patch(Circle((0.07, 0.957), 0.006, transform=ax.transAxes, facecolor="#10b981", zorder=11))
    # URL Pill
    url_box = FancyBboxPatch((0.10, 0.938), 0.45, 0.038, transform=ax.transAxes,
                            boxstyle="round,pad=0.004,rounding_size=0.01",
                            facecolor="#1e293b", edgecolor="#334155", linewidth=1, zorder=11)
    ax.add_patch(url_box)
    ax.text(0.11, 0.957, f"SECURE GOVT SSL | {url}", transform=ax.transAxes, color="#38bdf8", fontsize=8.5, va="center", zorder=12, family="monospace")
    ax.text(0.96, 0.957, title, transform=ax.transAxes, color="#ffffff", fontsize=10, weight="bold", ha="right", va="center", zorder=12)


# =============================================================================
# 1. FIGURE 1: 4-TIER CLOUD-EDGE SYSTEM ARCHITECTURE
# =============================================================================
def gen_figure_architecture():
    fig, ax = plt.subplots(figsize=(13.76, 7.74), dpi=200)
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    draw_blueprint_grid(ax)

    draw_header(ax,
                "MUDRAN-SEWA: 4-TIER CLOUD-EDGE SYSTEM ARCHITECTURE",
                "Directorate of Printing & Stationery, Assam (Bamunimaidam, Guwahati) • NESFIC-D-39",
                "Assam SDC Certified", C_PILLAR_EMERALD)

    tiers = [
        {
            "num": "TIER 1", "title": "Client Multi-Persona Layer", "color": C_PILLAR_BLUE, "bg": "#eff6ff", "border": "#93c5fd",
            "subtitle": "Progressive Web Apps & Scanners",
            "items": [
                ("Storekeeper Inward PWA", "Reel & Ream GRN check-in, barcode scanning, mill lot logging"),
                ("Press Floor Superintendent", "Harris Web & Heidelberg job queue, machine speed telemetry"),
                ("District e-Indent Portal", "35 DC Commissionerates quota check & digital sanction orders"),
                ("Transit Fleet Scanner", "Driver handheld scanner, QR E-Gatepass decode & GPS tracking")
            ],
            "metrics": ["Sub-Second", "Offline DB"]
        },
        {
            "num": "TIER 2", "title": "Cloudflare Edge & SDC Gateway", "color": C_PILLAR_CYAN, "bg": "#f0fdfa", "border": "#99f6e4",
            "subtitle": "Serverless Routing & Security",
            "items": [
                ("Cloudflare Pages Edge", "Edge REST APIs (<50ms global latency across 300+ PoPs)"),
                ("State Data Centre Proxy", "Assam SDC sovereign proxy ensuring in-state data custody"),
                ("Authentication & RBAC", "JWT session tokens, cryptographic roles (Store, Press, DC, Admin)"),
                ("WAF & Rate Limiting", "Enterprise DDoS shielding, OWASP SQLi/XSS filtering & CSP")
            ],
            "metrics": ["< 50ms Edge", "Zero-Trust"]
        },
        {
            "num": "TIER 3", "title": "Core Microservices Engine", "color": C_PILLAR_EMERALD, "bg": "#ecfdf5", "border": "#a7f3d0",
            "subtitle": "Statutory Calculation Pipeline",
            "items": [
                ("Raw Material Stock Ledger", "Real-time GSM/weight math, lot buffer alert (<800 reams)"),
                ("Press Scrap Telemetry", "Real-time trimming scrap math: ScrapLoss(%) > 3.0% alert"),
                ("e-Indent Sanction Service", "Department quota verification, automated sanction slip"),
                ("Gazette Vault Signer", "The Assam Gazette (Asom Rajpatra) SHA-256 digital checksums")
            ],
            "metrics": ["Reconciled", "< 2% Scrap"]
        },
        {
            "num": "TIER 4", "title": "Data Persistence & Audit Vault", "color": C_PILLAR_AMBER, "bg": "#fffbeb", "border": "#fde68a",
            "subtitle": "Relational Storage & Audit Trail",
            "items": [
                ("Cloudflare D1 / PostgreSQL", "Relational ACID schema for inventory, indents & gatepasses"),
                ("PostGIS Spatial Corridors", "Assam transit corridors (NH-27, NH-715, NH-37 waypoints)"),
                ("Chained SHA-256 Audit Trail", "Append-only ledger satisfying CAG Form GFR-19 annual audits"),
                ("Object Store (R2 / S3)", "Encrypted storage for scanned GRN receipts & gazette PDFs")
            ],
            "metrics": ["100% ACID", "GFR-19 Ready"]
        }
    ]

    card_width = 0.222
    gap = 0.02
    left_start = 0.035
    card_height = 0.72

    for i, t in enumerate(tiers):
        x = left_start + i * (card_width + gap)
        y = 0.12

        # Outer card
        card = FancyBboxPatch((x, y), card_width, card_height, transform=ax.transAxes,
                              boxstyle="round,pad=0.005,rounding_size=0.015",
                              facecolor=t["bg"], edgecolor=t["border"], linewidth=1.5, zorder=2)
        ax.add_patch(card)

        # Header Pill
        hdr = FancyBboxPatch((x, y + card_height - 0.088), card_width, 0.088, transform=ax.transAxes,
                             boxstyle="round,pad=0.005,rounding_size=0.015",
                             facecolor=t["color"], edgecolor=None, zorder=3)
        ax.add_patch(hdr)
        ax.text(x + 0.015, y + card_height - 0.026, t["num"], fontsize=8.5, weight="bold", color="#ffffff", zorder=4)
        ax.text(x + 0.015, y + card_height - 0.052, t["title"], fontsize=9.6, weight="bold", color="#ffffff", zorder=4)
        ax.text(x + 0.015, y + card_height - 0.074, t["subtitle"], fontsize=7.2, color="#f1f5f9", zorder=4)

        # Items with textwrap to strictly contain within box
        item_y = y + card_height - 0.118
        for header_text, desc_text in t["items"]:
            ax.add_patch(Circle((x + 0.014, item_y - 0.006), 0.004, transform=ax.transAxes, facecolor=t["color"], zorder=5))
            ax.text(x + 0.024, item_y, header_text, fontsize=8.5, weight="bold", color=C_NAVY_TITLE, zorder=5)
            
            wrapped = textwrap.fill(desc_text, width=28)
            ax.text(x + 0.024, item_y - 0.022, wrapped, fontsize=7.2, color="#475569", zorder=5, va="top")
            item_y -= 0.122

        # Metric Badges at bottom
        bx = x + 0.012
        badge_y = y + 0.022
        for b in t["metrics"]:
            bw = 0.095
            bp = FancyBboxPatch((bx, badge_y), bw, 0.032, transform=ax.transAxes,
                                boxstyle="round,pad=0.003,rounding_size=0.006",
                                facecolor="#ffffff", edgecolor=t["color"], linewidth=1, zorder=6)
            ax.add_patch(bp)
            ax.text(bx + bw/2, badge_y + 0.016, b, fontsize=6.8, weight="bold", color=t["color"], ha="center", va="center", zorder=7)
            bx += bw + 0.008

        # Horizontal flow connector arrows
        if i < len(tiers) - 1:
            ax.annotate("", xy=(x + card_width + gap + 0.003, 0.48), xytext=(x + card_width - 0.003, 0.48),
                        arrowprops=dict(arrowstyle="->", color=C_MUTED, lw=2.2, mutation_scale=14), zorder=8)

    out_path = os.path.join(ASSETS_DIR, "d39_fig_architecture.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Generated: {out_path}")


# =============================================================================
# 2. FIGURE 2: END-TO-END STATIONERY LIFECYCLE & SUPPLY CHAIN PIPELINE
# =============================================================================
def gen_figure_lifecycle():
    fig, ax = plt.subplots(figsize=(13.76, 7.74), dpi=200)
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    draw_blueprint_grid(ax)

    draw_header(ax,
                "END-TO-END STATIONERY LIFECYCLE & SUPPLY CHAIN PIPELINE",
                "Government of Assam • Directorate of Printing & Stationery (Bamunimaidam, Guwahati) • NESFIC-D-39",
                "Full Closed Loop", C_PILLAR_EMERALD)

    stages = [
        {
            "step": "STAGE 1", "title": "Paper Mill Inflow & GRN", "color": C_PILLAR_BLUE, "bg": "#eff6ff", "border": "#93c5fd",
            "desc": "Raw Paper Reel Reception",
            "points": ["Mill lot serialization (Maplitho, Bond, Ledger)", "Inward Goods Received Note (GRN) creation", "GSM & basis weight calibration (60–300 GSM)", "Automated buffer threshold (<800 reams alert)"]
        },
        {
            "step": "STAGE 2", "title": "e-Indent Quota Sanction", "color": C_PILLAR_CYAN, "bg": "#f0fdfa", "border": "#99f6e4",
            "desc": "Department Requisitions",
            "points": ["35 District DC Offices submit requisitions", "Automated department stationery quota check", "Priority tagging (Routine, Assembly, Election)", "Instant digital Sanction Order issuance (<24h)"]
        },
        {
            "step": "STAGE 3", "title": "Press Floor & Scrap Guard", "color": C_PILLAR_EMERALD, "bg": "#ecfdf5", "border": "#a7f3d0",
            "desc": "Multi-Line Printing Execution",
            "points": ["Harris Web Offset & Heidelberg line scheduling", "The Assam Gazette (Asom Rajpatra) production", "Real-time paper consumption telemetry", "Automated trimming scrap alert (>3.0% danger)"]
        },
        {
            "step": "STAGE 4", "title": "Packaging & QR Gatepass", "color": C_PILLAR_AMBER, "bg": "#fffbeb", "border": "#fde68a",
            "desc": "Security & Gate Dispatch",
            "points": ["Finished stationery carton packing & sealing", "Instant generation of QR E-Gatepass", "Vehicle reg (AS-01-GC-4412) & driver phone link", "SHA-256 cryptographic tamper-evident seal"]
        },
        {
            "step": "STAGE 5", "title": "Transit & District Handshake", "color": C_PILLAR_PURPLE, "bg": "#faf5ff", "border": "#e9d5ff",
            "desc": "Highway Corridors & Delivery",
            "points": ["Highway tracking along NH-27, NH-715, NH-37", "Inter-district transit checkpoint logging", "District Treasury Officer OTP delivery handshake", "Instant stock reconciliation with zero leakage"]
        }
    ]

    card_w = 0.174
    gap = 0.02
    left_start = 0.028
    card_h = 0.70

    for i, s in enumerate(stages):
        x = left_start + i * (card_w + gap)
        y = 0.14

        card = FancyBboxPatch((x, y), card_w, card_h, transform=ax.transAxes,
                              boxstyle="round,pad=0.005,rounding_size=0.015",
                              facecolor=s["bg"], edgecolor=s["border"], linewidth=1.5, zorder=2)
        ax.add_patch(card)

        # Step Pill
        hdr = FancyBboxPatch((x, y + card_h - 0.082), card_w, 0.082, transform=ax.transAxes,
                             boxstyle="round,pad=0.005,rounding_size=0.015",
                             facecolor=s["color"], edgecolor=None, zorder=3)
        ax.add_patch(hdr)
        ax.text(x + 0.010, y + card_h - 0.026, s["step"], fontsize=8, weight="bold", color="#ffffff", zorder=4)
        ax.text(x + 0.010, y + card_h - 0.050, s["title"], fontsize=8.6, weight="bold", color="#ffffff", zorder=4)
        ax.text(x + 0.010, y + card_h - 0.070, s["desc"], fontsize=6.8, color="#f1f5f9", zorder=4)

        # Bullets wrapped cleanly
        by = y + card_h - 0.110
        for p in s["points"]:
            ax.add_patch(Circle((x + 0.012, by - 0.006), 0.0035, transform=ax.transAxes, facecolor=s["color"], zorder=5))
            wrapped_p = textwrap.fill(p, width=22)
            ax.text(x + 0.022, by, wrapped_p, fontsize=7.1, color="#1e293b", zorder=5, va="top")
            by -= 0.125

        # Flow arrow between cards
        if i < len(stages) - 1:
            ax.annotate("", xy=(x + card_w + gap + 0.002, 0.49), xytext=(x + card_w - 0.002, 0.49),
                        arrowprops=dict(arrowstyle="->", color=C_PILLAR_EMERALD, lw=2.2, mutation_scale=14), zorder=8)

    # Bottom Milestone Banner
    banner_box = FancyBboxPatch((0.028, 0.035), 0.944, 0.065, transform=ax.transAxes,
                                boxstyle="round,pad=0.005,rounding_size=0.01",
                                facecolor="#004d40", edgecolor="#065f46", linewidth=1.5, zorder=2)
    ax.add_patch(banner_box)
    ax.text(0.5, 0.076, "TRANSFORMATION TARGETS & BENCHMARK GAINS", fontsize=9, weight="bold", color="#f59e0b", ha="center", zorder=3)
    ax.text(0.5, 0.050, "Indent Turnaround: 21 Days -> < 24 Hours  |  Press Trimming Scrap: >5% -> <2.0%  |  Highway Transit Reconciled: 100%  |  Annual Savings: Rs. 45+ Lakhs",
            fontsize=8.2, weight="bold", color="#ffffff", ha="center", zorder=3)

    out_path = os.path.join(ASSETS_DIR, "d39_fig_lifecycle_engine.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Generated: {out_path}")


# =============================================================================
# 3. FIGURE 3: PRESS TRIMMING SCRAP & BINDING WASTAGE CONTROL FRAMEWORK
# =============================================================================
def gen_figure_wastage():
    fig, ax = plt.subplots(figsize=(13.76, 7.74), dpi=200)
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    draw_blueprint_grid(ax)

    draw_header(ax,
                "PRESS TRIMMING SCRAP & WASTAGE CONTROL FRAMEWORK",
                "Algorithmic Material Anomaly Detection & Raw Paper Conservation • NESFIC-D-39",
                "Max Tolerance < 3.0%", C_PILLAR_AMBER)

    cards = [
        {
            "title": "1. Paper Basis Specifications", "color": C_PILLAR_BLUE, "bg": "#eff6ff", "border": "#93c5fd",
            "items": [
                ("Maplitho 60–80 GSM", "Harris Web Offset text, ordinary gazette, treasury challans"),
                ("Executive Bond 80 GSM", "Confidential Assembly bills, legislative budget estimates"),
                ("Azurelaid Ledger 90 GSM", "Land Revenue Jamabandi/Patta permanent registers"),
                ("Gloss Art Board 300 GSM", "High-durability statutory covers, rule books & binders")
            ]
        },
        {
            "title": "2. Machine Line Tolerances", "color": C_PILLAR_CYAN, "bg": "#f0fdfa", "border": "#99f6e4",
            "items": [
                ("Harris Web Offset Rotary", "Reel-fed maplitho, 12mm web edge trim, Max Scrap: 3.0%"),
                ("Heidelberg Sheet-Fed #2", "Guillotine head/foot cut, 6mm allowance, Max Scrap: 2.0%"),
                ("High-Speed Sheet-Fed #3", "Revenue register forms, 6mm trim, Max Scrap: 2.0%"),
                ("Art Board Cutting Line #4", "Spine, creasing & edge trim, Max Scrap: 2.5%")
            ]
        },
        {
            "title": "3. Mathematical Formulation", "color": C_PILLAR_EMERALD, "bg": "#ecfdf5", "border": "#a7f3d0",
            "items": [
                ("Trimming Scrap Formula", "ScrapLoss(%) = [(W_in - W_good) / W_in] × 100"),
                ("Threshold Alert Rule", "IF ScrapLoss(%) > 3.0% -> TRIGGER RED MACHINE PAUSE"),
                ("Safety Buffer Formula", "Stock < (DailyRate × LeadDays) + ReserveBuffer"),
                ("Reconciliation Metric", "Paper_Guwahati(kg) == Stationery_District(kg)")
            ]
        },
        {
            "title": "4. Corrective Enforcement", "color": C_PILLAR_AMBER, "bg": "#fffbeb", "border": "#fde68a",
            "items": [
                ("Sub-3% Normal Run", "Auto-clearance to folding & automated binding lines"),
                (">3% Anomaly Alarm", "Guillotine auto-pause & alert to Press Superintendent"),
                ("Mill Roll Defect Flag", "Paper tear or GSM discrepancy logged to supplier GRN"),
                ("CAG Audit Reconciliation", "Form GFR-19 scrap report pinned with SHA-256")
            ]
        }
    ]

    card_w = 0.222
    gap = 0.02
    left_start = 0.035
    card_h = 0.54

    for i, c in enumerate(cards):
        x = left_start + i * (card_w + gap)
        y = 0.31

        card = FancyBboxPatch((x, y), card_w, card_h, transform=ax.transAxes,
                              boxstyle="round,pad=0.005,rounding_size=0.015",
                              facecolor=c["bg"], edgecolor=c["border"], linewidth=1.5, zorder=2)
        ax.add_patch(card)

        # Header Pill
        hdr = FancyBboxPatch((x, y + card_h - 0.075), card_w, 0.075, transform=ax.transAxes,
                             boxstyle="round,pad=0.005,rounding_size=0.015",
                             facecolor=c["color"], edgecolor=None, zorder=3)
        ax.add_patch(hdr)
        ax.text(x + 0.012, y + card_h - 0.045, c["title"], fontsize=9.2, weight="bold", color="#ffffff", zorder=4)

        # Items wrapped cleanly
        iy = y + card_h - 0.105
        for title_text, desc_text in c["items"]:
            ax.add_patch(Circle((x + 0.014, iy - 0.006), 0.0035, transform=ax.transAxes, facecolor=c["color"], zorder=5))
            ax.text(x + 0.022, iy, title_text, fontsize=8.4, weight="bold", color=C_NAVY_TITLE, zorder=5)
            
            wrapped_desc = textwrap.fill(desc_text, width=28)
            ax.text(x + 0.022, iy - 0.020, wrapped_desc, fontsize=7.1, color="#475569", zorder=5, va="top")
            iy -= 0.105

    # Bottom Big Banner: Mathematical Callout & Economic Impact
    box_bot = FancyBboxPatch((0.035, 0.04), 0.93, 0.23, transform=ax.transAxes,
                            boxstyle="round,pad=0.008,rounding_size=0.015",
                            facecolor="#00332c", edgecolor="#004d40", linewidth=1.5, zorder=2)
    ax.add_patch(box_bot)

    ax.text(0.5, 0.23, "MATHEMATICAL FORMULATION & ANNUAL RAW MATERIAL CONSERVATION IMPACT",
            fontsize=10, weight="bold", color="#f59e0b", ha="center", zorder=3)

    # Left formula box
    f_box = FancyBboxPatch((0.055, 0.065), 0.43, 0.14, transform=ax.transAxes,
                           boxstyle="round,pad=0.005,rounding_size=0.01",
                           facecolor="#00241e", edgecolor="#065f46", linewidth=1, zorder=4)
    ax.add_patch(f_box)
    ax.text(0.07, 0.175, "Trimming Scrap Loss % Formulation:", fontsize=8.2, weight="bold", color="#a7f3d0", zorder=5)
    ax.text(0.07, 0.145, "ScrapLoss(%) = [ (Input_kg - GoodProduct_kg) / Input_kg ] × 100", fontsize=7.8, weight="bold", color="#ffffff", family="monospace", zorder=5)
    ax.text(0.07, 0.115, "Safety Buffer Reorder Trigger Formulation:", fontsize=8.2, weight="bold", color="#a7f3d0", zorder=5)
    ax.text(0.07, 0.085, "ReorderTrigger = CurrentStock < (DailyRate × LeadDays) + SafetyReserve", fontsize=7.8, weight="bold", color="#ffffff", family="monospace", zorder=5)

    # Right impact box
    i_box = FancyBboxPatch((0.515, 0.065), 0.43, 0.14, transform=ax.transAxes,
                           boxstyle="round,pad=0.005,rounding_size=0.01",
                           facecolor="#00241e", edgecolor="#065f46", linewidth=1, zorder=4)
    ax.add_patch(i_box)
    ax.text(0.53, 0.175, "Economic Impact for Assam State Press:", fontsize=8.2, weight="bold", color="#fde68a", zorder=5)
    ax.text(0.53, 0.145, "• Historical Scrap Rate: > 5.5% paper trimming & binding scrap loss", fontsize=7.4, color="#ffffff", zorder=5)
    ax.text(0.53, 0.120, "• Mudran-Sewa Controlled Rate: < 2.0% optimal scrap with telemetry", fontsize=7.4, color="#a7f3d0", weight="bold", zorder=5)
    ax.text(0.53, 0.095, "• Annual Paper Conservation: > 38 Metric Tonnes saved across lines", fontsize=7.4, color="#ffffff", zorder=5)
    ax.text(0.53, 0.070, "• Direct State Financial Savings: > Rs. 45 Lakhs saved annually in paper", fontsize=7.8, color="#f59e0b", weight="bold", zorder=5)

    out_path = os.path.join(ASSETS_DIR, "d39_fig_wastage_framework.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Generated: {out_path}")


# =============================================================================
# 4. WIREFRAME 1: RAW MATERIAL INVENTORY & STOREKEEPER PORTAL
# =============================================================================
def gen_wireframe_store():
    fig, ax = plt.subplots(figsize=(13.76, 7.74), dpi=200)
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Mudran-Sewa | Storekeeper Portal", "https://mudran.sascol.com/storekeeper")

    # Left Sidebar
    sb = FancyBboxPatch((0.02, 0.04), 0.18, 0.87, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#00332c", edgecolor="#004d40", linewidth=1)
    ax.add_patch(sb)
    ax.text(0.035, 0.88, "MUDRAN-SEWA", fontsize=11, weight="bold", color="#ffffff")
    ax.text(0.035, 0.86, "Directorate of Printing & Stationery", fontsize=6.8, color="#a7f3d0")

    menu_items = [
        ("• Paper Reel Registry", True),
        ("• Ream Stock (GSM)", False),
        ("• CTP Offset Plates", False),
        ("• Printing Inks & Solvents", False),
        ("• Inward GRN Entry", False),
        ("! Safety Buffer Alerts", False),
        ("• Form GFR-19 Export", False)
    ]
    my = 0.80
    for m, active in menu_items:
        if active:
            bg_p = FancyBboxPatch((0.025, my - 0.025), 0.17, 0.04, transform=ax.transAxes,
                                  boxstyle="round,pad=0.003,rounding_size=0.006",
                                  facecolor="#065f46", edgecolor=None)
            ax.add_patch(bg_p)
            ax.text(0.038, my - 0.005, m, fontsize=8.5, weight="bold", color="#ffffff")
        else:
            ax.text(0.038, my - 0.005, m, fontsize=8.2, color="#cbd5e1")
        my -= 0.06

    # Top KPI Cards
    kpis = [
        ("TOTAL REAMS IN STORE", "12,450 Reams", "Across 4 Warehouses", C_PILLAR_BLUE),
        ("PAPER REELS INWARD", "340 Metric Tonnes", "Maplitho & Ledger", C_PILLAR_CYAN),
        ("CRITICAL STOCK ALERTS", "2 Items Low", "Below 800 Ream Buffer", C_PILLAR_CRIMSON),
        ("ACTIVE GRNs TODAY", "14 Mill Lots", "Inspected & Verified", C_PILLAR_EMERALD),
    ]
    kw = 0.18
    kgap = 0.015
    for i, (ktitle, kval, ksub, kcol) in enumerate(kpis):
        kx = 0.215 + i * (kw + kgap)
        kp = FancyBboxPatch((kx, 0.77), kw, 0.14, transform=ax.transAxes,
                            boxstyle="round,pad=0.005,rounding_size=0.01",
                            facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=1)
        ax.add_patch(kp)
        ax.add_patch(Rectangle((kx, 0.77), 0.008, 0.14, transform=ax.transAxes, facecolor=kcol, edgecolor=None))
        ax.text(kx + 0.018, 0.88, ktitle, fontsize=7.2, weight="bold", color="#64748b")
        ax.text(kx + 0.018, 0.835, kval, fontsize=13, weight="bold", color="#0f172a")
        ax.text(kx + 0.018, 0.795, ksub, fontsize=7.2, color=kcol, weight="bold")

    # Main Data Table: Raw Paper Inventory Registry
    tp = FancyBboxPatch((0.215, 0.04), 0.55, 0.71, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1)
    ax.add_patch(tp)

    # Table Header Banner
    ax.add_patch(Rectangle((0.215, 0.70), 0.55, 0.05, transform=ax.transAxes, facecolor="#004d40", edgecolor=None))
    ax.text(0.23, 0.725, "Master Paper Inventory Registry (Central Store Shed #1 & #2, Bamunimaidam)", fontsize=9, weight="bold", color="#ffffff")

    # Column Headers with carefully calibrated non-overlapping x positions
    ax.add_patch(Rectangle((0.215, 0.65), 0.55, 0.045, transform=ax.transAxes, facecolor="#f1f5f9", edgecolor=None))
    cols = [(0.225, "Reel / Ream ID"), (0.315, "Specification"), (0.455, "Mill Lot No"), (0.550, "Stock (Reams)"), (0.640, "Buffer"), (0.705, "Status")]
    for cx, ctitle in cols:
        ax.text(cx, 0.665, ctitle, fontsize=7.6, weight="bold", color="#334155")

    rows = [
        ("MAP-80-0914", "Maplitho 80 GSM", "LOT-HP-2026-88", "3,200 Reams", "800", "OPTIMAL", "#10b981"),
        ("BND-80-1102", "Exec Bond 80 GSM", "LOT-TN-2026-14", "1,850 Reams", "600", "OPTIMAL", "#10b981"),
        ("LDG-90-0441", "Ledger 90 GSM", "LOT-BL-2026-09", "450 Reams", "800", "BUFFER ALERT", "#ef4444"),
        ("ART-300-022", "Art Board 300 GSM", "LOT-ITC-2026-31", "920 Reams", "400", "OPTIMAL", "#10b981"),
        ("MAP-60-0588", "Maplitho 60 GSM", "LOT-HP-2026-92", "380 Reams", "500", "BUFFER ALERT", "#ef4444"),
        ("KFT-120-007", "Kraft 120 GSM", "LOT-STAR-2026-03", "1,400 Reams", "300", "OPTIMAL", "#10b981"),
    ]
    ry = 0.60
    for r_id, r_spec, r_lot, r_stock, r_buf, r_stat, r_col in rows:
        ax.add_patch(Rectangle((0.215, ry - 0.015), 0.55, 0.05, transform=ax.transAxes, facecolor="#ffffff" if (rows.index((r_id, r_spec, r_lot, r_stock, r_buf, r_stat, r_col)) % 2 == 0) else "#f8fafc", edgecolor="#f1f5f9", linewidth=0.5))
        ax.text(0.225, ry, r_id, fontsize=7.6, weight="bold", color="#0f172a")
        ax.text(0.315, ry, r_spec, fontsize=7.4, color="#1e293b")
        ax.text(0.455, ry, r_lot, fontsize=7.0, color="#64748b", family="monospace")
        ax.text(0.550, ry, r_stock, fontsize=7.6, weight="bold", color="#0f172a")
        ax.text(0.640, ry, r_buf, fontsize=7.4, color="#64748b")
        
        # Pill for status
        sp = FancyBboxPatch((0.702, ry - 0.008), 0.055, 0.024, transform=ax.transAxes,
                            boxstyle="round,pad=0.002,rounding_size=0.005",
                            facecolor=r_col, edgecolor=None)
        ax.add_patch(sp)
        ax.text(0.729, ry + 0.004, r_stat, fontsize=5.8, weight="bold", color="#ffffff", ha="center")
        ry -= 0.06

    # Right Quick Action Panel: Inward GRN Modal Simulation
    rp = FancyBboxPatch((0.78, 0.04), 0.198, 0.71, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#f0fdf4", edgecolor="#86efac", linewidth=1)
    ax.add_patch(rp)
    ax.text(0.795, 0.715, "INWARD GRN ACTION", fontsize=9, weight="bold", color="#065f46")
    ax.text(0.795, 0.69, "Scan Mill Delivery Note & QR", fontsize=7.2, color="#475569")

    form_fields = [
        ("Mill Supplier", "Hindustan Paper Corp"),
        ("Invoice / Challan No", "INV-2026-CH-9921"),
        ("Paper Grade & GSM", "Maplitho 80 GSM"),
        ("Quantity Received", "400 Reams (20 Bundles)"),
        ("Quality Check", "Passed (Moisture 6.2%)"),
    ]
    fy = 0.64
    for flabel, fval in form_fields:
        ax.text(0.795, fy, flabel, fontsize=7.4, weight="bold", color="#1e293b")
        fb = FancyBboxPatch((0.795, fy - 0.038), 0.17, 0.03, transform=ax.transAxes,
                            boxstyle="round,pad=0.002,rounding_size=0.005",
                            facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=0.8)
        ax.add_patch(fb)
        ax.text(0.805, fy - 0.023, fval, fontsize=7.2, color="#475569")
        fy -= 0.065

    # Submit Button
    btn = FancyBboxPatch((0.795, 0.15), 0.17, 0.045, transform=ax.transAxes,
                         boxstyle="round,pad=0.004,rounding_size=0.008",
                         facecolor="#004d40", edgecolor=None)
    ax.add_patch(btn)
    ax.text(0.88, 0.172, "APPROVE INWARD GRN", fontsize=8.2, weight="bold", color="#ffffff", ha="center")

    out_path = os.path.join(ASSETS_DIR, "d39_wireframe1_store.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Generated: {out_path}")


# =============================================================================
# 5. WIREFRAME 2: PRESS PRODUCTION FLOOR & TRIMMING SCRAP TELEMETRY
# =============================================================================
def gen_wireframe_press():
    fig, ax = plt.subplots(figsize=(13.76, 7.74), dpi=200)
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Mudran-Sewa | Press Floor Telemetry", "https://mudran.sascol.com/press-floor")

    # Top KPI Row
    kpis = [
        ("ACTIVE PRESS LINES", "4 / 5 Running", "Bamunimaidam Central Press", C_PILLAR_EMERALD),
        ("CURRENT SPEED", "8,500 Imp/Hr", "Harris Web Rotary Line #1", C_PILLAR_BLUE),
        ("DAILY PAPER INTAKE", "4.8 Metric Tonnes", "Across 3 Shifts", C_PILLAR_CYAN),
        ("AVERAGE SCRAP RATE", "1.85% Optimal", "Benchmark Ceiling: 3.0%", C_PILLAR_AMBER),
    ]
    kw = 0.222
    kgap = 0.02
    for i, (ktitle, kval, ksub, kcol) in enumerate(kpis):
        kx = 0.035 + i * (kw + kgap)
        kp = FancyBboxPatch((kx, 0.77), kw, 0.14, transform=ax.transAxes,
                            boxstyle="round,pad=0.005,rounding_size=0.01",
                            facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=1)
        ax.add_patch(kp)
        ax.add_patch(Rectangle((kx, 0.77), 0.008, 0.14, transform=ax.transAxes, facecolor=kcol, edgecolor=None))
        ax.text(kx + 0.018, 0.88, ktitle, fontsize=7.5, weight="bold", color="#64748b")
        ax.text(kx + 0.018, 0.835, kval, fontsize=13.5, weight="bold", color="#0f172a")
        ax.text(kx + 0.018, 0.795, ksub, fontsize=7.2, color=kcol, weight="bold")

    # Left Container: Active Machine Lines
    left_w = 0.46
    lp = FancyBboxPatch((0.035, 0.04), left_w, 0.71, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1)
    ax.add_patch(lp)
    ax.add_patch(Rectangle((0.035, 0.70), left_w, 0.05, transform=ax.transAxes, facecolor="#004d40", edgecolor=None))
    ax.text(0.05, 0.725, "Live Press Machine Queues & Real-Time Job Progress", fontsize=9.2, weight="bold", color="#ffffff")

    machine_lines = [
        {
            "name": "Line 1: Harris Web Offset (Reel-Fed Rotary)", "status": "RUNNING", "col": "#10b981",
            "job": "JOB-GAZ-2026-042: The Assam Gazette Extraordinary",
            "paper": "Maplitho 80 GSM | Reel #MAP-80-0914 | 2,400 kg intake",
            "scrap": "Trimming Scrap: 58 kg (2.41%) - Optimal (< 3.0%)",
            "progress": 0.82
        },
        {
            "name": "Line 2: Heidelberg Sheet-Fed Offset", "status": "RUNNING", "col": "#10b981",
            "job": "JOB-BUD-2026-018: Assembly Budget Estimates 2026-27",
            "paper": "Executive Sunlit Bond 80 GSM | 1,800 kg intake",
            "scrap": "Trimming Scrap: 32 kg (1.78%) - High Precision (< 2.0%)",
            "progress": 0.45
        },
        {
            "name": "Line 3: High-Speed Sheet-Fed Form Press", "status": "RUNNING", "col": "#10b981",
            "job": "JOB-JAM-2026-104: Land Revenue Jamabandi Register",
            "paper": "Azurelaid Ledger 90 GSM | 3,200 kg intake",
            "scrap": "Trimming Scrap: 64 kg (2.00%) - Pass (< 2.0%)",
            "progress": 0.65
        }
    ]
    my = 0.64
    for m in machine_lines:
        mc = FancyBboxPatch((0.05, my - 0.14), left_w - 0.03, 0.17, transform=ax.transAxes,
                            boxstyle="round,pad=0.005,rounding_size=0.008",
                            facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=0.8)
        ax.add_patch(mc)
        ax.text(0.065, my + 0.008, m["name"], fontsize=8.5, weight="bold", color="#0f172a")
        
        sp = FancyBboxPatch((0.41, my), 0.065, 0.024, transform=ax.transAxes,
                            boxstyle="round,pad=0.002,rounding_size=0.005",
                            facecolor=m["col"], edgecolor=None)
        ax.add_patch(sp)
        ax.text(0.442, my + 0.012, m["status"], fontsize=6.8, weight="bold", color="#ffffff", ha="center")

        ax.text(0.065, my - 0.02, m["job"], fontsize=7.8, color="#0369a1", weight="bold")
        ax.text(0.065, my - 0.045, m["paper"], fontsize=7.2, color="#475569")
        ax.text(0.065, my - 0.070, m["scrap"], fontsize=7.2, color="#059669", weight="bold")

        # Progress bar
        ax.add_patch(Rectangle((0.065, my - 0.105), left_w - 0.06, 0.018, transform=ax.transAxes, facecolor="#e2e8f0", edgecolor=None))
        ax.add_patch(Rectangle((0.065, my - 0.105), (left_w - 0.06) * m["progress"], 0.018, transform=ax.transAxes, facecolor="#059669", edgecolor=None))
        ax.text(left_w - 0.02, my - 0.096, f"{int(m['progress']*100)}%", fontsize=7, weight="bold", color="#0f172a", ha="right")

        my -= 0.20

    # Right Container: Real-Time Trimming Scrap Telemetry Graph
    right_w = 0.46
    rp = FancyBboxPatch((0.505, 0.04), right_w, 0.71, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1)
    ax.add_patch(rp)
    ax.add_patch(Rectangle((0.505, 0.70), right_w, 0.05, transform=ax.transAxes, facecolor="#00332c", edgecolor=None))
    ax.text(0.52, 0.725, "Continuous Trimming Scrap Loss Telemetry vs Statutory Ceiling", fontsize=9.2, weight="bold", color="#ffffff")

    # Telemetry Graph Chart Box
    gb = FancyBboxPatch((0.52, 0.25), 0.43, 0.42, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.008",
                        facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=0.8)
    ax.add_patch(gb)

    x_pts = np.linspace(0.53, 0.93, 30)
    y_baseline = 0.38 + 0.06 * np.sin(np.linspace(0, 3*np.pi, 30)) * np.exp(-np.linspace(0, 0.8, 30))
    y_ceiling = np.full_like(x_pts, 0.54)

    # Ceiling line (Red dashed)
    for k in range(len(x_pts)-1):
        ax.plot([x_pts[k], x_pts[k+1]], [y_ceiling[k], y_ceiling[k+1]], transform=ax.transAxes, color="#ef4444", linestyle="--", linewidth=1.5, zorder=5)
    ax.text(0.93, 0.555, "3.0% Max Danger Ceiling", transform=ax.transAxes, color="#ef4444", fontsize=7.5, weight="bold", ha="right")

    # Actual Scrap Line (Emerald)
    for k in range(len(x_pts)-1):
        ax.plot([x_pts[k], x_pts[k+1]], [y_baseline[k], y_baseline[k+1]], transform=ax.transAxes, color="#059669", linewidth=2.5, zorder=6)
    ax.text(0.93, 0.42, "Actual Scrap % (1.85% Mean)", transform=ax.transAxes, color="#059669", fontsize=7.5, weight="bold", ha="right")

    # Bottom notes
    ax.text(0.52, 0.19, "ALGORITHMIC ANOMALY INTERCEPTION:", fontsize=8.5, weight="bold", color="#004d40")
    ax.text(0.52, 0.155, "• Continuous optical sensor feeds calculate paper scrap after rotary slitting & guillotine trim.", fontsize=7.5, color="#475569")
    ax.text(0.52, 0.125, "• Anomaly threshold of 3.0% ensures cutting errors are flagged before binding.", fontsize=7.5, color="#475569")
    ax.text(0.52, 0.095, "• Automatic machine lockout prevents raw paper loss escalation on web offset lines.", fontsize=7.5, color="#475569")

    out_path = os.path.join(ASSETS_DIR, "d39_wireframe2_press.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Generated: {out_path}")


# =============================================================================
# 6. WIREFRAME 3: INTER-DISTRICT FLEET TRANSIT RADAR & HIGHWAY TRACKER
# =============================================================================
def gen_wireframe_transit():
    fig, ax = plt.subplots(figsize=(13.76, 7.74), dpi=200)
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Mudran-Sewa | Inter-District Transit Radar", "https://mudran.sascol.com/transit-radar")

    # Center/Right: Highway Corridor Radar Map Box
    map_w = 0.58
    mp = FancyBboxPatch((0.39, 0.04), map_w, 0.87, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#0a1e17", edgecolor="#065f46", linewidth=1.5)
    ax.add_patch(mp)
    ax.text(0.41, 0.875, "ASSAM INTER-DISTRICT HIGHWAY TRANSIT RADAR", fontsize=11, weight="bold", color="#ffffff")
    ax.text(0.41, 0.850, "GPS Live Corridor Tracking: Bamunimaidam Central Press -> 35 District Treasuries", fontsize=7.5, color="#a7f3d0")

    # Concentric Radar circles for architectural high-tech aesthetic
    ax.add_patch(Circle((0.68, 0.48), 0.32, transform=ax.transAxes, facecolor="none", edgecolor="#14532d", linewidth=0.8, linestyle=":", zorder=3))
    ax.add_patch(Circle((0.68, 0.48), 0.20, transform=ax.transAxes, facecolor="none", edgecolor="#14532d", linewidth=0.8, linestyle=":", zorder=3))

    # NH-27 Route: Guwahati -> Nagaon -> Kaziranga -> Jorhat -> Dibrugarh (Shifted nicely inside map)
    route_x = [0.46, 0.55, 0.65, 0.77, 0.89]
    route_y = [0.42, 0.50, 0.56, 0.62, 0.70]
    for k in range(len(route_x)-1):
        ax.plot([route_x[k], route_x[k+1]], [route_y[k], route_y[k+1]], transform=ax.transAxes, color="#f59e0b", linewidth=4, zorder=5)

    # NH-37 Barak Valley Branch: Guwahati -> Silchar
    route2_x = [0.46, 0.52, 0.60]
    route2_y = [0.42, 0.28, 0.18]
    for k in range(len(route2_x)-1):
        ax.plot([route2_x[k], route2_x[k+1]], [route2_y[k], route2_y[k+1]], transform=ax.transAxes, color="#38bdf8", linewidth=3, linestyle="--", zorder=5)

    # City Hubs
    hubs = [
        (0.46, 0.42, "Guwahati (Press HQ)", "#10b981"),
        (0.55, 0.50, "Nagaon", "#ffffff"),
        (0.65, 0.56, "Kaziranga", "#ffffff"),
        (0.77, 0.62, "Jorhat (Branch Press)", "#38bdf8"),
        (0.89, 0.70, "Dibrugarh", "#ffffff"),
        (0.60, 0.18, "Silchar (Barak Valley)", "#f59e0b"),
    ]
    for hx, hy, hname, hcol in hubs:
        ax.add_patch(Circle((hx, hy), 0.012, transform=ax.transAxes, facecolor=hcol, edgecolor="#ffffff", linewidth=1.5, zorder=6))
        ax.text(hx, hy - 0.032, hname, fontsize=7.8, weight="bold", color="#ffffff", ha="center", zorder=7)

    # Active Truck Icons along route
    ax.add_patch(FancyBboxPatch((0.68, 0.58), 0.055, 0.028, transform=ax.transAxes,
                               boxstyle="round,pad=0.002,rounding_size=0.005",
                               facecolor="#10b981", edgecolor="#ffffff", linewidth=1, zorder=8))
    ax.text(0.707, 0.594, "AS-01-GC-4412", fontsize=6.2, weight="bold", color="#ffffff", ha="center", zorder=9)

    ax.add_patch(FancyBboxPatch((0.53, 0.26), 0.055, 0.028, transform=ax.transAxes,
                               boxstyle="round,pad=0.002,rounding_size=0.005",
                               facecolor="#38bdf8", edgecolor="#ffffff", linewidth=1, zorder=8))
    ax.text(0.557, 0.274, "AS-01-GC-8821", fontsize=6.2, weight="bold", color="#ffffff", ha="center", zorder=9)

    # Left Container: Active Dispatches List
    left_w = 0.35
    lp = FancyBboxPatch((0.02, 0.04), left_w, 0.87, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#ffffff", edgecolor="#cbd5e1", linewidth=1)
    ax.add_patch(lp)
    ax.add_patch(Rectangle((0.02, 0.86), left_w, 0.05, transform=ax.transAxes, facecolor="#004d40", edgecolor=None))
    ax.text(0.035, 0.885, "Active Inter-District Dispatches", fontsize=9.5, weight="bold", color="#ffffff")

    dispatches = [
        {
            "id": "GP-2026-0891", "veh": "AS-01-GC-4412", "dest": "Jorhat District Treasury",
            "cargo": "350 Cartons (Treasury Challans & Gazette)",
            "driver": "B. Das (+91 94350-XXXXX)", "status": "IN TRANSIT (ETA 2.5h)", "col": "#0284c7"
        },
        {
            "id": "GP-2026-0892", "veh": "AS-01-GC-8821", "dest": "Cachar District Treasury (Silchar)",
            "cargo": "500 Reams (Revenue Patta Forms)",
            "driver": "M. Saikia (+91 98640-XXXXX)", "status": "IN TRANSIT (ETA 5.0h)", "col": "#0284c7"
        },
        {
            "id": "GP-2026-0890", "veh": "AS-01-GC-1190", "dest": "Nagaon DC Commissionerate",
            "cargo": "200 Cartons (Administrative Forms)",
            "driver": "R. Kalita (+91 91012-XXXXX)", "status": "DELIVERED (OTP Verified)", "col": "#059669"
        }
    ]
    dy = 0.80
    for d in dispatches:
        dc = FancyBboxPatch((0.035, dy - 0.165), left_w - 0.03, 0.19, transform=ax.transAxes,
                            boxstyle="round,pad=0.005,rounding_size=0.008",
                            facecolor="#f8fafc", edgecolor="#cbd5e1", linewidth=0.8)
        ax.add_patch(dc)
        ax.text(0.048, dy + 0.005, d["id"], fontsize=8.5, weight="bold", color="#0f172a")
        
        sp = FancyBboxPatch((0.23, dy - 0.005), 0.12, 0.024, transform=ax.transAxes,
                            boxstyle="round,pad=0.002,rounding_size=0.005",
                            facecolor=d["col"], edgecolor=None)
        ax.add_patch(sp)
        ax.text(0.290, dy + 0.007, d["status"], fontsize=6.2, weight="bold", color="#ffffff", ha="center")

        ax.text(0.048, dy - 0.025, f"Destination: {d['dest']}", fontsize=7.8, weight="bold", color="#0369a1")
        ax.text(0.048, dy - 0.050, f"Cargo: {d['cargo']}", fontsize=7.2, color="#475569")
        ax.text(0.048, dy - 0.075, f"Vehicle: {d['veh']} | Driver: {d['driver']}", fontsize=7.2, color="#1e293b")
        dy -= 0.22

    out_path = os.path.join(ASSETS_DIR, "d39_wireframe3_transit.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Generated: {out_path}")


# =============================================================================
# 7. WIREFRAME 4: TAMPER-EVIDENT QR E-GATEPASS & HIGH-SECURITY GAZETTE VAULT
# =============================================================================
def gen_wireframe_gatepass():
    fig, ax = plt.subplots(figsize=(13.76, 7.74), dpi=200)
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    draw_browser_chrome(ax, "Mudran-Sewa | Gatepass & Gazette Vault", "https://mudran.sascol.com/gatepass")

    half_w = 0.46
    lp = FancyBboxPatch((0.035, 0.04), half_w, 0.87, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#ffffff", edgecolor="#004d40", linewidth=1.5)
    ax.add_patch(lp)
    ax.add_patch(Rectangle((0.035, 0.85), half_w, 0.06, transform=ax.transAxes, facecolor="#004d40", edgecolor=None))
    ax.text(0.05, 0.885, "GOVERNMENT OF ASSAM • QR E-GATEPASS", fontsize=10, weight="bold", color="#ffffff")
    ax.text(0.05, 0.865, "Directorate of Printing & Stationery, Bamunimaidam, Guwahati", fontsize=7.2, color="#a7f3d0")

    gp_fields = [
        ("E-Gatepass ID:", "GP-2026-0891 (Cryptographically Signed)"),
        ("Origin Dispatch:", "Central Warehouse Shed #2, Bamunimaidam"),
        ("Destination:", "Jorhat District Treasury, Court Compound"),
        ("Vehicle Registration:", "AS-01-GC-4412 (Assam State Transport)"),
        ("Driver Name & Phone:", "Bhaben Das (+91 94350-12891)"),
        ("Cargo Manifest:", "350 Cartons (Treasury Challans Schedule LIII-107)"),
        ("Issued Date & Time:", "2026-11-22 08:30 IST | Gate Officer: #GO-44"),
        ("Delivery Handshake:", "OTP Verification Required upon Arrival")
    ]
    gy = 0.81
    for glabel, gval in gp_fields:
        ax.text(0.055, gy, glabel, fontsize=7.6, weight="bold", color="#1e293b")
        ax.text(0.19, gy, gval, fontsize=7.4, color="#475569")
        gy -= 0.045

    # Simulated QR Code Box
    qr_box = FancyBboxPatch((0.165, 0.16), 0.20, 0.26, transform=ax.transAxes,
                            boxstyle="round,pad=0.005,rounding_size=0.01",
                            facecolor="#f8fafc", edgecolor="#0f172a", linewidth=2)
    ax.add_patch(qr_box)

    np.random.seed(42)
    qr_grid = np.random.choice([0, 1], size=(12, 12), p=[0.45, 0.55])
    qr_grid[0:3, 0:3] = 1
    qr_grid[0:3, 9:12] = 1
    qr_grid[9:12, 0:3] = 1

    qx_start = 0.18
    qy_start = 0.18
    q_cell = 0.014
    for r in range(12):
        for c in range(12):
            if qr_grid[r, c] == 1:
                ax.add_patch(Rectangle((qx_start + c * q_cell, qy_start + (11 - r) * q_cell), q_cell, q_cell, transform=ax.transAxes, facecolor="#0f172a", edgecolor=None))

    ax.text(0.265, 0.12, "SCAN WITH MOBILE HANDHELD TO VERIFY MANIFEST", fontsize=7.2, weight="bold", color="#004d40", ha="center")
    ax.text(0.265, 0.09, "SHA-256: 7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069", fontsize=6, color="#64748b", family="monospace", ha="center")

    # Right Half: The Assam Gazette High-Security Vault
    rp = FancyBboxPatch((0.505, 0.04), half_w, 0.87, transform=ax.transAxes,
                        boxstyle="round,pad=0.005,rounding_size=0.01",
                        facecolor="#ffffff", edgecolor="#0284c7", linewidth=1.5)
    ax.add_patch(rp)
    ax.add_patch(Rectangle((0.505, 0.85), half_w, 0.06, transform=ax.transAxes, facecolor="#0284c7", edgecolor=None))
    ax.text(0.52, 0.885, "THE ASSAM GAZETTE (ASOM RAJPATRA) STATUTORY VAULT", fontsize=10, weight="bold", color="#ffffff")
    ax.text(0.52, 0.865, "Cryptographic Immutability & Official Notification Verification Registry", fontsize=7.2, color="#e0f2fe")

    gaz_items = [
        ("Gazette Notification No:", "GAZ-ORD-2026-44 (Ordinary Edition)"),
        ("Publishing Authority:", "Information, Public Relations, Printing & Stationery Dept"),
        ("Date of Publication:", "Guwahati, Saturday, 21st November 2026"),
        ("Press Line Assigned:", "Harris Web Offset Press #1 (Bamunimaidam)"),
        ("Total Copies Printed:", "15,000 Official Copies (Reams: 300)"),
        ("Statutory Integrity:", "STAMPED & VERIFIED [IMMUTABLE]")
    ]
    zy = 0.81
    for zlabel, zval in gaz_items:
        ax.text(0.525, zy, zlabel, fontsize=7.6, weight="bold", color="#1e293b")
        ax.text(0.67, zy, zval, fontsize=7.4, color="#0284c7" if "VERIFIED" in zval else "#475569", weight="bold" if "VERIFIED" in zval else "normal")
        zy -= 0.045

    # Gazette Digital Checksum Box
    g_chk = FancyBboxPatch((0.525, 0.36), 0.42, 0.16, transform=ax.transAxes,
                           boxstyle="round,pad=0.005,rounding_size=0.008",
                           facecolor="#f0f9ff", edgecolor="#7dd3fc", linewidth=1)
    ax.add_patch(g_chk)
    ax.text(0.54, 0.48, "CRYPTOGRAPHIC SHA-256 DIGITAL SEAL", fontsize=8.5, weight="bold", color="#0369a1")
    ax.text(0.54, 0.445, "Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", fontsize=6.8, color="#0f172a", family="monospace")
    ax.text(0.54, 0.415, "Status: Matches Directorate Master Statutory Ledger bit-for-bit", fontsize=7.2, color="#059669", weight="bold")
    ax.text(0.54, 0.385, "Verification: Instant QR validation via public citizen portal", fontsize=7.2, color="#64748b")

    # Bottom Seal Badge
    seal_p = FancyBboxPatch((0.525, 0.08), 0.42, 0.24, transform=ax.transAxes,
                            boxstyle="round,pad=0.005,rounding_size=0.008",
                            facecolor="#ecfdf5", edgecolor="#a7f3d0", linewidth=1)
    ax.add_patch(seal_p)
    ax.text(0.735, 0.27, "OFFICIAL STATE SECURITY CLEARANCE", fontsize=9, weight="bold", color="#065f46", ha="center")
    ax.text(0.735, 0.23, "Printed under authority of the Government of Assam", fontsize=7.5, color="#334155", ha="center")
    ax.text(0.735, 0.19, "• Tamper-proof digital archiving in Assam State Data Centre (SDC)", fontsize=7.2, color="#475569", ha="center")
    ax.text(0.735, 0.15, "• Non-repudiation guaranteed by chained SHA-256 ledger", fontsize=7.2, color="#475569", ha="center")
    ax.text(0.735, 0.11, "• 100% compliant with CAG Form GFR-19 statutory standards", fontsize=7.2, color="#059669", weight="bold", ha="center")

    out_path = os.path.join(ASSETS_DIR, "d39_wireframe4_gatepass.png")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.close()
    print(f"Generated: {out_path}")


if __name__ == "__main__":
    print("Generating High-Impact 16:9 Widescreen Technological Framework Infographics...")
    gen_figure_architecture()
    gen_figure_lifecycle()
    gen_figure_wastage()
    gen_wireframe_store()
    gen_wireframe_press()
    gen_wireframe_transit()
    gen_wireframe_gatepass()
    print("All technological framework infographics generated successfully!")
