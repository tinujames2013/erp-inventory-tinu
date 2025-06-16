<template>
  <div class="container mt-4">
    <div class="row">
      <div
        class="col-md-3 mb-4"
        v-for="product in store.products"
        :key="product.id"
      >
        <div class="card h-100">
          <img
            src="https://via.placeholder.com/250x200.png?text=Product+Image"
            class="card-img-top"
            alt="product.name"
          />
          <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <p class="card-text">Supplier ID: {{ product.supplier }}</p>
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item">Rs. {{ product.price }}</li>
            <li class="list-group-item">
              Stock: {{ getStock(product.id) }} units
            </li>
          </ul>
          <div class="card-body text-center">
            <button class="btn btn-primary" @click="placeOrder(product.id)">
              Place Order
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useProductStore } from '../stores/productStore'
import { api } from '../api'

const store = useProductStore()
const stocks = ref([])

onMounted(async () => {
  await store.fetchProducts()
  const res = await api.get('stocks/')
  stocks.value = res.data
})

const getStock = (productId) => {
  const stock = stocks.value.find((s) => s.product === productId)
  return stock ? stock.quantity : 'N/A'
}

const placeOrder = async (productId) => {
  try {
    await api.post('orders/', {
      items: [{ product: productId, quantity: 1 }],
    })
    alert('✅ Order placed successfully!')
  } catch (err) {
    alert('❌ Failed to place order: ' + err.message)
  }
}
</script>

<style>
.card-img-top {
  object-fit: cover;
  height: 200px;
}
</style>
