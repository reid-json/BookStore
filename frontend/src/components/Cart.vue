<template>
  <div class="cart">
    <h2>Your Cart</h2>
    <div v-if="loading" class="loading">Loading cart...</div>
    <div v-else-if="items.length === 0" class="empty">Your cart is empty.</div>
    <div v-else class="cart-layout">
      <div class="cart-items">
        <div class="cart-grid">
          <div v-for="item in items" :key="item.cart_item_id" class="cart-item">
            <p class="item-title">{{ item.isbn.title }}</p>
            <div class="actions">
              <span class="qty">Qty: {{ item.quantity }}</span>
              <button @click="removeFromCart(item.isbn.isbn)">Remove</button>
            </div>
          </div>
        </div>
      </div>

      <div class="checkout-panel">
        <h3 class="form-title">Enter Payment Information</h3>
        <div class="checkout-form">
          <input v-model="name" placeholder="Name" />
          <input v-model="address" placeholder="Address" />
          <input v-model="card" placeholder="Card Number" />
          <input v-model="cvv" placeholder="CVV" />
        </div>
        <div class="order-btn-wrapper">
          <button class="order-btn" @click="placeOrder">Order</button>
        </div>
      </div>
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
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&display=swap');

.cart {
  padding: 2rem;
  background-color: #121212;
  color: #f0f0f0;
  font-family: 'Quicksand', serif;
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

.cart-layout {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  align-items: flex-start;
}

.cart-items {
  flex: 2;
  min-width: 300px;
}

.cart-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1.5rem;
}

.cart-item {
  background-color: #1e1e1e;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
  text-align: center;
}

.item-title {
  font-size: 1.1rem;
  color: #fff;
  margin-bottom: 0.5rem;
}

.actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.qty {
  font-weight: bold;
  color: #a0e0a0;
}

button {
  padding: 0.4rem 1rem;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: inherit;
}

button:hover {
  background-color: #c82333;
}

/* Checkout Panel */
.checkout-panel {
  flex: 1;
  min-width: 280px;
  background-color: #1e1e1e;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
}

.form-title {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  text-align: center;
  color: #a0e0a0;
}

.checkout-form {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.checkout-form input {
  padding: 0.6rem;
  border: 1px solid #444;
  border-radius: 4px;
  background-color: #121212;
  color: #f0f0f0;
  font-family: inherit;
}

.checkout-form input::placeholder {
  color: #888;
}

.order-btn-wrapper {
  margin-top: 1.5rem;
  text-align: center;
}

.order-btn {
  padding: 0.6rem 1.2rem;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-family: inherit;
}

.order-btn:hover {
  background-color: #218838;
}
</style>