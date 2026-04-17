# Stage 1: Build frontend
FROM node:18-alpine AS frontend-builder
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Build backend
FROM python:3.11-slim
WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Copy frontend build from stage 1
COPY --from=frontend-builder /app/dist ./dist

EXPOSE 5000

ENV FLASK_ENV=production
ENV DEBUG=False

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
