<template>
  <div class="confirmation">
    <h2>Payment Successful!</h2>
    <p>Your order has been finalized and is now complete.</p>
    <p>Thank you for shopping with us!</p>

    <router-link to="/orders">
      <button class="view-orders-btn">View My Orders</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Confirmation',
  mounted() {
    const paymentId = this.$route.query.payment_id;
    if (!paymentId) {
      this.$router.push('/cart'); // fallback if accessed directly
    }
  }
};
</script>

<style scoped>
.confirmation {
  padding: 2rem;
  font-family: Arial, sans-serif;
  text-align: center;
}

.view-orders-btn {
  margin-top: 1.5rem;
  padding: 0.6rem 1.2rem;
  background-color: #17a2b8;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.view-orders-btn:hover {
  background-color: #138496;
}
</style>