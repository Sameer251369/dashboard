# MBA Program KPI Dashboard

A modern, fully dynamic KPI dashboard for MBA programs built with Python (Flask) backend and React frontend.

## Features

✨ **Modern UI** - Dark theme with smooth animations and gradients
📊 **Interactive Charts** - Real-time chart.js visualizations
📈 **KPI Tracking** - Track 29 key performance indicators
🔍 **Smart Filtering** - Filter KPIs by status (Achieved/Not Achieved)
📱 **Responsive Design** - Works seamlessly on desktop and mobile
⚡ **Real-time API** - Python Flask API with CORS support

## Project Structure

```
mba-dashboard/
├── backend/           # Python Flask API
│   ├── app.py        # Main Flask application
│   └── requirements.txt
├── frontend/          # React + TypeScript frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── services/     # API service
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   ├── vite.config.ts
│   └── index.html
└── README.md
```

## Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

## Backend Setup

### 1. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run Flask Server

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Frontend Setup

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Run Development Server

```bash
npm run dev
```

The dashboard will open at `http://localhost:3000`

## API Endpoints

- `GET /api/kpis` - Get all KPIs
- `GET /api/kpis/:category` - Get KPIs by category (Program/MBA)
- `GET /api/kpis/status/:status` - Get KPIs by status
- `GET /api/summary` - Get dashboard summary
- `GET /api/charts/category` - Get category chart data
- `GET /api/charts/student-metrics` - Get student metrics
- `GET /api/charts/gap-analysis` - Get gap analysis
- `GET /api/health` - Health check

## Development

### Build Frontend for Production

```bash
cd frontend
npm run build
```

Output will be in `frontend/dist/`

## Technology Stack

### Backend
- Flask 3.0
- Flask-CORS
- Python 3.8+

### Frontend
- React 18
- TypeScript
- Vite
- Tailwind CSS
- Chart.js
- Lucide React (Icons)
- Axios

## Color Scheme

- **Achieved**: Green (#10b981)
- **Not Achieved**: Red (#ef4444)
- **Background**: Dark Slate (#0f172a)
- **Cards**: Slate (#1e293b)

## Features Details

### Summary Cards
- Total KPIs count
- Achieved KPIs with success rate
- Not Achieved KPIs
- Student Satisfaction score

### Charts
- **Achievement by Category**: Stacked bar chart comparing Program vs MBA KPIs
- **Target vs Actual**: Grouped bar chart showing student metrics

### KPI Table
- Full KPI listing with code, name, target, actual, and progress
- Filter buttons for quick status filtering
- Progress bars for visual representation
- Status badges (Achieved/Not Achieved)

## Customization

### Adding New KPIs

Edit `backend/app.py` and add new entries to the `kpis` list:

```python
{
  "code": "KPI-XX-01",
  "name": "Your KPI Name",
  "target": 100,
  "actual": 85,
  "status": "Achieved",  # or "Not Achieved"
  "category": "Program"  # or "MBA"
}
```

### Styling

The frontend uses Tailwind CSS. Modify `frontend/tailwind.config.js` or add custom styles in `frontend/src/index.css`.

## Troubleshooting

### CORS Error
Make sure the backend is running on `http://localhost:5000` and the frontend can reach it.

### Port Already in Use
- Backend: Change port in `app.py` - `app.run(debug=True, port=5001)`
- Frontend: Change port in `vite.config.ts` - `port: 3001`

### Dependencies Issues
- Python: `pip install --upgrade -r requirements.txt`
- Node: `npm cache clean --force && npm install`

## License

MIT

## Created

Built with ❤️ for MBA Program KPI Tracking

---

**Ready to use!** Run both servers and enjoy your modern KPI dashboard! 🚀
