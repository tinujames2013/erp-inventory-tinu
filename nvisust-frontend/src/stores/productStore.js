import { defineStore } from 'pinia'
import { api } from '../api'

export const useProductStore = defineStore('product', {
  state: () => ({
    products: [],
    loading: false,
    error: null
  }),
  actions: {
    async fetchProducts() {
      this.loading = true
      try {
        const res = await api.get('products/')
        this.products = res.data
      } catch (err) {
        this.error = err.message
      } finally {
        this.loading = false
      }
    },
    async addProduct(product) {
      await api.post('products/', product)
      await this.fetchProducts()
    },
    async deleteProduct(id) {
      await api.delete(`products/${id}/`)
      await this.fetchProducts()
    },
    async updateProduct(id, updatedProduct) {
      await api.put(`products/${id}/`, updatedProduct)
      await this.fetchProducts()
    }
  }
})
