# Render.com Deployment (Permanently Free Tier)

**Render.com** offers a **permanently free tier** - no credit card, no time limit!

## 📋 Step-by-Step

### **1. Sign Up (2 minutes)**

1. Go to: https://render.com
2. Click "Sign up"
3. Choose "Sign up with GitHub"
4. Authorize Render

### **2. Create Web Service (1 minute)**

1. Click "New +" button
2. Select "Web Service"
3. Choose "Deploy an existing project from a Git repository"
4. Select this repository

### **3. Configure Service (2 minutes)**

Fill in the form:

| Field | Value |
|-------|-------|
| **Name** | mba-kpi-dashboard |
| **Environment** | Python 3 |
| **Build Command** | `pip install -r backend/requirements.txt && cd frontend && npm install && npm run build` |
| **Start Command** | `cd backend && gunicorn app:app` |
| **Plan** | Free |

### **4. Set Environment Variables (1 minute)**

Click "Environment" and add:

```
FLASK_ENV = production
DEBUG = False
ALLOWED_ORIGINS = https://mba-kpi-dashboard.onrender.com
```

### **5. Deploy! (1 minute)**

Click "Create Web Service"

Wait 3-5 minutes for build and deployment...

✅ **Done!** Your app is live!

---

## 🌍 Access Your App

After deployment completes:

**Dashboard**: https://mba-kpi-dashboard.onrender.com

View the URL in Render Dashboard under your service name.

---

## ✅ Verification

Test these URLs:

1. **Frontend**: https://your-service.onrender.com
2. **API Health**: https://your-service.onrender.com/api/health
3. **All KPIs**: https://your-service.onrender.com/api/kpis

Should return JSON data ✅

---

## 🔄 Auto-Deploy from GitHub

**Enable Auto-Deploy:**

1. In Render Dashboard
2. Go to your service
3. Settings → Auto-Deploy
4. Toggle "Auto-deploy new pushes"

Now, every time you push to GitHub, Render auto-deploys!

---

## 📊 Monitor Your App

**Dashboard Features:**

- **Logs**: Real-time app output
- **Metrics**: CPU, memory, network
- **Deployments**: History of builds
- **Settings**: Configure environment

---

## 🆘 Troubleshooting

### **Build Takes Too Long**

Normal - first build takes 3-5 minutes. Subsequent builds are faster.

### **Build Failed**

Check logs:
1. Click "Logs" tab
2. Look for error messages
3. Common issues:
   - Missing `requirements.txt`
   - Wrong build command
   - npm package errors

### **App Won't Start**

Check runtime logs:
1. "Logs" tab
2. Look for Python errors
3. Try:
   - Restart service
   - Check environment variables
   - Verify ALLOWED_ORIGINS

### **Frontend Shows 404**

Ensure:
1. ✅ Frontend built: `npm run build`
2. ✅ `frontend/dist/` committed to git
3. ✅ Service redeployed

---

## 💡 Pro Tips

1. **Permanently Free**: Unlike Heroku, Render's free tier never expires
   - No credit card required
   - No time limit
   - Spin-down on inactivity

2. **Automatic Restarts**: Service restarts if it crashes

3. **GitHub Integration**: Just push code, Render handles it

4. **Custom Domain**:
   - Free: *.onrender.com subdomain
   - Paid: Your own domain

5. **Simple Scaling**:
   - Start free
   - Upgrade anytime if needed
   - Paid plans start at $7/month

---

## 🎯 Render vs Others

| Feature | Render | Railway | Heroku |
|---------|--------|---------|--------|
| Free Tier | ✅ Permanent | ✅ Limited | ❌ None |
| Auto-Deploy | ✅ Yes | ✅ Yes | ✅ Yes |
| Environment Vars | ✅ UI | ✅ UI | ✅ CLI |
| Cost | FREE | FREE ($5/mo) | $7/month |
| Support | Good | Good | Good |

---

## 📈 Scaling Your App

Start free, upgrade when needed:

| Tier | Cost | Use Case |
|------|------|----------|
| **Free** | FREE | Demo, testing |
| **Starter** | $7/month | Small production |
| **Standard** | $12/month | Growing apps |
| **Pro** | $25/month | Production apps |

---

## 🔐 Security Best Practices

1. ✅ Set `FLASK_ENV=production`
2. ✅ Set `DEBUG=False`
3. ✅ Update `ALLOWED_ORIGINS`
4. ✅ Use HTTPS (automatic)
5. ✅ Don't commit `.env` files

---

## 📚 Resources

- Render Docs: https://render.com/docs
- Deployment Guide: https://render.com/docs/deploy-web-service
- Environment Vars: https://render.com/docs/environment-variables
- Troubleshooting: https://render.com/docs/troubleshooting

---

## 🚀 Quick Start Summary

```
1. Sign up: https://render.com (GitHub)
2. New Service → Select repo
3. Configure: Python, build command, start command
4. Set environment variables
5. Deploy!
6. App live in 3-5 minutes ✅
```

---

## 🎉 You're Live!

Your dashboard is now running on Render with:

- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ Free tier
- ✅ Auto-restart
- ✅ GitHub auto-deploy

**Share your app**: `https://your-service.onrender.com`

No credit card. No time limit. Completely free! 🎊
