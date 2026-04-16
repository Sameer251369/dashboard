# Quick Start Guide

## ⚡ Fast Setup (5 minutes)

### Terminal 1: Backend (Python)

```bash
cd mba-dashboard/backend
pip install -r requirements.txt
python app.py
```

✅ Backend runs on `http://localhost:5000`

### Terminal 2: Frontend (React)

```bash
cd mba-dashboard/frontend
npm install
npm run dev
```

✅ Dashboard opens automatically on `http://localhost:3000`

---

## 🎨 What You Get

A professional KPI dashboard with:

1. **Summary Cards** - At a glance metrics
   - Total KPIs: 29
   - Achieved: 24 (82.8%)
   - Not Achieved: 5
   - Student Satisfaction: 4.27/5

2. **Interactive Charts**
   - Achievement by Category (Program vs MBA)
   - Target vs Actual Student Metrics

3. **KPI Table**
   - All 29 KPIs with detailed info
   - Progress bars
   - Filter by status (All/Achieved/Not Achieved)
   - Sortable and searchable

4. **Modern Design**
   - Dark theme with gradients
   - Smooth animations
   - Responsive layout
   - Professional color scheme

---

## 🔧 Configuration

### Change Backend Port
Edit `backend/app.py`:
```python
app.run(debug=True, port=5001)  # Change 5000 to 5001
```

### Change Frontend Port
Edit `frontend/vite.config.ts`:
```typescript
server: {
  port: 3001,  // Change 3000 to 3001
}
```

Also update API URL in `frontend/src/services/api.ts`:
```typescript
const API_BASE_URL = 'http://localhost:5001/api';
```

---

## 📊 Adding Custom KPIs

1. Open `backend/app.py`
2. Find the `kpis` list
3. Add new entry:
```python
{
  "code": "KPI-XX-01",
  "name": "Your KPI Name",
  "target": 100,
  "actual": 85,
  "status": "Achieved",
  "category": "Program"  # or "MBA"
}
```
4. Restart backend - changes apply instantly!

---

## 🚀 Production Build

```bash
cd frontend
npm run build
```

Output in `frontend/dist/` ready for deployment

---

## 💡 Tips

- Keep both servers running side by side
- Frontend auto-reloads on code changes
- Backend auto-reloads in debug mode
- Check console (F12) for any errors
- API is at http://localhost:5000/api

---

**Enjoy your new dashboard!** 🎉
