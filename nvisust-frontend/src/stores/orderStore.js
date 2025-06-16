import { defineStore } from 'pinia'
import { api } from '../api'

export const useOrderStore = defineStore('orderStore', {
  state: () => ({
    orders: []
  }),
  actions: {
    async fetchOrders() {
      const res = await api.get('orders/')
      this.orders = res.data
    },
    async placeOrder(productId, quantity) {
      try {
        const res = await api.post('orders/', {
          items: [
            { product: productId, quantity: quantity }
          ]
        })
        alert('✅ Order placed successfully!')
        await this.fetchOrders()
      } catch (err) {
        alert('❌ Order failed: ' + (err.response?.data?.non_field_errors?.[0] || err.message))
      }
    }
  }
})
