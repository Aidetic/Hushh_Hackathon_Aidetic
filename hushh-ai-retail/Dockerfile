# FROM node:18-alpine
FROM node:20.19.0

WORKDIR /app

# Copy package.json and package-lock.json files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port 5173 for Vite
EXPOSE 5173

# Command to run the app
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]