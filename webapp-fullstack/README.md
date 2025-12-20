# Full-Stack Web Application

> A complete web application template implementing the 3-layer architecture for reliable AI-assisted development.

## Architecture

This project uses the **3-layer architecture** for full-stack web development:

- **Layer 1: Directives** (`frontend/directives/`, `backend/directives/`) - Feature specs, API design, component patterns
- **Layer 2: Orchestration** (AI agent) - Intelligent routing between frontend and backend tasks
- **Layer 3: Execution** (Application code) - React/Next.js frontend, Node.js/Express backend

## Project Structure

```
.
├── frontend/               # Next.js/React application
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── hooks/         # Custom React hooks
│   │   └── styles/        # CSS/styling
│   ├── directives/        # Frontend feature specs
│   └── package.json
│
├── backend/                # Node.js/Express API
│   ├── src/
│   │   ├── routes/        # API endpoints
│   │   ├── controllers/   # Request handlers
│   │   ├── models/        # Data models
│   │   ├── middleware/    # Custom middleware
│   │   └── services/      # Business logic
│   ├── directives/        # Backend feature specs
│   └── package.json
│
├── shared/                 # Shared code between frontend/backend
│   ├── types/             # TypeScript types
│   └── utils/             # Shared utilities
│
├── docker-compose.yml      # Local development setup
└── improvements/           # Learning log
```

## Setup

### Prerequisites

- Node.js 18+ and npm
- PostgreSQL (optional, for database features)
- Docker (optional, for containerized development)

### Installation

1. **Install dependencies:**
   ```bash
   # Frontend
   cd frontend
   npm install
   
   # Backend
   cd ../backend
   npm install
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Setup database (if using):**
   ```bash
   cd backend
   npm run db:migrate
   npm run db:seed  # Optional: seed with sample data
   ```

## Development

### Start Development Servers

```bash
# Terminal 1 - Frontend (runs on http://localhost:3000)
cd frontend
npm run dev

# Terminal 2 - Backend API (runs on http://localhost:3001)
cd backend
npm run dev
```

### Using Docker

```bash
# Start all services
docker-compose up

# Stop services
docker-compose down
```

## Adding Features

### Frontend Features

1. **Create directive:** `frontend/directives/feature-name.md`
2. **Implement components:** `frontend/src/components/`
3. **Add pages/routes:** `frontend/src/pages/`
4. **Style:** `frontend/src/styles/`

### Backend Features

1. **Create directive:** `backend/directives/api-endpoint.md`
2. **Define routes:** `backend/src/routes/`
3. **Implement controllers:** `backend/src/controllers/`
4. **Add models:** `backend/src/models/`

### Shared Code

- **Types:** `shared/types/` - TypeScript interfaces/types
- **Utils:** `shared/utils/` - Helper functions used by both frontend and backend

## Testing

```bash
# Frontend tests
cd frontend
npm test

# Backend tests
cd backend
npm test

# E2E tests
npm run test:e2e
```

## Deployment

### Production Build

```bash
# Frontend
cd frontend
npm run build

# Backend
cd backend
npm run build
```

### Environment Variables

Update `.env` for production:
- Set `NODE_ENV=production`
- Use production database URLs
- Set secure secrets for JWT/sessions
- Configure CORS for production domain

### Deployment Options

- **Vercel** - Frontend (Next.js optimized)
- **Railway/Render** - Backend API
- **Docker** - Containerized deployment
- **AWS/GCP/Azure** - Full cloud deployment

## Common Operations

### Database Migrations

```bash
cd backend
npm run db:migrate       # Run migrations
npm run db:migrate:undo  # Rollback
npm run db:migrate:create name  # Create new migration
```

### Code Generation

```bash
# Generate new component
npm run generate:component ComponentName

# Generate new API route
npm run generate:route route-name
```

## Troubleshooting

### Port Already in Use

```bash
# Find and kill process on port 3000
lsof -ti:3000 | xargs kill

# Or use different ports in .env
```

### Database Connection Issues

- Verify PostgreSQL is running
- Check DATABASE_URL in .env
- Ensure database exists: `createdb dbname`

## Contributing

When you discover improvements:
1. Fix the issue in the code
2. Test thoroughly
3. Update relevant directive
4. Document in `improvements/IMPROVEMENTS.md`

## Tech Stack

**Frontend:**
- Next.js / React
- TypeScript
- Tailwind CSS / Styled Components
- React Query / SWR

**Backend:**
- Node.js / Express
- TypeScript
- PostgreSQL / MongoDB
- Prisma / TypeORM

**DevOps:**
- Docker
- GitHub Actions
- Vercel / Railway
