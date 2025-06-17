<script setup>
import { ref } from 'vue'
import { api } from '../api'

const productId = ref('')
const quantity = ref(1)

async function placeOrder() {
  try {
    const res = await api.post('orders/', {
      items: [{ product: productId.value, quantity: quantity.value }]
    })
    alert('✅ Order placed successfully!')
    productId.value = ''
    quantity.value = 1
  } catch (err) {
    console.error(err)
    alert('❌ Failed to place order: ' + err.response?.data?.items?.[0]?.product || err.message)
  }
}
</script>
