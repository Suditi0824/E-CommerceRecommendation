
# 🛍️ E-commerce Product Recommender System

An intelligent product recommendation system that combines collaborative filtering and content-based algorithms with AI-powered explanations. Built with Flask, SQLite, and smart recommendation logic.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)

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



- **🔌 RESTful API**
  - Clean, well-documented endpoints
  - JSON responses
  - CORS enabled for cross-origin requests

## 🎬 Demo
[Watch demo video](https://drive.google.com/file/d/18vEnaCMx1ZuUVT_itLzkbA2Rg500eN4D/view?usp=sharing)


### How It Works:
1. User browses products on the dashboard
2. Clicks on products they're interested in
3. System tracks interactions and analyzes behavior
4. AI generates personalized recommendations with explanations
5. User sees tailored product suggestions


### Sample Recommendation:
> **Fitness Tracker Watch** - $149.99
> 
> *"Perfect match! You've been interested in Electronics products, especially fitness items. This Fitness Tracker Watch fits your preferences perfectly."*

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Frontend (HTML/JS)                  │
│  • Product Grid                                      │
│  • Recommendation Display                            │
│  • User Input & History                              │
└───────────────────┬─────────────────────────────────┘
                    │ REST API (AJAX)
                    │
┌───────────────────▼─────────────────────────────────┐
│              Flask Backend Server                    │
│  ┌─────────────────────────────────────────────┐   │
│  │  API Routes                                  │   │
│  │  • /api/products                             │   │
│  │  • /api/interact                             │   │
│  │  • /api/recommendations/<user_id>            │   │
│  │  • /api/user-history/<user_id>               │   │
│  └─────────────────────────────────────────────┘   │
│                                                      │
│  ┌─────────────────────────────────────────────┐   │
│  │  Recommendation Engine                       │   │
│  │  • Collaborative Filtering                   │   │
│  │  • Content-Based Filtering                   │   │
│  │  • Hybrid Scoring Algorithm                  │   │
│  └─────────────────────────────────────────────┘   │
│                                                      │
│  ┌─────────────────────────────────────────────┐   │
│  │  AI Explanation Generator                    │   │
│  │  • Behavior Analysis                         │   │
│  │  • Pattern Matching                          │   │
│  │  • Personalized Text Generation              │   │
│  └─────────────────────────────────────────────┘   │
└───────────────────┬─────────────────────────────────┘
                    │
┌───────────────────▼─────────────────────────────────┐
│              SQLite Database                         │
│  ┌──────────────────┐  ┌────────────────────────┐  │
│  │  Products Table  │  │  Interactions Table    │  │
│  │  • id            │  │  • id                  │  │
│  │  • name          │  │  • user_id             │  │
│  │  • category      │  │  • product_id          │  │
│  │  • price         │  │  • interaction_type    │  │
│  │  • description   │  │  • timestamp           │  │
│  │  • tags          │  └────────────────────────┘  │
│  └──────────────────┘                               │
└─────────────────────────────────────────────────────┘
```

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

## 📖 Usage

### For End Users

1. **Browse Products**
   - Scroll through the product catalog
   - View product details, prices, and descriptions

2. **Interact with Products**
   - Click on products you're interested in
   - System records your preferences

3. **Get Recommendations**
   - Click "Get Recommendations" button
   - View personalized product suggestions
   - Read AI-generated explanations

4. **Track Your Activity**
   - View your interaction history at the bottom
   - See patterns in your browsing behavior

### For Developers

#### Starting Development Server
```bash
# Terminal 1: Backend
python app.py

# Terminal 2: Frontend (optional)
python -m http.server 8000
```

#### Running Tests
```bash
# Test API endpoints
curl http://localhost:5000/api/products
curl http://localhost:5000/api/recommendations/user123

# Test interaction recording
curl -X POST http://localhost:5000/api/interact \
  -H "Content-Type: application/json" \
  -d '{"user_id":"test_user","product_id":1,"type":"click"}'
```

## 📡 API Documentation

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Get All Products
```http
GET /api/products
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Wireless Bluetooth Headphones",
    "category": "Electronics",
    "price": 79.99,
    "description": "Premium noise-cancelling headphones...",
    "tags": "audio,wireless,music"
  }
]
```

#### 2. Record User Interaction
```http
POST /api/interact
Content-Type: application/json

