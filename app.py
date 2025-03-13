import streamlit as st
import pickle
import pandas as pd

st.header("📚 Books Recommendation System")

# Load the data
popular_books = pickle.load(open('popular.pkl', 'rb'))
similarity = pickle.load(open('similarity_scores.pkl', 'rb'))
books_df = pickle.load(open('books.pkl', 'rb'))

# Sort books by the number of ratings in descending order
popular_books = popular_books.sort_values(by='num_ratings', ascending=False)

# Sidebar navigation
menu = st.sidebar.radio("📌 Menu", ["🏠 Home", "🔍 Recommend", "ℹ About"])

# Home: Display top 50 popular books
if menu == "🏠 Home":
    st.subheader("📖 Top 50 Popular Books")

    # Select the top 50 books
    top_books = popular_books.head(50)

    # Create a grid layout
    for i in range(0, len(top_books), 3):
        cols = st.columns(3)  # Display 3 books per row
        for j in range(3):
            if i + j < len(top_books):
                book = top_books.iloc[i + j]  # Access DataFrame row properly
                with cols[j]:
                    st.image(book['Image-URL-M'], width=150)
                    st.write(f"**{book['Book-Title']}**")
                    st.write(f"✍️ Author: {book['Book-Author']}")
                    st.write(f"⭐ Ratings: {book['num_ratings']}")

# Recommend: Book Recommendation Feature
if menu == "🔍 Recommend":
    st.subheader("🔎 Get Book Recommendations")

    # Dropdown for book selection
    books_list = books_df['Book-Title'].unique()
    selected_book = st.selectbox("📌 Type or select a book:", books_list)

    if st.button("Get Recommendations"):
        # Function to get recommended books
        def recommend_books(book_name):
            # Ensure the book exists
            book_name = book_name.strip()
            if book_name not in books_df['Book-Title'].values:
                return []

            book_index = books_df[books_df['Book-Title'] == book_name].index[0]
            similar_books = sorted(
                list(enumerate(similarity[book_index])), key=lambda x: x[1], reverse=True
            )[1:6]  # Get top 5 similar books

            recommended_books = []
            for i in similar_books:
                book_data = books_df.iloc[i[0]]
                recommended_books.append({
                    "Title": book_data["Book-Title"],
                    "Author": book_data["Book-Author"],
                    "Image": book_data["Image-URL-M"]
                })

            return recommended_books

        recommendations = recommend_books(selected_book)

        if recommendations:
            st.subheader("📚 Recommended Books:")
            cols = st.columns(5)  # Display 5 books per row
            for idx, book in enumerate(recommendations):
                with cols[idx]:
                    st.image(book['Image'], width=120)
                    st.write(f"**{book['Title']}**")
                    st.write(f"✍️ {book['Author']}")
        else:
            # st.error("⚠️ No recommendations found. Try another book.")
            st.title("NO book found")

# About Page
if menu == "ℹ About":
    st.subheader("ℹ About This App")
    st.write("""
    - This **Books Recommendation System** suggests books based on similarity scores.
    - You can explore the **top 50 books** and find recommendations by selecting a book.
    - Developed using **Streamlit & Machine Learning**.
    """)
