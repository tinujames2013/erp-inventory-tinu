<template>
  <div>
    <h2>Place Order</h2>
    <form @submit.prevent="placeOrder">
      <label>
        Product ID:
        <input type="number" v-model="productId" required />
      </label>
      <label>
        Quantity:
        <input type="number" v-model="quantity" required />
      </label>
      <button type="submit">✅ Place Order</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { api } from '../api'

const productId = ref(1)
const quantity = ref(1)

async function placeOrder() {
  try {
    const res = await api.post('orders/', {
      items: [{ product: productId.value, quantity: quantity.value }]
    })
    alert('✅ Order placed successfully!')
    productId.value = 1
    quantity.value = 1
  } catch (err) {
    alert('❌ Failed to place order: ' + err.response?.data?.items?.[0]?.product || err.message)
  }
}
</script>
