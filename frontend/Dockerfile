FROM node:16

WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm install

# Copy the rest of the application
COPY . .

# Build the app
RUN npm run build

# Install serve to run the application
RUN npm install -g serve

EXPOSE 3000

# Serve the built application
CMD ["serve", "-s", "build", "-l", "3000"] 