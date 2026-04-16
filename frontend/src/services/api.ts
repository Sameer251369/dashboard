import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const dashboardAPI = {
  getKPIs: async () => {
    const response = await api.get('/kpis');
    return response.data;
  },

  getKPIsByCategory: async (category: string) => {
    const response = await api.get(`/kpis/${category}`);
    return response.data;
  },

  getKPIsByStatus: async (status: string) => {
    const response = await api.get(`/kpis/status/${status}`);
    return response.data;
  },

  getSummary: async () => {
    const response = await api.get('/summary');
    return response.data;
  },

  getCategoryChartData: async () => {
    const response = await api.get('/charts/category');
    return response.data;
  },

  getStudentMetrics: async () => {
    const response = await api.get('/charts/student-metrics');
    return response.data;
  },

  getGapAnalysis: async () => {
    const response = await api.get('/charts/gap-analysis');
    return response.data;
  },

  getHealth: async () => {
    const response = await api.get('/health');
    return response.data;
  },
};

export default api;
