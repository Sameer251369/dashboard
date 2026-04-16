from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__, static_folder='../frontend/dist', static_url_path='/')
CORS(app)

# ─── KPI Data ─────────────────────────────────────────────────────────────
kpis = [
    {"code": "KPI-PG-01", "name": "Students' evaluation of learning experience", "target": 4.1, "actual": 4.49, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-02", "name": "Students' evaluation of course quality", "target": 4.0, "actual": 4.45, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-03", "name": "Students' evaluation of academic supervision", "target": 3.5, "actual": 4.65, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-04", "name": "Average time for students' graduation", "target": 4, "actual": 4, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-05", "name": "Rate of students dropping out", "target": 10, "actual": 7.1, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-06", "name": "Employer's evaluation of graduates' competency", "target": 3.5, "actual": 4.17, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-07", "name": "Students' satisfaction with provided services", "target": 4.0, "actual": 4.27, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-08", "name": "Ratio of students to faculty members", "target": 22, "actual": 5, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-09", "name": "Percentage of publications of faculty members", "target": 55, "actual": 41.5, "status": "Not Achieved", "category": "Program"},
    {"code": "KPI-PG-10", "name": "Rate of published research per faculty member", "target": 1.73, "actual": 0.93, "status": "Not Achieved", "category": "Program"},
    {"code": "KPI-PG-11", "name": "Citations rate in refereed journals per faculty", "target": 14.29, "actual": 111, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-12", "name": "Percentage of student publications", "target": 5, "actual": 2, "status": "Achieved", "category": "Program"},
    {"code": "KPI-PG-13", "name": "Patents, innovative products, and awards", "target": 4.2, "actual": 5, "status": "Achieved", "category": "Program"},
    {"code": "MBA-PG-01", "name": "Avg. clarity of mission for stakeholders", "target": 3.5, "actual": 4.24, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-02", "name": "Stakeholder awareness of program mission", "target": 3.7, "actual": 4.12, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-03", "name": "Satisfaction with organizational environment", "target": 3.3, "actual": 4.32, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-04", "name": "Satisfaction with integrity, equity and equality", "target": 3.5, "actual": 4.28, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-05", "name": "Stakeholder satisfaction of program information", "target": 3.5, "actual": 4.24, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-06", "name": "Faculty in teaching strategy training programs", "target": 50, "actual": 15.91, "status": "Not Achieved", "category": "MBA"},
    {"code": "MBA-PG-07", "name": "Faculty in tech-in-teaching training programs", "target": 50, "actual": 27.27, "status": "Not Achieved", "category": "MBA"},
    {"code": "MBA-PG-08", "name": "Achieved training programs in faculty plan", "target": 70, "actual": 100, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-09", "name": "Faculty participated in training plan programs", "target": 50, "actual": 77.27, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-10", "name": "Student evaluation of course intro materials", "target": 4.0, "actual": 4.24, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-11", "name": "Faculty members per specialization in program", "target": 3, "actual": 8.3, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-12", "name": "Faculty participating in community services", "target": 10, "actual": 21, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-13", "name": "Publications aligned with CBE research priorities", "target": 70, "actual": 100, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-14", "name": "Satisfaction with LMS (Blackboard)", "target": 3.8, "actual": 4.23, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-15", "name": "Student satisfaction with academic advising", "target": 3.5, "actual": 3.77, "status": "Achieved", "category": "MBA"},
    {"code": "MBA-PG-16", "name": "Alumni activities planned per year", "target": 4, "actual": 3, "status": "Not Achieved", "category": "MBA"},
]

# ─── API Endpoints ────────────────────────────────────────────────────────
@app.route('/api/kpis', methods=['GET'])
def get_kpis():
    """Get all KPIs"""
    return jsonify(kpis)

@app.route('/api/kpis/<category>', methods=['GET'])
def get_kpis_by_category(category):
    """Get KPIs by category (Program or MBA)"""
    filtered = [k for k in kpis if k['category'] == category]
    return jsonify(filtered)

@app.route('/api/kpis/status/<status>', methods=['GET'])
def get_kpis_by_status(status):
    """Get KPIs by status (Achieved or Not Achieved)"""
    filtered = [k for k in kpis if k['status'] == status]
    return jsonify(filtered)

@app.route('/api/summary', methods=['GET'])
def get_summary():
    """Get dashboard summary statistics"""
    total = len(kpis)
    achieved = len([k for k in kpis if k['status'] == 'Achieved'])
    not_achieved = total - achieved
    
    # Calculate student satisfaction (average of first 7 student-related metrics)
    student_satisfaction = sum([k['actual'] for k in kpis[:7]]) / 7
    
    # Category breakdown
    program_kpis = [k for k in kpis if k['category'] == 'Program']
    mba_kpis = [k for k in kpis if k['category'] == 'MBA']
    
    program_achieved = len([k for k in program_kpis if k['status'] == 'Achieved'])
    mba_achieved = len([k for k in mba_kpis if k['status'] == 'Achieved'])
    
    return jsonify({
        'total': total,
        'achieved': achieved,
        'not_achieved': not_achieved,
        'success_rate': round((achieved / total) * 100, 1),
        'student_satisfaction': round(student_satisfaction, 2),
        'report_date': '24 August 2025',
        'academic_year': '2024',
        'categories': {
            'program': {
                'total': len(program_kpis),
                'achieved': program_achieved,
                'not_achieved': len(program_kpis) - program_achieved
            },
            'mba': {
                'total': len(mba_kpis),
                'achieved': mba_achieved,
                'not_achieved': len(mba_kpis) - mba_achieved
            }
        }
    })

@app.route('/api/charts/category', methods=['GET'])
def get_category_chart_data():
    """Get data for category achievement chart"""
    program = [k for k in kpis if k['category'] == 'Program']
    mba = [k for k in kpis if k['category'] == 'MBA']
    
    return jsonify({
        'labels': ['Program KPIs', 'MBA-Specific KPIs'],
        'achieved': [
            len([k for k in program if k['status'] == 'Achieved']),
            len([k for k in mba if k['status'] == 'Achieved'])
        ],
        'not_achieved': [
            len([k for k in program if k['status'] != 'Achieved']),
            len([k for k in mba if k['status'] != 'Achieved'])
        ]
    })

@app.route('/api/charts/student-metrics', methods=['GET'])
def get_student_metrics():
    """Get student-related metrics for comparison chart"""
    student_metrics = [
        {"name": "Learning experience", "target": 4.1, "actual": 4.49},
        {"name": "Course quality", "target": 4.0, "actual": 4.45},
        {"name": "Supervision", "target": 3.5, "actual": 4.65},
        {"name": "Satisfaction", "target": 4.0, "actual": 4.27},
        {"name": "Employer evaluation", "target": 3.5, "actual": 4.17},
    ]
    return jsonify(student_metrics)

@app.route('/api/charts/gap-analysis', methods=['GET'])
def get_gap_analysis():
    """Get gap analysis for not-achieved KPIs"""
    not_achieved = [k for k in kpis if k['status'] != 'Achieved']
    gap_data = []
    for k in not_achieved:
        gap = k['target'] - k['actual']
        gap_data.append({
            'code': k['code'],
            'name': k['name'],
            'target': k['target'],
            'actual': k['actual'],
            'gap': gap,
            'gap_percentage': round((gap / k['target']) * 100, 1)
        })
    return jsonify(gap_data)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'timestamp': datetime.now().isoformat()})

# ─── Serve React Frontend ──────────────────────────────────────────────────
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    """Serve React app - if it's not an API route"""
    if path.startswith('api/'):
        return jsonify({'error': 'API endpoint not found'}), 404
    
    # Try to serve the requested file
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    
    # Otherwise serve index.html for React Router
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
