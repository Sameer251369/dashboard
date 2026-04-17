# Netlify Deployment (For Frontend)

**Netlify** is perfect for hosting the **static frontend** with unlimited bandwidth and continuous deployment.

## 📋 How It Works

- **Frontend**: Hosted on Netlify (FREE, global CDN)
- **Backend**: On Railway/Render (FREE)
- **Communication**: Frontend calls backend API

## 🚀 Step-by-Step

### **1. Sign Up (1 minute)**

1. Go to: https://netlify.com
2. Click "Sign up"
3. Choose "Sign up with GitHub"
4. Authorize Netlify

### **2. Connect Repository (1 minute)**

1. Click "Add new site"
2. Select "Import an existing project"
3. Choose GitHub
4. Select this repository
5. Click "Import"

### **3. Build Configuration (1 minute)**

Netlify auto-detects from `netlify.toml`:

| Setting | Value |
|---------|-------|
| **Build Command** | `npm run build` |
| **Publish Directory** | `frontend/dist` |
| **Node Version** | 18 |

(These are already configured!)

### **4. Set Environment Variables (1 minute)**

In Netlify Dashboard:

1. Site Settings → Build & Deploy → Environment
2. Add Variable:
   ```
   VITE_API_URL = https://your-backend.railway.app/api
   ```

### **5. Deploy! (1 minute)**

Click "Deploy site"

Wait for build... ✅ **Done!**

---

## 🌍 Your Frontend is Live!

**Frontend URL**: `https://your-site.netlify.app`

---

## 🔌 Connect to Your Backend

Update environment variable to point to your backend:

```
VITE_API_URL = https://your-backend-service.onrender.com/api
```

**Example:**
- Backend on Render: `https://mba-kpi-dashboard.onrender.com/api`
- Frontend on Netlify: `https://mba-dashboard.netlify.app`

---

## ✅ Verification

1. Visit your Netlify URL
2. Dashboard should load
3. Check browser console (F12) for errors
4. Verify API calls succeed

---

## 🔄 Auto-Deploy

Every time you push to GitHub:

1. Netlify detects the push
2. Automatically builds frontend
3. Deploys new version
4. **No extra steps needed!**

---

## 📊 Monitor Your Site

**Netlify Dashboard:**

- **Deploys**: View build history
- **Logs**: Build and runtime logs
- **Analytics**: Traffic, performance
- **Functions**: Serverless functions (optional)

---

## 💡 Pro Tips

1. **Custom Domain** (Optional):
   - Buy domain on Netlify
   - Point DNS to Netlify
   - Automatic HTTPS

2. **Preview Deploys**:
   - Every GitHub PR gets a preview URL
   - Test before merging

3. **Rollback**:
   - Easily revert to previous version
   - One-click rollback

4. **Performance**:
   - Global CDN
   - Automatic image optimization
   - Instant caching

---

## 🎯 Complete Setup (Frontend + Backend)

### **Setup A: Railway Backend + Netlify Frontend** (Easiest)

```
Backend:
1. Railway.app → Deploy backend
2. Get URL: https://your-app.railway.app

Frontend:
1. Netlify → Deploy frontend
2. Set VITE_API_URL = https://your-app.railway.app/api
3. Done!
```

### **Setup B: Render Backend + Netlify Frontend**

```
Backend:
1. Render.com → Deploy backend
2. Get URL: https://your-service.onrender.com

Frontend:
1. Netlify → Deploy frontend
2. Set VITE_API_URL = https://your-service.onrender.com/api
3. Done!
```

---

## 🔐 Security

- ✅ HTTPS automatic
- ✅ DDoS protection
- ✅ SSL certificate free
- ✅ Security headers
- ✅ Secure environment variables

---

## 📈 Scaling

Netlify's free tier includes:

- **Unlimited bandwidth**
- **300 build minutes/month** (more than enough!)
- **Global CDN**
- **Automatic scaling**

---

## 🆘 Troubleshooting

### **Build Failed**

1. Check build logs in Netlify
2. Look for npm errors
3. Common issues:
   - Missing dependencies
   - TypeScript errors
   - Missing environment variables

### **API Calls 404**

Make sure backend URL is correct:

```javascript
// Check browser console
console.log('API URL:', import.meta.env.VITE_API_URL)
```

Should show: `https://your-backend.onrender.com/api`

### **CORS Errors**

Update backend's `ALLOWED_ORIGINS`:

```
ALLOWED_ORIGINS = https://your-site.netlify.app,https://your-site.com
```

### **Page Shows Blank**

1. Open DevTools (F12)
2. Check Console tab for errors
3. Check Network tab for API calls
4. Verify backend is running

---

## 📚 Resources

- Netlify Docs: https://docs.netlify.com
- Deploy Guide: https://docs.netlify.com/site-deploys/overview/
- Environment Variables: https://docs.netlify.com/configure-builds/environment-variables/
- Build Settings: https://docs.netlify.com/configure-builds/overview/

---

## 💰 Cost

| Feature | Cost |
|---------|------|
| **Static Hosting** | FREE |
| **Bandwidth** | Unlimited |
| **Build Minutes** | 300/month (FREE) |
| **Custom Domain** | FREE |
| **Netlify Functions** | Optional ($$ if used) |

---

## 🎯 Recommended Setup

**For best experience:**

```
Frontend: Netlify (FREE, fast CDN)
Backend: Railway or Render (FREE)
Total Cost: $0
Performance: Excellent (global CDN)
Auto-Deploy: Yes (both platforms)
```

---

## 🚀 Quick Start

```
1. Go to: https://netlify.com
2. Sign up with GitHub
3. Import repository
4. Set VITE_API_URL environment variable
5. Deploy!
6. Frontend live in 1-2 minutes ✅
```

---

## 📊 Architecture

```
Your Browser
    ↓
Netlify CDN (Frontend)
    ↓
API Call
    ↓
Railway/Render (Backend)
    ↓
KPI Data
```

Fast, reliable, free! 🚀

---

## ✅ Deployment Checklist

- [ ] Backend deployed (Railway/Render)
- [ ] Backend API URL working
- [ ] Frontend built locally: `npm run build`
- [ ] Netlify account created
- [ ] Repository connected
- [ ] `VITE_API_URL` set to backend URL
- [ ] Site deployed
- [ ] Dashboard accessible
- [ ] API calls working

---

## 🎉 You're Live!

Your app is now:
- **Frontend**: Global CDN (Netlify)
- **Backend**: Always-on server (Railway/Render)
- **Performance**: ⚡ Lightning fast
- **Cost**: FREE
- **Auto-Deploy**: Yes

**Share it**: `https://your-site.netlify.app`

No credit card. Unlimited bandwidth. Completely free! 🎊
