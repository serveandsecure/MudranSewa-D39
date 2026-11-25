# Cloudflare Deployment Guide
## Assam Government Press & Stationery Tracker (NESFIC-D-39)

The application is completely configured and optimized for zero-cost, high-speed global edge deployment on **Cloudflare Pages & Workers**.

---

### Method 1: Instant Deployment via Wrangler CLI (Recommended)

1. **Deploy using npx (No global install needed):**
   ```bash
   npm run deploy:cloudflare
   # Or directly:
   npx wrangler pages deploy apps/web/public --project-name=mudran-sewa
   ```
2. Follow the terminal prompt to log into your Cloudflare account (if not already authenticated).
3. Cloudflare will publish the site and provide a permanent global live URL:
   `https://mudran.sascol.com`

---

### Method 2: Automatic Git Integration via Cloudflare Dashboard

1. Push this repository to GitHub under `assam-gov-stationery-track` (or your chosen repository name).
2. Log into the [Cloudflare Dashboard](https://dash.cloudflare.com/) and go to **Workers & Pages** $\rightarrow$ **Create Application** $\rightarrow$ **Pages** $\rightarrow$ **Connect to Git**.
3. Select your repository `serveandsecure/MudranSewa-D39` and configure the build settings:
   - **Project Name:** `mudran-sewa` (or `assam-gov-stationery-track`)
   - **Production Branch:** `main` (or `master`)
   - **Framework Preset:** `None`
   - **Build Command:** *(leave empty or `npm test`)*
   - **Build Output Directory:** `apps/web/public`
   - **Root Directory:** `/` (or leave default)
4. Click **Save and Deploy**. Cloudflare will build and deploy your application worldwide in ~30 seconds with automatic SSL/TLS!

---

### Edge Features Configured:
- **`apps/web/public/_headers`:** Enforces HSTS, X-Frame-Options, CORS, and 24-hour browser caching for static CSS/JS/SVG assets.
- **`apps/web/public/_routes.json`:** Directs static and API requests efficiently.
- **`apps/web/functions/api/[[route]].js`:** Cloudflare Pages Function providing serverless edge API endpoints (`/api/verify/gatepass/:token`, `/api/health`, `/api/inventory`, `/api/requisitions`, `/api/press/jobs`, `/api/dispatch/gatepasses`, `/api/analytics`) across 300+ global Cloudflare data centers with <50ms latency.