{
  "user_id": "user123",
  "product_id": 1,
  "type": "click"
}
```

**Parameters:**
- `user_id` (string): Unique user identifier
- `product_id` (integer): Product ID
- `type` (string): Interaction type - "view", "click", or "purchase"

**Response:**
```json
{
  "status": "success"
}
```

#### 3. Get Personalized Recommendations
```http
GET /api/recommendations/<user_id>
```

**Response:**
```json
[
  {
    "id": 7,
    "name": "Fitness Tracker Watch",
    "category": "Electronics",
    "price": 149.99,
    "description": "Smart fitness tracker...",
    "tags": "fitness,smartwatch,health",
    "explanation": "Based on your interest in fitness items...",
    "score": 4.5
  }
]
```

#### 4. Get User History
```http
GET /api/user-history/<user_id>
```

**Response:**
```json
[
  {
    "product": "Yoga Mat Premium",
    "category": "Sports",
    "type": "click",
    "timestamp": "2025-10-15T01:00:00"
  }
]
```

## 🧠 How It Works

### Recommendation Algorithm

#### 1. **Collaborative Filtering**
```python
# Finds users with similar behavior
- User A clicked: [1, 2, 3]
- User B clicked: [2, 3, 4]
- Similarity score: 2 (products in common)
- Recommends product 4 to User A
```

#### 2. **Content-Based Filtering**
```python
# Analyzes product attributes
- User likes: Electronics (3x), Sports (2x)
- User tags: fitness (4x), wireless (2x)
- Scores products matching these patterns
```

#### 3. **Hybrid Scoring**
```python
final_score = (collaborative_score * 1.5) + content_score
# Collaborative weighted higher for better accuracy
```

#### 4. **Smart Explanations**
```python
# Analyzes user behavior patterns
- Identifies most viewed category
- Finds matching product tags
- Generates personalized explanation
- Falls back to generic if needed
```

### Sample Flow
```
User clicks "Yoga Mat" (Sports, fitness)
    ↓
System records interaction
    ↓
Algorithm analyzes:
  - Category: Sports ✓
  - Tags: fitness, yoga, wellness ✓
    ↓
Finds similar products:
  - Running Shoes (Sports, fitness) → Score: 3.5
  - Water Bottle (Sports, fitness) → Score: 3.0
  - Protein Powder (Food, fitness) → Score: 2.5
    ↓
Generates explanations:
  "Since you've been browsing Sports products,
   especially fitness items..."
    ↓
Returns top 3 recommendations
```

## 📁 Project Structure

```
ecommerce-recommender/
│
├── app.py                  # Flask backend server
├── index.html              # Frontend dashboard
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (optional)
├── README.md              # This file
│
├── ecommerce.db           # SQLite database (auto-generated)
│
└── screenshots/           # Demo screenshots (optional)
    ├── dashboard.png
    ├── recommendations.png
    └── history.png
```

## 🛠️ Technologies Used

### Backend
- **Flask 3.0.0** - Web framework
- **Flask-CORS 4.0.0** - Cross-origin resource sharing
- **SQLite3** - Database (built-in Python)
- **Python 3.8+** - Programming language

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling (Gradient backgrounds, animations)
- **Vanilla JavaScript** - Interactivity (Fetch API, DOM manipulation)

### Algorithms
- **Collaborative Filtering** - User-based similarity
- **Content-Based Filtering** - Feature matching
- **Hybrid Recommendation** - Combined approach

### Optional
- **Google Gemini AI** - Advanced explanations (fallback included)
- **python-dotenv** - Environment management

## 🎯 Future Improvements

### Short-term
- [ ] Add user authentication system
- [ ] Implement purchase tracking
- [ ] Add product search functionality
- [ ] Create admin dashboard for product management
- [ ] Add rating and review system

### Long-term
- [ ] Deploy to cloud (Heroku/AWS)
- [ ] Implement A/B testing for algorithms
- [ ] Add real-time notifications
- [ ] Mobile app version
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Integration with payment systems

### Algorithm Enhancements
- [ ] Deep learning recommendation model
- [ ] Session-based recommendations
- [ ] Time-decay for old interactions
- [ ] Seasonal product boosting
- [ ] Price sensitivity analysis

## 🧪 Testing

### Manual Testing Checklist
- [ ] Products load on page open
- [ ] Clicking product shows alert
- [ ] Recommendations appear after clicks
- [ ] Explanations are personalized
- [ ] History updates correctly
- [ ] Different users get different recommendations
- [ ] API endpoints return correct JSON
- [ ] Database persists after restart

### Test Scenarios

**Scenario 1: Electronics Enthusiast**
```bash
Click: Headphones → Keyboard → Laptop Stand
Expected: Recommends Fitness Tracker (electronics)
Result: ✅ Pass
```

**Scenario 2: Fitness Fanatic**
```bash
Click: Yoga Mat → Running Shoes → Water Bottle
Expected: Recommends Protein Powder, Fitness Tracker
Result: ✅ Pass
```

**Scenario 3: Multi-User**
```bash
User A clicks: Electronics items
User B clicks: Sports items
Expected: Different recommendations for each
Result: ✅ Pass
```

## 👤 Author

**Your Name**
- GitHub: [Suditi0824](https://github.com/Suditi0824)
- Email: suditi0824@gmail.com

## 🙏 Acknowledgments

- Inspired by recommendation systems from Amazon, Netflix, and Spotify
- Flask documentation and community
- SQLite for reliable embedded database
- Modern CSS gradient designs from UI/UX trends


---

## 🎉 Quick Start Summary

```bash
# 1. Install
pip install -r requirements.txt

# 2. Run Backend
python app.py

# 3. Open Frontend
# Double-click index.html OR
python -m http.server 8000

# 4. Test
# Open http://localhost:8000
# Click products and see recommendations!
```

---


*Last Updated: October 15, 2025*

