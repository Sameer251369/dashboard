# 🚀 Heroku Deployment Guide

Your MBA KPI Dashboard is now ready to deploy to Heroku!

## Prerequisites

1. **Heroku Account** (free tier available)
   - Sign up at https://www.heroku.com

2. **Heroku CLI** (Command Line Interface)
   - Download from: https://devcenter.heroku.com/articles/heroku-cli

3. **Git** (for version control)
   - Download from: https://git-scm.com

---

## Step-by-Step Deployment

### **Step 1: Install Heroku CLI**

Download and install from: https://devcenter.heroku.com/articles/heroku-cli

Verify installation:
```powershell
heroku --version
```

### **Step 2: Login to Heroku**

```powershell
heroku login
```

This opens your browser to login. Authenticate and return to terminal.

### **Step 3: Initialize Git (if not already done)**

```powershell
cd c:\Users\vboys\Downloads\files\mba-dashboard
git init
git add .
git commit -m "Initial commit: MBA KPI Dashboard"
```

### **Step 4: Create Heroku App**

```powershell
heroku create your-app-name
```

Replace `your-app-name` with something unique (e.g., `mba-kpi-dashboard-2024`)

Example:
```powershell
heroku create mba-kpi-dashboard-2024
```

### **Step 5: Build Frontend**

Before deploying, build the frontend:

```powershell
cd frontend
npm run build
cd ..
```

This creates the `frontend/dist/` folder that will be served by the backend.

### **Step 6: Deploy to Heroku**

```powershell
git add .
git commit -m "Build frontend for production"
git push heroku main
```

⏳ This will take 2-3 minutes. Watch the output for any errors.

### **Step 7: Access Your App**

```powershell
heroku open
```

Or visit: `https://your-app-name.herokuapp.com`

---

## ✅ Deployment Checklist

- [ ] Created Heroku account
- [ ] Installed Heroku CLI
- [ ] Installed Git
- [ ] Built frontend: `npm run build`
- [ ] Initialized Git repo: `git init`
- [ ] Created Heroku app: `heroku create your-app-name`
- [ ] Deployed: `git push heroku main`
- [ ] App is live at `https://your-app-name.herokuapp.com`

---

## 📊 After Deployment

### **View Logs**
```powershell
heroku logs --tail
```

### **Restart App**
```powershell
heroku restart
```

### **View App Info**
```powershell
heroku apps:info
```

### **Set Environment Variables**
```powershell
heroku config:set FLASK_ENV=production
```

---

## 🆘 Troubleshooting

### **Build Failed**
```powershell
# Check logs
heroku logs --tail

# Rebuild
git push heroku main --force
```

### **App Crashes on Start**
```powershell
# View error logs
heroku logs --tail

# Common issue: frontend not built
# Solution: 
cd frontend
npm run build
cd ..
git add .
git commit -m "Rebuild frontend"
git push heroku main
```

### **Frontend Shows 404**
Make sure `frontend/dist/` folder exists and was built.

```powershell
cd frontend
npm run build
cd ..
```

### **API Not Responding**
Check that `Procfile` exists in root directory with:
```
web: gunicorn app:app
```

---

## 🔄 Continuous Deployment

### **Connect GitHub Repository**

1. Push code to GitHub
2. In Heroku dashboard:
   - Go to your app
   - Click "Deploy" tab
   - Select "GitHub"
   - Connect repository
   - Enable "Automatic deploys"

Now any `git push` to main branch auto-deploys!

---

## 📦 Database (Optional)

If you need persistent data in the future:

```powershell
# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# View database URL
heroku config
```

---

## 💰 Cost Information

**Free Tier:**
- 550 free dyno-hours/month (enough for ~45 hours/month running)
- Perfect for testing and demo

**Paid Tier:**
- $7-50/month for production apps
- Recommended for always-on apps

Upgrade anytime in Heroku dashboard.

---

## 🔐 Security

### **Hide Sensitive Data**

Never commit `.env` files! Use Heroku config:

```powershell
heroku config:set API_KEY=your_secret_key
heroku config:set DEBUG=False
```

Access in Flask:
```python
import os
api_key = os.environ.get('API_KEY')
```

---

## 📈 Monitoring

### **View Resource Usage**
```powershell
heroku apps:info
```

### **View Metrics in Dashboard**
- Heroku dashboard → App → Metrics tab

### **Set Up Alerts**
- Heroku dashboard → Alerts tab

---

## 🚀 What's Next?

1. ✅ App is live on Heroku
2. Share your dashboard: `https://your-app-name.herokuapp.com`
3. Monitor logs regularly
4. Set up GitHub auto-deploy for continuous deployment
5. Add custom domain (optional, paid feature)

---

## 📚 Useful Commands

| Command | Purpose |
|---------|---------|
| `heroku apps` | List all apps |
| `heroku logs --tail` | View live logs |
| `heroku restart` | Restart app |
| `heroku open` | Open app in browser |
| `heroku destroy --app app-name` | Delete app |
| `git push heroku main` | Deploy to Heroku |
| `heroku config` | View environment variables |

---

## 🎉 Congratulations!

Your MBA KPI Dashboard is now live on the internet! 🌐

**Share it with others:**
- Tell them to visit: `https://your-app-name.herokuapp.com`
- It will work on any device
- No installation needed

---

## 💡 Pro Tips

1. **Custom Domain**
   - Add your own domain (premium feature)
   - `heroku domains:add yourdomain.com`

2. **Performance**
   - Use free tier for testing
   - Upgrade to paid for production

3. **Updates**
   - Make changes locally
   - Test with `npm run dev`
   - Commit and push: `git push heroku main`

4. **Backups**
   - Keep code on GitHub
   - Enable GitHub integration for auto-deploy

---

For more help: https://devcenter.heroku.com/articles/getting-started-with-python
