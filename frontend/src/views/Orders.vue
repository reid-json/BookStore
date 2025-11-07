<template>
  <div class="orders">
    <h2>Your Orders</h2>
    <div v-if="loading">Loading orders...</div>
    <div v-else-if="orders.length === 0">You have no finalized orders yet.</div>
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
.orders {
  padding: 2rem;
  font-family: Arial, sans-serif;
}

.order-group {
  margin-bottom: 2rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 6px;
}

h3 {
  margin-bottom: 0.5rem;
}

ul {
  list-style: none;
  padding-left: 0;
}

li {
  margin-bottom: 0.3rem;
}
</style>