<template>
  <div>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary px-3">
      <a class="navbar-brand" href="#">ERP Inventory</a>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item"><router-link class="nav-link" to="/">Products</router-link></li>
          <li class="nav-item"><router-link class="nav-link" to="/order">Place Order</router-link></li>
          <li class="nav-item"><router-link class="nav-link" to="/history">Order History</router-link></li>
        </ul>
      </div>
    </nav>

    <div class="container my-4">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h2>🧾 Product Dashboard</h2>

        <!-- Admin Mode Toggle -->
        <div class="form-check form-switch">
          <input class="form-check-input" type="checkbox" id="adminSwitch" v-model="isAdmin">
          <label class="form-check-label" for="adminSwitch">
            Admin Mode: <strong>{{ isAdmin ? 'ON' : 'OFF' }}</strong>
          </label>
        </div>
      </div>

      <!-- Product Cards -->
      <div class="row">
        <div class="col-md-3 mb-4" v-for="p in products" :key="p.id">
          <div class="card h-100 shadow">
            <img
              :src="p.image || 'https://via.placeholder.com/250x200.png?text=Product'"
              class="card-img-top"
              alt="Product"
              height="200"
            />
            <div class="card-body">
              <h5 class="card-title">{{ p.name }}</h5>
              <p class="card-text">Rs. {{ p.price }}</p>
              <p class="card-text">Stock: {{ getStock(p.id) }}</p>
              <p class="card-text">Supplier ID: {{ p.supplier }}</p>
              <button v-if="isAdmin" class="btn btn-danger btn-sm" @click="deleteProduct(p.id)">🗑️ Delete</button>
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

    <!-- Footer -->
    <footer class="bg-light py-3 text-center border-top mt-4">
      <p class="mb-0">© {{ new Date().getFullYear() }} Tinu James | ERP Inventory</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { api } from '../api'

const products = ref([])
const stocks = ref([])
const isAdmin = ref(true)

const form = ref({
  name: '',
  price: '',
  supplier: '',
  image: ''
})

const fetchProducts = async () => {
  const res = await api.get('/products/')
  products.value = res.data
}
const fetchStocks = async () => {
  const res = await api.get('/stocks/')
  stocks.value = res.data
}

const getStock = (productId) => {
  const stock = stocks.value.find(s => s.product === productId)
  return stock ? stock.quantity : 0
}

const addProduct = async () => {
  try {
    await api.post('/products/', form.value)
    await fetchProducts()
    form.value = { name: '', price: '', supplier: '', image: '' }
    alert('✅ Product added')
  } catch (err) {
    alert('❌ Error: ' + err.message)
  }
}

const deleteProduct = async (id) => {
  if (confirm('Delete this product?')) {
    await api.delete(`/products/${id}/`)
    await fetchProducts()
  }
}

onMounted(async () => {
  await fetchProducts()
  await fetchStocks()
})
</script>

<style>
body {
  background-color: #f8f9fa;
}
.card-title {
  font-weight: bold;
}
</style>
