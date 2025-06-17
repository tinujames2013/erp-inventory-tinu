<template>
  <div class="container mt-4">
    <h2>📦 Product List</h2>

    <form @submit.prevent="handleAddProduct" class="mb-3">
      <input v-model="newProduct.name" placeholder="Product Name" required />
      <input v-model.number="newProduct.price" placeholder="Price" required />
      <input v-model.number="newProduct.supplier" placeholder="Supplier ID" required />
      <button class="btn btn-success btn-sm">➕ Add</button>
    </form>

    <table class="table table-bordered">
      <thead>
        <tr>
          <th>Name</th>
          <th>Price</th>
          <th>Supplier</th>
          <th>Stock</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in store.products" :key="product.id">
          <td>{{ product.name }}</td>
          <td>{{ product.price }}</td>
          <td>{{ product.supplier }}</td>
          <td>-- (To be linked)</td>
          <td>
            <button class="btn btn-danger btn-sm" @click="store.deleteProduct(product.id)">🗑 Delete</button>
            <!-- Edit Option -->
            <button class="btn btn-warning btn-sm" @click="startEdit(product)">✏ Edit</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="editingProduct">
      <h4>Edit Product</h4>
      <form @submit.prevent="handleUpdateProduct">
        <input v-model="editingProduct.name" required />
        <input v-model.number="editingProduct.price" required />
        <input v-model.number="editingProduct.supplier" required />
        <button class="btn btn-primary btn-sm">✔ Save</button>
        <button class="btn btn-secondary btn-sm" @click="editingProduct = null">❌ Cancel</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useProductStore } from '../stores/productStore'

const store = useProductStore()
const newProduct = ref({ name: '', price: 0, supplier: 1 })
const editingProduct = ref(null)

onMounted(() => store.fetchProducts())

const handleAddProduct = () => {
  store.addProduct(newProduct.value)
  newProduct.value = { name: '', price: 0, supplier: 1 }
}

const startEdit = (product) => {
  editingProduct.value = { ...product }
}

const handleUpdateProduct = () => {
  store.updateProduct(editingProduct.value.id, editingProduct.value)
  editingProduct.value = null
}
</script>

<style scoped>
table {
  width: 100%;
}
input {
  margin-right: 8px;
}
</style>
