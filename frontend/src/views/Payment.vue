<template>
  <div class="payment">
    <h2>Payment</h2>
    <p>Order Total: ${{ amount }}</p>

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
            this.$router.push({ name: 'Orders' }); // ✅ Make sure 'Orders' route is defined
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
.payment {
  padding: 2rem;
  font-family: Arial, sans-serif;
}

.payment-form {
  margin-top: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.payment-form input,
.payment-form select {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  margin-top: 1rem;
  padding: 0.6rem 1.2rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}

.error {
  margin-top: 1rem;
  color: red;
}

.success {
  margin-top: 1rem;
  color: green;
}
</style>