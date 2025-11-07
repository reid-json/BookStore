<template>
  <div class="book-list">
    <h1>Book Catalog</h1>
    <div v-if="loading" class="loading">Loading books...</div>
    <div v-else class="book-grid">
      <div v-for="book in books" :key="book.isbn" class="book-card">
        <img :src="book.coverImage" alt="Cover" class="cover" />
        <div class="info">
          <h2>{{ book.title }}</h2>
          <p class="meta"><span>Author:</span> {{ book.author || 'Unknown' }}</p>
          <p class="meta"><span>Genre:</span> {{ book.genre }}</p>
          <p class="meta"><span>Price:</span> ${{ book.price }}</p>
          <p class="meta"><span>Stock:</span> {{ book.stock }}</p>
          <p class="meta"><span>Published:</span> {{ book.published_date }}</p>
          <button
              :class="{ added: addedToCart.includes(book.isbn) }"
              :disabled="book.stock === 0 || addedToCart.includes(book.isbn)"
              @click="addToCart(book)"
          >
            {{ book.stock === 0 ? 'Out of Stock' : addedToCart.includes(book.isbn) ? 'Added!' : 'Add to Cart' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Books',
  data() {
    return {
      books: [],
      loading: true,
      addedToCart: []
    };
  },
  mounted() {
    fetch('http://localhost:8000/api/books/')
        .then(res => res.json())
        .then(data => {
          this.books = data;
          this.loading = false;
        })
        .catch(err => {
          console.error('Error fetching books:', err);
          this.loading = false;
        });
  },
  methods: {
    async addToCart(book) {
      if (book.stock === 0 || this.addedToCart.includes(book.isbn)) return;

      this.addedToCart.push(book.isbn);

      const token = localStorage.getItem('authToken');
      try {
        const res = await fetch('http://localhost:8000/api/cartitem/cart/add/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          },
          body: JSON.stringify({ isbn: book.isbn, quantity: 1 })
        });

        const data = await res.json();
        if (!res.ok) throw new Error(data.error || 'Failed to add to cart');

        book.stock -= 1; // ✅ Update stock visually
      } catch (err) {
        console.error('Error adding to cart:', err);
      }

      setTimeout(() => {
        this.addedToCart = this.addedToCart.filter(id => id !== book.isbn);
      }, 1000);
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

.book-list {
  padding: 2rem;
  background-color: #424242;
  color: #f0f0f0;
  min-height: 100vh;
  font-family: 'Quicksand', serif;
}

h1 {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 2.2rem;
  color: #ffffff;
}

.loading {
  text-align: center;
  font-size: 1.2rem;
  color: #aaa;
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 2rem;
}

.book-card {
  background-color: #1e1e1e;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
  padding: 1rem;
  transition: transform 0.2s ease;
  text-align: center;
}

.book-card:hover {
  transform: scale(1.03);
}

.cover {
  width: 100%;
  height: 280px;
  object-fit: contain;
  background-color: #000;
  margin-bottom: 1rem;
}

.info h2 {
  margin: 0 0 0.5rem;
  font-size: 1.3rem;
  color: #fff;
}

.meta {
  margin: 0.4rem 0;
  font-size: 0.95rem;
  color: #d0d0d0;
}

.meta span {
  color: #a0e0a0;
  font-weight: bold;
}

button {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-family: inherit;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #388e3c;
}

button.added {
  background-color: #81c784;
  cursor: default;
}

button:disabled {
  background-color: #555;
  cursor: not-allowed;
}
</style>