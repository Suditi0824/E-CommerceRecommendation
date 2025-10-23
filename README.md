
# 🛍️ E-commerce Product Recommender System

An intelligent product recommendation system that combines collaborative filtering and content-based algorithms with AI-powered explanations. Built with Flask, SQLite, and smart recommendation logic.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)


## ✨ Features

- **🤖 Hybrid Recommendation Engine**
  - Collaborative filtering based on user similarity
  - Content-based filtering using categories and tags
  - Weighted scoring system for optimal results

- **💬 Smart Explanations**
  - AI-powered personalized explanations for each recommendation
  - Context-aware messaging based on user behavior
  - Fallback system for reliable explanations

- **📊 Real-time User Tracking**
  - Records views, clicks, and purchases
  - Persistent storage in SQLite database
  - User history and activity timeline

- **🎨 Interactive Dashboard**
  - Beautiful, modern UI with gradient design
  - Responsive grid layout
  - Real-time recommendation updates
  - User activity history display
    <img width="1375" height="1080" alt="image" src="https://github.com/user-attachments/assets/159669cd-fe7f-443b-8151-f543e3d3f960" />
    
    <img width="1101" height="645" alt="image1" src="https://github.com/user-attachments/assets/2c76b77e-8a6c-4d28-ba47-aa946931a126" />



### How It Works:
1. User browses products on the dashboard
2. Clicks on products they're interested in
3. System tracks interactions and analyzes behavior
4. AI generates personalized recommendations with explanations
5. User sees tailored product suggestions


## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Edge, Safari)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ecommerce-recommender.git
   cd ecommerce-recommender
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables (Optional)**
   ```bash
   # Create .env file
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```
   *Note: The system works without API key using smart fallback explanations*

4. **Run the backend server**
   ```bash
   python app.py
   ```
   
   You should see:
   ```
   ✅ Database initialized with sample products!
   🚀 Starting Flask server...
   📡 API Endpoints: ...
   * Running on http://127.0.0.1:5000
   ```

5. **Open the frontend**
   - **Option A:** Double-click `index.html` in your file explorer
   - **Option B:** Serve with Python (recommended):
     ```bash
     # Open new terminal
     python -m http.server 8000
     # Then open http://localhost:8000 in browser
     ```


## 🛠️ Technologies Used

### Backend
- **Flask 3.0.0** - Web framework
- **Python 3.8+** - Programming language

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (Gradient backgrounds, animations)
- **JavaScript** - Interactivity (Fetch API, DOM manipulation)

### Optional
- **Google Gemini AI** - Advanced explanations (fallback included)
- **python-dotenv** - Environment management


## 👤 Author

**Your Name**
- GitHub: [Suditi0824](https://github.com/Suditi0824)
- Email: suditi0824@gmail.com

```

---


