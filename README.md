# Roulette Application

A modern web application that allows users to spin a roulette wheel to randomly select names from a managed list, with full CRUD operations and analytics tracking.

## 🚀 Features

- **Interactive Roulette Wheel**: Spin to randomly select from available names
- **Name Management**: Full CRUD operations for managing participants
- **Analytics Dashboard**: View statistics, history, and export data
- **Modern Tech Stack**: Built with FastAPI (Python) and Vue.js 3 (TypeScript)
- **Real-time Updates**: WebSocket support for live interactions
- **Responsive Design**: Works on desktop and mobile devices

## 🏗️ Architecture

### Backend (Python)
- **FastAPI**: Modern, fast web framework with automatic API documentation
- **SQLAlchemy 2.0**: Async ORM for database operations
- **PostgreSQL**: Robust relational database
- **Redis**: Caching and session management
- **Pydantic**: Data validation and serialization
- **uv**: Fast Python package management

### Frontend (Vue.js 3)
- **Vue 3**: Progressive JavaScript framework with Composition API
- **TypeScript**: Type-safe development
- **Pinia**: Intuitive state management
- **Vue Router**: Client-side routing
- **Tailwind CSS**: Utility-first CSS framework
- **Vite**: Lightning-fast build tooling

## 📁 Project Structure

```
roulette/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   ├── config.py       # Configuration settings
│   │   ├── models/         # Database models
│   │   ├── api/            # API routes
│   │   ├── services/       # Business logic
│   │   └── repositories/   # Data access layer
│   ├── tests/              # Backend tests
│   └── pyproject.toml      # Python dependencies
│
├── frontend/               # Vue.js frontend
│   ├── src/
│   │   ├── components/     # Vue components
│   │   ├── views/          # Page views
│   │   ├── stores/         # Pinia stores
│   │   └── router/         # Vue Router config
│   ├── tests/              # Frontend tests
│   └── package.json        # Node.js dependencies
│
└── docker-compose.yml      # Docker development environment
```

## 🛠️ Development Setup

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker (optional, for database)

### Backend Setup

1. Install uv (Python package manager):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Navigate to backend directory and install dependencies:
```bash
cd backend
uv sync
```

3. Start the development server:
```bash
uv run uvicorn app.main:app --reload
```

4. API documentation will be available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Frontend Setup

1. Navigate to frontend directory and install dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm run dev
```

3. Application will be available at: http://localhost:3000

### Running Tests

**Backend Tests:**
```bash
cd backend
uv run pytest
```

**Frontend Tests:**
```bash
cd frontend
npm run test:unit          # Unit tests
npm run test:e2e           # E2E tests
```

## 🐳 Docker Development

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 📖 API Documentation

Once the backend is running, visit http://localhost:8000/docs for interactive API documentation.

### Key Endpoints

- `GET /health` - Health check
- `POST /api/v1/roulette/spin` - Spin the roulette
- `GET|POST|PUT|DELETE /api/v1/names` - Manage names
- `GET /api/v1/analytics/*` - Analytics endpoints

## 🧪 Testing Strategy

- **Unit Tests**: Test individual components and functions
- **Integration Tests**: Test API endpoints and database interactions
- **E2E Tests**: Test complete user workflows
- **Type Checking**: TypeScript and mypy for type safety

## 🚀 Production Deployment

### Docker Production Build

```bash
# Build production images
docker-compose -f docker-compose.prod.yml build

# Deploy
docker-compose -f docker-compose.prod.yml up -d
```

### Environment Variables

Copy `.env.example` files and configure:

**Backend (.env):**
```env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/roulette
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key-here
DEBUG=false
```

**Frontend (.env):**
```env
VITE_API_URL=http://localhost:8000
```

## 📊 Features Overview

### 🎰 Roulette Game
- Interactive spinning wheel animation
- Random name selection with fair distribution
- Real-time results display
- Session tracking for analytics

### 👥 Name Management
- Add/remove names from the pool
- Import/export name lists
- Enable/disable names without deletion
- Weighted selection (future enhancement)

### 📈 Analytics
- Game history and statistics
- Name selection frequency
- Export data in CSV/JSON formats
- Visual charts and graphs

## 🔮 Roadmap

- [ ] User authentication and roles
- [ ] Multiple roulette wheels/games
- [ ] Real-time multiplayer sessions
- [ ] Advanced analytics and reporting
- [ ] Mobile application
- [ ] WebRTC video chat integration
- [ ] Custom themes and branding

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with modern web technologies
- Inspired by the need for fair and transparent random selection
- Designed for scalability and maintainability

---

**Happy Spinning! 🎰**