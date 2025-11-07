<template>
  <div class="cart">
    <h2>Your Cart</h2>
    <div v-if="loading">Loading cart...</div>
    <div v-else-if="items.length === 0">Your cart is empty.</div>
    <div v-else>
      <div v-for="item in items" :key="item.cart_item_id" class="cart-item">
        <p>{{ item.isbn.title }} ({{ item.quantity }})</p>
        <button @click="removeFromCart(item.isbn.isbn)">Remove</button>
      </div>

      <div class="checkout-form">
        <input v-model="name" placeholder="Name" />
        <input v-model="address" placeholder="Address" />
        <input v-model="card" placeholder="Card Number" />
        <input v-model="cvv" placeholder="CVV" />
      </div>

      <button class="order-btn" @click="placeOrder">Order</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cart',
  data() {
    return {
      items: [],
      loading: true,
      name: '',
      address: '',
      card: '',
      cvv: ''
    };
  },
  mounted() {
    this.fetchCart();
  },
  methods: {
    async fetchCart() {
      const token = localStorage.getItem('authToken');
      const res = await fetch('http://localhost:8000/api/cartitem/cart/view/', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      this.items = await res.json();
      this.loading = false;
    },
    async removeFromCart(isbn) {
      const token = localStorage.getItem('authToken');
      await fetch('http://localhost:8000/api/cartitem/cart/remove/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ isbn })
      });
      await this.fetchCart();
    },
    calculateTotal() {
      return this.items.reduce((sum, item) => {
        return sum + item.isbn.price * item.quantity;
      }, 0).toFixed(2);
    },
    async placeOrder() {
      if (!this.name || !this.address || !this.card || !this.cvv) {
        alert("Please fill out all fields before placing your order.");
        return;
      }

      const token = localStorage.getItem('authToken');
      if (!token) {
        alert("You must be logged in to place an order.");
        return;
      }

      try {
        const res = await fetch('http://localhost:8000/api/order/place/', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            name: this.name,
            address: this.address,
            card: this.card,
            cvv: this.cvv
          })
        });

        const data = await res.json();
        if (res.ok) {
          const total = this.calculateTotal();
          this.$router.push({ name: 'Payment', query: { order_id: data.order_id, amount: total } });
        } else {
          alert(data.error || 'Order failed');
        }
      } catch (err) {
        console.error("Order request error:", err);
        alert("Something went wrong while placing your order.");
      }
    }
  }
};
</script>

<style scoped>
.cart {
  padding: 2rem;
  font-family: Arial, sans-serif;
}

.cart-item {
  margin-bottom: 1rem;
  padding: 1rem;
  border-bottom: 1px solid #ccc;
}

.checkout-form {
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.checkout-form input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  margin-top: 0.5rem;
  padding: 0.4rem 1rem;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #c82333;
}

.order-btn {
  margin-top: 1.5rem;
  padding: 0.6rem 1.2rem;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.order-btn:hover {
  background-color: #218838;
}
</style>