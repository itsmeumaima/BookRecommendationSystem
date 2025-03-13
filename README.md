# 📚 Books Recommendation System   

A **Machine Learning-based** book recommendation system built with **Streamlit**, which suggests books based on similarity scores and allows users to explore the **Top 50 Popular Books** ranked by ratings.  

---

## 🚀 Features  
✅ **Top 50 Popular Books** – Displayed with title, author, image, and ratings.  
✅ **Personalized Book Recommendation** – Select a book to get 5 similar recommendations.  
✅ **User-Friendly Interface** – Simple and interactive UI built with Streamlit.  
✅ **Fast Performance** – Precomputed similarity scores for quick recommendations.  

---

## 🛠 Tech Stack  
- **Python**  
- **Streamlit** (for UI)  
- **Pandas** (for data manipulation)  
- **Pickle** (for loading pre-trained recommendation models)  
- **Machine Learning** (for similarity-based recommendations)  

---

## 📂 Dataset Used  
This project uses a dataset containing book metadata, ratings, and similarity scores:  
- `popular.pkl` → Contains the top books sorted by popularity.  
- `books.pkl` → Contains book metadata like title, author, and image URL.  
- `similarity_scores.pkl` → Precomputed similarity matrix for recommendations.  

---

## 🔧 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/itsmeumaima/BookRecommendationSystem.git
cd BookRecommendationSystem
