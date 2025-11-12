<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goToCatalog() {
  router.push('/books')
}
</script>

<template>
  <div class="home">
    <section class="hero">
      <h1>Welcome to Shlves</h1>
      <p class="tagline">
        A corner of the digital world that invites you into another.
      </p>
      <button class="catalog-btn" @click="goToCatalog">Browse Catalog</button>
    </section>

    <section class="highlight">
      <div class="text">
        <h2>Featured: The Divine Comedy</h2>
        <p>~ "Turn and listen, for not only in my eyes is Paradise."</p>
      </div>
      <div class="visual">
        <img src="/divinecomedy.jpg" alt="Divine Comedy" class="hero-image" />
      </div>
    </section>

    <section class="grid-section">
      <div class="grid-block">
        <h2>Shlves Best Sellers</h2>
        <ul class="book-listing">
          <li><span class="book-title">Berserk Volume 1</span></li>
          <li><span class="book-title">The Mamba Mentality</span></li>
          <li><span class="book-title">Dune</span></li>
        </ul>
        <div class="catalog-button">
          <button @click="$router.push('/books')">View Catalog</button>
        </div>
      </div>

      <div class="grid-block">
        <h2>New Philosophy Arrivals</h2>
        <ul class="book-listing">
          <li><span class="book-title">Brave New World</span></li>
          <li><span class="book-title">Crime and Punishment</span></li>
        </ul>
        <div class="catalog-button">
          <button @click="$router.push('/books')">View Catalog</button>
        </div>
      </div>
    </section>

    <section class="about">
      <h2>About Us</h2>
      <p>
        We are an inspired group of individuals here at Shlves ready to bring our reader into their next journey.
        Check out our full catalog that is always updating!! Happy shopping!
      </p>
    </section>

    <section class="extras">
      <div class="extra-block">
        <h2>Coming Soon to Shlves </h2>
        <ul>
          <li>New Book Titles</li>
          <li>Mobile Support</li>
          <li>Text Updates</li>
        </ul>

      </div>
      <div class="extra-block">
        <h2>Book Quotes</h2>
        <p>
          <em>"Pain and suffering are always inevitable for a large intelligence and a deep heart.
          The really greate men must, I think, have great sadness on earth."</em> ~ Fyodor Dostoevsky
        </p>
        <p>
         <em>"From his slack hand the garland wreathed for Eve down dropped, and all the
          faded roses shed; Speechless he stood and pale, till thus at length. First to himself
          he inward silence broke."</em> ~ John Milton
        </p>
      </div>
    </section>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

.book-listing {
  list-style: none;
  padding: 0;
  margin: 1rem 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.book-listing li {
  background-color: #2a2a2a;
  padding: 0.6rem 1rem;
  border-radius: 6px;
}

.book-title {
  font-size: 1rem;
  color: #f0f0f0;
}

.catalog-button {
  margin-top: 1.5rem;
  text-align: center;
}

.catalog-button button {
  padding: 0.5rem 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 6px;
  font-family: inherit;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.catalog-button button:hover {
  background-color: #388e3c;
}

.home {
  background-color: #121212;
  color: #f0f0f0;
  font-family: 'Libre Baskerville', serif;
  padding: 2rem;
  min-height: 100vh;
}


.hero {
  text-align: center;
  margin-bottom: 3rem;
}

.hero h1 {
  font-size: 3rem;
  color: #ffffff;
  margin-bottom: 1rem;
}

.tagline {
  font-size: 1.2rem;
  color: #ccc;
  margin-bottom: 1.5rem;
}

.catalog-btn {
  padding: 0.6rem 1.2rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 6px;
  font-family: inherit;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.catalog-btn:hover {
  background-color: #388e3c;
}


.highlight {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  margin-bottom: 3rem;
  align-items: center;
}

.highlight .text {
  flex: 1;
  min-width: 280px;
}

.highlight .visual {
  flex: 1;
  min-width: 280px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-image {
  width: 100%;
  max-width: 300px;
  height: auto;
  object-fit: contain;
  border-radius: 6px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.3);
}


.grid-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.grid-block {
  background-color: #1e1e1e;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
}

.grid-block h2 {
  font-size: 1.4rem;
  margin-bottom: 1rem;
  color: #a0e0a0;
}

.grid-block p {
  font-size: 0.95rem;
  color: #ccc;
  line-height: 1.5;
}


.about {
  background-color: #1e1e1e;
  padding: 2rem;
  border-radius: 8px;
  margin-bottom: 3rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
}

.about h2 {
  font-size: 1.4rem;
  margin-bottom: 1rem;
  color: #a0e0a0;
}

.about p {
  font-size: 1rem;
  color: #ccc;
  line-height: 1.6;
}


.extras {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.extra-block {
  background-color: #1e1e1e;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
}

.extra-block h2 {
  font-size: 1.3rem;
  margin-bottom: 1rem;
  color: #a0e0a0;
}

.extra-block p {
  font-size: 0.95rem;
  color: #ccc;
  line-height: 1.5;
}
</style>