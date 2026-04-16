# Deployment Guide

## Local Deployment

### Option 1: Direct Run (Development)
```bash
# Terminal 1 - Backend
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

# Terminal 2 - Frontend
cd frontend
npm install
npm run dev
```

### Option 2: Docker Compose (Recommended)
```bash
docker-compose up --build
```

Access at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

---

## Production Deployment

### 1. Build Frontend
```bash
cd frontend
npm run build
```

Output: `frontend/dist/` directory

### 2. Prepare Backend
```bash
cd backend
pip install gunicorn
```

### 3. Update Flask for Production
Edit `backend/app.py`, change last line:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### 4. Run with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### 5. Serve Static Files
```bash
# Copy built frontend to backend static folder
cp -r frontend/dist/* backend/static/
```

---

## Cloud Deployment

### AWS EC2
```bash
# SSH into instance
ssh -i key.pem ubuntu@your-instance-ip

# Clone repo
git clone your-repo.git
cd mba-dashboard

# Install dependencies
sudo apt update
sudo apt install python3-pip nodejs npm

# Setup and run
docker-compose up -d
```

### Heroku
```bash
heroku create your-app-name
git push heroku main

# Set environment variables
heroku config:set FLASK_ENV=production
```

### DigitalOcean
```bash
# Droplet setup with Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Deploy
docker-compose up -d
```

### Vercel (Frontend Only)
```bash
cd frontend
npm install -g vercel
vercel deploy --prod
```

---

## Environment Configuration

Create `.env` files:

### `backend/.env`
```env
FLASK_ENV=production
DEBUG=False
PORT=5000
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
```

### `frontend/.env.production`
```env
VITE_API_URL=https://api.yourdomain.com
```

---

## Security Considerations

### 1. CORS Configuration
Update `backend/app.py`:
```python
CORS(app, resources={
    r"/api/*": {
        "origins": os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000').split(','),
        "methods": ["GET", "POST"],
    }
})
```

### 2. SSL/HTTPS
Use Nginx with Let's Encrypt:
```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    location / {
        proxy_pass http://localhost:3000;
    }
    
    location /api {
        proxy_pass http://localhost:5000;
    }
}
```

### 3. Environment Variables
Never commit `.env` files:
```bash
echo ".env" >> .gitignore
```

### 4. Rate Limiting
Add Flask-Limiter:
```bash
pip install Flask-Limiter
```

---

## Docker Deployment Checklist

- [ ] Build images: `docker-compose build`
- [ ] Start services: `docker-compose up -d`
- [ ] Check logs: `docker-compose logs -f`
- [ ] Test API: `curl http://localhost:5000/api/health`
- [ ] Test frontend: Open http://localhost:3000
- [ ] Stop services: `docker-compose down`

---

## Performance Optimization

### 1. Frontend
```bash
# Build with optimizations
npm run build -- --minify=terser
```

### 2. Backend
- Use Gunicorn with multiple workers: `-w 4`
- Add caching: `pip install flask-caching`
- Enable gzip compression

### 3. Database (if added)
- Add indexes
- Use connection pooling
- Implement caching layer

---

## Monitoring & Logging

### Frontend Monitoring
- Use Sentry: `npm install @sentry/react`
- Google Analytics
- Error tracking

### Backend Monitoring
- Use CloudWatch, DataDog, or New Relic
- Application logs to `/var/log/app.log`
- Error alerting

---

## Backup & Recovery

### Data Backup
```bash
# Backup database (if using)
mysqldump -u user -p database > backup.sql

# Restore
mysql -u user -p database < backup.sql
```

### Application Backup
```bash
# Version control (primary)
git push origin main

# Filesystem backup
tar -czf mba-dashboard-backup.tar.gz mba-dashboard/
```

---

## Scaling Considerations

### Horizontal Scaling
```bash
# Multiple backend instances
docker-compose up -d --scale backend=3
```

### Load Balancing
Use Nginx upstream:
```nginx
upstream backend {
    server backend1:5000;
    server backend2:5000;
    server backend3:5000;
}
```

### CDN for Static Assets
- Cloudflare
- AWS CloudFront
- Fastly

---

## Maintenance

### Update Dependencies
```bash
# Python
pip install -U pip
pip list --outdated
pip install --upgrade package-name

# Node
npm outdated
npm update
npm audit fix
```

### Database Maintenance
```bash
# If using SQLite
VACUUM;
ANALYZE;

# If using MySQL
OPTIMIZE TABLE table_name;
REPAIR TABLE table_name;
```

### Log Rotation
```bash
# Configure logrotate
/var/log/app.log {
    daily
    rotate 7
    compress
    delaycompress
}
```

---

## Rollback Procedure

```bash
# If deployment fails
git revert HEAD
docker-compose down
docker-compose up -d
```

---

## Cost Optimization

- Use cloud provider free tier during development
- Utilize serverless for sporadic traffic
- Implement caching to reduce database calls
- Use CDN for static assets
- Monitor and cleanup unused resources

---

## Support & Troubleshooting

### Common Issues

**502 Bad Gateway**
- Backend not running
- Port mismatch
- Check Docker logs: `docker-compose logs backend`

**CORS Error**
- Update ALLOWED_ORIGINS
- Check frontend .env file
- Verify API URL

**Out of Memory**
- Increase container limits
- Reduce worker processes
- Implement caching

---

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Docker Documentation](https://docs.docker.com/)
- [Nginx Configuration](https://nginx.org/en/docs/)
- [Let's Encrypt](https://letsencrypt.org/)

---

**For production deployments, always test thoroughly in staging first!**
