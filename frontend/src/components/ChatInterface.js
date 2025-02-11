import React, { useState } from 'react';
import { Box, TextField, Button, Paper, Typography, CircularProgress } from '@mui/material';
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function ChatInterface() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    try {
      setLoading(true);
      const userMessage = input;
      setInput('');
      
      // Add user message immediately
      setMessages(prev => [...prev, { type: 'user', content: userMessage }]);

      const response = await axios.post(`${API_URL}/api/chat`, {
        message: userMessage
      });

      // Add AI response
      setMessages(prev => [...prev, { 
        type: 'bot', 
        content: response.data.response,
        parsedCommand: response.data.parsed_command 
      }]);

    } catch (error) {
      console.error('Error sending message:', error);
      setMessages(prev => [...prev, { 
        type: 'error', 
        content: 'Sorry, there was an error processing your request.' 
      }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ maxWidth: 600, margin: '0 auto', p: 2 }}>
      <Paper sx={{ height: 400, overflow: 'auto', p: 2, mb: 2 }}>
        {messages.map((message, index) => (
          <Box key={index} sx={{ mb: 1 }}>
            <Typography
              sx={{
                backgroundColor: message.type === 'user' ? '#e3f2fd' : 
                               message.type === 'error' ? '#ffebee' : '#f5f5f5',
                p: 1,
                borderRadius: 1
              }}
            >
              {message.content}
            </Typography>
          </Box>
        ))}
      </Paper>
      <form onSubmit={sendMessage}>
        <Box sx={{ display: 'flex', gap: 1 }}>
          <TextField
            fullWidth
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message... (e.g., 'Remind me about gym at 7:30 AM')"
            variant="outlined"
            disabled={loading}
          />
          <Button 
            type="submit" 
            variant="contained" 
            disabled={loading}
          >
            {loading ? <CircularProgress size={24} /> : 'Send'}
          </Button>
        </Box>
      </form>
    </Box>
  );
}

export default ChatInterface; 