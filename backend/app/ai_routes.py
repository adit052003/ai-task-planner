# app/ai_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
import openai
from .config import Config  # Ensure this import is correct
from .models import User, Task, Reminder
from datetime import datetime
from .extensions import db
from dotenv import load_dotenv
import os
import json
from .email_utils import send_reminder_email

# Define the blueprint
ai = Blueprint('ai', __name__)

# Set up OpenAI API key
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def parse_command(text):
    """Parse user command using OpenAI to understand intent and parameters"""
    prompt = f"""
    Parse the following command and categorize it into one of these types:
    1. reminder (e.g., "Remind me about going to the gym")
    2. email_series (e.g., "Send daily emails about CI/CD")
    3. learning_series (e.g., "Help me learn Python")

    Command: {text}
    
    Return JSON format with:
    - type: reminder/email_series/learning_series
    - frequency: daily/weekly
    - time: specific time if mentioned
    - topic: main subject
    - recipients: email addresses if mentioned

    Return only the JSON, without any markdown formatting or backticks.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that parses user commands into structured data. Return only JSON without any markdown formatting."},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Clean up the response - remove markdown formatting if present
    content = response.choices[0].message['content']
    content = content.replace('```json', '').replace('```', '').strip()
    
    return content

@ai.route('/chat', methods=['POST'])
# @jwt_required()  # Comment this out for now
def chat():
    try:
        data = request.get_json() or {}
        user_input = data.get('message', '')
        print(f"Received message: {user_input}")
        
        if not user_input:
            return jsonify({'error': 'Message is required.'}), 400

        parsed_command = parse_command(user_input)
        print(f"Parsed command: {parsed_command}")
        
        # Convert string to dictionary
        command_data = json.loads(parsed_command)
        
        if command_data['type'] == 'reminder':
            # Create a new reminder with default values for empty or null fields
            reminder = Reminder(
                topic=command_data['topic'] if command_data.get('topic') else 'Untitled reminder',
                time=command_data['time'] if command_data.get('time') else '9:00 AM',
                frequency=command_data.get('frequency') if command_data.get('frequency') else 'one-time'
            )
            db.session.add(reminder)
            db.session.commit()
            
            # Send email notification
            send_reminder_email(reminder)
            
            response_message = f"I've set a {reminder.frequency} reminder for {reminder.topic} at {reminder.time}. You'll receive an email notification."
        else:
            response_message = f"I understood your request: {parsed_command}"

        return jsonify({
            'response': response_message,
            'parsed_command': command_data
        })

    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500