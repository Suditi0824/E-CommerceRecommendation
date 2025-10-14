"""
E-commerce Product Recommender with LLM Explanations
Fast implementation with Flask, SQLite, and FREE Gemini API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime
import os
from collections import defaultdict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import Gemini
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Initialize Gemini
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("⚠️  WARNING: GEMINI_API_KEY not found in .env file!")
else:
    genai.configure(api_key=GEMINI_API_KEY)
    print("✅ Gemini API configured successfully!")

# Database setup
def init_db():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    
    # Products table
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  category TEXT,
                  price REAL,
                  description TEXT,
                  tags TEXT)''')
    
    # User interactions table
    c.execute('''CREATE TABLE IF NOT EXISTS interactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id TEXT NOT NULL,
                  product_id INTEGER,
                  interaction_type TEXT,
                  timestamp TEXT,
                  FOREIGN KEY (product_id) REFERENCES products (id))''')
    
    # Check if products exist, if not add sample data
    c.execute('SELECT COUNT(*) FROM products')
    if c.fetchone()[0] == 0:
        sample_products = [
            ('Wireless Bluetooth Headphones', 'Electronics', 79.99, 
             'Premium noise-cancelling headphones with 30hr battery', 'audio,wireless,music'),
            ('Yoga Mat Premium', 'Sports', 34.99, 
             'Eco-friendly non-slip yoga mat with carrying strap', 'fitness,yoga,wellness'),
            ('Coffee Maker Deluxe', 'Kitchen', 129.99, 
             'Programmable coffee maker with thermal carafe', 'coffee,kitchen,appliances'),
            ('Running Shoes Pro', 'Sports', 89.99, 
             'Lightweight running shoes with gel cushioning', 'fitness,running,sports'),
            ('Laptop Stand Aluminum', 'Electronics', 45.99, 
             'Ergonomic adjustable laptop stand for better posture', 'office,ergonomic,accessories'),
            ('Organic Green Tea Set', 'Food', 24.99, 
             'Premium organic green tea collection, 50 bags', 'tea,organic,beverages'),
            ('Fitness Tracker Watch', 'Electronics', 149.99, 
             'Smart fitness tracker with heart rate and sleep monitoring', 'fitness,smartwatch,health'),
            ('Stainless Steel Water Bottle', 'Sports', 19.99, 
             'Insulated water bottle keeps drinks cold for 24hrs', 'hydration,eco-friendly,sports'),
            ('Mechanical Keyboard RGB', 'Electronics', 119.99, 
             'Gaming mechanical keyboard with customizable RGB lighting', 'gaming,keyboard,accessories'),
            ('Protein Powder Vanilla', 'Food', 39.99, 
             'Whey protein powder, 2lbs, vanilla flavor', 'fitness,nutrition,supplements')
        ]
        c.executemany('INSERT INTO products (name, category, price, description, tags) VALUES (?, ?, ?, ?, ?)',
                     sample_products)
    
    conn.commit()
    conn.close()

# Recommendation engine
def calculate_similarity(user_interactions, all_interactions):
    """Simple collaborative filtering based on user behavior"""
    user_products = set([i['product_id'] for i in user_interactions])
    
    # Find similar users
    similar_users = defaultdict(int)
    for interaction in all_interactions:
        if interaction['product_id'] in user_products and interaction['user_id'] != user_interactions[0]['user_id']:
            similar_users[interaction['user_id']] += 1
    
    # Get products from similar users
    recommended_products = defaultdict(int)
    for similar_user_id, similarity_score in similar_users.items():
        user_products_list = [i['product_id'] for i in all_interactions if i['user_id'] == similar_user_id]
        for product_id in user_products_list:
            if product_id not in user_products:
                recommended_products[product_id] += similarity_score
    
    return recommended_products

def get_content_based_recommendations(user_interactions, all_products):
    """Content-based filtering using product categories and tags"""
    user_categories = defaultdict(int)
    user_tags = defaultdict(int)
    
    # Analyze user preferences
    for interaction in user_interactions:
        product = next((p for p in all_products if p['id'] == interaction['product_id']), None)
        if product:
            user_categories[product['category']] += 1
            if product['tags']:
                for tag in product['tags'].split(','):
                    user_tags[tag.strip()] += 1
    
    # Score products
    scores = {}
    interacted_ids = {i['product_id'] for i in user_interactions}
    
    for product in all_products:
        if product['id'] not in interacted_ids:
            score = 0
            score += user_categories.get(product['category'], 0) * 2
            if product['tags']:
                for tag in product['tags'].split(','):
                    score += user_tags.get(tag.strip(), 0)
            scores[product['id']] = score
    
    return scores

def generate_llm_explanation(user_behavior, recommended_product):
    """Generate smart explanation based on user behavior patterns"""
    
    # Analyze user's browsing patterns
    categories_viewed = []
    tags_viewed = []
    
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    
    for item in user_behavior:
        c.execute('SELECT category, tags FROM products WHERE id = ?', (item['product_id'],))
        result = c.fetchone()
        if result:
            categories_viewed.append(result[0])
            if result[1]:
                tags_viewed.extend(result[1].split(','))
    
    conn.close()
    
    # Count frequencies
    category_counts = {}
    for cat in categories_viewed:
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    tag_counts = {}
    for tag in tags_viewed:
        tag = tag.strip()
        tag_counts[tag] = tag_counts.get(tag, 0) + 1
    
    # Get most common patterns
    most_viewed_category = max(category_counts, key=category_counts.get) if category_counts else "products"
    common_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:2]
    
    # Generate personalized explanations
    product_tags = recommended_product.get('tags', '').split(',')
    matching_tags = [tag.strip() for tag in product_tags if tag.strip() in [t[0] for t in common_tags]]
    
    # Create explanation based on matching patterns
    if recommended_product['category'] == most_viewed_category and matching_tags:
        explanation = f"Perfect match! You've been interested in {most_viewed_category} products, especially {matching_tags[0]} items. This {recommended_product['name']} fits your preferences perfectly."
    elif recommended_product['category'] == most_viewed_category:
        explanation = f"Since you've been browsing {most_viewed_category} products, we think you'll love this {recommended_product['name']}. {recommended_product['description']}"
    elif matching_tags:
        explanation = f"Based on your interest in {matching_tags[0]} products, this {recommended_product['name']} is a great match. It combines quality and functionality you're looking for!"
    else:
        explanation = f"Customers with similar interests loved this {recommended_product['name']}. {recommended_product['description']} - it might be just what you're looking for!"
    
    return explanation

# API Routes
@app.route('/api/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    products = [{'id': row[0], 'name': row[1], 'category': row[2], 
                 'price': row[3], 'description': row[4], 'tags': row[5]} 
                for row in c.fetchall()]
    conn.close()
    return jsonify(products)

@app.route('/api/interact', methods=['POST'])
def record_interaction():
    data = request.json
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    interaction_type = data.get('type', 'view')  # view, click, purchase
    
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('INSERT INTO interactions (user_id, product_id, interaction_type, timestamp) VALUES (?, ?, ?, ?)',
              (user_id, product_id, interaction_type, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'})

@app.route('/api/recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    
    # Get user interactions
    c.execute('SELECT product_id, interaction_type, timestamp FROM interactions WHERE user_id = ? ORDER BY timestamp DESC LIMIT 20',
              (user_id,))
    user_interactions = [{'user_id': user_id, 'product_id': row[0], 'type': row[1], 'timestamp': row[2]} 
                         for row in c.fetchall()]
    
    if not user_interactions:
        # New user - return popular products
        c.execute('''SELECT p.*, COUNT(i.id) as interaction_count 
                     FROM products p 
                     LEFT JOIN interactions i ON p.id = i.product_id 
                     GROUP BY p.id 
                     ORDER BY interaction_count DESC 
                     LIMIT 3''')
        products = [{'id': row[0], 'name': row[1], 'category': row[2], 
                     'price': row[3], 'description': row[4], 'tags': row[5],
                     'explanation': 'Popular product among our customers!'} 
                    for row in c.fetchall()]
        conn.close()
        return jsonify(products)
    
    # Get all interactions for collaborative filtering
    c.execute('SELECT user_id, product_id, interaction_type FROM interactions')
    all_interactions = [{'user_id': row[0], 'product_id': row[1], 'type': row[2]} 
                        for row in c.fetchall()]
    
    # Get all products
    c.execute('SELECT * FROM products')
    all_products = [{'id': row[0], 'name': row[1], 'category': row[2], 
                     'price': row[3], 'description': row[4], 'tags': row[5]} 
                    for row in c.fetchall()]
    
    # Combine collaborative and content-based filtering
    collab_scores = calculate_similarity(user_interactions, all_interactions)
    content_scores = get_content_based_recommendations(user_interactions, all_products)
    
    # Merge scores
    final_scores = {}
    for product_id in set(list(collab_scores.keys()) + list(content_scores.keys())):
        final_scores[product_id] = collab_scores.get(product_id, 0) * 1.5 + content_scores.get(product_id, 0)
    
    # Get top 3 recommendations
    top_product_ids = sorted(final_scores.items(), key=lambda x: x[1], reverse=True)[:3]
    
    recommendations = []
    for product_id, score in top_product_ids:
        product = next((p for p in all_products if p['id'] == product_id), None)
        if product:
            # Generate LLM explanation
            explanation = generate_llm_explanation(user_interactions[-5:], product)
            product['explanation'] = explanation
            product['score'] = score
            recommendations.append(product)
    
    conn.close()
    return jsonify(recommendations)

@app.route('/api/user-history/<user_id>', methods=['GET'])
def get_user_history(user_id):
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()
    c.execute('''SELECT p.name, p.category, i.interaction_type, i.timestamp 
                 FROM interactions i 
                 JOIN products p ON i.product_id = p.id 
                 WHERE i.user_id = ? 
                 ORDER BY i.timestamp DESC 
                 LIMIT 10''', (user_id,))
    history = [{'product': row[0], 'category': row[1], 'type': row[2], 'timestamp': row[3]} 
               for row in c.fetchall()]
    conn.close()
    return jsonify(history)

if __name__ == '__main__':
    init_db()
    print("✅ Database initialized with sample products!")
    print("🚀 Starting Flask server...")
    print("\n📡 API Endpoints:")
    print("  GET  /api/products - Get all products")
    print("  POST /api/interact - Record user interaction")
    print("  GET  /api/recommendations/<user_id> - Get personalized recommendations")
    print("  GET  /api/user-history/<user_id> - Get user interaction history")
    print("\n🤖 Using FREE Google Gemini AI for explanations!")
    app.run(debug=True, port=5000)