# 🚀 Vercel Deployment Guide for AMS Django Project

## ⚠️ Important Limitations

**Before deploying to Vercel, please note:**

Vercel is optimized for:
- ✅ Static sites and Next.js apps
- ✅ Serverless functions
- ✅ API endpoints

**Limitations with Django on Vercel:**
- ❌ Django Admin panel may not work properly
- ❌ File uploads won't persist (serverless = no file system)
- ❌ Cold starts (first request will be slow)
- ❌ 10-second execution timeout
- ❌ Database connections need careful management
- ❌ Sessions may not work reliably

**Alternative Recommendation:** Consider Railway, Render, or PythonAnywhere for full Django support.

---

## 📋 Prerequisites

1. ✅ GitHub account
2. ✅ Vercel account (sign up at https://vercel.com)
3. ✅ Your code pushed to GitHub (already done!)
4. ✅ Supabase database (already configured)

---

## 🚀 Step-by-Step Deployment

### Step 1: Prepare Your Project

All necessary files have been created:
- ✅ `vercel.json` - Vercel configuration
- ✅ `vercel_app.py` - WSGI entry point
- ✅ `.vercelignore` - Files to ignore
- ✅ Updated `settings.py` - Vercel-friendly settings

### Step 2: Commit and Push Changes

```bash
cd EMS
git add .
git commit -m "Add Vercel deployment configuration"
git push origin main
```

### Step 3: Deploy on Vercel

#### Option A: Using Vercel Website (Easiest)

1. **Go to Vercel**
   - Visit https://vercel.com
   - Click "Sign Up" or "Login"
   - Sign in with GitHub

2. **Import Project**
   - Click "Add New Project"
   - Select "Import Git Repository"
   - Find your `EMS` repository
   - Click "Import"

3. **Configure Project**
   - **Framework Preset**: Other
   - **Root Directory**: ./
   - **Build Command**: Leave empty or use `pip install -r requirements.txt`
   - **Output Directory**: Leave empty

4. **Add Environment Variables**
   Click "Environment Variables" and add:
   
   ```
   SECRET_KEY = django-insecure-your-secret-key-here
   DEBUG = False
   USE_SUPABASE = True
   DB_HOST = aws-1-ap-south-1.pooler.supabase.com
   DB_PORT = 6543
   DB_NAME = postgres
   DB_USER = postgres.ofytgjjxhnmluqhpejws
   DB_PASSWORD = Tayyab@102
   ALLOWED_HOSTS = .vercel.app,.now.sh
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment (2-3 minutes)
   - Get your URL: `https://your-project.vercel.app`

#### Option B: Using Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? ams-accommodation
# - Directory? ./
# - Override settings? No

# Add environment variables
vercel env add SECRET_KEY
vercel env add DB_HOST
vercel env add DB_PORT
vercel env add DB_NAME
vercel env add DB_USER
vercel env add DB_PASSWORD

# Deploy to production
vercel --prod
```

---

## 🔧 Post-Deployment Steps

### 1. Run Migrations (Important!)

Since Vercel is serverless, you need to run migrations locally or from another platform:

```bash
# Option 1: Run locally connected to Supabase
python manage.py migrate

# Option 2: Use Vercel CLI
vercel run python manage.py migrate
```

### 2. Create Static Files

```bash
python manage.py collectstatic --noinput
```

### 3. Test Your Deployment

Visit your Vercel URL:
- Homepage: `https://your-project.vercel.app/`
- Login: `https://your-project.vercel.app/auth/login/`
- Admin: `https://your-project.vercel.app/system-admin/` (may not work)

---

## 🐛 Common Issues & Solutions

### Issue 1: "Application Error" on Vercel

**Solution:**
- Check Vercel logs: Click "View Function Logs"
- Verify environment variables are set
- Ensure ALLOWED_HOSTS includes `.vercel.app`

### Issue 2: Static Files Not Loading

**Solution:**
```bash
# Update settings.py
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Run collectstatic
python manage.py collectstatic --noinput
```

### Issue 3: Database Connection Errors

**Solution:**
- Verify Supabase credentials
- Check if Supabase project is active
- Ensure DB_HOST uses Transaction Pooler (port 6543)

### Issue 4: CSRF Verification Failed

**Solution:**
Already added to settings.py:
```python
CSRF_TRUSTED_ORIGINS = [
    'https://*.vercel.app',
    'https://*.now.sh',
]
```

### Issue 5: Cold Starts (Slow First Load)

**This is normal for Vercel serverless.**
- First request: 3-10 seconds
- Subsequent requests: Fast
- Consider upgrading Vercel plan or use Railway/Render instead

---

## 🎯 What Works vs What Doesn't

### ✅ What Works on Vercel:
- Basic Django views
- Templates rendering
- Database queries (Supabase)
- Static pages
- User authentication
- API endpoints
- Forms

### ❌ What May Not Work:
- Django Admin panel (may be slow/buggy)
- File uploads (no persistent storage)
- Long-running tasks (10s timeout)
- WebSockets
- Background tasks
- Scheduled jobs

---

## 💡 Better Alternatives

### If You Face Issues with Vercel:

#### 1. **Railway** (Highly Recommended)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```
**Advantages:**
- Full Django support
- $5 free credit monthly
- Django admin works perfectly
- No cold starts
- File uploads work
- Better for production

#### 2. **Render**
- Free tier available
- No cold starts
- Full Django support
- Deploy from GitHub

#### 3. **PythonAnywhere**
- Free tier for Python apps
- Django-optimized
- Web-based console
- Easy setup

---

## 📊 Vercel Pricing

- **Hobby (Free)**:
  - 100 GB bandwidth/month
  - Serverless function execution
  - Automatic HTTPS
  - Good for testing

- **Pro ($20/month)**:
  - Unlimited bandwidth
  - Better performance
  - Team features
  - Priority support

---

## 🔒 Security Checklist

Before going live:
- [ ] Set `DEBUG = False`
- [ ] Generate strong `SECRET_KEY`
- [ ] Review `ALLOWED_HOSTS`
- [ ] Enable CSRF protection
- [ ] Set secure cookies
- [ ] Review database credentials
- [ ] Enable HTTPS (automatic on Vercel)
- [ ] Set up monitoring

---

## 📞 Need Help?

If deployment fails or features don't work:

1. **Check Vercel Logs**
   - Go to your project dashboard
   - Click "Deployments"
   - Click on latest deployment
   - View "Function Logs"

2. **Try Railway Instead**
   - Much better for Django
   - Full feature support
   - Easier debugging

3. **Contact Support**
   - Vercel Discord: https://vercel.com/discord
   - Railway Discord: https://discord.gg/railway

---

## ✅ Quick Deployment Checklist

- [ ] Files created (vercel.json, vercel_app.py)
- [ ] Settings updated (ALLOWED_HOSTS, CSRF)
- [ ] Code pushed to GitHub
- [ ] Vercel account created
- [ ] Repository imported to Vercel
- [ ] Environment variables added
- [ ] Deployment successful
- [ ] Migrations run
- [ ] Website tested
- [ ] Features verified

---

## 🎉 Deployment Complete!

Once deployed, your AMS project will be available at:
- `https://your-project-name.vercel.app`

**Remember:** Vercel works, but Railway/Render are better for Django!

---

## 📚 Resources

- Vercel Docs: https://vercel.com/docs
- Django Deployment: https://docs.djangoproject.com/en/5.0/howto/deployment/
- Supabase Docs: https://supabase.com/docs
- Railway Guide: https://railway.app/docs

---

**Good luck with your deployment! 🚀**

*For best Django experience, consider Railway or Render instead of Vercel.*

