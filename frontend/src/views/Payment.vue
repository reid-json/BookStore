<template>
  <div class="payment">
    <h2>Payment</h2>
    <p class="total">Order Total: ${{ amount }}</p>

    <div class="payment-panel">
      <div class="payment-form">
        <select v-model="method">
          <option disabled value="">Select Payment Method</option>
          <option value="credit_card">Credit Card</option>
          <option value="debit_card">Debit Card</option>
          <option value="paypal">PayPal</option>
        </select>

        <input v-model="card" placeholder="Card Number" />
        <button @click="submitPayment">Pay Now</button>
      </div>

      <div v-if="success" class="success">{{ success }}</div>
      <div v-if="error" class="error">{{ error }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Payment',
  data() {
    return {
      method: '',
      card: '',
      error: '',
      success: '',
      order_id: this.$route.query.order_id,
      amount: this.$route.query.amount
    };
  },
  methods: {
    async submitPayment() {
      this.error = '';
      this.success = '';
      const token = localStorage.getItem('authToken');

      try {
        const res = await fetch('http://localhost:8000/api/payment/process/', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            order: this.order_id,
            amount: this.amount,
            method: this.method,
            card: this.card
          })
        });

        const data = await res.json();

        if (res.ok) {
          this.success = "Payment successful! Redirecting to your orders...";
          setTimeout(() => {
            this.$router.push({ name: 'Orders' });
          }, 1500);
        } else {
          this.error = data.error || 'Payment failed';
        }
      } catch (err) {
        this.error = 'Network error. Please try again.';
        console.error(err);
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

.payment {
  padding: 2rem;
  background-color: #121212;
  color: #f0f0f0;
  font-family: 'Libre Baskerville', serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #ffffff;
  text-align: center;
}

.total {
  font-size: 1.2rem;
  color: #a0e0a0;
  margin-bottom: 2rem;
  text-align: center;
}

.payment-panel {
  background-color: #1e1e1e;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.payment-form {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  width: 100%;
}

.payment-form select,
.payment-form input {
  padding: 0.6rem;
  border: 1px solid #444;
  border-radius: 6px;
  background-color: #121212;
  color: #f0f0f0;
  font-family: inherit;
}

.payment-form input::placeholder {
  color: #888;
}

button {
  padding: 0.6rem 1.2rem;
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-family: inherit;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #218838;
}

.success {
  margin-top: 1rem;
  color: #a0e0a0;
  text-align: center;
}

.error {
  margin-top: 1rem;
  color: #ff6b6b;
  text-align: center;
}
</style>