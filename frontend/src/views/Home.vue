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
        <h2>Staff Picks</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, urna eu tincidunt consectetur, nisi nisl aliquet nunc, vitae tincidunt justo nulla nec eros.
        </p>
      </div>
      <div class="grid-block">
        <h2>New Arrivals</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.
        </p>
      </div>
    </section>

    <section class="about">
      <h2>About Us</h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
      </p>
    </section>

    <section class="extras">
      <div class="extra-block">
        <h2>Upcoming Events</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Join us for author talks, book signings, and community reads happening every month.
        </p>
      </div>
      <div class="extra-block">
        <h2>Reader Reviews</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Hear what fellow readers are saying about their latest finds and share your own thoughts.
        </p>
      </div>
    </section>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

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