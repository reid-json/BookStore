<template>
  <div class="orders">
    <h2>Your Orders</h2>
    <div v-if="loading" class="loading">Loading orders...</div>
    <div v-else-if="orders.length === 0" class="empty">You have no finalized orders yet.</div>
    <div v-else>
      <div v-for="order in orders" :key="order.order_id" class="order-group">
        <h3>Order ID: {{ order.order_id }}</h3>
        <ul>
          <li v-for="item in order.items" :key="item.id">
            {{ item.isbn.title }} — Quantity: {{ item.quantity }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Orders',
  data() {
    return {
      orders: [],
      loading: true
    };
  },
  mounted() {
    this.fetchOrders();
  },
  methods: {
    async fetchOrders() {
      const token = localStorage.getItem('authToken');
      const res = await fetch('http://localhost:8000/api/order/list/', {
        headers: { 'Authorization': `Bearer ${token}` }
      });

      const data = await res.json();
      this.orders = data;
      this.loading = false;
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

.orders {
  padding: 2rem;
  background-color: #121212;
  color: #f0f0f0;
  font-family: 'Libre Baskerville', serif;
  min-height: 100vh;
}

h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #ffffff;
}

.loading,
.empty {
  text-align: center;
  font-size: 1.2rem;
  color: #aaa;
}

.order-group {
  margin-bottom: 2rem;
  padding: 1rem;
  background-color: #1e1e1e;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
}

h3 {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
  color: #a0e0a0;
}

ul {
  list-style: none;
  padding-left: 0;
}

li {
  margin-bottom: 0.3rem;
  font-size: 0.95rem;
  color: #ccc;
}
</style>