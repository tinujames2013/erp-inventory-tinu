<template>
  <div>
    <h2>📜 Order History</h2>
    <ul>
      <li v-for="order in orders" :key="order.id">
        <strong>Order #{{ order.id }}</strong> – {{ order.date }}
        <ul>
          <li v-for="item in order.items" :key="item.id">
            Product ID: {{ item.product }} – Qty: {{ item.quantity }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { api } from '../api'

const orders = ref([])

onMounted(async () => {
  const res = await api.get('orders/')
  orders.value = res.data
})
</script>
