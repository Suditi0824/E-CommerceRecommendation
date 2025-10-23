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

- **🔌 RESTful API**
  - Clean, well-documented endpoints
  - JSON responses
  - CORS enabled for cross-origin requests

## 🎬 Demo

### How It Works:
1. User browses products on the dashboard
2. Clicks on products they're interested in
3. System tracks interactions and analyzes behavior
4. AI generates personalized recommendations with explanations
5. User sees tailored product suggestions
<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/your_video_id"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen
></iframe>

### Sample Recommendation:
> **Fitness Tracker Watch** - $149.99
> 
> *"Perfect match! You've been interested in Electronics products, especially fitness items. This Fitness Tracker Watch fits your preferences perfectly."*


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
   
     ```
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
- GitHub: [@Suditi0824](https://github.com/Suditi0824)

---

**Built with ❤️ for E-commerce Innovation**

*Last Updated: October 15, 2025*
