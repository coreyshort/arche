# API Service

> A backend API service template implementing the 3-layer architecture for reliable AI-assisted development.

## Architecture

This project uses the **3-layer architecture** for API development:

- **Layer 1: Directives** (`directives/`) - API design specs, endpoint definitions, authentication flows
- **Layer 2: Orchestration** (AI agent) - Intelligent routing between different service components
- **Layer 3: Execution** (API code) - Express/FastAPI routes, controllers, models, middleware

## Project Structure

```
.
├── src/
│   ├── routes/            # API endpoint definitions
│   ├── controllers/       # Request handlers and business logic
│   ├── models/            # Data models and schemas
│   ├── middleware/        # Custom middleware (auth, validation, etc.)
│   ├── services/          # Business logic services
│   ├── utils/             # Helper functions
│   └── index.js           # Application entry point
│
├── directives/            # API design and feature specs
├── tests/                 # Unit and integration tests
├── improvements/          # Learning log
├── Dockerfile             # Container definition
└── docker-compose.yml     # Local development setup
```

## Setup

### Prerequisites

- Node.js 18+ (or Python 3.10+ for Python backend)
- PostgreSQL or MongoDB
- Redis (optional, for caching)
- Docker (optional)

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   # or for Python: pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Setup database:**
   ```bash
   npm run db:migrate
   npm run db:seed  # Optional: seed with sample data
   ```

## Development

### Start Development Server

```bash
# Node.js
npm run dev

# Python
python src/main.py
# or: uvicorn src.main:app --reload
```

API will be available at `http://localhost:3001`

### Using Docker

```bash
# Start all services (API + Database + Redis)
docker-compose up

# Stop services
docker-compose down
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Refresh access token
- `POST /api/v1/auth/logout` - User logout

### Users
- `GET /api/v1/users` - List users (admin only)
- `GET /api/v1/users/:id` - Get user by ID
- `PUT /api/v1/users/:id` - Update user
- `DELETE /api/v1/users/:id` - Delete user

### Health Check
- `GET /health` - Health check endpoint
- `GET /api/v1/status` - API status

## Adding Features

### 1. Create Directive

Document the feature in `directives/`:
```markdown
# Feature: New Resource API

## Endpoints
- GET /api/v1/resources - List resources
- POST /api/v1/resources - Create resource

## Authentication
Required: JWT token

## Validation
...
```

### 2. Implement Route

Create route in `src/routes/`:
```javascript
// src/routes/resources.js
const express = require('express');
const router = express.Router();
const resourceController = require('../controllers/resourceController');
const auth = require('../middleware/auth');

router.get('/', auth, resourceController.list);
router.post('/', auth, resourceController.create);

module.exports = router;
```

### 3. Implement Controller

Create controller in `src/controllers/`:
```javascript
// src/controllers/resourceController.js
exports.list = async (req, res) => {
  // Implementation
};

exports.create = async (req, res) => {
  // Implementation
};
```

### 4. Add Model

Define data model in `src/models/`:
```javascript
// src/models/Resource.js
const { DataTypes } = require('sequelize');

module.exports = (sequelize) => {
  return sequelize.define('Resource', {
    // Schema definition
  });
};
```

## Testing

```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test tests/users.test.js

# Watch mode
npm run test:watch
```

## Database Migrations

```bash
# Create migration
npm run migrate:create migration-name

# Run migrations
npm run migrate:up

# Rollback
npm run migrate:down

# Reset database
npm run db:reset
```

## Deployment

### Production Build

```bash
npm run build
npm start
```

### Docker Deployment

```bash
# Build image
docker build -t api-service .

# Run container
docker run -p 3001:3001 --env-file .env api-service
```

### Environment Variables

For production, ensure you set:
- `NODE_ENV=production`
- Strong `JWT_SECRET` and `REFRESH_TOKEN_SECRET`
- Production database URL
- CORS origins for your domain
- Monitoring/logging services (Sentry, etc.)

## Security

- ✅ JWT authentication
- ✅ Password hashing (bcrypt)
- ✅ Rate limiting
- ✅ CORS configuration
- ✅ Helmet.js security headers
- ✅ Input validation
- ✅ SQL injection prevention
- ✅ XSS protection

## Monitoring

- Health check endpoint: `GET /health`
- Metrics endpoint: `GET /metrics` (if enabled)
- Logging with Winston/Pino
- Error tracking with Sentry (optional)

## Common Operations

### Adding Middleware

```javascript
// src/middleware/myMiddleware.js
module.exports = (req, res, next) => {
  // Middleware logic
  next();
};
```

### Adding Validation

```javascript
const { body } = require('express-validator');

const validateUser = [
  body('email').isEmail(),
  body('password').isLength({ min: 8 })
];
```

### Error Handling

```javascript
class AppError extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    this.isOperational = true;
  }
}
```

## Troubleshooting

### Port Already in Use
```bash
lsof -ti:3001 | xargs kill
```

### Database Connection Issues
- Check DATABASE_URL in .env
- Verify database is running
- Test connection: `psql $DATABASE_URL`

### Authentication Issues
- Verify JWT_SECRET is set
- Check token expiry settings
- Review middleware order

## Tech Stack

**Core:**
- Node.js / Express (or Python / FastAPI)
- TypeScript (optional)
- PostgreSQL / MongoDB

**Authentication:**
- JWT
- bcrypt
- Passport.js (optional)

**Validation:**
- express-validator / Joi

**Testing:**
- Jest / Mocha
- Supertest

**DevOps:**
- Docker
- GitHub Actions
- Railway / Render

## Contributing Back to Arche

As you work with this template, you'll discover better patterns, edge cases, and improvements. **Please contribute these learnings back:**

- Found a missing dependency? Create an issue.
- Discovered a better workflow? Share it.
- Hit an edge case? Document it.

Create issues at: https://github.com/coreyshort/arche/issues

Your improvements make arche stronger for everyone. This is how the system evolves—through real-world usage feeding back into better templates.


## A Virtuous Circle

If arche helps you build something valuable, consider helping others discover it. Not through marketing tactics, but through genuine sharing:

- If you write about your project, mention the tools that made it possible
- If colleagues face similar challenges, share what worked for you
- If you spot ways to make the documentation clearer, contribute them

Improvements to discoverability, documentation, and knowledge sharing are as valuable as code contributions. The goal is making good tools accessible to everyone who needs them.
