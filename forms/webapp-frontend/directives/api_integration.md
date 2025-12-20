# API Integration Directive

## Goal
Integrate external APIs consistently with proper error handling and type safety.

## Inputs
- API endpoint documentation
- Authentication requirements
- Data schemas/types

## Process

### 1. Create API Service
Place API client logic in `src/services/`:

```typescript
// src/services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: parseInt(import.meta.env.VITE_API_TIMEOUT || '10000'),
});

// Add interceptors for auth tokens, error handling
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('auth_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
```

### 2. Create Resource-Specific Services
```typescript
// src/services/userService.ts
import api from './api';

export interface User {
  id: string;
  name: string;
  email: string;
}

export const userService = {
  getAll: async (): Promise<User[]> => {
    const response = await api.get<User[]>('/users');
    return response.data;
  },
  
  getById: async (id: string): Promise<User> => {
    const response = await api.get<User>(`/users/${id}`);
    return response.data;
  },
  
  create: async (user: Omit<User, 'id'>): Promise<User> => {
    const response = await api.post<User>('/users', user);
    return response.data;
  },
};
```

### 3. Use in Components
```typescript
import { useEffect, useState } from 'react';
import { userService, User } from '../services/userService';

export const UserList = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        setLoading(true);
        const data = await userService.getAll();
        setUsers(data);
      } catch (err) {
        setError('Failed to load users');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  
  return (
    <ul>
      {users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
};
```

## Outputs
- Type-safe API service modules
- Configured axios instance with interceptors
- Components using services correctly

## Edge Cases
- Network timeouts → Show user-friendly error
- 401/403 responses → Redirect to login
- 500 errors → Log to error tracking service
- Rate limiting → Implement retry logic
- Offline mode → Cache responses, queue requests

## Tools/Scripts
- Axios for HTTP client
- TypeScript for type safety
- Environment variables for configuration

## Success Criteria
- All API calls are type-safe
- Errors are handled gracefully
- Loading states provide feedback
- Authentication tokens are managed securely
