import { createRouter, createWebHistory } from 'vue-router'
import ProductList from '../pages/ProductList.vue'
import OrderForm from '../pages/OrderForm.vue'
import OrderHistory from '../pages/OrderHistory.vue'

const routes = [
  { path: '/', component: ProductList },
  { path: '/order', component: OrderForm },
  { path: '/history', component: OrderHistory },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
