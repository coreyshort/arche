# Component Development Directive

## Goal
Create reusable, maintainable React components following consistent patterns.

## Inputs
- Component requirements and specifications
- Design mockups or wireframes
- Props interface definitions

## Process

### 1. Component Structure
- Use functional components with hooks
- Place in appropriate directory:
  - `src/components/` for reusable components
  - `src/pages/` for page-level components
- Follow naming convention: PascalCase for component names

### 2. Component Template
```typescript
// src/components/MyComponent.tsx
import React from 'react';
import './MyComponent.css';

interface MyComponentProps {
  // Define props with TypeScript
}

export const MyComponent: React.FC<MyComponentProps> = ({ 
  // destructure props
}) => {
  // Hooks at the top
  // Event handlers
  // Render logic
  
  return (
    <div className="my-component">
      {/* JSX content */}
    </div>
  );
};
```

### 3. State Management
- Use `useState` for local component state
- Use `useContext` for shared state
- Consider `useReducer` for complex state logic
- Keep state as close to where it's used as possible

### 4. Side Effects
- Use `useEffect` for API calls, subscriptions, timers
- Always clean up effects (return cleanup function)
- Specify dependencies array correctly

### 5. API Integration
- Place API calls in `src/services/`
- Components call service functions
- Handle loading states, errors, and success cases

### 6. Styling
- Co-locate CSS with components
- Use CSS modules or styled-components for scoping
- Follow mobile-first responsive design

## Outputs
- Functional, typed React component
- Associated styles
- Updated imports in parent components

## Edge Cases
- Handle loading states (skeleton/spinner)
- Handle error states (error boundaries)
- Handle empty states (no data)
- Ensure accessibility (ARIA labels, keyboard navigation)

## Tools/Scripts
- Component generator (if available in `execution/`)
- TypeScript for type safety
- ESLint for code quality

## Success Criteria
- Component renders correctly
- Props are properly typed
- No TypeScript or linting errors
- Responsive on all screen sizes
