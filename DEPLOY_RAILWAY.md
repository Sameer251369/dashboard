# Railway.app Deployment (Easiest & Cheapest)

**Railway.app** is the easiest way to deploy! Free $5/month credit, no credit card required initially.

## 📋 Step-by-Step

### **1. Sign Up (2 minutes)**

1. Go to: https://railway.app
2. Click "Start Now" → "Deploy with GitHub"
3. Authorize Railway to access GitHub
4. Approve access

### **2. Create New Project (1 minute)**

1. Click "New Project"
2. Select "Deploy from GitHub"
3. Choose this repository
4. Select the branch (usually `main` or `master`)

### **3. Configure & Deploy (1 minute)**

Railway auto-detects your project type!

**Automatic Setup:**
- ✅ Detects Python backend
- ✅ Reads `requirements.txt`
- ✅ Sets up environment
- ✅ Builds and deploys

### **4. Set Environment Variables (30 seconds)**

Click "Add Variable" and add:

```
FLASK_ENV = production
ALLOWED_ORIGINS = https://your-app.railway.app
DEBUG = False
```

### **5. Done! 🎉**

Your app is live at: `https://your-app.railway.app`

---

## ✅ Verification

Visit these URLs to verify deployment:

- **Dashboard**: https://your-app.railway.app
- **API Health**: https://your-app.railway.app/api/health
- **All KPIs**: https://your-app.railway.app/api/kpis

Should see JSON response like:
```json
{
  "code": "KPI-PG-01",
  "name": "Students' evaluation of learning experience",
  ...
}
```

---

## 🔄 Updates & Redeployment

**To update your app:**

1. Make changes locally
2. Commit: `git commit -m "Update"`
3. Push: `git push origin main`
4. Railway auto-deploys! ✅

No extra steps needed!

---

## 📊 Monitor Your App

In Railway Dashboard:

- **Logs**: Click "Logs" tab to see real-time output
- **Metrics**: CPU, memory, network usage
- **Deployments**: History of all deployments
- **Settings**: Environment variables, domains, builds

---

## 🆘 Troubleshooting

### **Build Failed**

Check logs:
1. Click "Deployments" tab
2. View failed build logs
3. Common issues:
   - Missing dependencies → Add to `requirements.txt`
   - Wrong start command → Check `railway.json`

### **App Crashes**

Check logs:
1. Click "Logs" tab
2. Look for errors
3. Common fixes:
   - Restart: Click "Restart" button
   - Check environment variables
   - Verify `ALLOWED_ORIGINS` includes your domain

### **Frontend 404 Errors**

Make sure:
1. ✅ Frontend built locally: `npm run build`
2. ✅ `frontend/dist/` folder committed to git
3. ✅ App redeployed

---

## 💡 Pro Tips

1. **Free Credit**: Railway gives $5/month free
   - Enough to run small app indefinitely
   - No credit card until you exceed limit

2. **Auto-Restart**: App automatically restarts if it crashes

3. **Environment Variables**: Add via UI, no `.env` files needed

4. **Custom Domain**: 
   - Paid feature ($5/month)
   - Use Railway subdomain for free

5. **Logs**: Check logs first for any issues

---

## 📈 Scaling

When your app grows:

1. Click "Plan" or "Pricing"
2. Upgrade to paid tier
3. Get more resources
4. No downtime!

---

## 🎯 Complete Deployment Flow

```
1. Create Railway account (free)
2. Connect GitHub
3. Select repository
4. Railway auto-builds & deploys
5. Set environment variables
6. Done! App is live ✅
```

**Total time: 5 minutes** ⏱️

---

## 📚 Resources

- Railway Docs: https://docs.railway.app
- GitHub Integration: https://docs.railway.app/guides/github
- Environment Variables: https://docs.railway.app/guides/environment-variables

---

## 🚀 Ready?

1. Go to: https://railway.app
2. Sign up with GitHub
3. Create project
4. Deploy!

**That's it!** Your app is live! 🎉
