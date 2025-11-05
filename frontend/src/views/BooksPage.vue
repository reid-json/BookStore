<template>
  <div class="book-list">
    <h1>Book Catalog</h1>
    <div v-if="loading">Loading books...</div>
    <div v-else>
      <div v-for="book in books" :key="book.isbn" class="book-card">
        <img :src="book.coverImage" alt="Cover" class="cover" />
        <div class="info">
          <h2>{{ book.title }}</h2>
          <p><strong>Author:</strong> {{ book.author || 'Unknown' }}</p>
          <p><strong>Genre:</strong> {{ book.genre }}</p>
          <p><strong>Price:</strong> ${{ book.price }}</p>
          <p><strong>Stock:</strong> {{ book.stock }}</p>
          <p><strong>Published:</strong> {{ book.published_date }}</p>
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
};
</script>

<style scoped>
.book-list {
  padding: 2rem;
  font-family: Arial, sans-serif;
}

.book-card {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  border-bottom: 1px solid #ccc;
  padding-bottom: 1rem;
}

.cover {
  width: 120px;
  height: auto;
  object-fit: cover;
  border: 1px solid #ddd;
}

.info h2 {
  margin: 0;
  font-size: 1.5rem;
}

.info p {
  margin: 0.3rem 0;
}
</style>