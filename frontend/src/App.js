import React from 'react';
import { Container, CssBaseline } from '@mui/material';
import ChatInterface from './components/ChatInterface';

function App() {
  return (
    <>
      <CssBaseline />
      <Container>
        <ChatInterface />
      </Container>
    </>
  );
}

export default App; 