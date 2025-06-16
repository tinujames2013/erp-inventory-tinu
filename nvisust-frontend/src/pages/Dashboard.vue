<template>
  <div>
    <h2 class="mb-4">🧾 Product Dashboard</h2>

    <!-- Admin Toggle -->
    <div class="form-check form-switch mb-3">
      <input class="form-check-input" type="checkbox" id="adminSwitch" v-model="isAdmin" />
      <label class="form-check-label" for="adminSwitch">
        Admin Mode: <strong>{{ isAdmin ? 'ON' : 'OFF' }}</strong>
      </label>
    </div>

    <!-- Product Cards -->
    <div class="row">
      <div
        class="col-md-3 mb-4"
        v-for="p in store.products"
        :key="p.id"
      >
        <div class="card h-100">
          <img
            :src="p.image || 'https://via.placeholder.com/250x200.png?text=Product'"
            class="card-img-top"
            alt="Product Image"
            height="200"
          />
          <div class="card-body">
            <h5 class="card-title">{{ p.name }}</h5>
            <p class="card-text">Rs. {{ p.price }}</p>
            <p class="card-text">Stock: {{ getStock(p.id) }}</p>
            <p class="card-text">Supplier: {{ p.supplier }}</p>
            <button v-if="isAdmin" class="btn btn-danger" @click="deleteProduct(p.id)">🗑️ Delete</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Add Product Form -->
    <div v-if="isAdmin" class="card mt-4 p-4">
      <h4>Add New Product</h4>
      <form @submit.prevent="addProduct">
        <input class="form-control my-2" v-model="form.name" placeholder="Product Name" required />
        <input class="form-control my-2" v-model.number="form.price" type="number" placeholder="Price" required />
        <input class="form-control my-2" v-model.number="form.supplier" type="number" placeholder="Supplier ID" required />
        <input class="form-control my-2" v-model="form.image" placeholder="Image URL (optional)" />
        <button class="btn btn-success mt-2">Add Product</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useProductStore } from '../stores/productStore'
import { api } from '../api'

const store = useProductStore()
const stocks = ref([])

const isAdmin = ref(true) // toggle this to test admin features

const form = ref({
  name: '',
  price: '',
  supplier: '',
  image: ''
})

onMounted(async () => {
  await store.fetchProducts()
  const res = await api.get('stocks/')
  stocks.value = res.data
})

const getStock = (productId) => {
  const stock = stocks.value.find(s => s.product === productId)
  return stock ? stock.quantity : 0
}

const addProduct = async () => {
  try {
    await api.post('products/', form.value)
    await store.fetchProducts()
    form.value = { name: '', price: '', supplier: '', image: '' }
    alert('✅ Product added successfully!')
  } catch (error) {
    alert('❌ Failed to add product: ' + error.message)
  }
}

const deleteProduct = async (id) => {
  if (confirm('Delete this product?')) {
    await api.delete(`products/${id}/`)
    await store.fetchProducts()
  }
}
</script>
